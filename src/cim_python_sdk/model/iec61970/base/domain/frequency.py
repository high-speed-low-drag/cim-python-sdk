"""CIM datatype Frequency (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Frequency(CimDatatype):
    """Cycles per second."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.Hz

    _cim_meta = ClassMeta(
        cim_name="Frequency",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{DD71FE93-4683-440c-8622-A8AA2EB44F6F}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.Hz, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
