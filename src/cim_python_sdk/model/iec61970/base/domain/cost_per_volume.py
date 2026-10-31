"""CIM datatype CostPerVolume (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta


class CostPerVolume(CimDatatype):
    """Cost per unit volume."""

    __slots__ = ()

    value_type = float

    _cim_meta = ClassMeta(
        cim_name="CostPerVolume",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{56D3E01F-B21E-4f00-A8F1-CBC80D384B3B}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "Currency", 0, 1, "enumeration"),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
