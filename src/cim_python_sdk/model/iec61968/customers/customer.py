"""CIM class Customer (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.person import Person
    from cim_python_sdk.model.iec61968.common.priority import Priority
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.customers.customer_account import CustomerAccount
    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.customers.customer_kind import CustomerKind
    from cim_python_sdk.model.iec61968.customers.customer_notification import CustomerNotification
    from cim_python_sdk.model.iec61968.customers.service_request import ServiceRequest
    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person import OldPerson
    from cim_python_sdk.model.iec61968.metering.end_device import EndDevice
    from cim_python_sdk.model.iec61968.operations.outage_plan import OutagePlan
    from cim_python_sdk.model.iec61968.operations.planned_outage_notification import (
        PlannedOutageNotification,
    )
    from cim_python_sdk.model.iec61968.work.work import Work


class Customer(OrganisationRole):
    """Organisation receiving services from service supplier."""

    __slots__ = (
        "_customer",
        "_customer_accounts",
        "_customer_agreements",
        "_customer_customer",
        "_customer_notifications",
        "_end_devices",
        "_erp_persons",
        "_outage_plan",
        "_person",
        "_planned_outage_notification",
        "_service_request",
        "_trouble_tickets",
        "_works",
        "kind",
        "locale",
        "priority",
        "puc_number",
        "special_need",
        "status",
        "vip",
    )

    kind: CustomerKind | None
    special_need: str | None
    vip: bool | None
    puc_number: str | None
    status: Status | None
    priority: Priority | None
    locale: str | None

    works: Many[Work] = Many(
        EndMeta(
            name="works",
            cim_role="Works",
            target="cim_python_sdk.model.iec61968.work.work:Work",
            many=True,
            lower=0,
            upper=None,
            inverse="customers",
            aggregation="none",
        )
    )
    erp_persons: Many[OldPerson] = Many(
        EndMeta(
            name="erp_persons",
            cim_role="ErpPersons",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person:OldPerson",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_data",
            aggregation="none",
        )
    )
    customer_agreements: Many[CustomerAgreement] = Many(
        EndMeta(
            name="customer_agreements",
            cim_role="CustomerAgreements",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="customer",
            aggregation="none",
        )
    )
    outage_plan: One[OutagePlan] = One(
        EndMeta(
            name="outage_plan",
            cim_role="OutagePlan",
            target="cim_python_sdk.model.iec61968.operations.outage_plan:OutagePlan",
            many=False,
            lower=0,
            upper=1,
            inverse="customer",
            aggregation="none",
        )
    )
    person: Many[Person] = Many(
        EndMeta(
            name="person",
            cim_role="Person",
            target="cim_python_sdk.model.iec61968.common.person:Person",
            many=True,
            lower=0,
            upper=None,
            inverse="customer",
            aggregation="none",
        )
    )
    customer_accounts: Many[CustomerAccount] = Many(
        EndMeta(
            name="customer_accounts",
            cim_role="CustomerAccounts",
            target="cim_python_sdk.model.iec61968.customers.customer_account:CustomerAccount",
            many=True,
            lower=0,
            upper=None,
            inverse="customer",
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
            inverse="customer",
            aggregation="none",
        )
    )
    customer: Many[Customer] = Many(
        EndMeta(
            name="customer",
            cim_role="Customer",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_customer",
            aggregation="none",
        )
    )
    customer_customer: One[Customer] = One(
        EndMeta(
            name="customer_customer",
            cim_role="Customer",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=False,
            lower=0,
            upper=1,
            inverse="customer",
            aggregation="none",
        )
    )
    planned_outage_notification: Many[PlannedOutageNotification] = Many(
        EndMeta(
            name="planned_outage_notification",
            cim_role="PlannedOutageNotification",
            target="cim_python_sdk.model.iec61968.operations.planned_outage_notification:PlannedOutageNotification",
            many=True,
            lower=0,
            upper=None,
            inverse="customer",
            aggregation="none",
        )
    )
    end_devices: Many[EndDevice] = Many(
        EndMeta(
            name="end_devices",
            cim_role="EndDevices",
            target="cim_python_sdk.model.iec61968.metering.end_device:EndDevice",
            many=True,
            lower=0,
            upper=None,
            inverse="customer",
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
            inverse="customer",
            aggregation="none",
        )
    )
    service_request: Many[ServiceRequest] = Many(
        EndMeta(
            name="service_request",
            cim_role="ServiceRequest",
            target="cim_python_sdk.model.iec61968.customers.service_request:ServiceRequest",
            many=True,
            lower=0,
            upper=None,
            inverse="customer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Customer",
        package="TC57CIM/IEC61968/Customers",
        guid="{80011596-1798-4c9c-94A2-182EE31D017B}",
        attributes=(
            AttrMeta("kind", "kind", "CustomerKind", 0, 1, "enumeration"),
            AttrMeta("special_need", "specialNeed", "str", 0, 1, "primitive"),
            AttrMeta("vip", "vip", "bool", 0, 1, "primitive", deprecated=True),
            AttrMeta("puc_number", "pucNumber", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
            AttrMeta("priority", "priority", "Priority", 0, 1, "compound"),
            AttrMeta("locale", "locale", "str", 0, 1, "primitive"),
        ),
        ends=(
            works.meta,
            erp_persons.meta,
            customer_agreements.meta,
            outage_plan.meta,
            person.meta,
            customer_accounts.meta,
            customer_notifications.meta,
            customer.meta,
            customer_customer.meta,
            planned_outage_notification.meta,
            end_devices.meta,
            trouble_tickets.meta,
            service_request.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: CustomerKind | None = None,
        special_need: str | None = None,
        vip: bool | None = None,
        puc_number: str | None = None,
        status: Status | None = None,
        priority: Priority | None = None,
        locale: str | None = None,
        works: Iterable[Work] | None = None,
        erp_persons: Iterable[OldPerson] | None = None,
        customer_agreements: Iterable[CustomerAgreement] | None = None,
        outage_plan: OutagePlan | None = None,
        person: Iterable[Person] | None = None,
        customer_accounts: Iterable[CustomerAccount] | None = None,
        customer_notifications: Iterable[CustomerNotification] | None = None,
        customer: Iterable[Customer] | None = None,
        customer_customer: Customer | None = None,
        planned_outage_notification: Iterable[PlannedOutageNotification] | None = None,
        end_devices: Iterable[EndDevice] | None = None,
        trouble_tickets: Iterable[TroubleTicket] | None = None,
        service_request: Iterable[ServiceRequest] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.special_need = special_need
        self.vip = vip
        self.puc_number = puc_number
        self.status = status
        self.priority = priority
        self.locale = locale
        if works is not None:
            Customer.works.extend(self, works)
        if erp_persons is not None:
            Customer.erp_persons.extend(self, erp_persons)
        if customer_agreements is not None:
            Customer.customer_agreements.extend(self, customer_agreements)
        if outage_plan is not None:
            self.outage_plan = outage_plan
        if person is not None:
            Customer.person.extend(self, person)
        if customer_accounts is not None:
            Customer.customer_accounts.extend(self, customer_accounts)
        if customer_notifications is not None:
            Customer.customer_notifications.extend(self, customer_notifications)
        if customer is not None:
            Customer.customer.extend(self, customer)
        if customer_customer is not None:
            self.customer_customer = customer_customer
        if planned_outage_notification is not None:
            Customer.planned_outage_notification.extend(self, planned_outage_notification)
        if end_devices is not None:
            Customer.end_devices.extend(self, end_devices)
        if trouble_tickets is not None:
            Customer.trouble_tickets.extend(self, trouble_tickets)
        if service_request is not None:
            Customer.service_request.extend(self, service_request)

    def add_work(self, work: Work) -> Self:
        return Customer.works.add(self, work)

    def remove_work(self, work: Work) -> Self:
        return Customer.works.remove(self, work)

    def clear_works(self) -> Self:
        return Customer.works.clear(self)

    def num_work(self) -> int:
        return Customer.works.count(self)

    def get_work_by_mrid(self, mrid: str) -> Work | None:
        return Customer.works.get_by_mrid(self, mrid)

    def add_erp_person(self, erp_person: OldPerson) -> Self:
        return Customer.erp_persons.add(self, erp_person)

    def remove_erp_person(self, erp_person: OldPerson) -> Self:
        return Customer.erp_persons.remove(self, erp_person)

    def clear_erp_persons(self) -> Self:
        return Customer.erp_persons.clear(self)

    def num_erp_person(self) -> int:
        return Customer.erp_persons.count(self)

    def get_erp_person_by_mrid(self, mrid: str) -> OldPerson | None:
        return Customer.erp_persons.get_by_mrid(self, mrid)

    def add_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return Customer.customer_agreements.add(self, customer_agreement)

    def remove_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return Customer.customer_agreements.remove(self, customer_agreement)

    def clear_customer_agreements(self) -> Self:
        return Customer.customer_agreements.clear(self)

    def num_customer_agreement(self) -> int:
        return Customer.customer_agreements.count(self)

    def get_customer_agreement_by_mrid(self, mrid: str) -> CustomerAgreement | None:
        return Customer.customer_agreements.get_by_mrid(self, mrid)

    def add_person(self, person: Person) -> Self:
        return Customer.person.add(self, person)

    def remove_person(self, person: Person) -> Self:
        return Customer.person.remove(self, person)

    def clear_person(self) -> Self:
        return Customer.person.clear(self)

    def num_person(self) -> int:
        return Customer.person.count(self)

    def get_person_by_mrid(self, mrid: str) -> Person | None:
        return Customer.person.get_by_mrid(self, mrid)

    def add_customer_account(self, customer_account: CustomerAccount) -> Self:
        return Customer.customer_accounts.add(self, customer_account)

    def remove_customer_account(self, customer_account: CustomerAccount) -> Self:
        return Customer.customer_accounts.remove(self, customer_account)

    def clear_customer_accounts(self) -> Self:
        return Customer.customer_accounts.clear(self)

    def num_customer_account(self) -> int:
        return Customer.customer_accounts.count(self)

    def get_customer_account_by_mrid(self, mrid: str) -> CustomerAccount | None:
        return Customer.customer_accounts.get_by_mrid(self, mrid)

    def add_customer_notification(self, customer_notification: CustomerNotification) -> Self:
        return Customer.customer_notifications.add(self, customer_notification)

    def remove_customer_notification(self, customer_notification: CustomerNotification) -> Self:
        return Customer.customer_notifications.remove(self, customer_notification)

    def clear_customer_notifications(self) -> Self:
        return Customer.customer_notifications.clear(self)

    def num_customer_notification(self) -> int:
        return Customer.customer_notifications.count(self)

    def add_customer(self, customer: Customer) -> Self:
        return Customer.customer.add(self, customer)

    def remove_customer(self, customer: Customer) -> Self:
        return Customer.customer.remove(self, customer)

    def clear_customer(self) -> Self:
        return Customer.customer.clear(self)

    def num_customer(self) -> int:
        return Customer.customer.count(self)

    def get_customer_by_mrid(self, mrid: str) -> Customer | None:
        return Customer.customer.get_by_mrid(self, mrid)

    def add_planned_outage_notification(
        self, planned_outage_notification: PlannedOutageNotification
    ) -> Self:
        return Customer.planned_outage_notification.add(self, planned_outage_notification)

    def remove_planned_outage_notification(
        self, planned_outage_notification: PlannedOutageNotification
    ) -> Self:
        return Customer.planned_outage_notification.remove(self, planned_outage_notification)

    def clear_planned_outage_notification(self) -> Self:
        return Customer.planned_outage_notification.clear(self)

    def num_planned_outage_notification(self) -> int:
        return Customer.planned_outage_notification.count(self)

    def get_planned_outage_notification_by_mrid(
        self, mrid: str
    ) -> PlannedOutageNotification | None:
        return Customer.planned_outage_notification.get_by_mrid(self, mrid)

    def add_end_device(self, end_device: EndDevice) -> Self:
        return Customer.end_devices.add(self, end_device)

    def remove_end_device(self, end_device: EndDevice) -> Self:
        return Customer.end_devices.remove(self, end_device)

    def clear_end_devices(self) -> Self:
        return Customer.end_devices.clear(self)

    def num_end_device(self) -> int:
        return Customer.end_devices.count(self)

    def get_end_device_by_mrid(self, mrid: str) -> EndDevice | None:
        return Customer.end_devices.get_by_mrid(self, mrid)

    def add_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return Customer.trouble_tickets.add(self, trouble_ticket)

    def remove_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return Customer.trouble_tickets.remove(self, trouble_ticket)

    def clear_trouble_tickets(self) -> Self:
        return Customer.trouble_tickets.clear(self)

    def num_trouble_ticket(self) -> int:
        return Customer.trouble_tickets.count(self)

    def get_trouble_ticket_by_mrid(self, mrid: str) -> TroubleTicket | None:
        return Customer.trouble_tickets.get_by_mrid(self, mrid)

    def add_service_request(self, service_request: ServiceRequest) -> Self:
        return Customer.service_request.add(self, service_request)

    def remove_service_request(self, service_request: ServiceRequest) -> Self:
        return Customer.service_request.remove(self, service_request)

    def clear_service_request(self) -> Self:
        return Customer.service_request.clear(self)

    def num_service_request(self) -> int:
        return Customer.service_request.count(self)

    def get_service_request_by_mrid(self, mrid: str) -> ServiceRequest | None:
        return Customer.service_request.get_by_mrid(self, mrid)
