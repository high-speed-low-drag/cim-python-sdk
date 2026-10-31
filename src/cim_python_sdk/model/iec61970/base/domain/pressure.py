"""CIM datatype Pressure (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Pressure(CimDatatype):
    """Pressure in pascals."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.Pa

    _cim_meta = ClassMeta(
        cim_name="Pressure",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{BBEF7CB4-FBE0-4bc5-9EB4-A3E586C7F34C}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.Pa, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
