"""CIM class TransactionBidResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.transaction_bid_clearing import (
        TransactionBidClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.transaction_bid import (
        TransactionBid,
    )


class TransactionBidResults(IdentifiedObject):
    """Contains the cleared results for each TransactionBid submitted to and accepted by the
    market."""

    __slots__ = ("_transaction_bid", "_transaction_bid_clearing", "cleared_mw", "cleared_price")

    cleared_mw: float | None
    cleared_price: float | None

    transaction_bid: One[TransactionBid] = One(
        EndMeta(
            name="transaction_bid",
            cim_role="TransactionBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.transaction_bid:TransactionBid",
            many=False,
            lower=0,
            upper=1,
            inverse="transaction_bid_results",
            aggregation="none",
        )
    )
    transaction_bid_clearing: One[TransactionBidClearing] = One(
        EndMeta(
            name="transaction_bid_clearing",
            cim_role="TransactionBidClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.transaction_bid_clearing:TransactionBidClearing",
            many=False,
            lower=1,
            upper=1,
            inverse="transaction_bid_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransactionBidResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{DFC58795-C87F-4cdb-AEE2-DF1BC5832E1B}",
        attributes=(
            AttrMeta("cleared_mw", "clearedMW", "float", 0, 1, "primitive"),
            AttrMeta("cleared_price", "clearedPrice", "float", 0, 1, "primitive"),
        ),
        ends=(
            transaction_bid.meta,
            transaction_bid_clearing.meta,
        ),
    )

    def __init__(
        self,
        *,
        cleared_mw: float | None = None,
        cleared_price: float | None = None,
        transaction_bid: TransactionBid | None = None,
        transaction_bid_clearing: TransactionBidClearing | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cleared_mw = cleared_mw
        self.cleared_price = cleared_price
        if transaction_bid is not None:
            self.transaction_bid = transaction_bid
        if transaction_bid_clearing is not None:
            self.transaction_bid_clearing = transaction_bid_clearing
