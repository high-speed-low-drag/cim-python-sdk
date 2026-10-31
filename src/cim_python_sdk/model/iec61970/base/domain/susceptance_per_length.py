"""CIM datatype SusceptancePerLength (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class SusceptancePerLength(CimDatatype):
    """Imaginary part of admittance per unit of length."""

    __slots__ = ()

    value_type = float
    multiplier = UnitMultiplier.none
    unit = UnitSymbol.SPerm

    _cim_meta = ClassMeta(
        cim_name="SusceptancePerLength",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{59A364BC-34EB-41b6-810C-88484A2D929C}",
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
