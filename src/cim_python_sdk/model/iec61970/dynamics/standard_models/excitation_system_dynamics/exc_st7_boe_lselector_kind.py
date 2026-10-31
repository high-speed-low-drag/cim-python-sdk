"""CIM enumeration ExcST7BOELselectorKind (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ExcST7BOELselectorKind(CimEnum):
    """Types of connections for the OEL input used for static excitation systems type 7B."""

    noOELinput = "noOELinput"
    addVref = "addVref"
    inputLVgate = "inputLVgate"
    outputLVgate = "outputLVgate"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ExcST7BOELselectorKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
            guid="{195B8230-9DE1-41fb-871D-72529EE326A1}",
            kind="enumeration",
        )
    )
