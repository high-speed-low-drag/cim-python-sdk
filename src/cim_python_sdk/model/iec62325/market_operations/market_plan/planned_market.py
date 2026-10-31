"""CIM class PlannedMarket (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_plan import MarketPlan
    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_run import MarketRun
    from cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market_event import (
        PlannedMarketEvent,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType


class PlannedMarket(CimObject):
    """Represent a planned market. For example a planned DA/HA/RT market."""

    __slots__ = (
        "_market_plan",
        "_market_run",
        "_planned_market_event",
        "market_end_time",
        "market_start_time",
        "market_type",
    )

    market_end_time: _dt.datetime | None
    market_start_time: _dt.datetime | None
    market_type: MarketType | None

    planned_market_event: Many[PlannedMarketEvent] = Many(
        EndMeta(
            name="planned_market_event",
            cim_role="PlannedMarketEvent",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market_event:PlannedMarketEvent",
            many=True,
            lower=1,
            upper=None,
            inverse="planned_market",
            aggregation="none",
        )
    )
    market_plan: One[MarketPlan] = One(
        EndMeta(
            name="market_plan",
            cim_role="MarketPlan",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_plan:MarketPlan",
            many=False,
            lower=1,
            upper=1,
            inverse="planned_market",
            aggregation="none",
        )
    )
    market_run: Many[MarketRun] = Many(
        EndMeta(
            name="market_run",
            cim_role="MarketRun",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_run:MarketRun",
            many=True,
            lower=0,
            upper=None,
            inverse="planned_market",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PlannedMarket",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{A865CCF4-5C55-4f2a-8404-AE694B815016}",
        attributes=(
            AttrMeta("market_end_time", "marketEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("market_start_time", "marketStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
        ),
        ends=(
            planned_market_event.meta,
            market_plan.meta,
            market_run.meta,
        ),
    )

    def __init__(
        self,
        *,
        market_end_time: _dt.datetime | None = None,
        market_start_time: _dt.datetime | None = None,
        market_type: MarketType | None = None,
        planned_market_event: Iterable[PlannedMarketEvent] | None = None,
        market_plan: MarketPlan | None = None,
        market_run: Iterable[MarketRun] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.market_end_time = market_end_time
        self.market_start_time = market_start_time
        self.market_type = market_type
        if planned_market_event is not None:
            PlannedMarket.planned_market_event.extend(self, planned_market_event)
        if market_plan is not None:
            self.market_plan = market_plan
        if market_run is not None:
            PlannedMarket.market_run.extend(self, market_run)

    def add_planned_market_event(self, planned_market_event: PlannedMarketEvent) -> Self:
        return PlannedMarket.planned_market_event.add(self, planned_market_event)

    def remove_planned_market_event(self, planned_market_event: PlannedMarketEvent) -> Self:
        return PlannedMarket.planned_market_event.remove(self, planned_market_event)

    def clear_planned_market_event(self) -> Self:
        return PlannedMarket.planned_market_event.clear(self)

    def num_planned_market_event(self) -> int:
        return PlannedMarket.planned_market_event.count(self)

    def get_planned_market_event_by_mrid(self, mrid: str) -> PlannedMarketEvent | None:
        return PlannedMarket.planned_market_event.get_by_mrid(self, mrid)

    def add_market_run(self, market_run: MarketRun) -> Self:
        return PlannedMarket.market_run.add(self, market_run)

    def remove_market_run(self, market_run: MarketRun) -> Self:
        return PlannedMarket.market_run.remove(self, market_run)

    def clear_market_run(self) -> Self:
        return PlannedMarket.market_run.clear(self)

    def num_market_run(self) -> int:
        return PlannedMarket.market_run.count(self)

    def get_market_run_by_mrid(self, mrid: str) -> MarketRun | None:
        return PlannedMarket.market_run.get_by_mrid(self, mrid)
