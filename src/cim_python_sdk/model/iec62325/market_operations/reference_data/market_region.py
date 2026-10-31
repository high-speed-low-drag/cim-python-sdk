"""CIM class MarketRegion (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
    AggregateNode,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.reserve_demand_curve import (
        ReserveDemandCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_market_region_results import (
        ExPostMarketRegionResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_region_results import (
        MarketRegionResults,
    )


class MarketRegion(AggregateNode):
    """A specialized class of AggregatedNode type. Defines the MarketRegions. Regions could be
    system Market Regions, Energy Regions or Ancillary Service Regions."""

    __slots__ = (
        "_ex_post_market_region_results",
        "_market_region_results",
        "_reserve_demand_curve",
    )

    market_region_results: Many[MarketRegionResults] = Many(
        EndMeta(
            name="market_region_results",
            cim_role="MarketRegionResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_region_results:MarketRegionResults",
            many=True,
            lower=1,
            upper=None,
            inverse="market_region",
            aggregation="none",
        )
    )
    ex_post_market_region_results: Many[ExPostMarketRegionResults] = Many(
        EndMeta(
            name="ex_post_market_region_results",
            cim_role="ExPostMarketRegionResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_market_region_results:ExPostMarketRegionResults",
            many=True,
            lower=0,
            upper=None,
            inverse="market_region",
            aggregation="none",
        )
    )
    reserve_demand_curve: Many[ReserveDemandCurve] = Many(
        EndMeta(
            name="reserve_demand_curve",
            cim_role="ReserveDemandCurve",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.reserve_demand_curve:ReserveDemandCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="market_region",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketRegion",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{2E8AF05C-A65B-4002-9AB4-40F7E351CF05}",
        ends=(
            market_region_results.meta,
            ex_post_market_region_results.meta,
            reserve_demand_curve.meta,
        ),
    )

    def __init__(
        self,
        *,
        market_region_results: Iterable[MarketRegionResults] | None = None,
        ex_post_market_region_results: Iterable[ExPostMarketRegionResults] | None = None,
        reserve_demand_curve: Iterable[ReserveDemandCurve] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if market_region_results is not None:
            MarketRegion.market_region_results.extend(self, market_region_results)
        if ex_post_market_region_results is not None:
            MarketRegion.ex_post_market_region_results.extend(self, ex_post_market_region_results)
        if reserve_demand_curve is not None:
            MarketRegion.reserve_demand_curve.extend(self, reserve_demand_curve)

    def add_market_region_result(self, market_region_result: MarketRegionResults) -> Self:
        return MarketRegion.market_region_results.add(self, market_region_result)

    def remove_market_region_result(self, market_region_result: MarketRegionResults) -> Self:
        return MarketRegion.market_region_results.remove(self, market_region_result)

    def clear_market_region_results(self) -> Self:
        return MarketRegion.market_region_results.clear(self)

    def num_market_region_result(self) -> int:
        return MarketRegion.market_region_results.count(self)

    def add_ex_post_market_region_result(
        self, ex_post_market_region_result: ExPostMarketRegionResults
    ) -> Self:
        return MarketRegion.ex_post_market_region_results.add(self, ex_post_market_region_result)

    def remove_ex_post_market_region_result(
        self, ex_post_market_region_result: ExPostMarketRegionResults
    ) -> Self:
        return MarketRegion.ex_post_market_region_results.remove(self, ex_post_market_region_result)

    def clear_ex_post_market_region_results(self) -> Self:
        return MarketRegion.ex_post_market_region_results.clear(self)

    def num_ex_post_market_region_result(self) -> int:
        return MarketRegion.ex_post_market_region_results.count(self)

    def add_reserve_demand_curve(self, reserve_demand_curve: ReserveDemandCurve) -> Self:
        return MarketRegion.reserve_demand_curve.add(self, reserve_demand_curve)

    def remove_reserve_demand_curve(self, reserve_demand_curve: ReserveDemandCurve) -> Self:
        return MarketRegion.reserve_demand_curve.remove(self, reserve_demand_curve)

    def clear_reserve_demand_curve(self) -> Self:
        return MarketRegion.reserve_demand_curve.clear(self)

    def num_reserve_demand_curve(self) -> int:
        return MarketRegion.reserve_demand_curve.count(self)

    def get_reserve_demand_curve_by_mrid(self, mrid: str) -> ReserveDemandCurve | None:
        return MarketRegion.reserve_demand_curve.get_by_mrid(self, mrid)
