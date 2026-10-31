"""CIM class TradeProduct (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.trade_type import TradeType
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade import Trade


class TradeProduct(CimObject):
    """TradeType TradeProduct

    IST (InterSC Trade) PHY (Physical Energy Trade)

    IST APN (Energy Trades at Aggregated Pricing Nodes)

    IST CPT (Converted Physical Energy Trade)

    AST (Ancilliary Services Trade) RUT (Regulation Up Trade)

    AST RDT (Regulation Down Trade)

    AST SRT (Spinning Reserve Trade)

    AST NRT (Non-Spinning Reserve Trade)

    UCT (Unit Commitment Trade) null"""

    __slots__ = ("_trade", "trade_product_type", "trade_type")

    trade_type: TradeType | None
    trade_product_type: str | None

    trade: Many[Trade] = Many(
        EndMeta(
            name="trade",
            cim_role="Trade",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade:Trade",
            many=True,
            lower=0,
            upper=None,
            inverse="trade_product",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TradeProduct",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{634B14D4-5D26-43dc-B7DC-BA7F311E04FF}",
        attributes=(
            AttrMeta("trade_type", "tradeType", "TradeType", 0, 1, "enumeration"),
            AttrMeta("trade_product_type", "tradeProductType", "str", 0, 1, "primitive"),
        ),
        ends=(trade.meta,),
    )

    def __init__(
        self,
        *,
        trade_type: TradeType | None = None,
        trade_product_type: str | None = None,
        trade: Iterable[Trade] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.trade_type = trade_type
        self.trade_product_type = trade_product_type
        if trade is not None:
            TradeProduct.trade.extend(self, trade)

    def add_trade(self, trade: Trade) -> Self:
        return TradeProduct.trade.add(self, trade)

    def remove_trade(self, trade: Trade) -> Self:
        return TradeProduct.trade.remove(self, trade)

    def clear_trade(self) -> Self:
        return TradeProduct.trade.clear(self)

    def num_trade(self) -> int:
        return TradeProduct.trade.count(self)

    def get_trade_by_mrid(self, mrid: str) -> Trade | None:
        return TradeProduct.trade.get_by_mrid(self, mrid)
