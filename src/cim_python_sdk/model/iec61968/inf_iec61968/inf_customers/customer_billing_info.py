"""CIM class CustomerBillingInfo (TC57CIM/IEC61968/InfIEC61968/InfCustomers). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.customer_billing_kind import (
        CustomerBillingKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item import (
        ErpInvoiceLineItem,
    )


class CustomerBillingInfo(Document):
    """The creation of the monthly customer billing statements is the method employed to notify
    Customers of charges, adjustments and credits applied to their account for Services and
    Products. The actuall billing occurs through an ErpInvoice. The CustomerBillingInfo
    includes information from the payment, collection, meter reading, installed meter,
    service, site, customer, customer account, customer agreement, services and pricing
    subject areas. Each component price shows up as a separate line item on the ErpInvoice.

    The Customer Billing Statement may include collection and account messages,
    marketing/civic event messages and bill inserts.

    One Customer Billing Statement is produced for all Agreements under a CustomerAccount
    per billing cycle date defined in 'CustomerAccount.billingCycle'.

    The history of CustomerBillingInfo, Invoices and Payments is to be maintained in
    associated ActivityRecords."""

    __slots__ = (
        "_customer_account",
        "_erp_invoice_line_items",
        "billing_date",
        "due_date",
        "kind",
        "last_payment_amt",
        "last_payment_date",
        "out_balance",
        "pymt_plan_amt",
        "pymt_plan_type",
    )

    kind: CustomerBillingKind | None
    billing_date: _dt.date | None
    due_date: _dt.date | None
    out_balance: _decimal.Decimal | None  # Money
    pymt_plan_amt: _decimal.Decimal | None  # Money
    pymt_plan_type: str | None
    last_payment_date: _dt.date | None
    last_payment_amt: _decimal.Decimal | None  # Money

    customer_account: One[CustomerAccount] = One(
        EndMeta(
            name="customer_account",
            cim_role="CustomerAccount",
            target="cim_python_sdk.model.iec61968.customers.customer_account:CustomerAccount",
            many=False,
            lower=0,
            upper=1,
            inverse="customer_billing_infos",
            aggregation="none",
        )
    )
    erp_invoice_line_items: Many[ErpInvoiceLineItem] = Many(
        EndMeta(
            name="erp_invoice_line_items",
            cim_role="ErpInvoiceLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_billing_infos",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CustomerBillingInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfCustomers",
        guid="{555E5812-1CAB-4db1-91AC-2A265CF3C3C5}",
        attributes=(
            AttrMeta("kind", "kind", "CustomerBillingKind", 0, 1, "enumeration"),
            AttrMeta("billing_date", "billingDate", "date", 0, 1, "primitive"),
            AttrMeta("due_date", "dueDate", "date", 0, 1, "primitive"),
            AttrMeta("out_balance", "outBalance", "Money", 0, 1, "cimdatatype"),
            AttrMeta("pymt_plan_amt", "pymtPlanAmt", "Money", 0, 1, "cimdatatype"),
            AttrMeta("pymt_plan_type", "pymtPlanType", "str", 0, 1, "primitive"),
            AttrMeta("last_payment_date", "lastPaymentDate", "date", 0, 1, "primitive"),
            AttrMeta("last_payment_amt", "lastPaymentAmt", "Money", 0, 1, "cimdatatype"),
        ),
        ends=(
            customer_account.meta,
            erp_invoice_line_items.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: CustomerBillingKind | None = None,
        billing_date: _dt.date | None = None,
        due_date: _dt.date | None = None,
        out_balance: _decimal.Decimal | None = None,
        pymt_plan_amt: _decimal.Decimal | None = None,
        pymt_plan_type: str | None = None,
        last_payment_date: _dt.date | None = None,
        last_payment_amt: _decimal.Decimal | None = None,
        customer_account: CustomerAccount | None = None,
        erp_invoice_line_items: Iterable[ErpInvoiceLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.billing_date = billing_date
        self.due_date = due_date
        self.out_balance = out_balance
        self.pymt_plan_amt = pymt_plan_amt
        self.pymt_plan_type = pymt_plan_type
        self.last_payment_date = last_payment_date
        self.last_payment_amt = last_payment_amt
        if customer_account is not None:
            self.customer_account = customer_account
        if erp_invoice_line_items is not None:
            CustomerBillingInfo.erp_invoice_line_items.extend(self, erp_invoice_line_items)

    def add_erp_invoice_line_item(self, erp_invoice_line_item: ErpInvoiceLineItem) -> Self:
        return CustomerBillingInfo.erp_invoice_line_items.add(self, erp_invoice_line_item)

    def remove_erp_invoice_line_item(self, erp_invoice_line_item: ErpInvoiceLineItem) -> Self:
        return CustomerBillingInfo.erp_invoice_line_items.remove(self, erp_invoice_line_item)

    def clear_erp_invoice_line_items(self) -> Self:
        return CustomerBillingInfo.erp_invoice_line_items.clear(self)

    def num_erp_invoice_line_item(self) -> int:
        return CustomerBillingInfo.erp_invoice_line_items.count(self)

    def get_erp_invoice_line_item_by_mrid(self, mrid: str) -> ErpInvoiceLineItem | None:
        return CustomerBillingInfo.erp_invoice_line_items.get_by_mrid(self, mrid)
