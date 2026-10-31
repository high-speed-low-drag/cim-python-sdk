"""CIM datatype ActivePowerPerFrequency (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class ActivePowerPerFrequency(CimDatatype):
    """Active power variation with frequency."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.WPers

    _cim_meta = ClassMeta(
        cim_name="ActivePowerPerFrequency",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{322D4C26-DEB6-4f9b-98CF-BA06ACD58EF8}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.WPers, static=True
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
