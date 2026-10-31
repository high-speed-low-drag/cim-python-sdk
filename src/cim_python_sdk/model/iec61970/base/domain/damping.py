"""CIM datatype Damping (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta
from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Damping(CimDatatype):
    """Per-unit active power variation with frequency referenced on the system apparent power
    base. Typical values are in the range 1,0 - 2,0."""

    __slots__ = ()

    value_type = float
    unit = UnitSymbol.onePerHz

    _cim_meta = ClassMeta(
        cim_name="Damping",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{9CD49278-B929-4acf-A09E-43660FD1F7F7}",
        kind="cimdatatype",
        attributes=(
            AttrMeta(
                "multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration", static=True
            ),
            AttrMeta(
                "unit", "unit", "UnitSymbol", 0, 1, "enumeration", UnitSymbol.onePerHz, static=True
            ),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )
