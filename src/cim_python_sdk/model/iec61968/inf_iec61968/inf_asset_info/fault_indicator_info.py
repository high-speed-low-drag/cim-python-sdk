"""CIM class FaultIndicatorInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.fault_indicator_reset_kind import (
        FaultIndicatorResetKind,
    )


class FaultIndicatorInfo(AssetInfo):
    """Parameters of fault indicator asset."""

    __slots__ = ("reset_kind",)

    reset_kind: FaultIndicatorResetKind | None

    _cim_meta = ClassMeta(
        cim_name="FaultIndicatorInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{04AAC775-8766-4880-B02A-117B106F26A9}",
        attributes=(
            AttrMeta("reset_kind", "resetKind", "FaultIndicatorResetKind", 0, 1, "enumeration"),
        ),
    )

    def __init__(
        self,
        *,
        reset_kind: FaultIndicatorResetKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.reset_kind = reset_kind
