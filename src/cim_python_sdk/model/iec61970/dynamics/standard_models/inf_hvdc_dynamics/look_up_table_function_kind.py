"""CIM enumeration LookUpTableFunctionKind (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class LookUpTableFunctionKind(CimEnum):
    """CIM enumeration LookUpTableFunctionKind."""

    additionalQcurrent = "additionalQcurrent"
    vdcol = "vdcol"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="LookUpTableFunctionKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics",
            guid="{3BEBAC1D-EFF7-4733-A4EE-E92CD6AA7910}",
            kind="enumeration",
        )
    )
