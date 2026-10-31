"""CIM datatype ApparentPower (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class ApparentPower(CimDatatype):
    """Product of the RMS value of the voltage and the RMS value of the current."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.VA

    _cim_meta = ClassMeta(
        cim_name="ApparentPower",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{95576B4A-D9AC-49fc-82ED-CB6DB2CE8584}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.VA, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
