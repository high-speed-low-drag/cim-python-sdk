"""CIM enumeration StaticLoadModelKind (TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class StaticLoadModelKind(CimEnum):
    """Type of static load model."""

    exponential = "exponential"
    zIP1 = "zIP1"
    zIP2 = "zIP2"
    constantZ = "constantZ"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="StaticLoadModelKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics",
            guid="{9D882F45-ACA2-4c41-B820-A8C4BED1126B}",
            kind="enumeration",
        )
    )
