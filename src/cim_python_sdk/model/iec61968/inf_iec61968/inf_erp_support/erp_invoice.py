"""CIM class ErpInvoice (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer_account import CustomerAccount
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.bill_media_kind import (
        BillMediaKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_kind import (
        ErpInvoiceKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item import (
        ErpInvoiceLineItem,
    )


class ErpInvoice(ErpDocument):
    """A roll up of invoice line items. The whole invoice has a due date and amount to be paid,
    with information such as customer, banks etc. being obtained through associations. The
    invoice roll up is based on individual line items that each contain amounts and
    descriptions for specific services or products."""

    __slots__ = (
        "_customer_account",
        "_erp_invoice_line_items",
        "amount",
        "bill_media_kind",
        "due_date",
        "kind",
        "mailed_date",
        "pro_forma",
        "reference_number",
        "transaction_date_time",
        "transfer_type",
    )

    kind: ErpInvoiceKind | None
    bill_media_kind: BillMediaKind | None
    reference_number: str | None
    amount: _decimal.Decimal | None  # Money
    due_date: _dt.date | None
    mailed_date: _dt.date | None
    transfer_type: str | None
    transaction_date_time: _dt.datetime | None
    pro_forma: bool | None

    erp_invoice_line_items: Many[ErpInvoiceLineItem] = Many(
        EndMeta(
            name="erp_invoice_line_items",
            cim_role="ErpInvoiceLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_invoice",
            aggregation="none",
        )
    )
    customer_account: One[CustomerAccount] = One(
        EndMeta(
            name="customer_account",
            cim_role="CustomerAccount",
            target="cim_python_sdk.model.iec61968.customers.customer_account:CustomerAccount",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_invoicees",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpInvoice",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{2A25121F-D3C9-413e-9DE0-67BD3846DD54}",
        attributes=(
            AttrMeta("kind", "kind", "ErpInvoiceKind", 0, 1, "enumeration"),
            AttrMeta("bill_media_kind", "billMediaKind", "BillMediaKind", 0, 1, "enumeration"),
            AttrMeta("reference_number", "referenceNumber", "str", 0, 1, "primitive"),
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("due_date", "dueDate", "date", 0, 1, "primitive"),
            AttrMeta("mailed_date", "mailedDate", "date", 0, 1, "primitive"),
            AttrMeta("transfer_type", "transferType", "str", 0, 1, "primitive"),
            AttrMeta("transaction_date_time", "transactionDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("pro_forma", "proForma", "bool", 0, 1, "primitive"),
        ),
        ends=(
            erp_invoice_line_items.meta,
            customer_account.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: ErpInvoiceKind | None = None,
        bill_media_kind: BillMediaKind | None = None,
        reference_number: str | None = None,
        amount: _decimal.Decimal | None = None,
        due_date: _dt.date | None = None,
        mailed_date: _dt.date | None = None,
        transfer_type: str | None = None,
        transaction_date_time: _dt.datetime | None = None,
        pro_forma: bool | None = None,
        erp_invoice_line_items: Iterable[ErpInvoiceLineItem] | None = None,
        customer_account: CustomerAccount | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.bill_media_kind = bill_media_kind
        self.reference_number = reference_number
        self.amount = amount
        self.due_date = due_date
        self.mailed_date = mailed_date
        self.transfer_type = transfer_type
        self.transaction_date_time = transaction_date_time
        self.pro_forma = pro_forma
        if erp_invoice_line_items is not None:
            ErpInvoice.erp_invoice_line_items.extend(self, erp_invoice_line_items)
        if customer_account is not None:
            self.customer_account = customer_account

    def add_erp_invoice_line_item(self, erp_invoice_line_item: ErpInvoiceLineItem) -> Self:
        return ErpInvoice.erp_invoice_line_items.add(self, erp_invoice_line_item)

    def remove_erp_invoice_line_item(self, erp_invoice_line_item: ErpInvoiceLineItem) -> Self:
        return ErpInvoice.erp_invoice_line_items.remove(self, erp_invoice_line_item)

    def clear_erp_invoice_line_items(self) -> Self:
        return ErpInvoice.erp_invoice_line_items.clear(self)

    def num_erp_invoice_line_item(self) -> int:
        return ErpInvoice.erp_invoice_line_items.count(self)

    def get_erp_invoice_line_item_by_mrid(self, mrid: str) -> ErpInvoiceLineItem | None:
        return ErpInvoice.erp_invoice_line_items.get_by_mrid(self, mrid)
