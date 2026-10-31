"""`Profile`, `ProfileSet` and `PropertyInfo`: a read-only view of a profile snapshot.

A snapshot (``data/<name>.json``, written by ``tools/dump_profiles.py``) lists, per profile, the
CIM classes it carries and the properties each class lists. Objects stay ordinary ``cim_python_sdk``
objects; a `Profile` only answers questions about them. Stdlib only; the JSON is read once, on
first use, and SDK classes are resolved lazily.

Conventions
-----------
* Classes are SDK classes (or CIM names). Enumerations and compounds the profile uses are
  profile classes too (`Profile.classes` holds them); the ``eu:`` extension classes included.
* `Profile.properties(cls)` is the union along the profile's superclass chain, base first, so
  ``ACLineSegment`` has ``IdentifiedObject.mRID`` as well as ``ACLineSegment.r``. A property is
  listed under the class that owns it in the profile: for an association that is the side
  written in CIMXML (not always the generic writer's choice, see tests/profiles/test_direction).
  No profile lists both ends of an association.
* ``IdentifiedObject.mRID`` is a profile attribute like any other (it is the Python ``mrid``).
* Gaps: a property the SDK does not have would still be listed, with ``python_name`` None. The
  CGMES 3.0 snapshot (ENTSO-E vocabularies) has none.
* ``min`` and ``max`` are the profile's multiplicity (``cims:multiplicity``); an unbounded profile
  maximum (``n``) falls back to the SDK multiplicity of the member (None = unbounded).
* Enum literals are CIM spellings (``CimEnum.value``), as the profile lists them. ``None`` in
  `PropertyInfo.literals` means the profile does not restrict them.
* Units: the SDK holds SI values (V, W, m). A profile set can fix a unit multiplier per datatype
  (CGMES: kV, MW, MVAr, MVA, km); `ProfileSet.unit_exponent` gives its power of ten.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from functools import cached_property
from importlib import resources
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator
    from typing import Any

    from cim_python_sdk._runtime import CimObject
    from cim_python_sdk.profiles._validate import ProfileIssue

KEYWORD_ORDER = ("EQ", "SSH", "TP", "SV", "DL", "GL", "OP", "SC", "EQBD", "DY")
# IEC 61970-301 UnitMultiplier literals -> power of ten
MULTIPLIER_EXPONENTS = {
    "y": -24, "z": -21, "a": -18, "f": -15, "p": -12, "n": -9, "micro": -6, "m": -3, "c": -2,
    "d": -1, "none": 0, "da": 1, "h": 2, "k": 3, "M": 6, "G": 9, "T": 12, "P": 15, "E": 18,
    "Z": 21, "Y": 24,
}  # fmt: skip


def _common() -> Any:
    from cim_python_sdk.serialization import _common as c

    return c


def _local(name: str) -> str:
    """``cim:Terminal`` / ``eu:BoundaryPoint`` -> the bare CIM name."""
    return name.rpartition(":")[2]


@dataclass(frozen=True)
class PropertyInfo:
    """One property of a class in a profile.

    ``name`` is the CIM name ``Declaring.property`` as the profile writes it
    (``ACLineSegment.r``, ``IdentifiedObject.shortName``); ``namespace`` its prefix (``cim`` or
    ``eu``). ``python_name`` is the attribute or end
    on the SDK class, None for a known gap. ``owner`` is the profile class that lists the
    property (an ancestor of the class it was asked for when inherited).
    """

    name: str
    namespace: str
    python_name: str | None
    kind: str | None  # attribute / association / None (unknown)
    min: int
    max: int | None  # effective: profile maxCardinality, else the SDK multiplicity
    range: str | None  # as in the snapshot: ``cim:Susceptance``, ``cim:Terminal``, ``xsd:string``
    range_kind: str | None  # datatype / enumeration / compound / class
    targets: tuple[str, ...]  # profile classes allowed as range (associations)
    literals: tuple[str, ...] | None  # allowed enum literals; None = unrestricted
    stereotypes: tuple[str, ...]
    owner: type
    many: bool = False  # the SDK end is multi-valued
    _spec: Any = field(default=None, repr=False, compare=False)  # AttrSpec / EndSpec

    @property
    def qname(self) -> str:
        return f"{self.namespace}:{self.name}"

    @property
    def required(self) -> bool:
        return self.min >= 1

    @property
    def in_sdk(self) -> bool:
        return self.python_name is not None

    @property
    def is_association(self) -> bool:
        return self.kind == "association"


@dataclass(frozen=True, eq=False)
class Profile:
    """One profile (``EQ``, ``SSH``, ...): its classes and their properties."""

    keyword: str
    name: str
    uri: str
    version: str
    comment: str
    base: str
    _raw: dict[str, Any] = field(repr=False)  # snapshot ``classes`` of this profile

    def __repr__(self) -> str:
        return f"Profile({self.keyword!r})"

    def __str__(self) -> str:
        return self.keyword

    # -- classes --------------------------------------------------------------------------

    @cached_property
    def _resolved(self) -> tuple[dict[str, type], dict[type, str]]:
        resolve = _common().resolve_class
        by_name: dict[str, type] = {}
        for n in self._raw:
            cls = resolve(n)
            if cls is not None:
                by_name[n] = cls
        return by_name, {c: n for n, c in by_name.items()}

    @cached_property
    def class_names(self) -> tuple[str, ...]:
        """CIM names of every class, enumeration and compound of the profile, sorted."""
        return tuple(sorted(self._raw))

    @cached_property
    def classes(self) -> tuple[type, ...]:
        """The SDK classes of `class_names` (the same objects as ``cim_python_sdk.X``)."""
        by_name = self._resolved[0]
        return tuple(by_name[n] for n in self.class_names if n in by_name)

    @cached_property
    def concrete_classes(self) -> tuple[type, ...]:
        by_name = self._resolved[0]
        return tuple(
            by_name[n] for n in self.class_names if n in by_name and self._raw[n]["concrete"]
        )

    def _name(self, cls: type | str) -> str | None:
        if isinstance(cls, str):
            n = _local(cls)
            return n if n in self._raw else None
        return self._resolved[1].get(cls)

    def has_class(self, cls: type | str) -> bool:
        return self._name(cls) is not None

    __contains__ = has_class

    def is_concrete(self, cls: type | str) -> bool:
        """The profile allows instances of `cls` (it is concrete in this profile)."""
        n = self._name(cls)
        return n is not None and bool(self._raw[n]["concrete"])

    def is_description(self, cls: type | str) -> bool:
        """Instances of `cls` are only described here (``rdf:about``), defined in another profile."""
        n = self._name(cls)
        return n is not None and "description" in self._raw[n]["stereotypes"]

    def element_class(self, cls: type) -> type | None:
        """The class instances of SDK class `cls` are written as in this profile: `cls` when the
        profile has it, else its nearest SDK ancestor in the profile that adds properties to its
        profile superclass (CGMES SSH describes an ACLineSegment as ``cim:Equipment`` with
        ``Equipment.inService``), else None."""
        if self.has_class(cls):
            return cls
        for anc in cls.__mro__[1:]:
            if getattr(anc, "_cim_meta", None) is None or not self.has_class(anc):
                continue
            own = {i.name for i in self.properties(anc)}
            sup = self.superclass(anc)
            if own and (sup is None or own != {i.name for i in self.properties(sup)}):
                return anc
        return None

    def is_enumeration(self, cls: type | str) -> bool:
        n = self._name(cls)
        return n is not None and bool(self._raw[n]["enumeration"])

    def superclass(self, cls: type | str) -> type | None:
        """The profile superclass (not the SDK one), or None."""
        n = self._name(cls)
        sup = None if n is None else self._raw[n]["super"]
        return self._resolved[0].get(sup) if sup else None

    # -- properties -----------------------------------------------------------------------

    @cached_property
    def _own_cache(self) -> dict[str, tuple[PropertyInfo, ...]]:
        return {}

    @cached_property
    def _props_cache(self) -> dict[str, tuple[PropertyInfo, ...]]:
        return {}

    def _own(self, name: str) -> tuple[PropertyInfo, ...]:
        r = self._own_cache.get(name)
        if r is None:
            r = self._own_cache[name] = self._build_own(name)
        return r

    def _build_own(self, name: str) -> tuple[PropertyInfo, ...]:
        c = _common()
        owner = self._resolved[0][name]
        plan = c.class_plan(owner) if owner._cim_meta.kind in ("class", "compound") else None
        out = []
        for key, p in self._raw[name]["properties"].items():
            spec = plan.by_prop.get(key) if plan is not None else None
            if spec is not None and spec.ns != p["ns"]:
                spec = None
            rng = p["range"]
            lits = None
            if p["range_kind"] == "enumeration" and rng:
                lits = self._raw.get(_local(rng), {}).get("literals")
            mx = p["max"]
            if mx is None and spec is not None:
                mx = spec.meta.upper
            out.append(
                PropertyInfo(
                    name=key,
                    namespace=p["ns"],
                    python_name=None if spec is None else spec.name,
                    kind=p["kind"],
                    min=p["min"] or 0,
                    max=mx,
                    range=rng,
                    range_kind=p["range_kind"],
                    targets=tuple(p["targets"]),
                    literals=None if lits is None else tuple(lits),
                    stereotypes=tuple(p["stereotypes"]),
                    owner=owner,
                    many=bool(spec is not None and getattr(spec, "many", False)),
                    _spec=spec,
                )
            )
        return tuple(out)

    def properties(self, cls: type | str) -> tuple[PropertyInfo, ...]:
        """Properties of `cls` in this profile, inherited along the profile superclass chain
        (base class first). Empty when the class is not in the profile."""
        n = self._name(cls)
        if n is None:
            return ()
        r = self._props_cache.get(n)
        if r is None:
            chain = []
            seen = set()
            cur: str | None = n
            while cur is not None and cur in self._raw and cur not in seen:
                seen.add(cur)
                chain.append(cur)
                cur = self._raw[cur]["super"]
            merged: dict[str, PropertyInfo] = {}
            for c_name in reversed(chain):
                if c_name in self._resolved[0]:
                    for info in self._own(c_name):
                        merged[info.name] = info
            r = self._props_cache[n] = tuple(merged.values())
        return r

    @cached_property
    def _index_cache(self) -> dict[str, dict[str, PropertyInfo]]:
        return {}

    def _index(self, cls: type | str) -> dict[str, PropertyInfo]:
        """Lookup by Python name, ``Declaring.prop`` name and the bare property name."""
        n = self._name(cls)
        if n is None:
            return {}
        idx = self._index_cache.get(n)
        if idx is None:
            idx = {}
            props = self.properties(n)
            for info in props:
                idx[info.name] = info
            for info in props:
                idx.setdefault(info.name.partition(".")[2], info)
            for info in props:
                if info.python_name is not None:
                    idx[info.python_name] = info
            self._index_cache[n] = idx
        return idx

    def property(self, cls: type | str, prop: str) -> PropertyInfo | None:
        """The property of `cls`, named by Python attribute (``r``), bare CIM name (``mRID``)
        or ``Declaring.prop`` (``cim:`` / ``eu:`` prefix optional); None if absent."""
        idx = self._index(cls)
        info = idx.get(prop)
        if info is None and ":" in prop:
            info = idx.get(prop.partition(":")[2])
        return info

    def has_property(self, cls: type | str, prop: str) -> bool:
        return self.property(cls, prop) is not None

    def required(self, cls: type | str) -> tuple[PropertyInfo, ...]:
        """Properties of `cls` with ``min >= 1`` in this profile."""
        return tuple(p for p in self.properties(cls) if p.required)

    @cached_property
    def _all_keys(self) -> frozenset[str]:
        return frozenset(k for c in self._raw.values() for k in c["properties"])

    def allowed_literals(self, enum_cls: type | str) -> tuple[str, ...]:
        """CIM literals the profile allows for an enumeration: all of the SDK enum's when the
        profile does not restrict them; empty when the enumeration is not in the profile."""
        n = self._name(enum_cls)
        if n is None:
            return ()
        lits = self._raw[n]["literals"]
        if lits is not None:
            return tuple(lits)
        cls = self._resolved[0][n]
        return tuple(m.value for m in cls)  # type: ignore[attr-defined]

    def validate(
        self, objects: Iterable[CimObject], *, include_reachable: bool = True
    ) -> list[ProfileIssue]:
        """`validate_profile(objects, self)`."""
        from cim_python_sdk.profiles._validate import validate_profile

        return validate_profile(objects, self, include_reachable=include_reachable)


@dataclass(frozen=True, eq=False)
class ProfileSet:
    """A named family of profiles, e.g. CGMES 3.0 (see `cim_python_sdk.profiles.cgmes3`)."""

    name: str
    profiles: tuple[Profile, ...]
    namespaces: dict[str, str] = field(repr=False)
    source: dict[str, str] = field(repr=False)
    # fixed unit per datatype: {"Voltage": ("k", "V")}; unit None when the profile fixes none
    units: dict[str, tuple[str, str | None]] = field(default_factory=dict, repr=False)

    @classmethod
    def from_snapshot(cls, data: dict[str, Any], name: str) -> ProfileSet:
        profs = []
        for kw, p in data["profiles"].items():
            profs.append(
                Profile(
                    keyword=kw,
                    name=p["name"],
                    uri=p["uri"],
                    version=p["version"],
                    comment=p["comment"],
                    base=p["base"],
                    _raw=p["classes"],
                )
            )
        profs.sort(
            key=lambda p: (
                KEYWORD_ORDER.index(p.keyword) if p.keyword in KEYWORD_ORDER else 99,
                p.keyword,
            )
        )
        units = {k: (v["multiplier"], v.get("unit")) for k, v in data.get("units", {}).items()}
        return cls(name, tuple(profs), dict(data["namespaces"]), dict(data["source"]), units)

    @classmethod
    def load(cls, resource: str, name: str) -> ProfileSet:
        """Read ``cim_python_sdk/profiles/data/<resource>`` (once per call; cache in the caller)."""
        text = resources.files("cim_python_sdk.profiles").joinpath("data", resource).read_text("utf-8")
        return cls.from_snapshot(json.loads(text), name)

    def __repr__(self) -> str:
        return f"ProfileSet({self.name!r}, {[p.keyword for p in self.profiles]})"

    def __iter__(self) -> Iterator[Profile]:
        return iter(self.profiles)

    def __len__(self) -> int:
        return len(self.profiles)

    def __contains__(self, item: object) -> bool:
        return item in self.profiles or (isinstance(item, str) and item in self._by_keyword)

    def __getitem__(self, keyword: str) -> Profile:
        return self.by_keyword(keyword)

    def __getattr__(self, name: str) -> Profile:
        if not name.startswith("_"):
            p = self._by_keyword.get(name)
            if p is not None:
                return p
        raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")

    @cached_property
    def _by_keyword(self) -> dict[str, Profile]:
        return {p.keyword: p for p in self.profiles}

    @cached_property
    def _by_uri(self) -> dict[str, Profile]:
        return {p.uri: p for p in self.profiles}

    @property
    def keywords(self) -> tuple[str, ...]:
        return tuple(p.keyword for p in self.profiles)

    def by_keyword(self, keyword: str) -> Profile:
        try:
            return self._by_keyword[keyword]
        except KeyError:
            raise KeyError(
                f"no profile {keyword!r} in {self.name} ({', '.join(self.keywords)})"
            ) from None

    def unit_exponent(self, datatype: str) -> int:
        """Power of ten of the multiplier the profiles fix for `datatype` (a CIM datatype name:
        3 for ``Voltage``, kV in CGMES; 6 for ``ActivePower``, MW). 0 when the profiles fix none
        or the datatype is not listed: the value is then written as held."""
        unit = self.units.get(datatype)
        return 0 if unit is None else MULTIPLIER_EXPONENTS[unit[0]]

    def by_uri(self, uri: str) -> Profile:
        """The profile with this ``md:Model.profile`` / ``dcterms:conformsTo`` URI."""
        try:
            return self._by_uri[uri]
        except KeyError:
            raise KeyError(f"no profile with URI {uri!r} in {self.name}") from None

    @cached_property
    def class_names(self) -> tuple[str, ...]:
        """Union of the CIM names of all profiles, sorted."""
        return tuple(sorted({n for p in self.profiles for n in p.class_names}))

    @cached_property
    def classes(self) -> tuple[type, ...]:
        """Union of the profile classes (classes, enumerations, compounds), sorted by CIM name."""
        by_name = {}
        for p in self.profiles:
            by_name.update(p._resolved[0])
        return tuple(by_name[n] for n in self.class_names if n in by_name)

    def has_class(self, cls: type | str) -> bool:
        return any(p.has_class(cls) for p in self.profiles)

    def profiles_of(self, cls: type | str, prop: str | None = None) -> tuple[Profile, ...]:
        """Profiles that carry `cls` (or, with `prop`, carry that property of it), in set order.
        `prop` is a Python attribute, bare CIM name or ``Declaring.prop`` (see `Profile.property`)."""
        if prop is None:
            return tuple(p for p in self.profiles if p.has_class(cls))
        return tuple(p for p in self.profiles if p.has_property(cls, prop))

    def defining_profiles(self, cls: type | str) -> tuple[Profile, ...]:
        """Profiles in which `cls` is concrete and not a description: where instances get
        ``rdf:ID`` (profiles that only reference or describe it are left out)."""
        return tuple(p for p in self.profiles if p.is_concrete(cls) and not p.is_description(cls))

    def validate(
        self,
        objects: Iterable[CimObject],
        profiles: Profile | Iterable[Profile] | None = None,
        *,
        include_reachable: bool = True,
    ) -> list[ProfileIssue]:
        """`validate_profile` against `profiles` (default: every profile of the set)."""
        from cim_python_sdk.profiles._validate import validate_profile

        return validate_profile(
            objects, self if profiles is None else profiles, include_reachable=include_reachable
        )
