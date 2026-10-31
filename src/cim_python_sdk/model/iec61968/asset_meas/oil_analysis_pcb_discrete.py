"""CIM class OilAnalysisPCBDiscrete (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_discrete import AssetDiscrete

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_pcb_discrete_kind import (
        OilAnalysisPCBDiscreteKind,
    )


class OilAnalysisPCBDiscrete(AssetDiscrete):
    """Asset oil analysis PCB type of discrete."""

    __slots__ = ("kind",)

    kind: OilAnalysisPCBDiscreteKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisPCBDiscrete",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{3F028E3C-2BD8-43ad-A73F-F26F4C1C30AF}",
        attributes=(AttrMeta("kind", "kind", "OilAnalysisPCBDiscreteKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisPCBDiscreteKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
