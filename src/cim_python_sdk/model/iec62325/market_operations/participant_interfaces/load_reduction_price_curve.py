"""CIM class LoadReductionPriceCurve (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_bid import (
        LoadBid,
    )


class LoadReductionPriceCurve(Curve):
    """This is the price sensitivity that bidder expresses for allowing market load
    interruption. Relationship between price (Y1-axis) vs. MW (X-axis)."""

    __slots__ = ("_load_bid",)

    load_bid: One[LoadBid] = One(
        EndMeta(
            name="load_bid",
            cim_role="LoadBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_bid:LoadBid",
            many=False,
            lower=1,
            upper=1,
            inverse="load_reduction_price_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadReductionPriceCurve",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{753672A1-11E1-4850-8525-DCD1CD02FB80}",
        ends=(load_bid.meta,),
    )

    def __init__(
        self,
        *,
        load_bid: LoadBid | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if load_bid is not None:
            self.load_bid = load_bid
