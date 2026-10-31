"""CIM class TransactionBidClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.transaction_bid_results import (
        TransactionBidResults,
    )


class TransactionBidClearing(MarketFactors):
    """Contains the intervals relavent for the associated TransactionBidResults. For example,
    Day Ahead cleared results for the transaction bids for each interval of the market day."""

    __slots__ = ("_transaction_bid_results",)

    transaction_bid_results: Many[TransactionBidResults] = Many(
        EndMeta(
            name="transaction_bid_results",
            cim_role="TransactionBidResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.transaction_bid_results:TransactionBidResults",
            many=True,
            lower=0,
            upper=None,
            inverse="transaction_bid_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransactionBidClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{A39B0D3F-B3C6-45e2-BA4F-E7C4CE37598A}",
        ends=(transaction_bid_results.meta,),
    )

    def __init__(
        self,
        *,
        transaction_bid_results: Iterable[TransactionBidResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if transaction_bid_results is not None:
            TransactionBidClearing.transaction_bid_results.extend(self, transaction_bid_results)

    def add_transaction_bid_result(self, transaction_bid_result: TransactionBidResults) -> Self:
        return TransactionBidClearing.transaction_bid_results.add(self, transaction_bid_result)

    def remove_transaction_bid_result(self, transaction_bid_result: TransactionBidResults) -> Self:
        return TransactionBidClearing.transaction_bid_results.remove(self, transaction_bid_result)

    def clear_transaction_bid_results(self) -> Self:
        return TransactionBidClearing.transaction_bid_results.clear(self)

    def num_transaction_bid_result(self) -> int:
        return TransactionBidClearing.transaction_bid_results.count(self)

    def get_transaction_bid_result_by_mrid(self, mrid: str) -> TransactionBidResults | None:
        return TransactionBidClearing.transaction_bid_results.get_by_mrid(self, mrid)
