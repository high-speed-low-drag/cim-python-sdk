"""CIM class PlannedMarketEvent (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_actual_event import (
        MarketActualEvent,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market import (
        PlannedMarket,
    )


class PlannedMarketEvent(IdentifiedObject):
    """This class represents planned events. Used to model the various planned events in a
    market (closing time, clearing time, etc.)"""

    __slots__ = ("_market_actual_event", "_planned_market", "event_type", "planned_time")

    event_type: str | None
    planned_time: int | None

    planned_market: Many[PlannedMarket] = Many(
        EndMeta(
            name="planned_market",
            cim_role="PlannedMarket",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market:PlannedMarket",
            many=True,
            lower=0,
            upper=None,
            inverse="planned_market_event",
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
            inverse="planned_market_event",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PlannedMarketEvent",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{F5455A24-65BB-48af-ADBB-F31BB885FD75}",
        attributes=(
            AttrMeta("event_type", "eventType", "str", 0, 1, "primitive"),
            AttrMeta("planned_time", "plannedTime", "int", 0, 1, "primitive"),
        ),
        ends=(
            planned_market.meta,
            market_actual_event.meta,
        ),
    )

    def __init__(
        self,
        *,
        event_type: str | None = None,
        planned_time: int | None = None,
        planned_market: Iterable[PlannedMarket] | None = None,
        market_actual_event: Iterable[MarketActualEvent] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.event_type = event_type
        self.planned_time = planned_time
        if planned_market is not None:
            PlannedMarketEvent.planned_market.extend(self, planned_market)
        if market_actual_event is not None:
            PlannedMarketEvent.market_actual_event.extend(self, market_actual_event)

    def add_planned_market(self, planned_market: PlannedMarket) -> Self:
        return PlannedMarketEvent.planned_market.add(self, planned_market)

    def remove_planned_market(self, planned_market: PlannedMarket) -> Self:
        return PlannedMarketEvent.planned_market.remove(self, planned_market)

    def clear_planned_market(self) -> Self:
        return PlannedMarketEvent.planned_market.clear(self)

    def num_planned_market(self) -> int:
        return PlannedMarketEvent.planned_market.count(self)

    def add_market_actual_event(self, market_actual_event: MarketActualEvent) -> Self:
        return PlannedMarketEvent.market_actual_event.add(self, market_actual_event)

    def remove_market_actual_event(self, market_actual_event: MarketActualEvent) -> Self:
        return PlannedMarketEvent.market_actual_event.remove(self, market_actual_event)

    def clear_market_actual_event(self) -> Self:
        return PlannedMarketEvent.market_actual_event.clear(self)

    def num_market_actual_event(self) -> int:
        return PlannedMarketEvent.market_actual_event.count(self)

    def get_market_actual_event_by_mrid(self, mrid: str) -> MarketActualEvent | None:
        return PlannedMarketEvent.market_actual_event.get_by_mrid(self, mrid)
