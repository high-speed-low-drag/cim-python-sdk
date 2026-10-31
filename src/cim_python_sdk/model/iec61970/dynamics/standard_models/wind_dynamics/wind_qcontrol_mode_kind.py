"""CIM enumeration WindQcontrolModeKind (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WindQcontrolModeKind(CimEnum):
    """General wind turbine Q control modes MqG."""

    voltage = "voltage"
    reactivePower = "reactivePower"
    openLoopReactivePower = "openLoopReactivePower"
    powerFactor = "powerFactor"
    openLooppowerFactor = "openLooppowerFactor"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WindQcontrolModeKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
            guid="{3625636B-98D9-4a47-A2D5-04D9EF31A7EA}",
            kind="enumeration",
        )
    )
