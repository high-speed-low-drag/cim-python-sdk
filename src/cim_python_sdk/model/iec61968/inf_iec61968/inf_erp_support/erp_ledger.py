"""CIM class ErpLedger (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_entry import (
        ErpLedgerEntry,
    )


class ErpLedger(ErpDocument):
    """In accounting transactions, a ledger is a book containing accounts to which debits and
    credits are posted from journals, where transactions are initially recorded. Journal
    entries are periodically posted to the ledger. Ledger Actual represents actual amounts
    by account within ledger within company or business area. Actual amounts may be
    generated in a source application and then loaded to a specific ledger within the
    enterprise general ledger or budget application."""

    __slots__ = ("_erp_ledger_entries",)

    erp_ledger_entries: Many[ErpLedgerEntry] = Many(
        EndMeta(
            name="erp_ledger_entries",
            cim_role="ErpLedgerEntries",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_entry:ErpLedgerEntry",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_ledger",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpLedger",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{E9DF60B7-4E1B-4d37-A980-EFBB2FBEFDA8}",
        ends=(erp_ledger_entries.meta,),
    )

    def __init__(
        self,
        *,
        erp_ledger_entries: Iterable[ErpLedgerEntry] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_ledger_entries is not None:
            ErpLedger.erp_ledger_entries.extend(self, erp_ledger_entries)

    def add_erp_ledger_entry(self, erp_ledger_entry: ErpLedgerEntry) -> Self:
        return ErpLedger.erp_ledger_entries.add(self, erp_ledger_entry)

    def remove_erp_ledger_entry(self, erp_ledger_entry: ErpLedgerEntry) -> Self:
        return ErpLedger.erp_ledger_entries.remove(self, erp_ledger_entry)

    def clear_erp_ledger_entries(self) -> Self:
        return ErpLedger.erp_ledger_entries.clear(self)

    def num_erp_ledger_entry(self) -> int:
        return ErpLedger.erp_ledger_entries.count(self)

    def get_erp_ledger_entry_by_mrid(self, mrid: str) -> ErpLedgerEntry | None:
        return ErpLedger.erp_ledger_entries.get_by_mrid(self, mrid)
