"""CIM class BidPriceCurve (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_price_schedule import (
        BidPriceSchedule,
    )


class BidPriceCurve(Curve):
    """Relationship between unit operating price in $/hour (Y-axis) and unit output in MW
    (X-axis)."""

    __slots__ = ("_bid_schedule",)

    bid_schedule: Many[BidPriceSchedule] = Many(
        EndMeta(
            name="bid_schedule",
            cim_role="BidSchedule",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_price_schedule:BidPriceSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="bid_price_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BidPriceCurve",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{D5563BE9-55F0-4d7f-B59C-90077147E532}",
        ends=(bid_schedule.meta,),
    )

    def __init__(
        self,
        *,
        bid_schedule: Iterable[BidPriceSchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if bid_schedule is not None:
            BidPriceCurve.bid_schedule.extend(self, bid_schedule)

    def add_bid_schedule(self, bid_schedule: BidPriceSchedule) -> Self:
        return BidPriceCurve.bid_schedule.add(self, bid_schedule)

    def remove_bid_schedule(self, bid_schedule: BidPriceSchedule) -> Self:
        return BidPriceCurve.bid_schedule.remove(self, bid_schedule)

    def clear_bid_schedule(self) -> Self:
        return BidPriceCurve.bid_schedule.clear(self)

    def num_bid_schedule(self) -> int:
        return BidPriceCurve.bid_schedule.count(self)

    def get_bid_schedule_by_mrid(self, mrid: str) -> BidPriceSchedule | None:
        return BidPriceCurve.bid_schedule.get_by_mrid(self, mrid)
