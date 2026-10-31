"""CIM class OilAnalysisPCBAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.oil_analysis_pcb_analog_kind import (
        OilAnalysisPCBAnalogKind,
    )


class OilAnalysisPCBAnalog(AssetAnalog):
    """Asset oil analysis PCB type of analog."""

    __slots__ = ("kind",)

    kind: OilAnalysisPCBAnalogKind | None

    _cim_meta = ClassMeta(
        cim_name="OilAnalysisPCBAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{B4DC7BB6-D455-49e2-87AE-30375070DBDC}",
        attributes=(AttrMeta("kind", "kind", "OilAnalysisPCBAnalogKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: OilAnalysisPCBAnalogKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
