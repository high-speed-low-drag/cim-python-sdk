"""CIM class AncillaryServiceClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_market_results.market_case_clearing import (
        MarketCaseClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_region_results import (
        MarketRegionResults,
    )


class AncillaryServiceClearing(MarketFactors):
    """Model of results of market clearing with respect to Ancillary Service products."""

    __slots__ = ("_market_case_clearing", "_market_region_results")

    market_case_clearing: One[MarketCaseClearing] = One(
        EndMeta(
            name="market_case_clearing",
            cim_role="MarketCaseClearing",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_market_results.market_case_clearing:MarketCaseClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="market_product_clearing",
            aggregation="none",
        )
    )
    market_region_results: Many[MarketRegionResults] = Many(
        EndMeta(
            name="market_region_results",
            cim_role="MarketRegionResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_region_results:MarketRegionResults",
            many=True,
            lower=1,
            upper=None,
            inverse="ancillary_service_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AncillaryServiceClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{0137CEC6-490C-4189-8727-73C31AA6CE08}",
        ends=(
            market_case_clearing.meta,
            market_region_results.meta,
        ),
    )

    def __init__(
        self,
        *,
        market_case_clearing: MarketCaseClearing | None = None,
        market_region_results: Iterable[MarketRegionResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if market_case_clearing is not None:
            self.market_case_clearing = market_case_clearing
        if market_region_results is not None:
            AncillaryServiceClearing.market_region_results.extend(self, market_region_results)

    def add_market_region_result(self, market_region_result: MarketRegionResults) -> Self:
        return AncillaryServiceClearing.market_region_results.add(self, market_region_result)

    def remove_market_region_result(self, market_region_result: MarketRegionResults) -> Self:
        return AncillaryServiceClearing.market_region_results.remove(self, market_region_result)

    def clear_market_region_results(self) -> Self:
        return AncillaryServiceClearing.market_region_results.clear(self)

    def num_market_region_result(self) -> int:
        return AncillaryServiceClearing.market_region_results.count(self)
