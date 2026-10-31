"""CIM datatype Susceptance (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Susceptance(CimDatatype):
    """Imaginary part of admittance."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.S

    _cim_meta = ClassMeta(
        cim_name="Susceptance",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{F246F97E-529D-4ec3-9F06-BAF4AFD0829B}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.S, static=True),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
        ),
    )
