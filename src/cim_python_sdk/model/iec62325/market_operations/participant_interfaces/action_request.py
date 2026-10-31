"""CIM class ActionRequest (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.action_type import ActionType
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade import Trade


class ActionRequest(CimObject):
    """Action request against an existing Trade."""

    __slots__ = ("_bid", "_trade", "action_name")

    action_name: ActionType | None

    trade: Many[Trade] = Many(
        EndMeta(
            name="trade",
            cim_role="Trade",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade:Trade",
            many=True,
            lower=0,
            upper=None,
            inverse="action_request",
            aggregation="none",
        )
    )
    bid: Many[Bid] = Many(
        EndMeta(
            name="bid",
            cim_role="Bid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid:Bid",
            many=True,
            lower=0,
            upper=None,
            inverse="action_request",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ActionRequest",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{E7BE52F0-B8A9-4d48-B746-7B06946B50CA}",
        attributes=(AttrMeta("action_name", "actionName", "ActionType", 0, 1, "enumeration"),),
        ends=(
            trade.meta,
            bid.meta,
        ),
    )

    def __init__(
        self,
        *,
        action_name: ActionType | None = None,
        trade: Iterable[Trade] | None = None,
        bid: Iterable[Bid] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.action_name = action_name
        if trade is not None:
            ActionRequest.trade.extend(self, trade)
        if bid is not None:
            ActionRequest.bid.extend(self, bid)

    def add_trade(self, trade: Trade) -> Self:
        return ActionRequest.trade.add(self, trade)

    def remove_trade(self, trade: Trade) -> Self:
        return ActionRequest.trade.remove(self, trade)

    def clear_trade(self) -> Self:
        return ActionRequest.trade.clear(self)

    def num_trade(self) -> int:
        return ActionRequest.trade.count(self)

    def get_trade_by_mrid(self, mrid: str) -> Trade | None:
        return ActionRequest.trade.get_by_mrid(self, mrid)

    def add_bid(self, bid: Bid) -> Self:
        return ActionRequest.bid.add(self, bid)

    def remove_bid(self, bid: Bid) -> Self:
        return ActionRequest.bid.remove(self, bid)

    def clear_bid(self) -> Self:
        return ActionRequest.bid.clear(self)

    def num_bid(self) -> int:
        return ActionRequest.bid.count(self)

    def get_bid_by_mrid(self, mrid: str) -> Bid | None:
        return ActionRequest.bid.get_by_mrid(self, mrid)
