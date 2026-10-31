"""CIM class MarketPlan (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market import (
        PlannedMarket,
    )


class MarketPlan(IdentifiedObject):
    """This class identifies a set of planned markets."""

    __slots__ = ("_planned_market", "trading_day")

    trading_day: _dt.datetime | None

    planned_market: Many[PlannedMarket] = Many(
        EndMeta(
            name="planned_market",
            cim_role="PlannedMarket",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.planned_market:PlannedMarket",
            many=True,
            lower=1,
            upper=None,
            inverse="market_plan",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketPlan",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{78D79406-CCAC-4e37-82FE-BBB5FDB0771B}",
        attributes=(AttrMeta("trading_day", "tradingDay", "datetime", 0, 1, "primitive"),),
        ends=(planned_market.meta,),
    )

    def __init__(
        self,
        *,
        trading_day: _dt.datetime | None = None,
        planned_market: Iterable[PlannedMarket] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.trading_day = trading_day
        if planned_market is not None:
            MarketPlan.planned_market.extend(self, planned_market)

    def add_planned_market(self, planned_market: PlannedMarket) -> Self:
        return MarketPlan.planned_market.add(self, planned_market)

    def remove_planned_market(self, planned_market: PlannedMarket) -> Self:
        return MarketPlan.planned_market.remove(self, planned_market)

    def clear_planned_market(self) -> Self:
        return MarketPlan.planned_market.clear(self)

    def num_planned_market(self) -> int:
        return MarketPlan.planned_market.count(self)
