"""CIM class OilAnalysisPaperAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_paper_analog_kind import (
        OilAnalysisPaperAnalogKind,
    )


class OilAnalysisPaperAnalog(AssetAnalog):
    """Asset oil inspection paper type of analog."""

    __slots__ = ("kind",)

    kind: OilAnalysisPaperAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisPaperAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{F1469DB0-F04E-4a16-B7A0-BC5659E2BFF0}",
        attributes=(AttrMeta("kind", "kind", "OilAnalysisPaperAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisPaperAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
