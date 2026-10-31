"""CIM enumeration WindPlantQcontrolModeKind (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WindPlantQcontrolModeKind(CimEnum):
    """Reactive power/voltage controller mode."""

    reactivePower = "reactivePower"
    powerFactor = "powerFactor"
    uqStatic = "uqStatic"
    voltageControl = "voltageControl"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WindPlantQcontrolModeKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
            guid="{599D33AA-458E-44cd-958D-CAEF63E8EAA5}",
            kind="enumeration",
        )
    )
