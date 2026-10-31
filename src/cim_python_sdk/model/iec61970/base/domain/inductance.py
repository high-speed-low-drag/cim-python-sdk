"""CIM datatype Inductance (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Inductance(CimDatatype):
    """Inductive part of reactance (imaginary part of impedance), at rated frequency."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.H

    _cim_meta = ClassMeta(
        cim_name="Inductance",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{A5C20135-6480-450b-812C-23263BCC8553}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.H, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
