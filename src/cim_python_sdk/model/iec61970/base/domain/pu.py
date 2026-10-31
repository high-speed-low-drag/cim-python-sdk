"""CIM datatype PU (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class PU(CimDatatype):
    """Per Unit - a positive or negative value referred to a defined base. Values typically
    range from -10 to +10."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.none
    multiplier = UnitMultiplier.none

    _cim_meta = ClassMeta(
        cim_name="PU",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{B47F1EC8-BE4F-47df-9ACA-3F12A128BF85}",
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
