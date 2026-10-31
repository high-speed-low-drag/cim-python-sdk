"""CIM enumeration ExcREXSFeedbackSignalKind (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ExcREXSFeedbackSignalKind(CimEnum):
    """Types of rate feedback signals."""

    fieldVoltage = "fieldVoltage"
    fieldCurrent = "fieldCurrent"
    outputVoltage = "outputVoltage"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ExcREXSFeedbackSignalKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
            guid="{D5C43B1C-5D32-4906-9916-02A0E8D90985}",
            kind="enumeration",
        )
    )
