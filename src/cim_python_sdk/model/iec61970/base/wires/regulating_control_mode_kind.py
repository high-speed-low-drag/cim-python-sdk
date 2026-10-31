"""CIM enumeration RegulatingControlModeKind (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RegulatingControlModeKind(CimEnum):
    """The kind of regulation model. For example regulating voltage, reactive power, active
    power, etc."""

    voltage = "voltage"
    activePower = "activePower"
    reactivePower = "reactivePower"
    currentFlow = "currentFlow"
    admittance = "admittance"
    timeScheduled = "timeScheduled"
    temperature = "temperature"
    powerFactor = "powerFactor"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RegulatingControlModeKind",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{7AA04AD0-E999-4595-877D-33844C01F860}",
            kind="enumeration",
        )
    )
