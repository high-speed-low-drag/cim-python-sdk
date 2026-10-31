"""CIM datatype Bearing (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Bearing(CimDatatype):
    """The bearing in degrees (with 360 degrees being True North). Measured in degrees
    clockwise from True North. 0 degrees indicates no direction being given."""

    __slots__ = ()

    value_type = float
    multiplier = UnitMultiplier.none
    unit = UnitSymbol.deg

    _cim_meta = ClassMeta(
        cim_name="Bearing",
        package="TC57CIM/IEC62325/Environmental/EnvDomain",
        guid="{FAB258CB-D0F4-49eb-82B5-1E3FE343A1EE}",
        kind="cimdatatype",
        attributes=(
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
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.deg, static=True
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
