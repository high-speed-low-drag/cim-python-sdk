"""CIM datatype RealEnergy (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class RealEnergy(CimDatatype):
    """Real electrical energy."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.Wh

    _cim_meta = ClassMeta(
        cim_name="RealEnergy",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{FD0D7251-962F-4c57-ACFB-C1F578AB6361}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.Wh, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
