"""CIM datatype ActivePowerChangeRate (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class ActivePowerChangeRate(CimDatatype):
    """Rate of change of active power per time."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.WPers

    _cim_meta = ClassMeta(
        cim_name="ActivePowerChangeRate",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{C872CC3E-AEC1-4ea2-93C8-0E51DDC2DA30}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.WPers, static=True
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
