"""CIM enumeration PhaseConnectedFaultKind (TC57CIM/IEC61970/Base/Faults). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PhaseConnectedFaultKind(CimEnum):
    """The type of fault connection among phases."""

    lineToGround = "lineToGround"
    lineToLine = "lineToLine"
    lineToLineToGround = "lineToLineToGround"
    lineOpen = "lineOpen"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PhaseConnectedFaultKind",
            package="TC57CIM/IEC61970/Base/Faults",
            guid="{B8167562-D487-4e40-82F9-26C9E487E1F1}",
            kind="enumeration",
        )
    )
