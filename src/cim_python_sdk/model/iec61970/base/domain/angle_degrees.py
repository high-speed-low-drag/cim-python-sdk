"""CIM datatype AngleDegrees (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class AngleDegrees(CimDatatype):
    """Measurement of angle in degrees."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.deg
    multiplier = UnitMultiplier.none

    _cim_meta = ClassMeta(
        cim_name="AngleDegrees",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{A633BDC9-A238-4f69-AF1B-FF8A5C2FFCC8}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.deg, static=True
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
