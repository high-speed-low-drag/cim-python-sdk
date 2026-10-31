"""CIM datatype Emission (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Emission(CimDatatype):
    """Quantity of emission per fuel heat content."""

    __slots__ = ()

    value_type = float
    multiplier = UnitMultiplier.none
    unit = UnitSymbol.kgPerJ

    _cim_meta = ClassMeta(
        cim_name="Emission",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{E1046D37-77EE-42b0-832A-8AF115835122}",
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
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.kgPerJ, static=True
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
