"""CIM datatype ConductancePerLength (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class ConductancePerLength(CimDatatype):
    """Real part of admittance per unit of length."""

    __slots__ = ()

    value_type = float
    multiplier = UnitMultiplier.none
    unit = UnitSymbol.SPerm

    _cim_meta = ClassMeta(
        cim_name="ConductancePerLength",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{0C25DC23-EAD4-4ea0-B0C3-D7C46488E3F8}",
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
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.SPerm, static=True
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
