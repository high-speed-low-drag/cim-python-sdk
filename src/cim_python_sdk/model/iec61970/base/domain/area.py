"""CIM datatype Area (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Area(CimDatatype):
    """Area."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.m2

    _cim_meta = ClassMeta(
        cim_name="Area",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{BD3D15F2-CB39-41a5-935D-7B8F490ECBF8}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.m2, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
