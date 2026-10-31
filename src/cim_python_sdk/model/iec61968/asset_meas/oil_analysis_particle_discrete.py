"""CIM class OilAnalysisParticleDiscrete (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_discrete import AssetDiscrete

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_particle_discrete_kind import (
        OilAnalysisParticleDiscreteKind,
    )


class OilAnalysisParticleDiscrete(AssetDiscrete):
    """Asset oil analysis particle type of discrete."""

    __slots__ = ("kind",)

    kind: OilAnalysisParticleDiscreteKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisParticleDiscrete",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{8495F790-20B3-4a9a-8B8A-9C452C9B3EDA}",
        attributes=(
            AttrMeta("kind", "kind", "OilAnalysisParticleDiscreteKind", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisParticleDiscreteKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
