"""CIM datatype Volume (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Volume(CimDatatype):
    """Volume."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.m3

    _cim_meta = ClassMeta(
        cim_name="Volume",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{20E0B5CF-6DA4-452c-A366-CBE9FC2DF962}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.m3, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
