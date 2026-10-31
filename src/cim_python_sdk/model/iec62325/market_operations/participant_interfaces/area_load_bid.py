"""CIM class AreaLoadBid (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_bid import (
        LoadBid,
    )


class AreaLoadBid(Bid):
    """AreaLoadBid is not submitted by a market participant into the Markets. Instead, it is
    simply an aggregation of all LoadBids contained wtihin a specific SubControlArea. This
    entity should inherit from Bid for representation of the timeframe (startTime, stopTime)
    and the market type."""

    __slots__ = ("_load_bid", "demand_bid_mw")

    demand_bid_mw: float | None

    load_bid: Many[LoadBid] = Many(
        EndMeta(
            name="load_bid",
            cim_role="LoadBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_bid:LoadBid",
            many=True,
            lower=0,
            upper=None,
            inverse="area_load_bid",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AreaLoadBid",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{C1523A5D-368D-4b7d-B379-FD344ABE9B5C}",
        attributes=(AttrMeta("demand_bid_mw", "demandBidMW", "float", 0, 1, "primitive"),),
        ends=(load_bid.meta,),
    )

    def __init__(
        self,
        *,
        demand_bid_mw: float | None = None,
        load_bid: Iterable[LoadBid] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.demand_bid_mw = demand_bid_mw
        if load_bid is not None:
            AreaLoadBid.load_bid.extend(self, load_bid)

    def add_load_bid(self, load_bid: LoadBid) -> Self:
        return AreaLoadBid.load_bid.add(self, load_bid)

    def remove_load_bid(self, load_bid: LoadBid) -> Self:
        return AreaLoadBid.load_bid.remove(self, load_bid)

    def clear_load_bid(self) -> Self:
        return AreaLoadBid.load_bid.clear(self)

    def num_load_bid(self) -> int:
        return AreaLoadBid.load_bid.count(self)

    def get_load_bid_by_mrid(self, mrid: str) -> LoadBid | None:
        return AreaLoadBid.load_bid.get_by_mrid(self, mrid)
