"""CIM enumeration IfdBaseKind (TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class IfdBaseKind(CimEnum):
    """Excitation base system mode."""

    ifag = "ifag"
    ifnl = "ifnl"
    iffl = "iffl"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="IfdBaseKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics",
            guid="{2EB6DACC-559E-46ac-A5B8-6BF0C250A461}",
            kind="enumeration",
        )
    )
