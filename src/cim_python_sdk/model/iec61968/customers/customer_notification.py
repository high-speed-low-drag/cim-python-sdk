"""CIM class CustomerNotification (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.customers.notification_trigger_kind import (
        NotificationTriggerKind,
    )
    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket
    from cim_python_sdk.model.iec61968.operations.incident import Incident


class CustomerNotification(CimObject):
    """Conditions for notifying the customer about the changes in the status of their service
    (e.g., outage restore, estimated restoration time, tariff or service level change, etc.)"""

    __slots__ = (
        "_customer",
        "_incident",
        "_trouble_tickets",
        "contact_type",
        "contact_value",
        "earliest_date_time_to_call",
        "latest_date_time_to_call",
        "trigger",
    )

    trigger: NotificationTriggerKind | None
    earliest_date_time_to_call: _dt.datetime | None
    latest_date_time_to_call: _dt.datetime | None
    contact_type: str | None
    contact_value: str | None

    trouble_tickets: Many[TroubleTicket] = Many(
        EndMeta(
            name="trouble_tickets",
            cim_role="TroubleTickets",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=True,
            lower=0,
            upper=None,
            inverse="notification",
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
            inverse="customer_notifications",
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
            inverse="customer_notifications",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CustomerNotification",
        package="TC57CIM/IEC61968/Customers",
        guid="{DD7A6789-1AF7-48d8-BEA1-E65E8AFCA371}",
        attributes=(
            AttrMeta("trigger", "trigger", "NotificationTriggerKind", 0, 1, "enumeration"),
            AttrMeta(
                "earliest_date_time_to_call",
                "earliestDateTimeToCall",
                "datetime",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "latest_date_time_to_call", "latestDateTimeToCall", "datetime", 0, 1, "primitive"
            ),
            AttrMeta("contact_type", "contactType", "str", 0, 1, "primitive"),
            AttrMeta("contact_value", "contactValue", "str", 0, 1, "primitive"),
        ),
        ends=(
            trouble_tickets.meta,
            customer.meta,
            incident.meta,
        ),
    )

    def __init__(
        self,
        *,
        trigger: NotificationTriggerKind | None = None,
        earliest_date_time_to_call: _dt.datetime | None = None,
        latest_date_time_to_call: _dt.datetime | None = None,
        contact_type: str | None = None,
        contact_value: str | None = None,
        trouble_tickets: Iterable[TroubleTicket] | None = None,
        customer: Customer | None = None,
        incident: Incident | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.trigger = trigger
        self.earliest_date_time_to_call = earliest_date_time_to_call
        self.latest_date_time_to_call = latest_date_time_to_call
        self.contact_type = contact_type
        self.contact_value = contact_value
        if trouble_tickets is not None:
            CustomerNotification.trouble_tickets.extend(self, trouble_tickets)
        if customer is not None:
            self.customer = customer
        if incident is not None:
            self.incident = incident

    def add_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return CustomerNotification.trouble_tickets.add(self, trouble_ticket)

    def remove_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return CustomerNotification.trouble_tickets.remove(self, trouble_ticket)

    def clear_trouble_tickets(self) -> Self:
        return CustomerNotification.trouble_tickets.clear(self)

    def num_trouble_ticket(self) -> int:
        return CustomerNotification.trouble_tickets.count(self)

    def get_trouble_ticket_by_mrid(self, mrid: str) -> TroubleTicket | None:
        return CustomerNotification.trouble_tickets.get_by_mrid(self, mrid)
