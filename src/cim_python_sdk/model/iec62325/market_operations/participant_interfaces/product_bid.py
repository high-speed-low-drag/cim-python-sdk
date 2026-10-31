"""CIM class ProductBid (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_product import (
        MarketProduct,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_distribution_factor import (
        BidDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_hourly_product_schedule import (
        BidHourlyProductSchedule,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_price_schedule import (
        BidPriceSchedule,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_self_sched import (
        BidSelfSched,
    )


class ProductBid(IdentifiedObject):
    """Component of a bid that pertains to one market product."""

    __slots__ = (
        "_bid",
        "_bid_distribution_factor",
        "_bid_hourly_product_schedule",
        "_bid_schedule",
        "_bid_self_sched",
        "_market_product",
    )

    bid_distribution_factor: Many[BidDistributionFactor] = Many(
        EndMeta(
            name="bid_distribution_factor",
            cim_role="BidDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_distribution_factor:BidDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="product_bid",
            aggregation="none",
        )
    )
    bid_self_sched: Many[BidSelfSched] = Many(
        EndMeta(
            name="bid_self_sched",
            cim_role="BidSelfSched",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_self_sched:BidSelfSched",
            many=True,
            lower=0,
            upper=None,
            inverse="product_bid",
            aggregation="none",
        )
    )
    bid: One[Bid] = One(
        EndMeta(
            name="bid",
            cim_role="Bid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid:Bid",
            many=False,
            lower=1,
            upper=1,
            inverse="product_bids",
            aggregation="none",
        )
    )
    bid_schedule: Many[BidPriceSchedule] = Many(
        EndMeta(
            name="bid_schedule",
            cim_role="BidSchedule",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_price_schedule:BidPriceSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="product_bid",
            aggregation="none",
        )
    )
    market_product: One[MarketProduct] = One(
        EndMeta(
            name="market_product",
            cim_role="MarketProduct",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_product:MarketProduct",
            many=False,
            lower=1,
            upper=1,
            inverse="product_bids",
            aggregation="none",
        )
    )
    bid_hourly_product_schedule: Many[BidHourlyProductSchedule] = Many(
        EndMeta(
            name="bid_hourly_product_schedule",
            cim_role="BidHourlyProductSchedule",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_hourly_product_schedule:BidHourlyProductSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="product_bid",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProductBid",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{417C5B05-3165-4405-8422-9275E3C59AC4}",
        ends=(
            bid_distribution_factor.meta,
            bid_self_sched.meta,
            bid.meta,
            bid_schedule.meta,
            market_product.meta,
            bid_hourly_product_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        bid_distribution_factor: Iterable[BidDistributionFactor] | None = None,
        bid_self_sched: Iterable[BidSelfSched] | None = None,
        bid: Bid | None = None,
        bid_schedule: Iterable[BidPriceSchedule] | None = None,
        market_product: MarketProduct | None = None,
        bid_hourly_product_schedule: Iterable[BidHourlyProductSchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if bid_distribution_factor is not None:
            ProductBid.bid_distribution_factor.extend(self, bid_distribution_factor)
        if bid_self_sched is not None:
            ProductBid.bid_self_sched.extend(self, bid_self_sched)
        if bid is not None:
            self.bid = bid
        if bid_schedule is not None:
            ProductBid.bid_schedule.extend(self, bid_schedule)
        if market_product is not None:
            self.market_product = market_product
        if bid_hourly_product_schedule is not None:
            ProductBid.bid_hourly_product_schedule.extend(self, bid_hourly_product_schedule)

    def add_bid_distribution_factor(self, bid_distribution_factor: BidDistributionFactor) -> Self:
        return ProductBid.bid_distribution_factor.add(self, bid_distribution_factor)

    def remove_bid_distribution_factor(
        self, bid_distribution_factor: BidDistributionFactor
    ) -> Self:
        return ProductBid.bid_distribution_factor.remove(self, bid_distribution_factor)

    def clear_bid_distribution_factor(self) -> Self:
        return ProductBid.bid_distribution_factor.clear(self)

    def num_bid_distribution_factor(self) -> int:
        return ProductBid.bid_distribution_factor.count(self)

    def add_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return ProductBid.bid_self_sched.add(self, bid_self_sched)

    def remove_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return ProductBid.bid_self_sched.remove(self, bid_self_sched)

    def clear_bid_self_sched(self) -> Self:
        return ProductBid.bid_self_sched.clear(self)

    def num_bid_self_sched(self) -> int:
        return ProductBid.bid_self_sched.count(self)

    def get_bid_self_sched_by_mrid(self, mrid: str) -> BidSelfSched | None:
        return ProductBid.bid_self_sched.get_by_mrid(self, mrid)

    def add_bid_schedule(self, bid_schedule: BidPriceSchedule) -> Self:
        return ProductBid.bid_schedule.add(self, bid_schedule)

    def remove_bid_schedule(self, bid_schedule: BidPriceSchedule) -> Self:
        return ProductBid.bid_schedule.remove(self, bid_schedule)

    def clear_bid_schedule(self) -> Self:
        return ProductBid.bid_schedule.clear(self)

    def num_bid_schedule(self) -> int:
        return ProductBid.bid_schedule.count(self)

    def get_bid_schedule_by_mrid(self, mrid: str) -> BidPriceSchedule | None:
        return ProductBid.bid_schedule.get_by_mrid(self, mrid)

    def add_bid_hourly_product_schedule(
        self, bid_hourly_product_schedule: BidHourlyProductSchedule
    ) -> Self:
        return ProductBid.bid_hourly_product_schedule.add(self, bid_hourly_product_schedule)

    def remove_bid_hourly_product_schedule(
        self, bid_hourly_product_schedule: BidHourlyProductSchedule
    ) -> Self:
        return ProductBid.bid_hourly_product_schedule.remove(self, bid_hourly_product_schedule)

    def clear_bid_hourly_product_schedule(self) -> Self:
        return ProductBid.bid_hourly_product_schedule.clear(self)

    def num_bid_hourly_product_schedule(self) -> int:
        return ProductBid.bid_hourly_product_schedule.count(self)

    def get_bid_hourly_product_schedule_by_mrid(self, mrid: str) -> BidHourlyProductSchedule | None:
        return ProductBid.bid_hourly_product_schedule.get_by_mrid(self, mrid)
