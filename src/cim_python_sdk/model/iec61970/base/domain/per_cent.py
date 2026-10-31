"""CIM datatype PerCent (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class PerCent(CimDatatype):
    """Percentage on a defined base. For example, specify as 100 to indicate at the defined
    base."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.none
    multiplier = UnitMultiplier.none

    _cim_meta = ClassMeta(
        cim_name="PerCent",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{8345A4E0-E4BB-45d6-894B-983BB43C4B4F}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.none, static=True
            ),
            AttrMeta(
                "multiplier",
                "multiplier",
                "UnitMultiplier",
                0,
                1,
                "enumeration",
                UnitMultiplier.none,
                static=True,
            ),
        ),
    )
