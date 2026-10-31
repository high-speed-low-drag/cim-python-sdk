"""CIM datatype CostRate (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta


class CostRate(CimDatatype):
    """Cost, in units of currency, per elapsed time."""

    __slots__ = ()

    value_type = float

    _cim_meta = ClassMeta(
        cim_name="CostRate",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{A8B9F2B7-69E6-4698-8492-D6A8E70D8755}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "Currency", 0, 1, "enumeration"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
