"""CIM datatype ActivePower (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class ActivePower(CimDatatype):
    """Product of RMS value of the voltage and the RMS value of the in-phase component of the
    current."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.W

    _cim_meta = ClassMeta(
        cim_name="ActivePower",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{E52EDC2D-8972-42c7-A7EB-D8C017E138A4}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.W, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
