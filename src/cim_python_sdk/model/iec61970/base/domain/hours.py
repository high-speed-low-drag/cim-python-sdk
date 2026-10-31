"""CIM datatype Hours (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Hours(CimDatatype):
    """Time specified in hours."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.h
    multiplier = UnitMultiplier.none

    _cim_meta = ClassMeta(
        cim_name="Hours",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{C8C67111-A8BF-46d8-B8DB-F0336CD201D1}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.h, static=True),
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
