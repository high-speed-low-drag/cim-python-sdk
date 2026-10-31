"""`CimObject`: the slotted base of every generated CIM class."""

from __future__ import annotations

from cim_python_sdk._runtime._compat import TYPE_CHECKING
from cim_python_sdk._runtime.meta import cim_attributes, cim_ends

if TYPE_CHECKING:
    from typing import Any, ClassVar

    from cim_python_sdk._runtime.ends import _End
    from cim_python_sdk._runtime.meta import ClassMeta

# per class: (required attribute names, ends with a lower bound or a finite upper bound)
_checks: dict[type, tuple[tuple[str, ...], tuple[_End[Any], ...]]] = {}


def _validation_plan(cls: type) -> tuple[tuple[str, ...], tuple[_End[Any], ...]]:
    plan = _checks.get(cls)
    if plan is None:
        attrs = tuple(a.name for a in cim_attributes(cls) if a.lower > 0 and not a.static)
        ends = tuple(
            getattr(cls, e.name)
            for e in cim_ends(cls)
            if e.lower > 0 or (e.many and e.upper is not None)
        )
        plan = _checks[cls] = (attrs, ends)
    return plan


# per class: (every slot name along the MRO, the subset that holds Many dicts)
_state_plans: dict[type, tuple[tuple[str, ...], frozenset[str]]] = {}


def _state_plan(cls: type) -> tuple[tuple[str, ...], frozenset[str]]:
    plan = _state_plans.get(cls)
    if plan is None:
        names: list[str] = []
        for k in reversed(cls.__mro__):
            slots = k.__dict__.get("__slots__", ())
            for n in (slots,) if isinstance(slots, str) else slots:
                if n != "__weakref__" and n != "__dict__":
                    names.append(n)
        many = frozenset("_" + e.name for e in cim_ends(cls) if e.many)
        plan = _state_plans[cls] = (tuple(names), many)
    return plan


class CimObject:
    """Base class. Equality and hashing are identity-based (inherited from object).

    Copying: `copy.deepcopy` and pickle work (also for cyclic graphs). Many ends are stored
    as ``{id(obj): obj}``, so the state holds plain lists and `__setstate__` rebuilds the
    dicts with the new ids. `copy.copy` raises TypeError: a shallow copy would share
    half-links with the original.
    """

    __slots__ = ("__weakref__",)
    _cim_meta: ClassVar[ClassMeta]

    def __init__(self, **kwargs: Any) -> None:
        if kwargs:
            names = ", ".join(repr(k) for k in kwargs)
            raise TypeError(f"{type(self).__name__}() got unexpected keyword argument(s): {names}")

    def __getstate__(self) -> dict[str, Any]:
        names, many = _state_plan(type(self))
        state: dict[str, Any] = {}
        for name in names:
            try:
                value = getattr(self, name)
            except AttributeError:
                continue  # unset slot
            state[name] = list(value.values()) if name in many else value
        return state

    def __setstate__(self, state: dict[str, Any]) -> None:
        _, many = _state_plan(type(self))
        for name, value in state.items():
            if name in many:
                value = {id(v): v for v in value}
            object.__setattr__(self, name, value)

    def __copy__(self) -> Any:
        raise TypeError(
            f"cannot shallow-copy {type(self).__name__}: a shallow copy would share association "
            "links with the original; use copy.deepcopy() instead"
        )

    def __repr__(self) -> str:
        mrid = getattr(self, "mrid", None)
        if mrid is not None:
            return f"{type(self).__name__}(mrid={mrid!r})"
        return f"{type(self).__name__}(id={id(self):#x})"

    def validate(self) -> list[str]:
        """Multiplicity problems as human-readable strings; never raises."""
        issues: list[str] = []
        try:
            cls = type(self)
            attrs, ends = _validation_plan(cls)
            for name in attrs:
                if getattr(self, name, None) is None:
                    issues.append(f"{self!r}: required attribute {name!r} is not set")
            for end in ends:
                n = end.count(self)
                lower, upper = end.meta.lower, end.meta.upper
                if n < lower:
                    if end.meta.many:
                        issues.append(
                            f"{self!r}: {end.name!r} has {n} item(s), needs at least {lower}"
                        )
                    else:
                        issues.append(f"{self!r}: required association {end.name!r} is not set")
                elif upper is not None and n > upper:
                    issues.append(f"{self!r}: {end.name!r} has {n} item(s), allows at most {upper}")
        except Exception as exc:  # noqa: BLE001 - validate() must never raise
            issues.append(f"{type(self).__name__}: validate() failed: {exc!r}")
        return issues
