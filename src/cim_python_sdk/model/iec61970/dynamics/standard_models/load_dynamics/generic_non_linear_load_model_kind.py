"""CIM enumeration GenericNonLinearLoadModelKind (TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class GenericNonLinearLoadModelKind(CimEnum):
    """Type of generic non-linear load model."""

    exponentialRecovery = "exponentialRecovery"
    loadAdaptive = "loadAdaptive"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="GenericNonLinearLoadModelKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics",
            guid="{2634FBEB-5D94-469a-B61C-F35CB8FB2012}",
            kind="enumeration",
        )
    )
