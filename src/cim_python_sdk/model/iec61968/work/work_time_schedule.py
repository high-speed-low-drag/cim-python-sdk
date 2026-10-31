"""CIM class WorkTimeSchedule (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.time_schedule import TimeSchedule

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.customers.service_request import ServiceRequest
    from cim_python_sdk.model.iec61968.work.base_work import BaseWork
    from cim_python_sdk.model.iec61968.work.work_time_schedule_kind import WorkTimeScheduleKind


class WorkTimeSchedule(TimeSchedule):
    """Time schedule specific to work."""

    __slots__ = ("_base_work", "_service_request", "kind")

    kind: WorkTimeScheduleKind | None

    base_work: One[BaseWork] = One(
        EndMeta(
            name="base_work",
            cim_role="BaseWork",
            target="cim_python_sdk.model.iec61968.work.base_work:BaseWork",
            many=False,
            lower=0,
            upper=1,
            inverse="time_schedules",
            aggregation="none",
        )
    )
    service_request: One[ServiceRequest] = One(
        EndMeta(
            name="service_request",
            cim_role="ServiceRequest",
            target="cim_python_sdk.model.iec61968.customers.service_request:ServiceRequest",
            many=False,
            lower=0,
            upper=1,
            inverse="work_time_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WorkTimeSchedule",
        package="TC57CIM/IEC61968/Work",
        guid="{151098F5-3E82-403f-89F2-3D53C5DF65E7}",
        attributes=(AttrMeta("kind", "kind", "WorkTimeScheduleKind", 0, 1, "enumeration"),),
        ends=(
            base_work.meta,
            service_request.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: WorkTimeScheduleKind | None = None,
        base_work: BaseWork | None = None,
        service_request: ServiceRequest | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if base_work is not None:
            self.base_work = base_work
        if service_request is not None:
            self.service_request = service_request
