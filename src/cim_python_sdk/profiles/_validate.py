"""`validate_profile`: check CIM objects against one or more profiles.

Checks, per object, against the selected profiles that carry its class:

* error: the class is in none of the selected profiles;
* error: the class is concrete in none of the selected profiles that carry it;
* warning: a property is set that none of the selected profiles lists for the class (an end
  also counts as listed when a selected profile lists the opposite end; ``IdentifiedObject.mRID`` is the
  object id and is never reported, an attribute still at its SDK default is ignored, and a
  property a selected profile lists under an ancestor of the class it does not carry counts as
  listed, see `Profile.element_class`);
* error: a required property (``min >= 1``) is missing, in each selected profile that lists it;
* error: more items on an end than the profile's (else the SDK's) maximum;
* error: an enumeration value outside the literals the profile allows.

Properties without an SDK counterpart (``python_name`` None) cannot be checked and are skipped.
Plans are cached per class and profile selection, so large networks cost one pass over the
objects.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from cim_python_sdk._runtime import CimObject
from cim_python_sdk.profiles._model import Profile, ProfileSet

if TYPE_CHECKING:
    from collections.abc import Iterable


@dataclass(frozen=True)
class ProfileIssue:
    """One finding. ``profile`` is a profile keyword, None when it concerns the whole selection."""

    severity: str  # "error" or "warning"
    object: CimObject
    profile: str | None
    property: str | None  # CIM name ``Declaring.prop``
    message: str

    def __str__(self) -> str:
        where = f" [{self.profile}]" if self.profile else ""
        return f"{self.severity}: {self.object!r}{where}: {self.message}"


# one profile entry of an attribute or end: (profile keyword, PropertyInfo, enum literals or None)
_Entry = tuple[str, Any, "frozenset[str] | None"]


class _Plan:
    __slots__ = ("attrs", "concrete", "ends", "kws", "members", "name")

    name: str
    members: tuple[Profile, ...]
    kws: str
    concrete: bool
    attrs: tuple[tuple[Any, tuple[_Entry, ...]], ...]  # (AttrSpec, entries); only those to check
    ends: tuple[tuple[Any, tuple[_Entry, ...]], ...]


_plans: dict[tuple[type, tuple[Profile, ...]], _Plan] = {}


def _normalize(profiles: Profile | ProfileSet | Iterable[Profile]) -> tuple[Profile, ...]:
    if isinstance(profiles, Profile):
        return (profiles,)
    if isinstance(profiles, ProfileSet):
        return profiles.profiles
    out = tuple(profiles)
    for p in out:
        if not isinstance(p, Profile):
            raise TypeError(f"not a Profile: {p!r}")
    if not out:
        raise ValueError("no profiles selected")
    return out


def _plan(cls: type, profiles: tuple[Profile, ...]) -> _Plan:
    key = (cls, profiles)
    plan = _plans.get(key)
    if plan is not None:
        return plan
    from cim_python_sdk.serialization._common import _end_key, class_plan

    plan = _Plan()
    plan.name = cls._cim_meta.cim_name  # type: ignore[attr-defined]
    plan.members = tuple(p for p in profiles if p.has_class(cls))
    plan.kws = ", ".join(p.keyword for p in plan.members)
    plan.concrete = any(p.is_concrete(cls) for p in plan.members)
    attrs: list[tuple[Any, tuple[_Entry, ...]]] = []
    ends: list[tuple[Any, tuple[_Entry, ...]]] = []
    if plan.members:
        by_py: dict[str, list[_Entry]] = {}
        for p in plan.members:
            for info in p.properties(cls):
                if info.python_name is not None:
                    lits = None if info.literals is None else frozenset(info.literals)
                    by_py.setdefault(info.python_name, []).append((p.keyword, info, lits))
        # listed under an ancestor in a profile without the class (SSH Equipment.inService of
        # an ACLineSegment): not reported as unlisted
        via_ancestor: set[str] = set()
        for p in profiles:
            if p not in plan.members:
                anc = p.element_class(cls)
                if anc is not None:
                    via_ancestor.update(i.python_name for i in p.properties(anc) if i.python_name)
        cplan = class_plan(cls)
        for spec in cplan.attrs:
            entries = tuple(by_py.get(spec.name, ()))
            if entries or spec.name not in via_ancestor:
                attrs.append((spec, entries))
        for es in cplan.ends:
            entries = tuple(by_py.get(es.name, ()))
            if not entries:
                if es.name in via_ancestor:
                    continue
                # listed through the opposite end?
                try:
                    inv = _end_key(es.desc.inverse)
                except Exception:  # noqa: BLE001 - an unresolvable end is checked as unlisted
                    inv = None
                if inv is not None and any(inv in p._all_keys for p in profiles):
                    continue
            ends.append((es, entries))
    plan.attrs = tuple(attrs)
    plan.ends = tuple(ends)
    _plans[key] = plan
    return plan


def validate_profile(
    objects: Iterable[CimObject] | CimObject,
    profiles: Profile | ProfileSet | Iterable[Profile],
    *,
    include_reachable: bool = True,
) -> list[ProfileIssue]:
    """Check `objects` (and, by default, everything reachable from them) against `profiles`.

    `profiles` is a `Profile`, a `ProfileSet` (all its profiles) or an iterable of profiles;
    only those are considered, so validating against ``cgmes3.EQ`` ignores what SSH or TP
    would require. Returns the issues in object order (CIM class name, mRID); never raises for
    model content.
    """
    from cim_python_sdk.serialization._common import collect

    selected = _normalize(profiles)
    if isinstance(objects, CimObject):
        objects = [objects]
    issues: list[ProfileIssue] = []

    def add(severity: str, obj: CimObject, kw: str | None, prop: str | None, msg: str) -> None:
        issues.append(ProfileIssue(severity, obj, kw, prop, msg))

    for obj in collect(objects, include_reachable):
        plan = _plan(type(obj), selected)
        if not plan.members:
            sel = ", ".join(p.keyword for p in selected)
            add(
                "error",
                obj,
                None,
                None,
                f"class {plan.name} is not in the selected profiles ({sel})",
            )
            continue
        if not plan.concrete:
            add("error", obj, plan.members[0].keyword, None,
                f"class {plan.name} is not concrete in {plan.kws}")  # fmt: skip
        for spec, entries in plan.attrs:
            v = getattr(obj, spec.name, None)
            if v is None:
                for kw, info, _ in entries:
                    if info.min >= 1:
                        add(
                            "error", obj, kw, info.name, f"required property {info.name} is not set"
                        )
            elif not entries:
                default = spec.meta.default
                if not spec.is_id and not (default is not None and v == default):
                    add("warning", obj, None, spec.prop,
                        f"property {spec.prop} is not in the selected profiles ({plan.kws})")  # fmt: skip
            elif spec.kind == "enumeration":
                value = getattr(v, "value", v)
                for kw, info, lits in entries:
                    if lits is not None and value not in lits:
                        allowed = ", ".join(info.literals or ())
                        add("error", obj, kw, info.name,
                            f"{info.name} = {value!r} is not allowed in {kw} (allowed: {allowed})")  # fmt: skip
        for es, entries in plan.ends:
            n = es.desc.count(obj)
            if n == 0 and not entries:
                continue
            if not entries:
                add("warning", obj, None, es.prop,
                    f"property {es.prop} is not in the selected profiles ({plan.kws})")  # fmt: skip
                continue
            for kw, info, _ in entries:
                if n == 0 and info.min >= 1 and not es.many:
                    add("error", obj, kw, info.name, f"required property {info.name} is not set")
                elif n < info.min:
                    add("error", obj, kw, info.name,
                        f"{info.name} has {n} item(s), needs at least {info.min}")  # fmt: skip
                elif info.max is not None and n > info.max:
                    add("error", obj, kw, info.name,
                        f"{info.name} has {n} item(s), allows at most {info.max}")  # fmt: skip
    return issues
