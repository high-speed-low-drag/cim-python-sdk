"""CIM compound AccountingUnit (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61970.base.domain.currency import Currency
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier


class AccountingUnit(CimCompound):
    """Unit for accounting; use either 'energyUnit' or 'currencyUnit' to specify the unit for
    'value'."""

    __slots__ = ("energy_unit", "monetary_unit", "multiplier", "value")

    value: float | None
    energy_unit: float | None  # RealEnergy
    monetary_unit: Currency | None
    multiplier: UnitMultiplier | None

    _cim_meta = ClassMeta(
        cim_name="AccountingUnit",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{5F0C90B2-8D7F-4468-B553-8A0AC39EA02E}",
        kind="compound",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("energy_unit", "energyUnit", "RealEnergy", 0, 1, "cimdatatype"),
            AttrMeta("monetary_unit", "monetaryUnit", "Currency", 0, 1, "enumeration"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
