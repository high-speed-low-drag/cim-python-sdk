"""CIM class ErpPayableLineItem (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item import (
        ErpInvoiceLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal_entry import (
        ErpJournalEntry,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable import ErpPayable
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payment import ErpPayment


class ErpPayableLineItem(ErpIdentifiedObject):
    """Of an ErpPayable, a line item references an ErpInvoiceLineitem or other source such as
    credit memos."""

    __slots__ = (
        "_erp_invoice_line_item",
        "_erp_journal_entries",
        "_erp_payable",
        "_erp_payments",
        "status",
    )

    status: Status | None

    erp_invoice_line_item: One[ErpInvoiceLineItem] = One(
        EndMeta(
            name="erp_invoice_line_item",
            cim_role="ErpInvoiceLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_payable_line_item",
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
            inverse="erp_payable_line_items",
            aggregation="none",
        )
    )
    erp_payable: One[ErpPayable] = One(
        EndMeta(
            name="erp_payable",
            cim_role="ErpPayable",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable:ErpPayable",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_payable_line_items",
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
            inverse="erp_payable_line_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpPayableLineItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{0BCC0D0E-6785-4bcc-A35C-D4820897FF73}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(
            erp_invoice_line_item.meta,
            erp_payments.meta,
            erp_payable.meta,
            erp_journal_entries.meta,
        ),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        erp_invoice_line_item: ErpInvoiceLineItem | None = None,
        erp_payments: Iterable[ErpPayment] | None = None,
        erp_payable: ErpPayable | None = None,
        erp_journal_entries: Iterable[ErpJournalEntry] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if erp_invoice_line_item is not None:
            self.erp_invoice_line_item = erp_invoice_line_item
        if erp_payments is not None:
            ErpPayableLineItem.erp_payments.extend(self, erp_payments)
        if erp_payable is not None:
            self.erp_payable = erp_payable
        if erp_journal_entries is not None:
            ErpPayableLineItem.erp_journal_entries.extend(self, erp_journal_entries)

    def add_erp_payment(self, erp_payment: ErpPayment) -> Self:
        return ErpPayableLineItem.erp_payments.add(self, erp_payment)

    def remove_erp_payment(self, erp_payment: ErpPayment) -> Self:
        return ErpPayableLineItem.erp_payments.remove(self, erp_payment)

    def clear_erp_payments(self) -> Self:
        return ErpPayableLineItem.erp_payments.clear(self)

    def num_erp_payment(self) -> int:
        return ErpPayableLineItem.erp_payments.count(self)

    def get_erp_payment_by_mrid(self, mrid: str) -> ErpPayment | None:
        return ErpPayableLineItem.erp_payments.get_by_mrid(self, mrid)

    def add_erp_journal_entry(self, erp_journal_entry: ErpJournalEntry) -> Self:
        return ErpPayableLineItem.erp_journal_entries.add(self, erp_journal_entry)

    def remove_erp_journal_entry(self, erp_journal_entry: ErpJournalEntry) -> Self:
        return ErpPayableLineItem.erp_journal_entries.remove(self, erp_journal_entry)

    def clear_erp_journal_entries(self) -> Self:
        return ErpPayableLineItem.erp_journal_entries.clear(self)

    def num_erp_journal_entry(self) -> int:
        return ErpPayableLineItem.erp_journal_entries.count(self)

    def get_erp_journal_entry_by_mrid(self, mrid: str) -> ErpJournalEntry | None:
        return ErpPayableLineItem.erp_journal_entries.get_by_mrid(self, mrid)
