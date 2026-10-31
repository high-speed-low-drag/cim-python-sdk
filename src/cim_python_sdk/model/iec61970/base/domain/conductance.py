"""CIM datatype Conductance (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Conductance(CimDatatype):
    """Factor by which voltage must be multiplied to give corresponding power lost from a
    circuit. Real part of admittance."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.S

    _cim_meta = ClassMeta(
        cim_name="Conductance",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{CCE4615A-C403-4c96-8122-26904C128276}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.S, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
