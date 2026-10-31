"""CIM class RecloserInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.old_switch_info import OldSwitchInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class RecloserInfo(OldSwitchInfo):
    """Properties of recloser assets."""

    __slots__ = (
        "ground_trip_capable",
        "ground_trip_normal_enabled",
        "ground_trip_rating",
        "phase_trip_rating",
        "reclose_lockout_count",
    )

    phase_trip_rating: float | None  # CurrentFlow
    reclose_lockout_count: int | None
    ground_trip_capable: bool | None
    ground_trip_normal_enabled: bool | None
    ground_trip_rating: float | None  # CurrentFlow

    _cim_meta = ClassMeta(
        cim_name="RecloserInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{DC3A327E-9773-42d8-B464-66CCD91FFBFF}",
        attributes=(
            AttrMeta("phase_trip_rating", "phaseTripRating", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("reclose_lockout_count", "recloseLockoutCount", "int", 0, 1, "primitive"),
            AttrMeta("ground_trip_capable", "groundTripCapable", "bool", 0, 1, "primitive"),
            AttrMeta(
                "ground_trip_normal_enabled", "groundTripNormalEnabled", "bool", 0, 1, "primitive"
            ),
            AttrMeta("ground_trip_rating", "groundTripRating", "CurrentFlow", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        phase_trip_rating: float | None = None,
        reclose_lockout_count: int | None = None,
        ground_trip_capable: bool | None = None,
        ground_trip_normal_enabled: bool | None = None,
        ground_trip_rating: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phase_trip_rating = phase_trip_rating
        self.reclose_lockout_count = reclose_lockout_count
        self.ground_trip_capable = ground_trip_capable
        self.ground_trip_normal_enabled = ground_trip_normal_enabled
        self.ground_trip_rating = ground_trip_rating
