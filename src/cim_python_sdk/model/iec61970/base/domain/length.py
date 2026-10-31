"""CIM datatype Length (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Length(CimDatatype):
    """Unit of length. It shall be a positive value or zero."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.m

    _cim_meta = ClassMeta(
        cim_name="Length",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{06F9A3F0-3AE3-4ad1-88F8-06C207238C3B}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.m, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
