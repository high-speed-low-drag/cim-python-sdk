"""Bases for enumerations, compounds and CIMDatatypes."""

from __future__ import annotations

import enum

from cim_python_sdk._runtime._compat import TYPE_CHECKING
from cim_python_sdk._runtime.meta import cim_attributes

if TYPE_CHECKING:
    from typing import Any, ClassVar

    from cim_python_sdk._runtime.meta import ClassMeta


class CimEnum(enum.Enum):
    """Base of generated enumerations. Member values are the CIM literal spellings."""

    def __str__(self) -> str:
        return str(self.value)


_fields: dict[type, tuple[tuple[str, Any], ...]] = {}


def _instance_fields(cls: type) -> tuple[tuple[str, Any], ...]:
    """(name, default) of every non-static attribute, from the metas."""
    f = _fields.get(cls)
    if f is None:
        f = _fields[cls] = tuple((a.name, a.default) for a in cim_attributes(cls) if not a.static)
    return f


class CimCompound:
    """Slotted value class for «Compound» types: keyword init from the metas, value equality.

    Generated subclasses declare ``__slots__``, annotations and ``_cim_meta`` only.
    """

    __slots__ = ()
    __hash__ = None  # type: ignore[assignment]  # mutable value object
    _cim_meta: ClassVar[ClassMeta]

    def __init__(self, **kwargs: Any) -> None:
        for name, default in _instance_fields(type(self)):
            setattr(self, name, kwargs.pop(name, default))
        if kwargs:
            names = ", ".join(repr(k) for k in kwargs)
            raise TypeError(f"{type(self).__name__}() got unexpected keyword argument(s): {names}")

    def _values(self) -> tuple[Any, ...]:
        return tuple(getattr(self, n, None) for n, _ in _instance_fields(type(self)))

    def __eq__(self, other: object) -> bool:
        if type(other) is not type(self):
            return NotImplemented
        return self._values() == other._values()  # type: ignore[attr-defined]

    def __repr__(self) -> str:
        parts = (
            f"{n}={v!r}"
            for (n, _), v in zip(_instance_fields(type(self)), self._values(), strict=True)
            if v is not None
        )
        return f"{type(self).__name__}({', '.join(parts)})"


class CimDatatype:
    """Base for «CIMDatatype» classes such as ``ActivePower``.

    Model attributes typed by a datatype hold the plain value (e.g. a float); the
    datatype class records the value type and the fixed unit/multiplier as class
    metadata (None when the model leaves it open). An instance wraps one value.
    """

    __slots__ = ("value",)
    _cim_meta: ClassVar[ClassMeta]
    value_type: ClassVar[type] = float
    unit: ClassVar[CimEnum | None] = None
    multiplier: ClassVar[CimEnum | None] = None

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def __eq__(self, other: object) -> bool:
        if type(other) is not type(self):
            return NotImplemented
        return self.value == other.value  # type: ignore[attr-defined]

    __hash__ = None  # type: ignore[assignment]

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.value!r})"
