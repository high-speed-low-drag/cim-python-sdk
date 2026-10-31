"""CIM class ScheduledEvent (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.common.scheduled_event_data import ScheduledEventData
    from cim_python_sdk.model.iec61968.common.status import Status


class ScheduledEvent(IdentifiedObject):
    """An event to trigger one or more activities, such as reading a meter, recalculating a
    bill, requesting work, when generating units must be scheduled for maintenance, when a
    transformer is scheduled to be refurbished, etc."""

    __slots__ = ("_assets", "_scheduled_event_data", "duration", "status", "type")

    type: str | None
    duration: float | None  # Seconds
    status: Status | None

    scheduled_event_data: One[ScheduledEventData] = One(
        EndMeta(
            name="scheduled_event_data",
            cim_role="ScheduledEventData",
            target="cim_python_sdk.model.iec61968.common.scheduled_event_data:ScheduledEventData",
            many=False,
            lower=0,
            upper=1,
            inverse="scheduled_events",
            aggregation="none",
        )
    )
    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="scheduled_events",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ScheduledEvent",
        package="TC57CIM/IEC61968/Common",
        guid="{5320DB66-1FF5-4e87-8029-8D8E938E9D72}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("duration", "duration", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            scheduled_event_data.meta,
            assets.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        duration: float | None = None,
        status: Status | None = None,
        scheduled_event_data: ScheduledEventData | None = None,
        assets: Iterable[Asset] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.duration = duration
        self.status = status
        if scheduled_event_data is not None:
            self.scheduled_event_data = scheduled_event_data
        if assets is not None:
            ScheduledEvent.assets.extend(self, assets)

    def add_asset(self, asset: Asset) -> Self:
        return ScheduledEvent.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return ScheduledEvent.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return ScheduledEvent.assets.clear(self)

    def num_asset(self) -> int:
        return ScheduledEvent.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return ScheduledEvent.assets.get_by_mrid(self, mrid)
