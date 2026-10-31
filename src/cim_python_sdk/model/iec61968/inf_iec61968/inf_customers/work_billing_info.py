"""CIM class WorkBillingInfo (TC57CIM/IEC61968/InfIEC61968/InfCustomers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer_account import CustomerAccount
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item import (
        ErpInvoiceLineItem,
    )
    from cim_python_sdk.model.iec61968.work.work import Work


class WorkBillingInfo(Document):
    """Billing information for work performed for the customer. The history of Work Billing
    Info, Invoices, and Payments is to be maintained in associated ActivityRecords."""

    __slots__ = (
        "_customer_account",
        "_erp_line_items",
        "_works",
        "cost_estimate",
        "deposit",
        "discount",
        "due_date_time",
        "issue_date_time",
        "received_date_time",
        "work_price",
    )

    issue_date_time: _dt.datetime | None
    due_date_time: _dt.datetime | None
    received_date_time: _dt.datetime | None
    work_price: _decimal.Decimal | None  # Money
    cost_estimate: _decimal.Decimal | None  # Money
    deposit: _decimal.Decimal | None  # Money
    discount: float | None

    customer_account: One[CustomerAccount] = One(
        EndMeta(
            name="customer_account",
            cim_role="CustomerAccount",
            target="cim_python_sdk.model.iec61968.customers.customer_account:CustomerAccount",
            many=False,
            lower=0,
            upper=1,
            inverse="work_billing_infos",
            aggregation="none",
        )
    )
    erp_line_items: Many[ErpInvoiceLineItem] = Many(
        EndMeta(
            name="erp_line_items",
            cim_role="ErpLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="work_billing_infos",
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
            inverse="work_billing_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WorkBillingInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfCustomers",
        guid="{259E88DB-BC1E-460c-93C8-A033E1E5F1BD}",
        attributes=(
            AttrMeta("issue_date_time", "issueDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("due_date_time", "dueDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("received_date_time", "receivedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("work_price", "workPrice", "Money", 0, 1, "cimdatatype"),
            AttrMeta("cost_estimate", "costEstimate", "Money", 0, 1, "cimdatatype"),
            AttrMeta("deposit", "deposit", "Money", 0, 1, "cimdatatype"),
            AttrMeta("discount", "discount", "float", 0, 1, "primitive"),
        ),
        ends=(
            customer_account.meta,
            erp_line_items.meta,
            works.meta,
        ),
    )

    def __init__(
        self,
        *,
        issue_date_time: _dt.datetime | None = None,
        due_date_time: _dt.datetime | None = None,
        received_date_time: _dt.datetime | None = None,
        work_price: _decimal.Decimal | None = None,
        cost_estimate: _decimal.Decimal | None = None,
        deposit: _decimal.Decimal | None = None,
        discount: float | None = None,
        customer_account: CustomerAccount | None = None,
        erp_line_items: Iterable[ErpInvoiceLineItem] | None = None,
        works: Iterable[Work] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.issue_date_time = issue_date_time
        self.due_date_time = due_date_time
        self.received_date_time = received_date_time
        self.work_price = work_price
        self.cost_estimate = cost_estimate
        self.deposit = deposit
        self.discount = discount
        if customer_account is not None:
            self.customer_account = customer_account
        if erp_line_items is not None:
            WorkBillingInfo.erp_line_items.extend(self, erp_line_items)
        if works is not None:
            WorkBillingInfo.works.extend(self, works)

    def add_erp_line_item(self, erp_line_item: ErpInvoiceLineItem) -> Self:
        return WorkBillingInfo.erp_line_items.add(self, erp_line_item)

    def remove_erp_line_item(self, erp_line_item: ErpInvoiceLineItem) -> Self:
        return WorkBillingInfo.erp_line_items.remove(self, erp_line_item)

    def clear_erp_line_items(self) -> Self:
        return WorkBillingInfo.erp_line_items.clear(self)

    def num_erp_line_item(self) -> int:
        return WorkBillingInfo.erp_line_items.count(self)

    def get_erp_line_item_by_mrid(self, mrid: str) -> ErpInvoiceLineItem | None:
        return WorkBillingInfo.erp_line_items.get_by_mrid(self, mrid)

    def add_work(self, work: Work) -> Self:
        return WorkBillingInfo.works.add(self, work)

    def remove_work(self, work: Work) -> Self:
        return WorkBillingInfo.works.remove(self, work)

    def clear_works(self) -> Self:
        return WorkBillingInfo.works.clear(self)

    def num_work(self) -> int:
        return WorkBillingInfo.works.count(self)

    def get_work_by_mrid(self, mrid: str) -> Work | None:
        return WorkBillingInfo.works.get_by_mrid(self, mrid)
