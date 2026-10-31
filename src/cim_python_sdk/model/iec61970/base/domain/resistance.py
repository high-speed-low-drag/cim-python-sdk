"""CIM datatype Resistance (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Resistance(CimDatatype):
    """Resistance (real part of impedance)."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.ohm

    _cim_meta = ClassMeta(
        cim_name="Resistance",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{EDB281E6-BBB4-438d-953B-7D746CAF55B5}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.ohm, static=True
            ),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
