"""CIM enumeration WindUVRTQcontrolModeKind (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WindUVRTQcontrolModeKind(CimEnum):
    """UVRT Q control modes MqUVRT."""

    mode0 = "mode0"
    mode1 = "mode1"
    mode2 = "mode2"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WindUVRTQcontrolModeKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
            guid="{74722AE7-62E4-42de-BC4A-5E39E2D3A666}",
            kind="enumeration",
        )
    )
