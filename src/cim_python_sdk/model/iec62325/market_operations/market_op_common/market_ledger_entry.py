"""CIM class MarketLedgerEntry (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.market_ledger import (
        MarketLedger,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.settlement import (
        Settlement,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mkt_account_kind import (
        MktAccountKind,
    )


class MarketLedgerEntry(CimObject):
    """Details of an individual entry in a ledger, which was posted from a journal on the
    posted date."""

    __slots__ = (
        "_market_ledger",
        "_settlement",
        "account_id",
        "account_kind",
        "amount",
        "posted_date_time",
        "status",
        "transaction_date_time",
    )

    account_id: str | None
    account_kind: MktAccountKind | None
    amount: _decimal.Decimal | None  # Money
    posted_date_time: _dt.datetime | None
    status: Status | None
    transaction_date_time: _dt.datetime | None

    settlement: Many[Settlement] = Many(
        EndMeta(
            name="settlement",
            cim_role="Settlement",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.settlement:Settlement",
            many=True,
            lower=0,
            upper=None,
            inverse="market_ledger_entry",
            aggregation="none",
        )
    )
    market_ledger: One[MarketLedger] = One(
        EndMeta(
            name="market_ledger",
            cim_role="MarketLedger",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.market_ledger:MarketLedger",
            many=False,
            lower=1,
            upper=1,
            inverse="market_ledger_entries",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketLedgerEntry",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{6820DAEE-AAED-43ee-9364-DA01ED2BCB7D}",
        attributes=(
            AttrMeta("account_id", "accountID", "str", 0, 1, "primitive"),
            AttrMeta("account_kind", "accountKind", "MktAccountKind", 0, 1, "enumeration"),
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("posted_date_time", "postedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
            AttrMeta("transaction_date_time", "transactionDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            settlement.meta,
            market_ledger.meta,
        ),
    )

    def __init__(
        self,
        *,
        account_id: str | None = None,
        account_kind: MktAccountKind | None = None,
        amount: _decimal.Decimal | None = None,
        posted_date_time: _dt.datetime | None = None,
        status: Status | None = None,
        transaction_date_time: _dt.datetime | None = None,
        settlement: Iterable[Settlement] | None = None,
        market_ledger: MarketLedger | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.account_id = account_id
        self.account_kind = account_kind
        self.amount = amount
        self.posted_date_time = posted_date_time
        self.status = status
        self.transaction_date_time = transaction_date_time
        if settlement is not None:
            MarketLedgerEntry.settlement.extend(self, settlement)
        if market_ledger is not None:
            self.market_ledger = market_ledger

    def add_settlement(self, settlement: Settlement) -> Self:
        return MarketLedgerEntry.settlement.add(self, settlement)

    def remove_settlement(self, settlement: Settlement) -> Self:
        return MarketLedgerEntry.settlement.remove(self, settlement)

    def clear_settlement(self) -> Self:
        return MarketLedgerEntry.settlement.clear(self)

    def num_settlement(self) -> int:
        return MarketLedgerEntry.settlement.count(self)

    def get_settlement_by_mrid(self, mrid: str) -> Settlement | None:
        return MarketLedgerEntry.settlement.get_by_mrid(self, mrid)
