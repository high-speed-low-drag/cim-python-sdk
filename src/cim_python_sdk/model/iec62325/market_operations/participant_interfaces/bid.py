"""CIM class Bid (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.market_participant import MarketParticipant
    from cim_python_sdk.model.iec62325.market_operations.market_plan.energy_market import (
        EnergyMarket,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile import (
        ChargeProfile,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid import (
        MitigatedBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid_segment import (
        MitigatedBidSegment,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.rmr_determination import (
        RMRDetermination,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.action_request import (
        ActionRequest,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_hourly_schedule import (
        BidHourlySchedule,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid import (
        ProductBid,
    )


class Bid(Document):
    """Represents both bids to purchase and offers to sell energy or ancillary services in an
    RTO-sponsored market."""

    __slots__ = (
        "_action_request",
        "_bid_hourly_schedule",
        "_charge_profiles",
        "_energy_market",
        "_market_participant",
        "_mitigated_bid",
        "_mitigated_bid_segment",
        "_product_bids",
        "_rmr_determination",
        "market_type",
        "start_time",
        "stop_time",
    )

    start_time: _dt.datetime | None
    stop_time: _dt.datetime | None
    market_type: MarketType | None

    rmr_determination: Many[RMRDetermination] = Many(
        EndMeta(
            name="rmr_determination",
            cim_role="RMRDetermination",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.rmr_determination:RMRDetermination",
            many=True,
            lower=0,
            upper=None,
            inverse="bid",
            aggregation="none",
        )
    )
    mitigated_bid: Many[MitigatedBid] = Many(
        EndMeta(
            name="mitigated_bid",
            cim_role="MitigatedBid",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid:MitigatedBid",
            many=True,
            lower=0,
            upper=None,
            inverse="bid",
            aggregation="none",
        )
    )
    market_participant: One[MarketParticipant] = One(
        EndMeta(
            name="market_participant",
            cim_role="MarketParticipant",
            target="cim_python_sdk.model.iec62325.market_common.market_participant:MarketParticipant",
            many=False,
            lower=0,
            upper=1,
            inverse="bid",
            aggregation="none",
        )
    )
    energy_market: One[EnergyMarket] = One(
        EndMeta(
            name="energy_market",
            cim_role="EnergyMarket",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.energy_market:EnergyMarket",
            many=False,
            lower=1,
            upper=1,
            inverse="bids",
            aggregation="none",
        )
    )
    bid_hourly_schedule: Many[BidHourlySchedule] = Many(
        EndMeta(
            name="bid_hourly_schedule",
            cim_role="BidHourlySchedule",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_hourly_schedule:BidHourlySchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="bid",
            aggregation="none",
        )
    )
    charge_profiles: Many[ChargeProfile] = Many(
        EndMeta(
            name="charge_profiles",
            cim_role="ChargeProfiles",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile:ChargeProfile",
            many=True,
            lower=0,
            upper=None,
            inverse="bid",
            aggregation="none",
        )
    )
    mitigated_bid_segment: Many[MitigatedBidSegment] = Many(
        EndMeta(
            name="mitigated_bid_segment",
            cim_role="MitigatedBidSegment",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid_segment:MitigatedBidSegment",
            many=True,
            lower=0,
            upper=None,
            inverse="bid",
            aggregation="none",
        )
    )
    product_bids: Many[ProductBid] = Many(
        EndMeta(
            name="product_bids",
            cim_role="ProductBids",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid:ProductBid",
            many=True,
            lower=1,
            upper=None,
            inverse="bid",
            aggregation="none",
        )
    )
    action_request: One[ActionRequest] = One(
        EndMeta(
            name="action_request",
            cim_role="ActionRequest",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.action_request:ActionRequest",
            many=False,
            lower=1,
            upper=1,
            inverse="bid",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Bid",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{E904C7AF-F98A-4448-AC67-C1DD40DD70D4}",
        attributes=(
            AttrMeta("start_time", "startTime", "datetime", 0, 1, "primitive"),
            AttrMeta("stop_time", "stopTime", "datetime", 0, 1, "primitive"),
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
        ),
        ends=(
            rmr_determination.meta,
            mitigated_bid.meta,
            market_participant.meta,
            energy_market.meta,
            bid_hourly_schedule.meta,
            charge_profiles.meta,
            mitigated_bid_segment.meta,
            product_bids.meta,
            action_request.meta,
        ),
    )

    def __init__(
        self,
        *,
        start_time: _dt.datetime | None = None,
        stop_time: _dt.datetime | None = None,
        market_type: MarketType | None = None,
        rmr_determination: Iterable[RMRDetermination] | None = None,
        mitigated_bid: Iterable[MitigatedBid] | None = None,
        market_participant: MarketParticipant | None = None,
        energy_market: EnergyMarket | None = None,
        bid_hourly_schedule: Iterable[BidHourlySchedule] | None = None,
        charge_profiles: Iterable[ChargeProfile] | None = None,
        mitigated_bid_segment: Iterable[MitigatedBidSegment] | None = None,
        product_bids: Iterable[ProductBid] | None = None,
        action_request: ActionRequest | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.start_time = start_time
        self.stop_time = stop_time
        self.market_type = market_type
        if rmr_determination is not None:
            Bid.rmr_determination.extend(self, rmr_determination)
        if mitigated_bid is not None:
            Bid.mitigated_bid.extend(self, mitigated_bid)
        if market_participant is not None:
            self.market_participant = market_participant
        if energy_market is not None:
            self.energy_market = energy_market
        if bid_hourly_schedule is not None:
            Bid.bid_hourly_schedule.extend(self, bid_hourly_schedule)
        if charge_profiles is not None:
            Bid.charge_profiles.extend(self, charge_profiles)
        if mitigated_bid_segment is not None:
            Bid.mitigated_bid_segment.extend(self, mitigated_bid_segment)
        if product_bids is not None:
            Bid.product_bids.extend(self, product_bids)
        if action_request is not None:
            self.action_request = action_request

    def add_rmr_determination(self, rmr_determination: RMRDetermination) -> Self:
        return Bid.rmr_determination.add(self, rmr_determination)

    def remove_rmr_determination(self, rmr_determination: RMRDetermination) -> Self:
        return Bid.rmr_determination.remove(self, rmr_determination)

    def clear_rmr_determination(self) -> Self:
        return Bid.rmr_determination.clear(self)

    def num_rmr_determination(self) -> int:
        return Bid.rmr_determination.count(self)

    def add_mitigated_bid(self, mitigated_bid: MitigatedBid) -> Self:
        return Bid.mitigated_bid.add(self, mitigated_bid)

    def remove_mitigated_bid(self, mitigated_bid: MitigatedBid) -> Self:
        return Bid.mitigated_bid.remove(self, mitigated_bid)

    def clear_mitigated_bid(self) -> Self:
        return Bid.mitigated_bid.clear(self)

    def num_mitigated_bid(self) -> int:
        return Bid.mitigated_bid.count(self)

    def get_mitigated_bid_by_mrid(self, mrid: str) -> MitigatedBid | None:
        return Bid.mitigated_bid.get_by_mrid(self, mrid)

    def add_bid_hourly_schedule(self, bid_hourly_schedule: BidHourlySchedule) -> Self:
        return Bid.bid_hourly_schedule.add(self, bid_hourly_schedule)

    def remove_bid_hourly_schedule(self, bid_hourly_schedule: BidHourlySchedule) -> Self:
        return Bid.bid_hourly_schedule.remove(self, bid_hourly_schedule)

    def clear_bid_hourly_schedule(self) -> Self:
        return Bid.bid_hourly_schedule.clear(self)

    def num_bid_hourly_schedule(self) -> int:
        return Bid.bid_hourly_schedule.count(self)

    def get_bid_hourly_schedule_by_mrid(self, mrid: str) -> BidHourlySchedule | None:
        return Bid.bid_hourly_schedule.get_by_mrid(self, mrid)

    def add_charge_profile(self, charge_profile: ChargeProfile) -> Self:
        return Bid.charge_profiles.add(self, charge_profile)

    def remove_charge_profile(self, charge_profile: ChargeProfile) -> Self:
        return Bid.charge_profiles.remove(self, charge_profile)

    def clear_charge_profiles(self) -> Self:
        return Bid.charge_profiles.clear(self)

    def num_charge_profile(self) -> int:
        return Bid.charge_profiles.count(self)

    def get_charge_profile_by_mrid(self, mrid: str) -> ChargeProfile | None:
        return Bid.charge_profiles.get_by_mrid(self, mrid)

    def add_mitigated_bid_segment(self, mitigated_bid_segment: MitigatedBidSegment) -> Self:
        return Bid.mitigated_bid_segment.add(self, mitigated_bid_segment)

    def remove_mitigated_bid_segment(self, mitigated_bid_segment: MitigatedBidSegment) -> Self:
        return Bid.mitigated_bid_segment.remove(self, mitigated_bid_segment)

    def clear_mitigated_bid_segment(self) -> Self:
        return Bid.mitigated_bid_segment.clear(self)

    def num_mitigated_bid_segment(self) -> int:
        return Bid.mitigated_bid_segment.count(self)

    def add_product_bid(self, product_bid: ProductBid) -> Self:
        return Bid.product_bids.add(self, product_bid)

    def remove_product_bid(self, product_bid: ProductBid) -> Self:
        return Bid.product_bids.remove(self, product_bid)

    def clear_product_bids(self) -> Self:
        return Bid.product_bids.clear(self)

    def num_product_bid(self) -> int:
        return Bid.product_bids.count(self)

    def get_product_bid_by_mrid(self, mrid: str) -> ProductBid | None:
        return Bid.product_bids.get_by_mrid(self, mrid)
