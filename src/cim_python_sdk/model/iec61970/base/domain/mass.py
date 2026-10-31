"""CIM datatype Mass (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier


class Mass(CimDatatype):
    """Mass."""

    __slots__ = ()

    value_type = float
    multiplier = UnitMultiplier.k

    _cim_meta = ClassMeta(
        cim_name="Mass",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{3090EC66-8B19-4224-A206-00BFE70ECED0}",
        kind="cimdatatype",
        attributes=(
            AttrMeta(
                "multiplier",
                "multiplier",
                "UnitMultiplier",
                0,
                1,
                "enumeration",
                UnitMultiplier.k,
                static=True,
            ),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
