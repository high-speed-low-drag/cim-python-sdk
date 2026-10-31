"""CIM class OilAnalysisMetalsAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_metals_analog_kind import (
        OilAnalysisMetalsAnalogKind,
    )


class OilAnalysisMetalsAnalog(AssetAnalog):
    """Asset oil analysis metals type of analog."""

    __slots__ = ("kind",)

    kind: OilAnalysisMetalsAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisMetalsAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{8721552D-692E-43a1-A287-EDEE8383AED7}",
        attributes=(AttrMeta("kind", "kind", "OilAnalysisMetalsAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisMetalsAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
