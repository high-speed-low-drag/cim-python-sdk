"""CIM compound FaultImpedance (TC57CIM/IEC61970/Base/Faults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class FaultImpedance(CimCompound):
    """Impedance description for the fault."""

    __slots__ = ("r_ground", "r_line_to_line", "x_ground", "x_line_to_line")

    r_ground: float | None  # Resistance
    r_line_to_line: float | None  # Resistance
    x_ground: float | None  # Reactance
    x_line_to_line: float | None  # Reactance

    _cim_meta = ClassMeta(
        cim_name="FaultImpedance",
        package="TC57CIM/IEC61970/Base/Faults",
        guid="{1BEA10DB-2F71-467b-82A6-6C453C5657A5}",
        kind="compound",
        attributes=(
            AttrMeta("r_ground", "rGround", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r_line_to_line", "rLineToLine", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("x_ground", "xGround", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_line_to_line", "xLineToLine", "Reactance", 0, 1, "cimdatatype"),
        ),
    )
