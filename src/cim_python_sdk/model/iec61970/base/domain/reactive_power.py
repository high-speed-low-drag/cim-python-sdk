"""CIM datatype ReactivePower (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class ReactivePower(CimDatatype):
    """Product of RMS value of the voltage and the RMS value of the quadrature component of the
    current."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.VAr

    _cim_meta = ClassMeta(
        cim_name="ReactivePower",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{C15CB4E4-4430-43ea-AF69-BC3250B1F4A3}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.VAr, static=True
            ),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
