"""CIM datatype MagneticField (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class MagneticField(CimDatatype):
    """Magnetic field in nanotesla."""

    __slots__ = ()

    value_type = float
    multiplier = UnitMultiplier.n
    unit = UnitSymbol.T

    _cim_meta = ClassMeta(
        cim_name="MagneticField",
        package="TC57CIM/IEC62325/Environmental/EnvDomain",
        guid="{2C3CA1D1-1DBB-4f95-9BC9-60B0DD26DA65}",
        kind="cimdatatype",
        attributes=(
            AttrMeta(
                "multiplier",
                "multiplier",
                "UnitMultiplier",
                0,
                1,
                "enumeration",
                UnitMultiplier.n,
                static=True,
            ),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.T, static=True),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
