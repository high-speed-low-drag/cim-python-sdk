"""CIM class OilAnalysisFluidDiscrete (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_discrete import AssetDiscrete

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_fluid_discrete_kind import (
        OilAnalysisFluidDiscreteKind,
    )


class OilAnalysisFluidDiscrete(AssetDiscrete):
    """Asset oil analysis fluid type of discrete."""

    __slots__ = ("kind",)

    kind: OilAnalysisFluidDiscreteKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisFluidDiscrete",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{2B492897-7038-4a4f-85D2-9FA689A45A21}",
        attributes=(AttrMeta("kind", "kind", "OilAnalysisFluidDiscreteKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisFluidDiscreteKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
