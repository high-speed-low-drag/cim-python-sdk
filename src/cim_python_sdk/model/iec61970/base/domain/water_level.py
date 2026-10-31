"""CIM datatype WaterLevel (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class WaterLevel(CimDatatype):
    """Reservoir water level referred to a given datum such as mean sea level."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.m

    _cim_meta = ClassMeta(
        cim_name="WaterLevel",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{97337107-69C4-4b94-B996-1375EF171312}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.m, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
