"""CIM datatype Voltage (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from tests.runtime.minimodel.unit_symbol import UnitSymbol


class Voltage(CimDatatype):
    """Electrical voltage, can be both AC and DC."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.V

    _cim_meta = ClassMeta(
        cim_name="Voltage",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{00000000-0000-0000-0000-00000000B001}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.V, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
