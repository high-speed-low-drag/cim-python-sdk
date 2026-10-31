"""CIM class ProtectionEquipmentInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ProtectionEquipmentInfo(AssetInfo):
    """Properties of protection equipment asset."""

    __slots__ = ("ground_trip", "phase_trip")

    ground_trip: float | None  # CurrentFlow
    phase_trip: float | None  # CurrentFlow

    _cim_meta = ClassMeta(
        cim_name="ProtectionEquipmentInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{8996F48A-CD6B-4c7a-A7B4-AA9C5F8E51BA}",
        attributes=(
            AttrMeta("ground_trip", "groundTrip", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("phase_trip", "phaseTrip", "CurrentFlow", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ground_trip: float | None = None,
        phase_trip: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ground_trip = ground_trip
        self.phase_trip = phase_trip
