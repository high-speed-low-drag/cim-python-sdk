"""CIM enumeration ExcIEEEST1AUELselectorKind (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ExcIEEEST1AUELselectorKind(CimEnum):
    """Types of connections for the UEL input used in ExcIEEEST1A."""

    ignoreUELsignal = "ignoreUELsignal"
    inputHVgateVoltageOutput = "inputHVgateVoltageOutput"
    inputHVgateErrorSignal = "inputHVgateErrorSignal"
    inputAddedToErrorSignal = "inputAddedToErrorSignal"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ExcIEEEST1AUELselectorKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
            guid="{1A5A9C7E-881D-4271-A694-3409A68164BC}",
            kind="enumeration",
        )
    )
