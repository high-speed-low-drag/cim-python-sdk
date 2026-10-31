"""CIM datatype Speed (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Speed(CimDatatype):
    """Distance per unit of time."""

    __slots__ = ()

    value_type = float
    multiplier = UnitMultiplier.none
    unit = UnitSymbol.mPers

    _cim_meta = ClassMeta(
        cim_name="Speed",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{B2B55BF9-D1CD-4a20-8B96-E9509B356C6D}",
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
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.mPers, static=True
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
