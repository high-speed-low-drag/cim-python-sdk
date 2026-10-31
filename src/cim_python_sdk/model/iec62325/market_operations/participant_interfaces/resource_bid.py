"""CIM class ResourceBid (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_error import (
        BidError,
    )


class ResourceBid(Bid):
    """Energy bid for generation, load, or virtual type for the whole of the market-trading
    period (i.e., one day in day ahead market or one hour in the real time market)."""

    __slots__ = (
        "_bid_error",
        "aggregation_flag",
        "bid_status",
        "commodity_type",
        "contingency_avail_flag",
        "created_iso",
        "energy_max_day",
        "energy_min_day",
        "market_sep_flag",
        "min_dispatch_time",
        "resource_loading_type",
        "shut_downs_max_day",
        "shut_downs_max_week",
        "start_ups_max_day",
        "start_ups_max_week",
        "virtual",
    )

    aggregation_flag: int | None
    bid_status: str | None
    commodity_type: str | None
    contingency_avail_flag: YesNo | None
    created_iso: YesNo | None
    energy_max_day: float | None
    energy_min_day: float | None
    market_sep_flag: str | None
    min_dispatch_time: int | None
    resource_loading_type: int | None
    shut_downs_max_day: int | None
    shut_downs_max_week: int | None
    start_ups_max_day: int | None
    start_ups_max_week: int | None
    virtual: bool | None

    bid_error: Many[BidError] = Many(
        EndMeta(
            name="bid_error",
            cim_role="BidError",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_error:BidError",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_bid",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceBid",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{C30DB807-0AE3-4e0c-AAE1-4E9433E532BA}",
        attributes=(
            AttrMeta("aggregation_flag", "aggregationFlag", "int", 0, 1, "primitive"),
            AttrMeta("bid_status", "bidStatus", "str", 0, 1, "primitive"),
            AttrMeta("commodity_type", "commodityType", "str", 0, 1, "primitive"),
            AttrMeta(
                "contingency_avail_flag", "contingencyAvailFlag", "YesNo", 0, 1, "enumeration"
            ),
            AttrMeta("created_iso", "createdISO", "YesNo", 0, 1, "enumeration"),
            AttrMeta("energy_max_day", "energyMaxDay", "float", 0, 1, "primitive"),
            AttrMeta("energy_min_day", "energyMinDay", "float", 0, 1, "primitive"),
            AttrMeta("market_sep_flag", "marketSepFlag", "str", 0, 1, "primitive"),
            AttrMeta("min_dispatch_time", "minDispatchTime", "int", 0, 1, "primitive"),
            AttrMeta("resource_loading_type", "resourceLoadingType", "int", 0, 1, "primitive"),
            AttrMeta("shut_downs_max_day", "shutDownsMaxDay", "int", 0, 1, "primitive"),
            AttrMeta("shut_downs_max_week", "shutDownsMaxWeek", "int", 0, 1, "primitive"),
            AttrMeta("start_ups_max_day", "startUpsMaxDay", "int", 0, 1, "primitive"),
            AttrMeta("start_ups_max_week", "startUpsMaxWeek", "int", 0, 1, "primitive"),
            AttrMeta("virtual", "virtual", "bool", 0, 1, "primitive"),
        ),
        ends=(bid_error.meta,),
    )

    def __init__(
        self,
        *,
        aggregation_flag: int | None = None,
        bid_status: str | None = None,
        commodity_type: str | None = None,
        contingency_avail_flag: YesNo | None = None,
        created_iso: YesNo | None = None,
        energy_max_day: float | None = None,
        energy_min_day: float | None = None,
        market_sep_flag: str | None = None,
        min_dispatch_time: int | None = None,
        resource_loading_type: int | None = None,
        shut_downs_max_day: int | None = None,
        shut_downs_max_week: int | None = None,
        start_ups_max_day: int | None = None,
        start_ups_max_week: int | None = None,
        virtual: bool | None = None,
        bid_error: Iterable[BidError] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.aggregation_flag = aggregation_flag
        self.bid_status = bid_status
        self.commodity_type = commodity_type
        self.contingency_avail_flag = contingency_avail_flag
        self.created_iso = created_iso
        self.energy_max_day = energy_max_day
        self.energy_min_day = energy_min_day
        self.market_sep_flag = market_sep_flag
        self.min_dispatch_time = min_dispatch_time
        self.resource_loading_type = resource_loading_type
        self.shut_downs_max_day = shut_downs_max_day
        self.shut_downs_max_week = shut_downs_max_week
        self.start_ups_max_day = start_ups_max_day
        self.start_ups_max_week = start_ups_max_week
        self.virtual = virtual
        if bid_error is not None:
            ResourceBid.bid_error.extend(self, bid_error)

    def add_bid_error(self, bid_error: BidError) -> Self:
        return ResourceBid.bid_error.add(self, bid_error)

    def remove_bid_error(self, bid_error: BidError) -> Self:
        return ResourceBid.bid_error.remove(self, bid_error)

    def clear_bid_error(self) -> Self:
        return ResourceBid.bid_error.clear(self)

    def num_bid_error(self) -> int:
        return ResourceBid.bid_error.count(self)

    def get_bid_error_by_mrid(self, mrid: str) -> BidError | None:
        return ResourceBid.bid_error.get_by_mrid(self, mrid)
