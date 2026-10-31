"""CIM class MarketLedger (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.market_ledger_entry import (
        MarketLedgerEntry,
    )


class MarketLedger(CimObject):
    """In accounting transactions, a ledger is a book containing accounts to which debits and
    credits are posted from journals, where transactions are initially recorded. Journal
    entries are periodically posted to the ledger. Ledger actual represents actual amounts
    by account within ledger within company or within business area. Actual amounts may be
    generated in a source application and then loaded to a specific ledger within the
    enterprise general ledger or budget application."""

    __slots__ = ("_market_ledger_entries",)

    market_ledger_entries: Many[MarketLedgerEntry] = Many(
        EndMeta(
            name="market_ledger_entries",
            cim_role="MarketLedgerEntries",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.market_ledger_entry:MarketLedgerEntry",
            many=True,
            lower=0,
            upper=None,
            inverse="market_ledger",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketLedger",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{A6A29DB1-79CF-43de-8520-8874A84D0551}",
        ends=(market_ledger_entries.meta,),
    )

    def __init__(
        self,
        *,
        market_ledger_entries: Iterable[MarketLedgerEntry] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if market_ledger_entries is not None:
            MarketLedger.market_ledger_entries.extend(self, market_ledger_entries)

    def add_market_ledger_entry(self, market_ledger_entry: MarketLedgerEntry) -> Self:
        return MarketLedger.market_ledger_entries.add(self, market_ledger_entry)

    def remove_market_ledger_entry(self, market_ledger_entry: MarketLedgerEntry) -> Self:
        return MarketLedger.market_ledger_entries.remove(self, market_ledger_entry)

    def clear_market_ledger_entries(self) -> Self:
        return MarketLedger.market_ledger_entries.clear(self)

    def num_market_ledger_entry(self) -> int:
        return MarketLedger.market_ledger_entries.count(self)
