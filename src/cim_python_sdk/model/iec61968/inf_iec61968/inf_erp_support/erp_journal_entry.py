"""CIM class ErpJournalEntry (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item import (
        ErpInvoiceLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal import ErpJournal
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_entry import (
        ErpLedgerEntry,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable_line_item import (
        ErpPayableLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_line_item import (
        ErpRecLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cost_type import CostType


class ErpJournalEntry(ErpIdentifiedObject):
    """Details of an individual entry in a journal, which is to be posted to a ledger on the
    posting date."""

    __slots__ = (
        "_cost_types",
        "_erp_invoice_line_item",
        "_erp_journal",
        "_erp_ledger_entry",
        "_erp_payable_line_items",
        "_erp_rec_line_items",
        "account_id",
        "amount",
        "posting_date_time",
        "source_id",
        "status",
        "transaction_date_time",
    )

    account_id: str | None
    amount: _decimal.Decimal | None  # Money
    posting_date_time: _dt.datetime | None
    transaction_date_time: _dt.datetime | None
    source_id: str | None
    status: Status | None

    erp_rec_line_items: Many[ErpRecLineItem] = Many(
        EndMeta(
            name="erp_rec_line_items",
            cim_role="ErpRecLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_line_item:ErpRecLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_journal_entries",
            aggregation="none",
        )
    )
    erp_ledger_entry: One[ErpLedgerEntry] = One(
        EndMeta(
            name="erp_ledger_entry",
            cim_role="ErpLedgerEntry",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_entry:ErpLedgerEntry",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_jounal_entry",
            aggregation="none",
        )
    )
    cost_types: Many[CostType] = Many(
        EndMeta(
            name="cost_types",
            cim_role="CostTypes",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cost_type:CostType",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_journal_entries",
            aggregation="none",
        )
    )
    erp_invoice_line_item: One[ErpInvoiceLineItem] = One(
        EndMeta(
            name="erp_invoice_line_item",
            cim_role="ErpInvoiceLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_journal_entries",
            aggregation="none",
        )
    )
    erp_payable_line_items: Many[ErpPayableLineItem] = Many(
        EndMeta(
            name="erp_payable_line_items",
            cim_role="ErpPayableLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable_line_item:ErpPayableLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_journal_entries",
            aggregation="none",
        )
    )
    erp_journal: One[ErpJournal] = One(
        EndMeta(
            name="erp_journal",
            cim_role="ErpJournal",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal:ErpJournal",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_journal_entries",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpJournalEntry",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{92318DC0-968A-40de-B828-7C3C5B67BCEC}",
        attributes=(
            AttrMeta("account_id", "accountID", "str", 0, 1, "primitive"),
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("posting_date_time", "postingDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("transaction_date_time", "transactionDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("source_id", "sourceID", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            erp_rec_line_items.meta,
            erp_ledger_entry.meta,
            cost_types.meta,
            erp_invoice_line_item.meta,
            erp_payable_line_items.meta,
            erp_journal.meta,
        ),
    )

    def __init__(
        self,
        *,
        account_id: str | None = None,
        amount: _decimal.Decimal | None = None,
        posting_date_time: _dt.datetime | None = None,
        transaction_date_time: _dt.datetime | None = None,
        source_id: str | None = None,
        status: Status | None = None,
        erp_rec_line_items: Iterable[ErpRecLineItem] | None = None,
        erp_ledger_entry: ErpLedgerEntry | None = None,
        cost_types: Iterable[CostType] | None = None,
        erp_invoice_line_item: ErpInvoiceLineItem | None = None,
        erp_payable_line_items: Iterable[ErpPayableLineItem] | None = None,
        erp_journal: ErpJournal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.account_id = account_id
        self.amount = amount
        self.posting_date_time = posting_date_time
        self.transaction_date_time = transaction_date_time
        self.source_id = source_id
        self.status = status
        if erp_rec_line_items is not None:
            ErpJournalEntry.erp_rec_line_items.extend(self, erp_rec_line_items)
        if erp_ledger_entry is not None:
            self.erp_ledger_entry = erp_ledger_entry
        if cost_types is not None:
            ErpJournalEntry.cost_types.extend(self, cost_types)
        if erp_invoice_line_item is not None:
            self.erp_invoice_line_item = erp_invoice_line_item
        if erp_payable_line_items is not None:
            ErpJournalEntry.erp_payable_line_items.extend(self, erp_payable_line_items)
        if erp_journal is not None:
            self.erp_journal = erp_journal

    def add_erp_rec_line_item(self, erp_rec_line_item: ErpRecLineItem) -> Self:
        return ErpJournalEntry.erp_rec_line_items.add(self, erp_rec_line_item)

    def remove_erp_rec_line_item(self, erp_rec_line_item: ErpRecLineItem) -> Self:
        return ErpJournalEntry.erp_rec_line_items.remove(self, erp_rec_line_item)

    def clear_erp_rec_line_items(self) -> Self:
        return ErpJournalEntry.erp_rec_line_items.clear(self)

    def num_erp_rec_line_item(self) -> int:
        return ErpJournalEntry.erp_rec_line_items.count(self)

    def get_erp_rec_line_item_by_mrid(self, mrid: str) -> ErpRecLineItem | None:
        return ErpJournalEntry.erp_rec_line_items.get_by_mrid(self, mrid)

    def add_cost_type(self, cost_type: CostType) -> Self:
        return ErpJournalEntry.cost_types.add(self, cost_type)

    def remove_cost_type(self, cost_type: CostType) -> Self:
        return ErpJournalEntry.cost_types.remove(self, cost_type)

    def clear_cost_types(self) -> Self:
        return ErpJournalEntry.cost_types.clear(self)

    def num_cost_type(self) -> int:
        return ErpJournalEntry.cost_types.count(self)

    def get_cost_type_by_mrid(self, mrid: str) -> CostType | None:
        return ErpJournalEntry.cost_types.get_by_mrid(self, mrid)

    def add_erp_payable_line_item(self, erp_payable_line_item: ErpPayableLineItem) -> Self:
        return ErpJournalEntry.erp_payable_line_items.add(self, erp_payable_line_item)

    def remove_erp_payable_line_item(self, erp_payable_line_item: ErpPayableLineItem) -> Self:
        return ErpJournalEntry.erp_payable_line_items.remove(self, erp_payable_line_item)

    def clear_erp_payable_line_items(self) -> Self:
        return ErpJournalEntry.erp_payable_line_items.clear(self)

    def num_erp_payable_line_item(self) -> int:
        return ErpJournalEntry.erp_payable_line_items.count(self)

    def get_erp_payable_line_item_by_mrid(self, mrid: str) -> ErpPayableLineItem | None:
        return ErpJournalEntry.erp_payable_line_items.get_by_mrid(self, mrid)
