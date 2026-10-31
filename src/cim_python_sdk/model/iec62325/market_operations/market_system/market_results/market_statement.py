"""CIM class MarketStatement (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement_line_item import (
        MarketStatementLineItem,
    )


class MarketStatement(Document):
    """A statement is a roll up of statement line items. Each statement along with its line
    items provide the details of specific charges at any given time. Used by Billing and
    Settlement."""

    __slots__ = (
        "_market_statement_line_item",
        "end",
        "reference_number",
        "start",
        "trade_date",
        "transaction_date",
    )

    trade_date: _dt.datetime | None
    reference_number: str | None
    start: _dt.datetime | None
    end: _dt.datetime | None
    transaction_date: _dt.datetime | None

    market_statement_line_item: Many[MarketStatementLineItem] = Many(
        EndMeta(
            name="market_statement_line_item",
            cim_role="MarketStatementLineItem",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement_line_item:MarketStatementLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="market_statement",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketStatement",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{6EF21B53-20A7-4174-BC67-2E175BCEEDDB}",
        attributes=(
            AttrMeta("trade_date", "tradeDate", "datetime", 0, 1, "primitive"),
            AttrMeta("reference_number", "referenceNumber", "str", 0, 1, "primitive"),
            AttrMeta("start", "start", "datetime", 0, 1, "primitive"),
            AttrMeta("end", "end", "datetime", 0, 1, "primitive"),
            AttrMeta("transaction_date", "transactionDate", "datetime", 0, 1, "primitive"),
        ),
        ends=(market_statement_line_item.meta,),
    )

    def __init__(
        self,
        *,
        trade_date: _dt.datetime | None = None,
        reference_number: str | None = None,
        start: _dt.datetime | None = None,
        end: _dt.datetime | None = None,
        transaction_date: _dt.datetime | None = None,
        market_statement_line_item: Iterable[MarketStatementLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.trade_date = trade_date
        self.reference_number = reference_number
        self.start = start
        self.end = end
        self.transaction_date = transaction_date
        if market_statement_line_item is not None:
            MarketStatement.market_statement_line_item.extend(self, market_statement_line_item)

    def add_market_statement_line_item(
        self, market_statement_line_item: MarketStatementLineItem
    ) -> Self:
        return MarketStatement.market_statement_line_item.add(self, market_statement_line_item)

    def remove_market_statement_line_item(
        self, market_statement_line_item: MarketStatementLineItem
    ) -> Self:
        return MarketStatement.market_statement_line_item.remove(self, market_statement_line_item)

    def clear_market_statement_line_item(self) -> Self:
        return MarketStatement.market_statement_line_item.clear(self)

    def num_market_statement_line_item(self) -> int:
        return MarketStatement.market_statement_line_item.count(self)

    def get_market_statement_line_item_by_mrid(self, mrid: str) -> MarketStatementLineItem | None:
        return MarketStatement.market_statement_line_item.get_by_mrid(self, mrid)
