"""CIM datatype KiloActivePower (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class KiloActivePower(CimDatatype):
    """Active power in kilowatts."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.W
    multiplier = UnitMultiplier.k

    _cim_meta = ClassMeta(
        cim_name="KiloActivePower",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{BE17081C-6888-4153-B4AB-A672392B7467}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.W, static=True),
            AttrMeta(
                "multiplier",
                "multiplier",
                "UnitMultiplier",
                0,
                1,
                "enumeration",
                UnitMultiplier.k,
                static=True,
            ),
        ),
    )
