"""CIM class InspectionDataSet (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.scheduled_event_data import ScheduledEventData


class InspectionDataSet(ProcedureDataSet):
    """Documents the result of one inspection, for a given attribute of an asset."""

    __slots__ = ("_according_to_schedules", "location_condition")

    location_condition: str | None

    according_to_schedules: Many[ScheduledEventData] = Many(
        EndMeta(
            name="according_to_schedules",
            cim_role="AccordingToSchedules",
            target="cim_python_sdk.model.iec61968.common.scheduled_event_data:ScheduledEventData",
            many=True,
            lower=0,
            upper=None,
            inverse="inspection_data_set",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InspectionDataSet",
        package="TC57CIM/IEC61968/Assets",
        guid="{3E6EAF5A-9EEE-4ef1-B083-0A204C6A67B7}",
        attributes=(AttrMeta("location_condition", "locationCondition", "str", 0, 1, "primitive"),),
        ends=(according_to_schedules.meta,),
    )

    def __init__(
        self,
        *,
        location_condition: str | None = None,
        according_to_schedules: Iterable[ScheduledEventData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.location_condition = location_condition
        if according_to_schedules is not None:
            InspectionDataSet.according_to_schedules.extend(self, according_to_schedules)

    def add_according_to_schedule(self, according_to_schedule: ScheduledEventData) -> Self:
        return InspectionDataSet.according_to_schedules.add(self, according_to_schedule)

    def remove_according_to_schedule(self, according_to_schedule: ScheduledEventData) -> Self:
        return InspectionDataSet.according_to_schedules.remove(self, according_to_schedule)

    def clear_according_to_schedules(self) -> Self:
        return InspectionDataSet.according_to_schedules.clear(self)

    def num_according_to_schedule(self) -> int:
        return InspectionDataSet.according_to_schedules.count(self)
