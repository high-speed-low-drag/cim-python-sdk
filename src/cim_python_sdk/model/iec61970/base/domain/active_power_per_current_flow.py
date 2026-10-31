"""CIM datatype ActivePowerPerCurrentFlow (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class ActivePowerPerCurrentFlow(CimDatatype):
    """Active power variation with current flow."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.WPerA

    _cim_meta = ClassMeta(
        cim_name="ActivePowerPerCurrentFlow",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{D0F4E10E-A379-4a83-A452-974B8D2B45AD}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.WPerA, static=True
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
