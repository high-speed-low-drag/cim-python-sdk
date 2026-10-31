"""CIM class OilAnalysisMoistureAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_moisture_analog_kind import (
        OilAnalysisMoistureAnalogKind,
    )


class OilAnalysisMoistureAnalog(AssetAnalog):
    """Asset oil analysis moisture type of analog."""

    __slots__ = ("kind",)

    kind: OilAnalysisMoistureAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisMoistureAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{6B74F4C9-042F-4a13-9428-8AB9CEFAC414}",
        attributes=(
            AttrMeta("kind", "kind", "OilAnalysisMoistureAnalogKind", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisMoistureAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
