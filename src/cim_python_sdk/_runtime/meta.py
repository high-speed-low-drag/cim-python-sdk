"""Frozen class metadata (`_cim_meta`) and MRO helpers.

Every generated class carries ``_cim_meta: ClassMeta`` describing only what the
class itself declares. `all_metas`, `cim_attributes` and `cim_ends` merge the
metas along the MRO (base first; a re-declared attribute replaces the inherited
one in place).

Namespaces: `ClassMeta`, `AttrMeta` and `EndMeta` carry ``namespace``, the RDF namespace prefix
of their CIM name (a key of `NAMESPACES`; default ``"cim"``). The CGMES European extensions are
``"eu"``: classes such as ``BoundaryPoint`` and members added to CIM classes such as
``IdentifiedObject.shortName``. A member's namespace is its own, not its class's.
"""

from __future__ import annotations

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any, NoReturn


class _Frozen:
    """Slotted, immutable record with value equality."""

    __slots__: tuple[str, ...] = ()

    def _values(self) -> tuple[Any, ...]:
        return tuple(getattr(self, n) for n in self.__slots__)

    def __setattr__(self, name: str, value: object) -> NoReturn:
        raise AttributeError(f"{type(self).__name__} is frozen")

    def __delattr__(self, name: str) -> NoReturn:
        raise AttributeError(f"{type(self).__name__} is frozen")

    def __eq__(self, other: object) -> bool:
        if type(other) is not type(self):
            return NotImplemented
        return self._values() == other._values()  # type: ignore[attr-defined]

    def __hash__(self) -> int:
        return hash(self._values())

    def __repr__(self) -> str:
        fields = ", ".join(f"{n}={getattr(self, n)!r}" for n in self.__slots__)
        return f"{type(self).__name__}({fields})"


_set = object.__setattr__

CIM = "cim"
NAMESPACES: dict[str, str] = {
    "cim": "http://iec.ch/TC57/CIM100#",
    "eu": "http://iec.ch/TC57/CIM100-European#",
}


class AttrMeta(_Frozen):
    """One UML attribute. Attributes typed by a CIMDatatype hold the plain value."""

    __slots__ = ("name", "cim_name", "py_type", "lower", "upper", "kind", "default", "static", "deprecated", "namespace")  # noqa: RUF023

    name: str  # Python attribute name
    cim_name: str
    py_type: str  # CIM-level type name: "float", "ActivePower", "AssetKind", "StreetAddress"
    lower: int
    upper: int | None
    kind: str  # primitive / cimdatatype / enumeration / compound
    default: Any  # the Python default value (enum member, number, str) or None
    static: bool  # class-level constant: not a slot and not an __init__ parameter
    deprecated: bool
    namespace: str  # prefix in NAMESPACES

    def __init__(
        self,
        name: str,
        cim_name: str,
        py_type: str,
        lower: int,
        upper: int | None,
        kind: str,
        default: Any = None,
        static: bool = False,
        deprecated: bool = False,
        namespace: str = CIM,
    ) -> None:
        _set(self, "name", name)
        _set(self, "cim_name", cim_name)
        _set(self, "py_type", py_type)
        _set(self, "lower", lower)
        _set(self, "upper", upper)
        _set(self, "kind", kind)
        _set(self, "default", default)
        _set(self, "static", static)
        _set(self, "deprecated", deprecated)
        _set(self, "namespace", namespace)


class EndMeta(_Frozen):
    """One association end owned by a class."""

    __slots__ = ("name", "cim_role", "target", "many", "lower", "upper", "inverse", "aggregation", "deprecated", "namespace")  # noqa: RUF023

    name: str  # Python attribute name of the end
    cim_role: str | None
    target: str  # "module:ClassName" of the class at the other end
    many: bool
    lower: int
    upper: int | None
    inverse: str  # Python name of the end on the target class that points back
    aggregation: str  # none / shared / composite
    deprecated: bool
    namespace: str  # prefix in NAMESPACES (of the association, the same on both ends)

    def __init__(
        self,
        name: str,
        cim_role: str | None,
        target: str,
        many: bool,
        lower: int,
        upper: int | None,
        inverse: str,
        aggregation: str = "none",
        deprecated: bool = False,
        namespace: str = CIM,
    ) -> None:
        _set(self, "name", name)
        _set(self, "cim_role", cim_role)
        _set(self, "target", target)
        _set(self, "many", many)
        _set(self, "lower", lower)
        _set(self, "upper", upper)
        _set(self, "inverse", inverse)
        _set(self, "aggregation", aggregation)
        _set(self, "deprecated", deprecated)
        _set(self, "namespace", namespace)


class ClassMeta(_Frozen):
    """What one class declares itself (not inherited members)."""

    __slots__ = ("cim_name", "package", "guid", "kind", "deprecated", "attributes", "ends", "namespace")  # noqa: RUF023

    cim_name: str
    package: str
    guid: str
    kind: str  # class / compound / cimdatatype / enumeration
    deprecated: bool
    attributes: tuple[AttrMeta, ...]
    ends: tuple[EndMeta, ...]
    namespace: str  # prefix in NAMESPACES

    def __init__(
        self,
        cim_name: str,
        package: str,
        guid: str,
        kind: str = "class",
        deprecated: bool = False,
        attributes: tuple[AttrMeta, ...] = (),
        ends: tuple[EndMeta, ...] = (),
        namespace: str = CIM,
    ) -> None:
        _set(self, "cim_name", cim_name)
        _set(self, "package", package)
        _set(self, "guid", guid)
        _set(self, "kind", kind)
        _set(self, "deprecated", deprecated)
        _set(self, "attributes", tuple(attributes))
        _set(self, "ends", tuple(ends))
        _set(self, "namespace", namespace)


_metas_cache: dict[type, tuple[ClassMeta, ...]] = {}
_attrs_cache: dict[type, tuple[AttrMeta, ...]] = {}
_ends_cache: dict[type, tuple[EndMeta, ...]] = {}


def all_metas(cls: type) -> tuple[ClassMeta, ...]:
    """The `_cim_meta` of `cls` and of every ancestor that has one, base first."""
    r = _metas_cache.get(cls)
    if r is None:
        r = tuple(
            m
            for k in reversed(cls.__mro__)
            if isinstance(m := k.__dict__.get("_cim_meta"), ClassMeta)
        )
        _metas_cache[cls] = r
    return r


def cim_attributes(cls: type) -> tuple[AttrMeta, ...]:
    """All attribute metas of `cls`, inherited first; an override replaces in place."""
    r = _attrs_cache.get(cls)
    if r is None:
        d: dict[str, AttrMeta] = {}
        for m in all_metas(cls):
            for a in m.attributes:
                d[a.name] = a
        r = _attrs_cache[cls] = tuple(d.values())
    return r


def cim_ends(cls: type) -> tuple[EndMeta, ...]:
    """All association-end metas of `cls`, inherited first."""
    r = _ends_cache.get(cls)
    if r is None:
        r = _ends_cache[cls] = tuple(e for m in all_metas(cls) for e in m.ends)
    return r
