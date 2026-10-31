"""CIM datatype CostPerEnergyUnit (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta


class CostPerEnergyUnit(CimDatatype):
    """Cost, in units of currency, per quantity of electrical energy generated."""

    __slots__ = ()

    value_type = float

    _cim_meta = ClassMeta(
        cim_name="CostPerEnergyUnit",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{781B4357-DF24-4f4f-BBE3-8C8CE1C0F2E5}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "Currency", 0, 1, "enumeration"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
