"""CIM class ServiceRequest (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.work.work_request import WorkRequest

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.customers.service_kind import ServiceKind
    from cim_python_sdk.model.iec61968.customers.service_location import ServiceLocation
    from cim_python_sdk.model.iec61968.customers.service_request_kind import ServiceRequestKind
    from cim_python_sdk.model.iec61968.work.work_time_schedule import WorkTimeSchedule


class ServiceRequest(WorkRequest):
    """CIM class ServiceRequest."""

    __slots__ = (
        "_customer",
        "_service_location",
        "_work_time_schedule",
        "appointment_requested",
        "kind",
        "service_kind",
        "service_size",
    )

    appointment_requested: bool | None
    kind: ServiceRequestKind | None
    service_kind: ServiceKind | None
    service_size: str | None

    work_time_schedule: Many[WorkTimeSchedule] = Many(
        EndMeta(
            name="work_time_schedule",
            cim_role="WorkTimeSchedule",
            target="cim_python_sdk.model.iec61968.work.work_time_schedule:WorkTimeSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="service_request",
            aggregation="none",
        )
    )
    service_location: One[ServiceLocation] = One(
        EndMeta(
            name="service_location",
            cim_role="ServiceLocation",
            target="cim_python_sdk.model.iec61968.customers.service_location:ServiceLocation",
            many=False,
            lower=0,
            upper=1,
            inverse="service_request",
            aggregation="none",
        )
    )
    customer: One[Customer] = One(
        EndMeta(
            name="customer",
            cim_role="Customer",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=False,
            lower=0,
            upper=1,
            inverse="service_request",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ServiceRequest",
        package="TC57CIM/IEC61968/Customers",
        guid="{36ADC4E2-651D-4ce9-9E50-A9513D380F6C}",
        attributes=(
            AttrMeta("appointment_requested", "appointmentRequested", "bool", 1, 1, "primitive"),
            AttrMeta("kind", "kind", "ServiceRequestKind", 1, 1, "enumeration"),
            AttrMeta("service_kind", "serviceKind", "ServiceKind", 1, 1, "enumeration"),
            AttrMeta("service_size", "serviceSize", "str", 1, 1, "primitive"),
        ),
        ends=(
            work_time_schedule.meta,
            service_location.meta,
            customer.meta,
        ),
    )

    def __init__(
        self,
        *,
        appointment_requested: bool | None = None,
        kind: ServiceRequestKind | None = None,
        service_kind: ServiceKind | None = None,
        service_size: str | None = None,
        work_time_schedule: Iterable[WorkTimeSchedule] | None = None,
        service_location: ServiceLocation | None = None,
        customer: Customer | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.appointment_requested = appointment_requested
        self.kind = kind
        self.service_kind = service_kind
        self.service_size = service_size
        if work_time_schedule is not None:
            ServiceRequest.work_time_schedule.extend(self, work_time_schedule)
        if service_location is not None:
            self.service_location = service_location
        if customer is not None:
            self.customer = customer

    def add_work_time_schedule(self, work_time_schedule: WorkTimeSchedule) -> Self:
        return ServiceRequest.work_time_schedule.add(self, work_time_schedule)

    def remove_work_time_schedule(self, work_time_schedule: WorkTimeSchedule) -> Self:
        return ServiceRequest.work_time_schedule.remove(self, work_time_schedule)

    def clear_work_time_schedule(self) -> Self:
        return ServiceRequest.work_time_schedule.clear(self)

    def num_work_time_schedule(self) -> int:
        return ServiceRequest.work_time_schedule.count(self)

    def get_work_time_schedule_by_mrid(self, mrid: str) -> WorkTimeSchedule | None:
        return ServiceRequest.work_time_schedule.get_by_mrid(self, mrid)
