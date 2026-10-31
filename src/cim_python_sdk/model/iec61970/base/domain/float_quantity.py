"""CIM compound FloatQuantity (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class FloatQuantity(CimCompound):
    """Quantity with float value and associated unit information."""

    __slots__ = ("multiplier", "unit", "value")

    value: float | None
    unit: UnitSymbol | None
    multiplier: UnitMultiplier | None

    _cim_meta = ClassMeta(
        cim_name="FloatQuantity",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{6E887B5A-F340-462c-9186-8556588ACE6C}",
        kind="compound",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
