"""CIM class MarketActualEvent (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_run import MarketRun
    from cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market_event import (
        PlannedMarketEvent,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_event_status_kind import (
        MarketEventStatusKind,
    )


class MarketActualEvent(IdentifiedObject):
    """This class represents the actual instance of an event."""

    __slots__ = (
        "_market_run",
        "_planned_market_event",
        "event_comments",
        "event_end_time",
        "event_start_time",
        "event_status",
        "event_type",
    )

    event_comments: str | None
    event_end_time: _dt.datetime | None
    event_start_time: _dt.datetime | None
    event_status: MarketEventStatusKind | None
    event_type: str | None

    planned_market_event: One[PlannedMarketEvent] = One(
        EndMeta(
            name="planned_market_event",
            cim_role="PlannedMarketEvent",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market_event:PlannedMarketEvent",
            many=False,
            lower=0,
            upper=1,
            inverse="market_actual_event",
            aggregation="none",
        )
    )
    market_run: One[MarketRun] = One(
        EndMeta(
            name="market_run",
            cim_role="MarketRun",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_run:MarketRun",
            many=False,
            lower=0,
            upper=1,
            inverse="market_actual_event",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketActualEvent",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{4A7047CA-692A-4f28-B52C-2F3FFF88BBDA}",
        attributes=(
            AttrMeta("event_comments", "eventComments", "str", 1, 1, "primitive"),
            AttrMeta("event_end_time", "eventEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("event_start_time", "eventStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("event_status", "eventStatus", "MarketEventStatusKind", 1, 1, "enumeration"),
            AttrMeta("event_type", "eventType", "str", 1, 1, "primitive"),
        ),
        ends=(
            planned_market_event.meta,
            market_run.meta,
        ),
    )

    def __init__(
        self,
        *,
        event_comments: str | None = None,
        event_end_time: _dt.datetime | None = None,
        event_start_time: _dt.datetime | None = None,
        event_status: MarketEventStatusKind | None = None,
        event_type: str | None = None,
        planned_market_event: PlannedMarketEvent | None = None,
        market_run: MarketRun | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.event_comments = event_comments
        self.event_end_time = event_end_time
        self.event_start_time = event_start_time
        self.event_status = event_status
        self.event_type = event_type
        if planned_market_event is not None:
            self.planned_market_event = planned_market_event
        if market_run is not None:
            self.market_run = market_run
