"""CIM compound StringQuantity (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class StringQuantity(CimCompound):
    """Quantity with string value (when it is not important whether it is an integral or a
    floating point number) and associated unit information."""

    __slots__ = ("multiplier", "unit", "value")

    value: str | None
    unit: UnitSymbol | None
    multiplier: UnitMultiplier | None

    _cim_meta = ClassMeta(
        cim_name="StringQuantity",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{C2DA5F9A-96E4-4c11-8EC6-B29AE5783A1A}",
        kind="compound",
        attributes=(
            AttrMeta("value", "value", "str", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
