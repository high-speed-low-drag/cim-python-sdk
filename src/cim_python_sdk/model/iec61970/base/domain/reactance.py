"""CIM datatype Reactance (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Reactance(CimDatatype):
    """Reactance (imaginary part of impedance), at rated frequency."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.ohm

    _cim_meta = ClassMeta(
        cim_name="Reactance",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{F1C90FB4-B7BE-4528-A974-E36BBEAB8616}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.ohm, static=True
            ),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
