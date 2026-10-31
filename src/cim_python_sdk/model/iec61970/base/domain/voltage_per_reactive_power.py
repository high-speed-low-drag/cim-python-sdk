"""CIM datatype VoltagePerReactivePower (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class VoltagePerReactivePower(CimDatatype):
    """Voltage variation with reactive power."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.VPerVAr

    _cim_meta = ClassMeta(
        cim_name="VoltagePerReactivePower",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{00D99B0C-4D20-43b7-AFA4-B0F9746CFE74}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.VPerVAr, static=True
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
