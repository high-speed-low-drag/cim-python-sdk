"""CIM datatype AngleRadians (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class AngleRadians(CimDatatype):
    """Phase angle in radians."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.rad
    multiplier = UnitMultiplier.none

    _cim_meta = ClassMeta(
        cim_name="AngleRadians",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{E491E83D-03A0-4cad-86D4-30A09EF320F3}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.rad, static=True
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
