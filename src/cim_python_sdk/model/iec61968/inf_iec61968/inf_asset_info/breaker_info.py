"""CIM class BreakerInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.old_switch_info import OldSwitchInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class BreakerInfo(OldSwitchInfo):
    """Properties of breaker assets."""

    __slots__ = ("phase_trip",)

    phase_trip: float | None  # CurrentFlow

    _cim_meta = ClassMeta(
        cim_name="BreakerInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{5C4FDE4B-F495-43fa-A2C1-9E015D4E32CF}",
        attributes=(AttrMeta("phase_trip", "phaseTrip", "CurrentFlow", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        phase_trip: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.phase_trip = phase_trip
