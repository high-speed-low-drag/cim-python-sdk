"""CIM class TroubleOrder (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket
    from cim_python_sdk.model.iec61968.operations.incident import Incident
    from cim_python_sdk.model.iec61968.operations.unplanned_outage import UnplannedOutage
    from cim_python_sdk.model.iec61968.work.work_task import WorkTask
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class TroubleOrder(Document):
    """Trouble order sends an incident to a crew to initiate a response to an unplanned outage."""

    __slots__ = (
        "_incident",
        "_location",
        "_trouble_ticket",
        "_unplanned_outage",
        "_work_task",
        "planned_execution_interval",
    )

    comment: str | None
    planned_execution_interval: DateTimeInterval | None

    work_task: Many[WorkTask] = Many(
        EndMeta(
            name="work_task",
            cim_role="WorkTask",
            target="cim_python_sdk.model.iec61968.work.work_task:WorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="trouble_order",
            aggregation="none",
        )
    )
    location: One[Location] = One(
        EndMeta(
            name="location",
            cim_role="Location",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=False,
            lower=0,
            upper=1,
            inverse="trouble_order",
            aggregation="none",
        )
    )
    incident: One[Incident] = One(
        EndMeta(
            name="incident",
            cim_role="Incident",
            target="cim_python_sdk.model.iec61968.operations.incident:Incident",
            many=False,
            lower=0,
            upper=1,
            inverse="trouble_order",
            aggregation="none",
        )
    )
    trouble_ticket: Many[TroubleTicket] = Many(
        EndMeta(
            name="trouble_ticket",
            cim_role="TroubleTicket",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=True,
            lower=0,
            upper=None,
            inverse="trouble_order",
            aggregation="none",
        )
    )
    unplanned_outage: One[UnplannedOutage] = One(
        EndMeta(
            name="unplanned_outage",
            cim_role="UnplannedOutage",
            target="cim_python_sdk.model.iec61968.operations.unplanned_outage:UnplannedOutage",
            many=False,
            lower=0,
            upper=1,
            inverse="trouble_order",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TroubleOrder",
        package="TC57CIM/IEC61968/Operations",
        guid="{7C67A635-A909-4e41-82B5-2A786790D362}",
        attributes=(
            AttrMeta("comment", "comment", "str", 1, 1, "primitive"),
            AttrMeta(
                "planned_execution_interval",
                "plannedExecutionInterval",
                "DateTimeInterval",
                0,
                1,
                "compound",
            ),
        ),
        ends=(
            work_task.meta,
            location.meta,
            incident.meta,
            trouble_ticket.meta,
            unplanned_outage.meta,
        ),
    )

    def __init__(
        self,
        *,
        comment: str | None = None,
        planned_execution_interval: DateTimeInterval | None = None,
        work_task: Iterable[WorkTask] | None = None,
        location: Location | None = None,
        incident: Incident | None = None,
        trouble_ticket: Iterable[TroubleTicket] | None = None,
        unplanned_outage: UnplannedOutage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.comment = comment
        self.planned_execution_interval = planned_execution_interval
        if work_task is not None:
            TroubleOrder.work_task.extend(self, work_task)
        if location is not None:
            self.location = location
        if incident is not None:
            self.incident = incident
        if trouble_ticket is not None:
            TroubleOrder.trouble_ticket.extend(self, trouble_ticket)
        if unplanned_outage is not None:
            self.unplanned_outage = unplanned_outage

    def add_work_task(self, work_task: WorkTask) -> Self:
        return TroubleOrder.work_task.add(self, work_task)

    def remove_work_task(self, work_task: WorkTask) -> Self:
        return TroubleOrder.work_task.remove(self, work_task)

    def clear_work_task(self) -> Self:
        return TroubleOrder.work_task.clear(self)

    def num_work_task(self) -> int:
        return TroubleOrder.work_task.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> WorkTask | None:
        return TroubleOrder.work_task.get_by_mrid(self, mrid)

    def add_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return TroubleOrder.trouble_ticket.add(self, trouble_ticket)

    def remove_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return TroubleOrder.trouble_ticket.remove(self, trouble_ticket)

    def clear_trouble_ticket(self) -> Self:
        return TroubleOrder.trouble_ticket.clear(self)

    def num_trouble_ticket(self) -> int:
        return TroubleOrder.trouble_ticket.count(self)

    def get_trouble_ticket_by_mrid(self, mrid: str) -> TroubleTicket | None:
        return TroubleOrder.trouble_ticket.get_by_mrid(self, mrid)
