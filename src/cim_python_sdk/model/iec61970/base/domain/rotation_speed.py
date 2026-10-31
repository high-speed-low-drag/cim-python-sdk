"""CIM datatype RotationSpeed (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class RotationSpeed(CimDatatype):
    """Number of revolutions per second."""

    __slots__ = ()

    value_type = float
    multiplier = UnitMultiplier.none
    unit = UnitSymbol.Hz

    _cim_meta = ClassMeta(
        cim_name="RotationSpeed",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{D9556FC3-5453-44d9-94C5-07D51D3BAD82}",
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
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.Hz, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
