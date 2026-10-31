"""CIM class MarketRun (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market import Market
    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_actual_event import (
        MarketActualEvent,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market import (
        PlannedMarket,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.execution_type import (
        ExecutionType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType


class MarketRun(IdentifiedObject):
    """This class represents an actual instance of a planned market. For example, a Day Ahead
    market opens with the Bid Submission, ends with the closing of the Bid Submission. The
    market run represent the whole process. MarketRuns can be defined for markets such as
    Day Ahead Market, Real Time Market, Hour Ahead Market, Week Ahead Market, etc."""

    __slots__ = (
        "_market",
        "_market_actual_event",
        "_planned_market",
        "execution_type",
        "market_approval_time",
        "market_approved_status",
        "market_end_time",
        "market_start_time",
        "market_type",
        "reported_state",
        "run_state",
    )

    execution_type: ExecutionType | None
    market_approval_time: _dt.datetime | None
    market_approved_status: bool | None
    market_end_time: _dt.datetime | None
    market_start_time: _dt.datetime | None
    market_type: MarketType | None
    reported_state: str | None
    run_state: str | None

    market: One[Market] = One(
        EndMeta(
            name="market",
            cim_role="Market",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market:Market",
            many=False,
            lower=1,
            upper=1,
            inverse="market_run",
            aggregation="none",
        )
    )
    market_actual_event: Many[MarketActualEvent] = Many(
        EndMeta(
            name="market_actual_event",
            cim_role="MarketActualEvent",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_actual_event:MarketActualEvent",
            many=True,
            lower=1,
            upper=None,
            inverse="market_run",
            aggregation="none",
        )
    )
    planned_market: One[PlannedMarket] = One(
        EndMeta(
            name="planned_market",
            cim_role="PlannedMarket",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market:PlannedMarket",
            many=False,
            lower=1,
            upper=1,
            inverse="market_run",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketRun",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{E99740BA-F157-4353-95B5-F466E80BB1BC}",
        attributes=(
            AttrMeta("execution_type", "executionType", "ExecutionType", 0, 1, "enumeration"),
            AttrMeta("market_approval_time", "marketApprovalTime", "datetime", 0, 1, "primitive"),
            AttrMeta("market_approved_status", "marketApprovedStatus", "bool", 0, 1, "primitive"),
            AttrMeta("market_end_time", "marketEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("market_start_time", "marketStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
            AttrMeta("reported_state", "reportedState", "str", 0, 1, "primitive"),
            AttrMeta("run_state", "runState", "str", 0, 1, "primitive"),
        ),
        ends=(
            market.meta,
            market_actual_event.meta,
            planned_market.meta,
        ),
    )

    def __init__(
        self,
        *,
        execution_type: ExecutionType | None = None,
        market_approval_time: _dt.datetime | None = None,
        market_approved_status: bool | None = None,
        market_end_time: _dt.datetime | None = None,
        market_start_time: _dt.datetime | None = None,
        market_type: MarketType | None = None,
        reported_state: str | None = None,
        run_state: str | None = None,
        market: Market | None = None,
        market_actual_event: Iterable[MarketActualEvent] | None = None,
        planned_market: PlannedMarket | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.execution_type = execution_type
        self.market_approval_time = market_approval_time
        self.market_approved_status = market_approved_status
        self.market_end_time = market_end_time
        self.market_start_time = market_start_time
        self.market_type = market_type
        self.reported_state = reported_state
        self.run_state = run_state
        if market is not None:
            self.market = market
        if market_actual_event is not None:
            MarketRun.market_actual_event.extend(self, market_actual_event)
        if planned_market is not None:
            self.planned_market = planned_market

    def add_market_actual_event(self, market_actual_event: MarketActualEvent) -> Self:
        return MarketRun.market_actual_event.add(self, market_actual_event)

    def remove_market_actual_event(self, market_actual_event: MarketActualEvent) -> Self:
        return MarketRun.market_actual_event.remove(self, market_actual_event)

    def clear_market_actual_event(self) -> Self:
        return MarketRun.market_actual_event.clear(self)

    def num_market_actual_event(self) -> int:
        return MarketRun.market_actual_event.count(self)

    def get_market_actual_event_by_mrid(self, mrid: str) -> MarketActualEvent | None:
        return MarketRun.market_actual_event.get_by_mrid(self, mrid)
