"""CIM compound DecimalQuantity (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal

    from cim_python_sdk.model.iec61970.base.domain.currency import Currency
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class DecimalQuantity(CimCompound):
    """Quantity with decimal value and associated unit or currency information."""

    __slots__ = ("currency", "multiplier", "unit", "value")

    value: _decimal.Decimal | None
    unit: UnitSymbol | None
    multiplier: UnitMultiplier | None
    currency: Currency | None

    _cim_meta = ClassMeta(
        cim_name="DecimalQuantity",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{B344AA52-5E10-485f-A78F-8A7F0C5543C8}",
        kind="compound",
        attributes=(
            AttrMeta("value", "value", "Decimal", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("currency", "currency", "Currency", 0, 1, "enumeration"),
        ),
    )
