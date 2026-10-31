"""CIM class UnplannedOutage (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.operations.outage import Outage

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.field_dispatch_history import FieldDispatchHistory
    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket
    from cim_python_sdk.model.iec61968.operations.incident import Incident
    from cim_python_sdk.model.iec61968.operations.outage_cause_kind import OutageCauseKind
    from cim_python_sdk.model.iec61968.operations.trouble_order import TroubleOrder


class UnplannedOutage(Outage):
    """Document describing the consequence of an unplanned outage in a part of the electrical
    network. For the purposes of this model, an unplanned outage refers to a state where
    energy is not delivered; such as, customers out of service, a street light is not
    served, etc.

    A unplanned outage may be created upon:

    - impacts the SAIDI calculation

    - a breaker trip,

    - a fault indicator status change,

    - a meter event indicating customer outage,

    - a reception of one or more customer trouble calls, or

    - an operator command, reflecting information obtained from the field crew.

    Outage restoration may be performed using a switching plan which complements the outage
    information with detailed switching activities, including the relationship to the crew
    and work."""

    __slots__ = (
        "_field_dispatch_history",
        "_incident_unplanned_outage",
        "_trouble_order",
        "_trouble_ticket",
        "cause",
        "cause_kind",
        "reported_start_time",
    )

    cause: str | None
    cause_kind: OutageCauseKind | None
    reported_start_time: _dt.datetime | None

    trouble_ticket: Many[TroubleTicket] = Many(
        EndMeta(
            name="trouble_ticket",
            cim_role="TroubleTicket",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=True,
            lower=0,
            upper=None,
            inverse="unplanned_outage",
            aggregation="none",
        )
    )
    trouble_order: Many[TroubleOrder] = Many(
        EndMeta(
            name="trouble_order",
            cim_role="TroubleOrder",
            target="cim_python_sdk.model.iec61968.operations.trouble_order:TroubleOrder",
            many=True,
            lower=0,
            upper=None,
            inverse="unplanned_outage",
            aggregation="none",
        )
    )
    field_dispatch_history: One[FieldDispatchHistory] = One(
        EndMeta(
            name="field_dispatch_history",
            cim_role="FieldDispatchHistory",
            target="cim_python_sdk.model.iec61968.common.field_dispatch_history:FieldDispatchHistory",
            many=False,
            lower=0,
            upper=1,
            inverse="unplanned_outage",
            aggregation="none",
        )
    )
    incident_unplanned_outage: Many[Incident] = Many(
        EndMeta(
            name="incident_unplanned_outage",
            cim_role="Incident",
            target="cim_python_sdk.model.iec61968.operations.incident:Incident",
            many=True,
            lower=0,
            upper=None,
            inverse="unplanned_outage",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UnplannedOutage",
        package="TC57CIM/IEC61968/Operations",
        guid="{7E6D39E3-90B7-419f-9A40-A63CEA976DE4}",
        attributes=(
            AttrMeta("cause", "cause", "str", 0, 1, "primitive"),
            AttrMeta("cause_kind", "causeKind", "OutageCauseKind", 0, 1, "enumeration"),
            AttrMeta("reported_start_time", "reportedStartTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            trouble_ticket.meta,
            trouble_order.meta,
            field_dispatch_history.meta,
            incident_unplanned_outage.meta,
        ),
    )

    def __init__(
        self,
        *,
        cause: str | None = None,
        cause_kind: OutageCauseKind | None = None,
        reported_start_time: _dt.datetime | None = None,
        trouble_ticket: Iterable[TroubleTicket] | None = None,
        trouble_order: Iterable[TroubleOrder] | None = None,
        field_dispatch_history: FieldDispatchHistory | None = None,
        incident_unplanned_outage: Iterable[Incident] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cause = cause
        self.cause_kind = cause_kind
        self.reported_start_time = reported_start_time
        if trouble_ticket is not None:
            UnplannedOutage.trouble_ticket.extend(self, trouble_ticket)
        if trouble_order is not None:
            UnplannedOutage.trouble_order.extend(self, trouble_order)
        if field_dispatch_history is not None:
            self.field_dispatch_history = field_dispatch_history
        if incident_unplanned_outage is not None:
            UnplannedOutage.incident_unplanned_outage.extend(self, incident_unplanned_outage)

    def add_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return UnplannedOutage.trouble_ticket.add(self, trouble_ticket)

    def remove_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return UnplannedOutage.trouble_ticket.remove(self, trouble_ticket)

    def clear_trouble_ticket(self) -> Self:
        return UnplannedOutage.trouble_ticket.clear(self)

    def num_trouble_ticket(self) -> int:
        return UnplannedOutage.trouble_ticket.count(self)

    def get_trouble_ticket_by_mrid(self, mrid: str) -> TroubleTicket | None:
        return UnplannedOutage.trouble_ticket.get_by_mrid(self, mrid)

    def add_trouble_order(self, trouble_order: TroubleOrder) -> Self:
        return UnplannedOutage.trouble_order.add(self, trouble_order)

    def remove_trouble_order(self, trouble_order: TroubleOrder) -> Self:
        return UnplannedOutage.trouble_order.remove(self, trouble_order)

    def clear_trouble_order(self) -> Self:
        return UnplannedOutage.trouble_order.clear(self)

    def num_trouble_order(self) -> int:
        return UnplannedOutage.trouble_order.count(self)

    def get_trouble_order_by_mrid(self, mrid: str) -> TroubleOrder | None:
        return UnplannedOutage.trouble_order.get_by_mrid(self, mrid)

    def add_incident_unplanned_outage(self, incident_unplanned_outage: Incident) -> Self:
        return UnplannedOutage.incident_unplanned_outage.add(self, incident_unplanned_outage)

    def remove_incident_unplanned_outage(self, incident_unplanned_outage: Incident) -> Self:
        return UnplannedOutage.incident_unplanned_outage.remove(self, incident_unplanned_outage)

    def clear_incident_unplanned_outage(self) -> Self:
        return UnplannedOutage.incident_unplanned_outage.clear(self)

    def num_incident_unplanned_outage(self) -> int:
        return UnplannedOutage.incident_unplanned_outage.count(self)

    def get_incident_unplanned_outage_by_mrid(self, mrid: str) -> Incident | None:
        return UnplannedOutage.incident_unplanned_outage.get_by_mrid(self, mrid)
