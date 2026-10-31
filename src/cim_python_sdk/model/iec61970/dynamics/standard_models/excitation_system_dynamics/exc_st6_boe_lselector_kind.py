"""CIM enumeration ExcST6BOELselectorKind (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ExcST6BOELselectorKind(CimEnum):
    """Types of connections for the OEL input used for static excitation systems type 6B."""

    noOELinput = "noOELinput"
    beforeUEL = "beforeUEL"
    afterUEL = "afterUEL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ExcST6BOELselectorKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
            guid="{C53689DF-C5DD-496d-8153-DFC748199B83}",
            kind="enumeration",
        )
    )
