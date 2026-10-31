"""CIM enumeration ExcST7BUELselectorKind (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ExcST7BUELselectorKind(CimEnum):
    """Types of connections for the UEL input used for static excitation systems type 7B."""

    noUELinput = "noUELinput"
    addVref = "addVref"
    inputHVgate = "inputHVgate"
    outputHVgate = "outputHVgate"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ExcST7BUELselectorKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
            guid="{3777F9AB-A057-48e3-B662-216096146DB0}",
            kind="enumeration",
        )
    )
