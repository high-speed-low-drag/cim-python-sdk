"""CIM datatype Minutes (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Minutes(CimDatatype):
    """Time in minutes."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.min
    multiplier = UnitMultiplier.none

    _cim_meta = ClassMeta(
        cim_name="Minutes",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{68F89418-6302-42a8-8177-5637B46ED1DB}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.min, static=True
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
