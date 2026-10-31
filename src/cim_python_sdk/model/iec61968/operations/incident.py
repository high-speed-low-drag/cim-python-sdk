"""CIM class Incident (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.common.hazard import Hazard
    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.common.operator import Operator
    from cim_python_sdk.model.iec61968.customers.customer_notification import CustomerNotification
    from cim_python_sdk.model.iec61968.customers.incident_hazard import IncidentHazard
    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket
    from cim_python_sdk.model.iec61968.operations.outage import Outage
    from cim_python_sdk.model.iec61968.operations.trouble_order import TroubleOrder
    from cim_python_sdk.model.iec61968.operations.unplanned_outage import UnplannedOutage
    from cim_python_sdk.model.iec61968.work.work import Work


class Incident(Document):
    """Description of a problem in the field that may be reported in a trouble ticket or come
    from another source. It may have to do with an outage."""

    __slots__ = (
        "_asset",
        "_customer_notifications",
        "_hazard",
        "_incident_hazard",
        "_location",
        "_outage",
        "_owner",
        "_trouble_order",
        "_trouble_tickets",
        "_unplanned_outage",
        "_works",
        "cause",
    )

    cause: str | None

    asset: Many[Asset] = Many(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="incident",
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
            inverse="incident",
            aggregation="none",
        )
    )
    works: Many[Work] = Many(
        EndMeta(
            name="works",
            cim_role="Works",
            target="cim_python_sdk.model.iec61968.work.work:Work",
            many=True,
            lower=0,
            upper=None,
            inverse="incidents",
            aggregation="none",
        )
    )
    trouble_tickets: Many[TroubleTicket] = Many(
        EndMeta(
            name="trouble_tickets",
            cim_role="TroubleTickets",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=True,
            lower=0,
            upper=None,
            inverse="incident",
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
            inverse="incident_incident_hazard",
            aggregation="none",
        )
    )
    outage: One[Outage] = One(
        EndMeta(
            name="outage",
            cim_role="Outage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=False,
            lower=0,
            upper=1,
            inverse="incident",
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
            inverse="incident",
            aggregation="none",
        )
    )
    owner: One[Operator] = One(
        EndMeta(
            name="owner",
            cim_role="Owner",
            target="cim_python_sdk.model.iec61968.common.operator:Operator",
            many=False,
            lower=0,
            upper=1,
            inverse="incidents",
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
            inverse="incident",
            aggregation="none",
        )
    )
    customer_notifications: Many[CustomerNotification] = Many(
        EndMeta(
            name="customer_notifications",
            cim_role="CustomerNotifications",
            target="cim_python_sdk.model.iec61968.customers.customer_notification:CustomerNotification",
            many=True,
            lower=0,
            upper=None,
            inverse="incident",
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
            inverse="incident_unplanned_outage",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Incident",
        package="TC57CIM/IEC61968/Operations",
        guid="{0ED91420-F3BF-47ae-B626-192C9A40CC1A}",
        attributes=(AttrMeta("cause", "cause", "str", 0, 1, "primitive"),),
        ends=(
            asset.meta,
            trouble_order.meta,
            works.meta,
            trouble_tickets.meta,
            incident_hazard.meta,
            outage.meta,
            location.meta,
            owner.meta,
            hazard.meta,
            customer_notifications.meta,
            unplanned_outage.meta,
        ),
    )

    def __init__(
        self,
        *,
        cause: str | None = None,
        asset: Iterable[Asset] | None = None,
        trouble_order: TroubleOrder | None = None,
        works: Iterable[Work] | None = None,
        trouble_tickets: Iterable[TroubleTicket] | None = None,
        incident_hazard: Iterable[IncidentHazard] | None = None,
        outage: Outage | None = None,
        location: Location | None = None,
        owner: Operator | None = None,
        hazard: Iterable[Hazard] | None = None,
        customer_notifications: Iterable[CustomerNotification] | None = None,
        unplanned_outage: UnplannedOutage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cause = cause
        if asset is not None:
            Incident.asset.extend(self, asset)
        if trouble_order is not None:
            self.trouble_order = trouble_order
        if works is not None:
            Incident.works.extend(self, works)
        if trouble_tickets is not None:
            Incident.trouble_tickets.extend(self, trouble_tickets)
        if incident_hazard is not None:
            Incident.incident_hazard.extend(self, incident_hazard)
        if outage is not None:
            self.outage = outage
        if location is not None:
            self.location = location
        if owner is not None:
            self.owner = owner
        if hazard is not None:
            Incident.hazard.extend(self, hazard)
        if customer_notifications is not None:
            Incident.customer_notifications.extend(self, customer_notifications)
        if unplanned_outage is not None:
            self.unplanned_outage = unplanned_outage

    def add_asset(self, asset: Asset) -> Self:
        return Incident.asset.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return Incident.asset.remove(self, asset)

    def clear_asset(self) -> Self:
        return Incident.asset.clear(self)

    def num_asset(self) -> int:
        return Incident.asset.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return Incident.asset.get_by_mrid(self, mrid)

    def add_work(self, work: Work) -> Self:
        return Incident.works.add(self, work)

    def remove_work(self, work: Work) -> Self:
        return Incident.works.remove(self, work)

    def clear_works(self) -> Self:
        return Incident.works.clear(self)

    def num_work(self) -> int:
        return Incident.works.count(self)

    def get_work_by_mrid(self, mrid: str) -> Work | None:
        return Incident.works.get_by_mrid(self, mrid)

    def add_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return Incident.trouble_tickets.add(self, trouble_ticket)

    def remove_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return Incident.trouble_tickets.remove(self, trouble_ticket)

    def clear_trouble_tickets(self) -> Self:
        return Incident.trouble_tickets.clear(self)

    def num_trouble_ticket(self) -> int:
        return Incident.trouble_tickets.count(self)

    def get_trouble_ticket_by_mrid(self, mrid: str) -> TroubleTicket | None:
        return Incident.trouble_tickets.get_by_mrid(self, mrid)

    def add_incident_hazard(self, incident_hazard: IncidentHazard) -> Self:
        return Incident.incident_hazard.add(self, incident_hazard)

    def remove_incident_hazard(self, incident_hazard: IncidentHazard) -> Self:
        return Incident.incident_hazard.remove(self, incident_hazard)

    def clear_incident_hazard(self) -> Self:
        return Incident.incident_hazard.clear(self)

    def num_incident_hazard(self) -> int:
        return Incident.incident_hazard.count(self)

    def get_incident_hazard_by_mrid(self, mrid: str) -> IncidentHazard | None:
        return Incident.incident_hazard.get_by_mrid(self, mrid)

    def add_hazard(self, hazard: Hazard) -> Self:
        return Incident.hazard.add(self, hazard)

    def remove_hazard(self, hazard: Hazard) -> Self:
        return Incident.hazard.remove(self, hazard)

    def clear_hazard(self) -> Self:
        return Incident.hazard.clear(self)

    def num_hazard(self) -> int:
        return Incident.hazard.count(self)

    def get_hazard_by_mrid(self, mrid: str) -> Hazard | None:
        return Incident.hazard.get_by_mrid(self, mrid)

    def add_customer_notification(self, customer_notification: CustomerNotification) -> Self:
        return Incident.customer_notifications.add(self, customer_notification)

    def remove_customer_notification(self, customer_notification: CustomerNotification) -> Self:
        return Incident.customer_notifications.remove(self, customer_notification)

    def clear_customer_notifications(self) -> Self:
        return Incident.customer_notifications.clear(self)

    def num_customer_notification(self) -> int:
        return Incident.customer_notifications.count(self)
