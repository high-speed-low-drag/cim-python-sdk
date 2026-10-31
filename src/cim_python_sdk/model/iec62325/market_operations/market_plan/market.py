"""CIM class Market (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import (
        MarketFactors,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_product import (
        MarketProduct,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_run import MarketRun


class Market(IdentifiedObject):
    """Market (e.g. Day Ahead Market, Real Time Market) with a description of the Market
    operation control parameters."""

    __slots__ = (
        "_market_factors",
        "_market_products",
        "_market_run",
        "actual_end",
        "actual_start",
        "dst",
        "end",
        "local_time_zone",
        "start",
        "status",
        "time_interval_length",
        "trading_day",
        "trading_period",
    )

    actual_end: _dt.datetime | None
    actual_start: _dt.datetime | None
    dst: bool | None
    end: _dt.datetime | None
    local_time_zone: str | None
    start: _dt.datetime | None
    status: str | None
    time_interval_length: float | None
    trading_day: _dt.datetime | None
    trading_period: str | None

    market_run: Many[MarketRun] = Many(
        EndMeta(
            name="market_run",
            cim_role="MarketRun",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_run:MarketRun",
            many=True,
            lower=0,
            upper=None,
            inverse="market",
            aggregation="none",
        )
    )
    market_products: Many[MarketProduct] = Many(
        EndMeta(
            name="market_products",
            cim_role="MarketProducts",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_product:MarketProduct",
            many=True,
            lower=1,
            upper=None,
            inverse="market",
            aggregation="none",
        )
    )
    market_factors: Many[MarketFactors] = Many(
        EndMeta(
            name="market_factors",
            cim_role="MarketFactors",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors:MarketFactors",
            many=True,
            lower=0,
            upper=None,
            inverse="market",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Market",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{0E7800EF-F016-473c-A6CA-15C11994D3B1}",
        attributes=(
            AttrMeta("actual_end", "actualEnd", "datetime", 0, 1, "primitive"),
            AttrMeta("actual_start", "actualStart", "datetime", 0, 1, "primitive"),
            AttrMeta("dst", "dst", "bool", 0, 1, "primitive"),
            AttrMeta("end", "end", "datetime", 0, 1, "primitive"),
            AttrMeta("local_time_zone", "localTimeZone", "str", 0, 1, "primitive"),
            AttrMeta("start", "start", "datetime", 0, 1, "primitive"),
            AttrMeta("status", "status", "str", 0, 1, "primitive"),
            AttrMeta("time_interval_length", "timeIntervalLength", "float", 0, 1, "primitive"),
            AttrMeta("trading_day", "tradingDay", "datetime", 0, 1, "primitive"),
            AttrMeta("trading_period", "tradingPeriod", "str", 0, 1, "primitive"),
        ),
        ends=(
            market_run.meta,
            market_products.meta,
            market_factors.meta,
        ),
    )

    def __init__(
        self,
        *,
        actual_end: _dt.datetime | None = None,
        actual_start: _dt.datetime | None = None,
        dst: bool | None = None,
        end: _dt.datetime | None = None,
        local_time_zone: str | None = None,
        start: _dt.datetime | None = None,
        status: str | None = None,
        time_interval_length: float | None = None,
        trading_day: _dt.datetime | None = None,
        trading_period: str | None = None,
        market_run: Iterable[MarketRun] | None = None,
        market_products: Iterable[MarketProduct] | None = None,
        market_factors: Iterable[MarketFactors] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.actual_end = actual_end
        self.actual_start = actual_start
        self.dst = dst
        self.end = end
        self.local_time_zone = local_time_zone
        self.start = start
        self.status = status
        self.time_interval_length = time_interval_length
        self.trading_day = trading_day
        self.trading_period = trading_period
        if market_run is not None:
            Market.market_run.extend(self, market_run)
        if market_products is not None:
            Market.market_products.extend(self, market_products)
        if market_factors is not None:
            Market.market_factors.extend(self, market_factors)

    def add_market_run(self, market_run: MarketRun) -> Self:
        return Market.market_run.add(self, market_run)

    def remove_market_run(self, market_run: MarketRun) -> Self:
        return Market.market_run.remove(self, market_run)

    def clear_market_run(self) -> Self:
        return Market.market_run.clear(self)

    def num_market_run(self) -> int:
        return Market.market_run.count(self)

    def get_market_run_by_mrid(self, mrid: str) -> MarketRun | None:
        return Market.market_run.get_by_mrid(self, mrid)

    def add_market_product(self, market_product: MarketProduct) -> Self:
        return Market.market_products.add(self, market_product)

    def remove_market_product(self, market_product: MarketProduct) -> Self:
        return Market.market_products.remove(self, market_product)

    def clear_market_products(self) -> Self:
        return Market.market_products.clear(self)

    def num_market_product(self) -> int:
        return Market.market_products.count(self)

    def get_market_product_by_mrid(self, mrid: str) -> MarketProduct | None:
        return Market.market_products.get_by_mrid(self, mrid)

    def add_market_factor(self, market_factor: MarketFactors) -> Self:
        return Market.market_factors.add(self, market_factor)

    def remove_market_factor(self, market_factor: MarketFactors) -> Self:
        return Market.market_factors.remove(self, market_factor)

    def clear_market_factors(self) -> Self:
        return Market.market_factors.clear(self)

    def num_market_factor(self) -> int:
        return Market.market_factors.count(self)

    def get_market_factor_by_mrid(self, mrid: str) -> MarketFactors | None:
        return Market.market_factors.get_by_mrid(self, mrid)
