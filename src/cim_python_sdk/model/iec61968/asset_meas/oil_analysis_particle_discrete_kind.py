"""CIM enumeration OilAnalysisParticleDiscreteKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisParticleDiscreteKind(CimEnum):
    """Discretes representing oil particulate analysis result."""

    opacity = "opacity"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisParticleDiscreteKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{4C443F53-AB38-4774-922D-140EFB8852F6}",
            kind="enumeration",
        )
    )
