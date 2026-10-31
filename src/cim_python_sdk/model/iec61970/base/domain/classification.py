"""CIM datatype Classification (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Classification(CimDatatype):
    """Classification of level. Specify as 1..n, with 1 being the most detailed, highest
    priority, etc as described on the attribute using this data type."""

    __slots__ = ()

    value_type = int
    unit = UnitSymbol.none
    multiplier = UnitMultiplier.none

    _cim_meta = ClassMeta(
        cim_name="Classification",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{567D00ED-9FD9-4cd1-9B12-70AEA6F11BFC}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "int", 0, 1, "primitive"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.none, static=True
            ),
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
        ),
    )
