"""CIM datatype CurrentFlow (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class CurrentFlow(CimDatatype):
    """Electrical current with sign convention: positive flow is out of the conducting
    equipment into the connectivity node. Can be both AC and DC."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.A

    _cim_meta = ClassMeta(
        cim_name="CurrentFlow",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{DC3FD69C-E9B2-440d-A113-BE84B71BA691}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.A, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
