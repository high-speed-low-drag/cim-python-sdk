"""CIM enumeration GovHydro4ModelKind (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class GovHydro4ModelKind(CimEnum):
    """Possible types of GovHydro4 models."""

    simple = "simple"
    francisPelton = "francisPelton"
    kaplan = "kaplan"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="GovHydro4ModelKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
            guid="{DC8738E4-F4A7-44cc-A3C2-A247C6EC76A7}",
            kind="enumeration",
        )
    )
