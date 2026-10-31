"""CIM class ErpInvoiceLineItem (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.user_attribute import UserAttribute
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.customer_billing_info import (
        CustomerBillingInfo,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.work_billing_info import (
        WorkBillingInfo,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice import ErpInvoice
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item_kind import (
        ErpInvoiceLineItemKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal_entry import (
        ErpJournalEntry,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable_line_item import (
        ErpPayableLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payment import ErpPayment
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item import (
        ErpQuoteLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_delv_line_item import (
        ErpRecDelvLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_line_item import (
        ErpRecLineItem,
    )
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class ErpInvoiceLineItem(ErpDocument):
    """An individual line item on an invoice."""

    __slots__ = (
        "_component_erp_invoice_line_items",
        "_container_erp_invoice_line_item",
        "_customer_billing_infos",
        "_erp_invoice",
        "_erp_journal_entries",
        "_erp_payable_line_item",
        "_erp_payments",
        "_erp_quote_line_item",
        "_erp_rec_delv_line_item",
        "_erp_rec_line_item",
        "_user_attributes",
        "_work_billing_infos",
        "bill_period",
        "gl_account",
        "gl_date_time",
        "kind",
        "line_amount",
        "line_number",
        "line_version",
        "net_amount",
        "previous_amount",
    )

    kind: ErpInvoiceLineItemKind | None
    line_number: str | None
    line_amount: float | None
    gl_account: str | None
    gl_date_time: _dt.datetime | None
    bill_period: DateTimeInterval | None
    line_version: str | None
    previous_amount: float | None
    net_amount: float | None

    erp_payable_line_item: One[ErpPayableLineItem] = One(
        EndMeta(
            name="erp_payable_line_item",
            cim_role="ErpPayableLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable_line_item:ErpPayableLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_invoice_line_item",
            aggregation="none",
        )
    )
    erp_payments: Many[ErpPayment] = Many(
        EndMeta(
            name="erp_payments",
            cim_role="ErpPayments",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payment:ErpPayment",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_invoice_line_items",
            aggregation="none",
        )
    )
    erp_rec_line_item: One[ErpRecLineItem] = One(
        EndMeta(
            name="erp_rec_line_item",
            cim_role="ErpRecLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_line_item:ErpRecLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_invoice_line_item",
            aggregation="none",
        )
    )
    container_erp_invoice_line_item: One[ErpInvoiceLineItem] = One(
        EndMeta(
            name="container_erp_invoice_line_item",
            cim_role="ContainerErpInvoiceLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="component_erp_invoice_line_items",
            aggregation="none",
        )
    )
    component_erp_invoice_line_items: Many[ErpInvoiceLineItem] = Many(
        EndMeta(
            name="component_erp_invoice_line_items",
            cim_role="ComponentErpInvoiceLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="container_erp_invoice_line_item",
            aggregation="none",
        )
    )
    erp_quote_line_item: One[ErpQuoteLineItem] = One(
        EndMeta(
            name="erp_quote_line_item",
            cim_role="ErpQuoteLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item:ErpQuoteLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_invoice_line_item",
            aggregation="none",
        )
    )
    user_attributes: Many[UserAttribute] = Many(
        EndMeta(
            name="user_attributes",
            cim_role="UserAttributes",
            target="cim_python_sdk.model.iec61968.common.user_attribute:UserAttribute",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_invoice_line_items",
            aggregation="none",
        )
    )
    erp_journal_entries: Many[ErpJournalEntry] = Many(
        EndMeta(
            name="erp_journal_entries",
            cim_role="ErpJournalEntries",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal_entry:ErpJournalEntry",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_invoice_line_item",
            aggregation="none",
        )
    )
    work_billing_infos: Many[WorkBillingInfo] = Many(
        EndMeta(
            name="work_billing_infos",
            cim_role="WorkBillingInfos",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.work_billing_info:WorkBillingInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_line_items",
            aggregation="none",
        )
    )
    erp_invoice: One[ErpInvoice] = One(
        EndMeta(
            name="erp_invoice",
            cim_role="ErpInvoice",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice:ErpInvoice",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_invoice_line_items",
            aggregation="none",
        )
    )
    customer_billing_infos: Many[CustomerBillingInfo] = Many(
        EndMeta(
            name="customer_billing_infos",
            cim_role="CustomerBillingInfos",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.customer_billing_info:CustomerBillingInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_invoice_line_items",
            aggregation="none",
        )
    )
    erp_rec_delv_line_item: One[ErpRecDelvLineItem] = One(
        EndMeta(
            name="erp_rec_delv_line_item",
            cim_role="ErpRecDelvLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_delv_line_item:ErpRecDelvLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_invoice_line_item",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpInvoiceLineItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{53C3B43C-F9BD-45a5-98A8-C8820D20F3FF}",
        attributes=(
            AttrMeta("kind", "kind", "ErpInvoiceLineItemKind", 0, 1, "enumeration"),
            AttrMeta("line_number", "lineNumber", "str", 0, 1, "primitive"),
            AttrMeta("line_amount", "lineAmount", "float", 0, 1, "primitive"),
            AttrMeta("gl_account", "glAccount", "str", 0, 1, "primitive"),
            AttrMeta("gl_date_time", "glDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("bill_period", "billPeriod", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("line_version", "lineVersion", "str", 0, 1, "primitive"),
            AttrMeta("previous_amount", "previousAmount", "float", 0, 1, "primitive"),
            AttrMeta("net_amount", "netAmount", "float", 0, 1, "primitive"),
        ),
        ends=(
            erp_payable_line_item.meta,
            erp_payments.meta,
            erp_rec_line_item.meta,
            container_erp_invoice_line_item.meta,
            component_erp_invoice_line_items.meta,
            erp_quote_line_item.meta,
            user_attributes.meta,
            erp_journal_entries.meta,
            work_billing_infos.meta,
            erp_invoice.meta,
            customer_billing_infos.meta,
            erp_rec_delv_line_item.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: ErpInvoiceLineItemKind | None = None,
        line_number: str | None = None,
        line_amount: float | None = None,
        gl_account: str | None = None,
        gl_date_time: _dt.datetime | None = None,
        bill_period: DateTimeInterval | None = None,
        line_version: str | None = None,
        previous_amount: float | None = None,
        net_amount: float | None = None,
        erp_payable_line_item: ErpPayableLineItem | None = None,
        erp_payments: Iterable[ErpPayment] | None = None,
        erp_rec_line_item: ErpRecLineItem | None = None,
        container_erp_invoice_line_item: ErpInvoiceLineItem | None = None,
        component_erp_invoice_line_items: Iterable[ErpInvoiceLineItem] | None = None,
        erp_quote_line_item: ErpQuoteLineItem | None = None,
        user_attributes: Iterable[UserAttribute] | None = None,
        erp_journal_entries: Iterable[ErpJournalEntry] | None = None,
        work_billing_infos: Iterable[WorkBillingInfo] | None = None,
        erp_invoice: ErpInvoice | None = None,
        customer_billing_infos: Iterable[CustomerBillingInfo] | None = None,
        erp_rec_delv_line_item: ErpRecDelvLineItem | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.line_number = line_number
        self.line_amount = line_amount
        self.gl_account = gl_account
        self.gl_date_time = gl_date_time
        self.bill_period = bill_period
        self.line_version = line_version
        self.previous_amount = previous_amount
        self.net_amount = net_amount
        if erp_payable_line_item is not None:
            self.erp_payable_line_item = erp_payable_line_item
        if erp_payments is not None:
            ErpInvoiceLineItem.erp_payments.extend(self, erp_payments)
        if erp_rec_line_item is not None:
            self.erp_rec_line_item = erp_rec_line_item
        if container_erp_invoice_line_item is not None:
            self.container_erp_invoice_line_item = container_erp_invoice_line_item
        if component_erp_invoice_line_items is not None:
            ErpInvoiceLineItem.component_erp_invoice_line_items.extend(
                self, component_erp_invoice_line_items
            )
        if erp_quote_line_item is not None:
            self.erp_quote_line_item = erp_quote_line_item
        if user_attributes is not None:
            ErpInvoiceLineItem.user_attributes.extend(self, user_attributes)
        if erp_journal_entries is not None:
            ErpInvoiceLineItem.erp_journal_entries.extend(self, erp_journal_entries)
        if work_billing_infos is not None:
            ErpInvoiceLineItem.work_billing_infos.extend(self, work_billing_infos)
        if erp_invoice is not None:
            self.erp_invoice = erp_invoice
        if customer_billing_infos is not None:
            ErpInvoiceLineItem.customer_billing_infos.extend(self, customer_billing_infos)
        if erp_rec_delv_line_item is not None:
            self.erp_rec_delv_line_item = erp_rec_delv_line_item

    def add_erp_payment(self, erp_payment: ErpPayment) -> Self:
        return ErpInvoiceLineItem.erp_payments.add(self, erp_payment)

    def remove_erp_payment(self, erp_payment: ErpPayment) -> Self:
        return ErpInvoiceLineItem.erp_payments.remove(self, erp_payment)

    def clear_erp_payments(self) -> Self:
        return ErpInvoiceLineItem.erp_payments.clear(self)

    def num_erp_payment(self) -> int:
        return ErpInvoiceLineItem.erp_payments.count(self)

    def get_erp_payment_by_mrid(self, mrid: str) -> ErpPayment | None:
        return ErpInvoiceLineItem.erp_payments.get_by_mrid(self, mrid)

    def add_component_erp_invoice_line_item(
        self, component_erp_invoice_line_item: ErpInvoiceLineItem
    ) -> Self:
        return ErpInvoiceLineItem.component_erp_invoice_line_items.add(
            self, component_erp_invoice_line_item
        )

    def remove_component_erp_invoice_line_item(
        self, component_erp_invoice_line_item: ErpInvoiceLineItem
    ) -> Self:
        return ErpInvoiceLineItem.component_erp_invoice_line_items.remove(
            self, component_erp_invoice_line_item
        )

    def clear_component_erp_invoice_line_items(self) -> Self:
        return ErpInvoiceLineItem.component_erp_invoice_line_items.clear(self)

    def num_component_erp_invoice_line_item(self) -> int:
        return ErpInvoiceLineItem.component_erp_invoice_line_items.count(self)

    def get_component_erp_invoice_line_item_by_mrid(self, mrid: str) -> ErpInvoiceLineItem | None:
        return ErpInvoiceLineItem.component_erp_invoice_line_items.get_by_mrid(self, mrid)

    def add_user_attribute(self, user_attribute: UserAttribute) -> Self:
        return ErpInvoiceLineItem.user_attributes.add(self, user_attribute)

    def remove_user_attribute(self, user_attribute: UserAttribute) -> Self:
        return ErpInvoiceLineItem.user_attributes.remove(self, user_attribute)

    def clear_user_attributes(self) -> Self:
        return ErpInvoiceLineItem.user_attributes.clear(self)

    def num_user_attribute(self) -> int:
        return ErpInvoiceLineItem.user_attributes.count(self)

    def add_erp_journal_entry(self, erp_journal_entry: ErpJournalEntry) -> Self:
        return ErpInvoiceLineItem.erp_journal_entries.add(self, erp_journal_entry)

    def remove_erp_journal_entry(self, erp_journal_entry: ErpJournalEntry) -> Self:
        return ErpInvoiceLineItem.erp_journal_entries.remove(self, erp_journal_entry)

    def clear_erp_journal_entries(self) -> Self:
        return ErpInvoiceLineItem.erp_journal_entries.clear(self)

    def num_erp_journal_entry(self) -> int:
        return ErpInvoiceLineItem.erp_journal_entries.count(self)

    def get_erp_journal_entry_by_mrid(self, mrid: str) -> ErpJournalEntry | None:
        return ErpInvoiceLineItem.erp_journal_entries.get_by_mrid(self, mrid)

    def add_work_billing_info(self, work_billing_info: WorkBillingInfo) -> Self:
        return ErpInvoiceLineItem.work_billing_infos.add(self, work_billing_info)

    def remove_work_billing_info(self, work_billing_info: WorkBillingInfo) -> Self:
        return ErpInvoiceLineItem.work_billing_infos.remove(self, work_billing_info)

    def clear_work_billing_infos(self) -> Self:
        return ErpInvoiceLineItem.work_billing_infos.clear(self)

    def num_work_billing_info(self) -> int:
        return ErpInvoiceLineItem.work_billing_infos.count(self)

    def get_work_billing_info_by_mrid(self, mrid: str) -> WorkBillingInfo | None:
        return ErpInvoiceLineItem.work_billing_infos.get_by_mrid(self, mrid)

    def add_customer_billing_info(self, customer_billing_info: CustomerBillingInfo) -> Self:
        return ErpInvoiceLineItem.customer_billing_infos.add(self, customer_billing_info)

    def remove_customer_billing_info(self, customer_billing_info: CustomerBillingInfo) -> Self:
        return ErpInvoiceLineItem.customer_billing_infos.remove(self, customer_billing_info)

    def clear_customer_billing_infos(self) -> Self:
        return ErpInvoiceLineItem.customer_billing_infos.clear(self)

    def num_customer_billing_info(self) -> int:
        return ErpInvoiceLineItem.customer_billing_infos.count(self)

    def get_customer_billing_info_by_mrid(self, mrid: str) -> CustomerBillingInfo | None:
        return ErpInvoiceLineItem.customer_billing_infos.get_by_mrid(self, mrid)
