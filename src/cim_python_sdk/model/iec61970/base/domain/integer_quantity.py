"""CIM compound IntegerQuantity (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class IntegerQuantity(CimCompound):
    """Quantity with integer value and associated unit information."""

    __slots__ = ("multiplier", "unit", "value")

    value: int | None
    unit: UnitSymbol | None
    multiplier: UnitMultiplier | None

    _cim_meta = ClassMeta(
        cim_name="IntegerQuantity",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{932A8711-818C-4821-877F-4EF3AA27D4AD}",
        kind="compound",
        attributes=(
            AttrMeta("value", "value", "int", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
