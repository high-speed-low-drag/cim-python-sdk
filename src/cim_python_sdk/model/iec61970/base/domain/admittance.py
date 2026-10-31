"""CIM datatype Admittance (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Admittance(CimDatatype):
    """Ratio of current to voltage."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.S

    _cim_meta = ClassMeta(
        cim_name="Admittance",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{30AC6821-E972-456a-8F64-0765D7361767}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.S, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
