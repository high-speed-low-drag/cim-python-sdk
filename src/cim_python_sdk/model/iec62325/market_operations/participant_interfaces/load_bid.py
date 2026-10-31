"""CIM class LoadBid (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.resource_bid import (
    ResourceBid,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.area_load_bid import (
        AreaLoadBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_reduction_price_curve import (
        LoadReductionPriceCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.ramp_rate_curve import (
        RampRateCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_load import (
        RegisteredLoad,
    )


class LoadBid(ResourceBid):
    """Offer to supply energy/ancillary services from a load resource (participating load
    reduces consumption)."""

    __slots__ = (
        "_area_load_bid",
        "_load_reduction_price_curve",
        "_ramp_rate_curve",
        "_registered_load",
        "drop_ramp_rate",
        "load_red_initiation_cost",
        "load_red_initiation_time",
        "market_date",
        "metered_value",
        "min_load",
        "min_load_reduction",
        "min_load_reduction_cost",
        "min_load_reduction_interval",
        "min_time_bet_load_red",
        "pick_up_ramp_rate",
        "price_setting",
        "req_notice_time",
        "shutdown_cost",
    )

    drop_ramp_rate: float | None  # ActivePowerChangeRate
    load_red_initiation_cost: _decimal.Decimal | None  # Money
    load_red_initiation_time: float | None
    market_date: _dt.datetime | None
    metered_value: bool | None
    min_load: float | None  # ActivePower
    min_load_reduction: float | None  # ActivePower
    min_load_reduction_cost: _decimal.Decimal | None  # Money
    min_load_reduction_interval: float | None
    min_time_bet_load_red: float | None
    pick_up_ramp_rate: float | None  # ActivePowerChangeRate
    price_setting: bool | None
    req_notice_time: float | None
    shutdown_cost: _decimal.Decimal | None  # Money

    registered_load: One[RegisteredLoad] = One(
        EndMeta(
            name="registered_load",
            cim_role="RegisteredLoad",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_load:RegisteredLoad",
            many=False,
            lower=0,
            upper=1,
            inverse="load_bids",
            aggregation="none",
        )
    )
    area_load_bid: One[AreaLoadBid] = One(
        EndMeta(
            name="area_load_bid",
            cim_role="AreaLoadBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.area_load_bid:AreaLoadBid",
            many=False,
            lower=0,
            upper=1,
            inverse="load_bid",
            aggregation="none",
        )
    )
    load_reduction_price_curve: Many[LoadReductionPriceCurve] = Many(
        EndMeta(
            name="load_reduction_price_curve",
            cim_role="LoadReductionPriceCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_reduction_price_curve:LoadReductionPriceCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="load_bid",
            aggregation="none",
        )
    )
    ramp_rate_curve: Many[RampRateCurve] = Many(
        EndMeta(
            name="ramp_rate_curve",
            cim_role="RampRateCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.ramp_rate_curve:RampRateCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="load_bid",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadBid",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{EDE7D5E6-419B-4e2b-9E96-D9FCD6797B89}",
        attributes=(
            AttrMeta(
                "drop_ramp_rate", "dropRampRate", "ActivePowerChangeRate", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "load_red_initiation_cost", "loadRedInitiationCost", "Money", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "load_red_initiation_time", "loadRedInitiationTime", "float", 0, 1, "primitive"
            ),
            AttrMeta("market_date", "marketDate", "datetime", 0, 1, "primitive"),
            AttrMeta("metered_value", "meteredValue", "bool", 0, 1, "primitive"),
            AttrMeta("min_load", "minLoad", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_load_reduction", "minLoadReduction", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "min_load_reduction_cost", "minLoadReductionCost", "Money", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "min_load_reduction_interval",
                "minLoadReductionInterval",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta("min_time_bet_load_red", "minTimeBetLoadRed", "float", 0, 1, "primitive"),
            AttrMeta(
                "pick_up_ramp_rate", "pickUpRampRate", "ActivePowerChangeRate", 0, 1, "cimdatatype"
            ),
            AttrMeta("price_setting", "priceSetting", "bool", 0, 1, "primitive"),
            AttrMeta("req_notice_time", "reqNoticeTime", "float", 0, 1, "primitive"),
            AttrMeta("shutdown_cost", "shutdownCost", "Money", 0, 1, "cimdatatype"),
        ),
        ends=(
            registered_load.meta,
            area_load_bid.meta,
            load_reduction_price_curve.meta,
            ramp_rate_curve.meta,
        ),
    )

    def __init__(
        self,
        *,
        drop_ramp_rate: float | None = None,
        load_red_initiation_cost: _decimal.Decimal | None = None,
        load_red_initiation_time: float | None = None,
        market_date: _dt.datetime | None = None,
        metered_value: bool | None = None,
        min_load: float | None = None,
        min_load_reduction: float | None = None,
        min_load_reduction_cost: _decimal.Decimal | None = None,
        min_load_reduction_interval: float | None = None,
        min_time_bet_load_red: float | None = None,
        pick_up_ramp_rate: float | None = None,
        price_setting: bool | None = None,
        req_notice_time: float | None = None,
        shutdown_cost: _decimal.Decimal | None = None,
        registered_load: RegisteredLoad | None = None,
        area_load_bid: AreaLoadBid | None = None,
        load_reduction_price_curve: Iterable[LoadReductionPriceCurve] | None = None,
        ramp_rate_curve: Iterable[RampRateCurve] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.drop_ramp_rate = drop_ramp_rate
        self.load_red_initiation_cost = load_red_initiation_cost
        self.load_red_initiation_time = load_red_initiation_time
        self.market_date = market_date
        self.metered_value = metered_value
        self.min_load = min_load
        self.min_load_reduction = min_load_reduction
        self.min_load_reduction_cost = min_load_reduction_cost
        self.min_load_reduction_interval = min_load_reduction_interval
        self.min_time_bet_load_red = min_time_bet_load_red
        self.pick_up_ramp_rate = pick_up_ramp_rate
        self.price_setting = price_setting
        self.req_notice_time = req_notice_time
        self.shutdown_cost = shutdown_cost
        if registered_load is not None:
            self.registered_load = registered_load
        if area_load_bid is not None:
            self.area_load_bid = area_load_bid
        if load_reduction_price_curve is not None:
            LoadBid.load_reduction_price_curve.extend(self, load_reduction_price_curve)
        if ramp_rate_curve is not None:
            LoadBid.ramp_rate_curve.extend(self, ramp_rate_curve)

    def add_load_reduction_price_curve(
        self, load_reduction_price_curve: LoadReductionPriceCurve
    ) -> Self:
        return LoadBid.load_reduction_price_curve.add(self, load_reduction_price_curve)

    def remove_load_reduction_price_curve(
        self, load_reduction_price_curve: LoadReductionPriceCurve
    ) -> Self:
        return LoadBid.load_reduction_price_curve.remove(self, load_reduction_price_curve)

    def clear_load_reduction_price_curve(self) -> Self:
        return LoadBid.load_reduction_price_curve.clear(self)

    def num_load_reduction_price_curve(self) -> int:
        return LoadBid.load_reduction_price_curve.count(self)

    def get_load_reduction_price_curve_by_mrid(self, mrid: str) -> LoadReductionPriceCurve | None:
        return LoadBid.load_reduction_price_curve.get_by_mrid(self, mrid)

    def add_ramp_rate_curve(self, ramp_rate_curve: RampRateCurve) -> Self:
        return LoadBid.ramp_rate_curve.add(self, ramp_rate_curve)

    def remove_ramp_rate_curve(self, ramp_rate_curve: RampRateCurve) -> Self:
        return LoadBid.ramp_rate_curve.remove(self, ramp_rate_curve)

    def clear_ramp_rate_curve(self) -> Self:
        return LoadBid.ramp_rate_curve.clear(self)

    def num_ramp_rate_curve(self) -> int:
        return LoadBid.ramp_rate_curve.count(self)

    def get_ramp_rate_curve_by_mrid(self, mrid: str) -> RampRateCurve | None:
        return LoadBid.ramp_rate_curve.get_by_mrid(self, mrid)
