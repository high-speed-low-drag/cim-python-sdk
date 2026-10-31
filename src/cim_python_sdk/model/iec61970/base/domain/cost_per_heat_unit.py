"""CIM datatype CostPerHeatUnit (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta


class CostPerHeatUnit(CimDatatype):
    """Cost, in units of currency, per quantity of heat generated."""

    __slots__ = ()

    value_type = float

    _cim_meta = ClassMeta(
        cim_name="CostPerHeatUnit",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{E1913AA6-E24F-4b45-BB9B-946567FC7AF6}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "Currency", 0, 1, "enumeration"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
