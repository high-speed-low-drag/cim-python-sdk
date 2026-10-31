"""CIM class BaseWork (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.priority import Priority
    from cim_python_sdk.model.iec61968.customers.service_request_kind import ServiceRequestKind
    from cim_python_sdk.model.iec61968.work.work_activity_record import WorkActivityRecord
    from cim_python_sdk.model.iec61968.work.work_location import WorkLocation
    from cim_python_sdk.model.iec61968.work.work_status_kind import WorkStatusKind
    from cim_python_sdk.model.iec61968.work.work_time_schedule import WorkTimeSchedule


class BaseWork(Document):
    """Common representation for work and work tasks."""

    __slots__ = (
        "_time_schedules",
        "_work_activity_records",
        "_work_location",
        "kind",
        "priority",
        "status_kind",
    )

    kind: ServiceRequestKind | None
    priority: Priority | None
    status_kind: WorkStatusKind | None

    time_schedules: Many[WorkTimeSchedule] = Many(
        EndMeta(
            name="time_schedules",
            cim_role="TimeSchedules",
            target="cim_python_sdk.model.iec61968.work.work_time_schedule:WorkTimeSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="base_work",
            aggregation="none",
        )
    )
    work_location: One[WorkLocation] = One(
        EndMeta(
            name="work_location",
            cim_role="WorkLocation",
            target="cim_python_sdk.model.iec61968.work.work_location:WorkLocation",
            many=False,
            lower=0,
            upper=1,
            inverse="base_works",
            aggregation="none",
        )
    )
    work_activity_records: Many[WorkActivityRecord] = Many(
        EndMeta(
            name="work_activity_records",
            cim_role="WorkActivityRecords",
            target="cim_python_sdk.model.iec61968.work.work_activity_record:WorkActivityRecord",
            many=True,
            lower=0,
            upper=None,
            inverse="base_work",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BaseWork",
        package="TC57CIM/IEC61968/Work",
        guid="{1E095EF2-6606-4ede-A9E1-40D0E9881415}",
        attributes=(
            AttrMeta("kind", "kind", "ServiceRequestKind", 0, 1, "enumeration"),
            AttrMeta("priority", "priority", "Priority", 0, 1, "compound"),
            AttrMeta("status_kind", "statusKind", "WorkStatusKind", 0, 1, "enumeration"),
        ),
        ends=(
            time_schedules.meta,
            work_location.meta,
            work_activity_records.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: ServiceRequestKind | None = None,
        priority: Priority | None = None,
        status_kind: WorkStatusKind | None = None,
        time_schedules: Iterable[WorkTimeSchedule] | None = None,
        work_location: WorkLocation | None = None,
        work_activity_records: Iterable[WorkActivityRecord] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.priority = priority
        self.status_kind = status_kind
        if time_schedules is not None:
            BaseWork.time_schedules.extend(self, time_schedules)
        if work_location is not None:
            self.work_location = work_location
        if work_activity_records is not None:
            BaseWork.work_activity_records.extend(self, work_activity_records)

    def add_time_schedule(self, time_schedule: WorkTimeSchedule) -> Self:
        return BaseWork.time_schedules.add(self, time_schedule)

    def remove_time_schedule(self, time_schedule: WorkTimeSchedule) -> Self:
        return BaseWork.time_schedules.remove(self, time_schedule)

    def clear_time_schedules(self) -> Self:
        return BaseWork.time_schedules.clear(self)

    def num_time_schedule(self) -> int:
        return BaseWork.time_schedules.count(self)

    def get_time_schedule_by_mrid(self, mrid: str) -> WorkTimeSchedule | None:
        return BaseWork.time_schedules.get_by_mrid(self, mrid)

    def add_work_activity_record(self, work_activity_record: WorkActivityRecord) -> Self:
        return BaseWork.work_activity_records.add(self, work_activity_record)

    def remove_work_activity_record(self, work_activity_record: WorkActivityRecord) -> Self:
        return BaseWork.work_activity_records.remove(self, work_activity_record)

    def clear_work_activity_records(self) -> Self:
        return BaseWork.work_activity_records.clear(self)

    def num_work_activity_record(self) -> int:
        return BaseWork.work_activity_records.count(self)

    def get_work_activity_record_by_mrid(self, mrid: str) -> WorkActivityRecord | None:
        return BaseWork.work_activity_records.get_by_mrid(self, mrid)
