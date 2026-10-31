"""CIM class OilAnalysisParticleAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_particle_analog_kind import (
        OilAnalysisParticleAnalogKind,
    )


class OilAnalysisParticleAnalog(AssetAnalog):
    """Asset oil analysis particle type of analog."""

    __slots__ = ("kind",)

    kind: OilAnalysisParticleAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisParticleAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{D22A10AB-551E-47be-9E54-5F3D1857B7BB}",
        attributes=(
            AttrMeta("kind", "kind", "OilAnalysisParticleAnalogKind", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisParticleAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
