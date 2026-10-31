"""CIM class ErpJournal (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal_entry import (
        ErpJournalEntry,
    )


class ErpJournal(ErpDocument):
    """Book for recording accounting transactions as they occur. Transactions and adjustments
    are first recorded in a journal, which is like a diary of instructions, advising which
    account to be charged and by how much.

    A journal represents a change in the balances of a business's financial accounts. Many
    tasks or transactions throughout an enterprise will result in the creation of a journal.
    Some examples are creating a customer invoice, paying a vendor, transferring inventory,
    or paying employees."""

    __slots__ = ("_erp_journal_entries",)

    erp_journal_entries: Many[ErpJournalEntry] = Many(
        EndMeta(
            name="erp_journal_entries",
            cim_role="ErpJournalEntries",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal_entry:ErpJournalEntry",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_journal",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpJournal",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{89974BFB-E268-45d8-A05F-020CAA9C3781}",
        ends=(erp_journal_entries.meta,),
    )

    def __init__(
        self,
        *,
        erp_journal_entries: Iterable[ErpJournalEntry] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_journal_entries is not None:
            ErpJournal.erp_journal_entries.extend(self, erp_journal_entries)

    def add_erp_journal_entry(self, erp_journal_entry: ErpJournalEntry) -> Self:
        return ErpJournal.erp_journal_entries.add(self, erp_journal_entry)

    def remove_erp_journal_entry(self, erp_journal_entry: ErpJournalEntry) -> Self:
        return ErpJournal.erp_journal_entries.remove(self, erp_journal_entry)

    def clear_erp_journal_entries(self) -> Self:
        return ErpJournal.erp_journal_entries.clear(self)

    def num_erp_journal_entry(self) -> int:
        return ErpJournal.erp_journal_entries.count(self)

    def get_erp_journal_entry_by_mrid(self, mrid: str) -> ErpJournalEntry | None:
        return ErpJournal.erp_journal_entries.get_by_mrid(self, mrid)
