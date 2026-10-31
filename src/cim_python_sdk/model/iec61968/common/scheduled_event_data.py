"""CIM class ScheduledEventData (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.inspection_data_set import InspectionDataSet
    from cim_python_sdk.model.iec61968.common.scheduled_event import ScheduledEvent
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class ScheduledEventData(CimObject):
    """Schedule parameters for an activity that is to occur, is occurring, or has completed."""

    __slots__ = (
        "_inspection_data_set",
        "_scheduled_events",
        "estimated_window",
        "requested_window",
        "status",
    )

    requested_window: DateTimeInterval | None
    estimated_window: DateTimeInterval | None
    status: Status | None

    scheduled_events: Many[ScheduledEvent] = Many(
        EndMeta(
            name="scheduled_events",
            cim_role="ScheduledEvents",
            target="cim_python_sdk.model.iec61968.common.scheduled_event:ScheduledEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="scheduled_event_data",
            aggregation="none",
        )
    )
    inspection_data_set: One[InspectionDataSet] = One(
        EndMeta(
            name="inspection_data_set",
            cim_role="InspectionDataSet",
            target="cim_python_sdk.model.iec61968.assets.inspection_data_set:InspectionDataSet",
            many=False,
            lower=1,
            upper=1,
            inverse="according_to_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ScheduledEventData",
        package="TC57CIM/IEC61968/Common",
        guid="{49C8A8CF-3B31-49e1-AF68-279D11721DE2}",
        attributes=(
            AttrMeta("requested_window", "requestedWindow", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("estimated_window", "estimatedWindow", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            scheduled_events.meta,
            inspection_data_set.meta,
        ),
    )

    def __init__(
        self,
        *,
        requested_window: DateTimeInterval | None = None,
        estimated_window: DateTimeInterval | None = None,
        status: Status | None = None,
        scheduled_events: Iterable[ScheduledEvent] | None = None,
        inspection_data_set: InspectionDataSet | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.requested_window = requested_window
        self.estimated_window = estimated_window
        self.status = status
        if scheduled_events is not None:
            ScheduledEventData.scheduled_events.extend(self, scheduled_events)
        if inspection_data_set is not None:
            self.inspection_data_set = inspection_data_set

    def add_scheduled_event(self, scheduled_event: ScheduledEvent) -> Self:
        return ScheduledEventData.scheduled_events.add(self, scheduled_event)

    def remove_scheduled_event(self, scheduled_event: ScheduledEvent) -> Self:
        return ScheduledEventData.scheduled_events.remove(self, scheduled_event)

    def clear_scheduled_events(self) -> Self:
        return ScheduledEventData.scheduled_events.clear(self)

    def num_scheduled_event(self) -> int:
        return ScheduledEventData.scheduled_events.count(self)

    def get_scheduled_event_by_mrid(self, mrid: str) -> ScheduledEvent | None:
        return ScheduledEventData.scheduled_events.get_by_mrid(self, mrid)
