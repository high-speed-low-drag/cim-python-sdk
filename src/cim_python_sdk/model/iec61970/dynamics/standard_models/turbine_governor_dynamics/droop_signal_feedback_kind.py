"""CIM enumeration DroopSignalFeedbackKind (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DroopSignalFeedbackKind(CimEnum):
    """Governor droop signal feedback source."""

    electricalPower = "electricalPower"
    none = "none"
    fuelValveStroke = "fuelValveStroke"
    governorOutput = "governorOutput"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DroopSignalFeedbackKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
            guid="{1E70C8DC-5E3B-4808-80FE-4D191596ABE9}",
            kind="enumeration",
        )
    )
