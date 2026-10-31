"""CIM enumeration RemoteSignalKind (TC57CIM/IEC61970/Dynamics/StandardInterconnections). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RemoteSignalKind(CimEnum):
    """Type of input signal coming from remote bus."""

    remoteBusVoltageFrequency = "remoteBusVoltageFrequency"
    remoteBusVoltageFrequencyDeviation = "remoteBusVoltageFrequencyDeviation"
    remoteBusFrequency = "remoteBusFrequency"
    remoteBusFrequencyDeviation = "remoteBusFrequencyDeviation"
    remoteBusVoltageAmplitude = "remoteBusVoltageAmplitude"
    remoteBusVoltage = "remoteBusVoltage"
    remoteBranchCurrentAmplitude = "remoteBranchCurrentAmplitude"
    remoteBusVoltageAmplitudeDerivative = "remoteBusVoltageAmplitudeDerivative"
    remotePuBusVoltageDerivative = "remotePuBusVoltageDerivative"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RemoteSignalKind",
            package="TC57CIM/IEC61970/Dynamics/StandardInterconnections",
            guid="{8A481858-022C-4903-B46C-7440303AB35A}",
            kind="enumeration",
        )
    )
