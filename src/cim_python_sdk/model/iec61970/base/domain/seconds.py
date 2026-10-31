"""CIM datatype Seconds (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Seconds(CimDatatype):
    """Time, in seconds."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.s
    multiplier = UnitMultiplier.none

    _cim_meta = ClassMeta(
        cim_name="Seconds",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{A2008978-193D-4955-8102-599E43C7CFE4}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.s, static=True),
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
