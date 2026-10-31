"""CIM class OilAnalysisGasAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_gas_analog_kind import (
        OilAnalysisGasAnalogKind,
    )


class OilAnalysisGasAnalog(AssetAnalog):
    """Asset oil analysis gas type of analog."""

    __slots__ = ("kind",)

    kind: OilAnalysisGasAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisGasAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{5C08DE43-EAD9-479f-A078-ED491F372F54}",
        attributes=(AttrMeta("kind", "kind", "OilAnalysisGasAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisGasAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
