"""CIM datatype HeatRate (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class HeatRate(CimDatatype):
    """Heat generated, in energy per time unit of elapsed time."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.J

    _cim_meta = ClassMeta(
        cim_name="HeatRate",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{8E0A1478-92E7-445a-9F23-9BCEB17FD303}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.J, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
