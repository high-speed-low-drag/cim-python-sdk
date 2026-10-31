"""CIM datatype Capacitance (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Capacitance(CimDatatype):
    """Capacitive part of reactance (imaginary part of impedance), at rated frequency."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.F

    _cim_meta = ClassMeta(
        cim_name="Capacitance",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{B2C696FA-9529-4b58-9D82-4062406AEACF}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.F, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
