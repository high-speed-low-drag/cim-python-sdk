"""CIM class TroubleTicket (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.hazard import Hazard
    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.common.trouble_reporter import TroubleReporter
    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.customers.customer_notification import CustomerNotification
    from cim_python_sdk.model.iec61968.customers.incident_hazard import IncidentHazard
    from cim_python_sdk.model.iec61968.customers.service_location import ServiceLocation
    from cim_python_sdk.model.iec61968.customers.trouble_reporting_kind import TroubleReportingKind
    from cim_python_sdk.model.iec61968.customers.trouble_symptoms import TroubleSymptoms
    from cim_python_sdk.model.iec61968.operations.incident import Incident
    from cim_python_sdk.model.iec61968.operations.trouble_order import TroubleOrder
    from cim_python_sdk.model.iec61968.operations.unplanned_outage import UnplannedOutage


class TroubleTicket(Document):
    """CIM class TroubleTicket."""

    __slots__ = (
        "_customer",
        "_hazard",
        "_incident",
        "_incident_hazard",
        "_location",
        "_notification",
        "_service_location",
        "_trouble_order",
        "_trouble_reporter",
        "_trouble_symptoms",
        "_unplanned_outage",
        "date_time_of_report",
        "first_responder_status",
        "multiple_premises",
        "reporting_kind",
        "resolved_date_time",
        "trouble_code",
    )

    reporting_kind: TroubleReportingKind | None
    date_time_of_report: _dt.datetime | None
    trouble_code: str | None
    first_responder_status: str | None
    resolved_date_time: _dt.datetime | None
    comment: str | None
    multiple_premises: bool | None

    trouble_symptoms: One[TroubleSymptoms] = One(
        EndMeta(
            name="trouble_symptoms",
            cim_role="TroubleSymptoms",
            target="cim_python_sdk.model.iec61968.customers.trouble_symptoms:TroubleSymptoms",
            many=False,
            lower=0,
            upper=1,
            inverse="trouble_ticket",
            aggregation="none",
        )
    )
    notification: Many[CustomerNotification] = Many(
        EndMeta(
            name="notification",
            cim_role="Notification",
            target="cim_python_sdk.model.iec61968.customers.customer_notification:CustomerNotification",
            many=True,
            lower=0,
            upper=None,
            inverse="trouble_tickets",
            aggregation="none",
        )
    )
    trouble_order: One[TroubleOrder] = One(
        EndMeta(
            name="trouble_order",
            cim_role="TroubleOrder",
            target="cim_python_sdk.model.iec61968.operations.trouble_order:TroubleOrder",
            many=False,
            lower=0,
            upper=1,
            inverse="trouble_ticket",
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
            inverse="trouble_tickets",
            aggregation="none",
        )
    )
    service_location: One[ServiceLocation] = One(
        EndMeta(
            name="service_location",
            cim_role="ServiceLocation",
            target="cim_python_sdk.model.iec61968.customers.service_location:ServiceLocation",
            many=False,
            lower=1,
            upper=1,
            inverse="trouble_ticket_service_location",
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
            inverse="trouble_ticket",
            aggregation="none",
        )
    )
    hazard: Many[Hazard] = Many(
        EndMeta(
            name="hazard",
            cim_role="Hazard",
            target="cim_python_sdk.model.iec61968.common.hazard:Hazard",
            many=True,
            lower=0,
            upper=None,
            inverse="trouble_ticket",
            aggregation="none",
        )
    )
    trouble_reporter: One[TroubleReporter] = One(
        EndMeta(
            name="trouble_reporter",
            cim_role="TroubleReporter",
            target="cim_python_sdk.model.iec61968.common.trouble_reporter:TroubleReporter",
            many=False,
            lower=0,
            upper=1,
            inverse="trouble_ticket",
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
            inverse="trouble_ticket",
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
            inverse="trouble_tickets",
            aggregation="none",
        )
    )
    incident_hazard: Many[IncidentHazard] = Many(
        EndMeta(
            name="incident_hazard",
            cim_role="IncidentHazard",
            target="cim_python_sdk.model.iec61968.customers.incident_hazard:IncidentHazard",
            many=True,
            lower=0,
            upper=None,
            inverse="trouble_ticket_incident_hazard",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TroubleTicket",
        package="TC57CIM/IEC61968/Customers",
        guid="{1976402F-5A73-4079-A2B1-0044903352D2}",
        attributes=(
            AttrMeta(
                "reporting_kind", "reportingKind", "TroubleReportingKind", 0, 1, "enumeration"
            ),
            AttrMeta("date_time_of_report", "dateTimeOfReport", "datetime", 0, 1, "primitive"),
            AttrMeta("trouble_code", "troubleCode", "str", 0, 1, "primitive"),
            AttrMeta("first_responder_status", "firstResponderStatus", "str", 0, 1, "primitive"),
            AttrMeta("resolved_date_time", "resolvedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("comment", "comment", "str", 1, 1, "primitive"),
            AttrMeta("multiple_premises", "multiplePremises", "bool", 1, 1, "primitive"),
        ),
        ends=(
            trouble_symptoms.meta,
            notification.meta,
            trouble_order.meta,
            incident.meta,
            service_location.meta,
            unplanned_outage.meta,
            hazard.meta,
            trouble_reporter.meta,
            location.meta,
            customer.meta,
            incident_hazard.meta,
        ),
    )

    def __init__(
        self,
        *,
        reporting_kind: TroubleReportingKind | None = None,
        date_time_of_report: _dt.datetime | None = None,
        trouble_code: str | None = None,
        first_responder_status: str | None = None,
        resolved_date_time: _dt.datetime | None = None,
        comment: str | None = None,
        multiple_premises: bool | None = None,
        trouble_symptoms: TroubleSymptoms | None = None,
        notification: Iterable[CustomerNotification] | None = None,
        trouble_order: TroubleOrder | None = None,
        incident: Incident | None = None,
        service_location: ServiceLocation | None = None,
        unplanned_outage: UnplannedOutage | None = None,
        hazard: Iterable[Hazard] | None = None,
        trouble_reporter: TroubleReporter | None = None,
        location: Location | None = None,
        customer: Customer | None = None,
        incident_hazard: Iterable[IncidentHazard] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.reporting_kind = reporting_kind
        self.date_time_of_report = date_time_of_report
        self.trouble_code = trouble_code
        self.first_responder_status = first_responder_status
        self.resolved_date_time = resolved_date_time
        self.comment = comment
        self.multiple_premises = multiple_premises
        if trouble_symptoms is not None:
            self.trouble_symptoms = trouble_symptoms
        if notification is not None:
            TroubleTicket.notification.extend(self, notification)
        if trouble_order is not None:
            self.trouble_order = trouble_order
        if incident is not None:
            self.incident = incident
        if service_location is not None:
            self.service_location = service_location
        if unplanned_outage is not None:
            self.unplanned_outage = unplanned_outage
        if hazard is not None:
            TroubleTicket.hazard.extend(self, hazard)
        if trouble_reporter is not None:
            self.trouble_reporter = trouble_reporter
        if location is not None:
            self.location = location
        if customer is not None:
            self.customer = customer
        if incident_hazard is not None:
            TroubleTicket.incident_hazard.extend(self, incident_hazard)

    def add_notification(self, notification: CustomerNotification) -> Self:
        return TroubleTicket.notification.add(self, notification)

    def remove_notification(self, notification: CustomerNotification) -> Self:
        return TroubleTicket.notification.remove(self, notification)

    def clear_notification(self) -> Self:
        return TroubleTicket.notification.clear(self)

    def num_notification(self) -> int:
        return TroubleTicket.notification.count(self)

    def add_hazard(self, hazard: Hazard) -> Self:
        return TroubleTicket.hazard.add(self, hazard)

    def remove_hazard(self, hazard: Hazard) -> Self:
        return TroubleTicket.hazard.remove(self, hazard)

    def clear_hazard(self) -> Self:
        return TroubleTicket.hazard.clear(self)

    def num_hazard(self) -> int:
        return TroubleTicket.hazard.count(self)

    def get_hazard_by_mrid(self, mrid: str) -> Hazard | None:
        return TroubleTicket.hazard.get_by_mrid(self, mrid)

    def add_incident_hazard(self, incident_hazard: IncidentHazard) -> Self:
        return TroubleTicket.incident_hazard.add(self, incident_hazard)

    def remove_incident_hazard(self, incident_hazard: IncidentHazard) -> Self:
        return TroubleTicket.incident_hazard.remove(self, incident_hazard)

    def clear_incident_hazard(self) -> Self:
        return TroubleTicket.incident_hazard.clear(self)

    def num_incident_hazard(self) -> int:
        return TroubleTicket.incident_hazard.count(self)

    def get_incident_hazard_by_mrid(self, mrid: str) -> IncidentHazard | None:
        return TroubleTicket.incident_hazard.get_by_mrid(self, mrid)
