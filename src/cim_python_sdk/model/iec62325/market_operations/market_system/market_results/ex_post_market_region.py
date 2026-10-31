"""CIM class ExPostMarketRegion (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_market_region_results import (
        ExPostMarketRegionResults,
    )


class ExPostMarketRegion(MarketFactors):
    """Model of ex-post calculation of cleared MW on a regional basis."""

    __slots__ = ("_ex_post_market_region_results",)

    ex_post_market_region_results: One[ExPostMarketRegionResults] = One(
        EndMeta(
            name="ex_post_market_region_results",
            cim_role="ExPostMarketRegionResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_market_region_results:ExPostMarketRegionResults",
            many=False,
            lower=0,
            upper=1,
            inverse="ex_post_market_region",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExPostMarketRegion",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{7BE3E59F-BA80-4c3e-83B5-B52985D66244}",
        ends=(ex_post_market_region_results.meta,),
    )

    def __init__(
        self,
        *,
        ex_post_market_region_results: ExPostMarketRegionResults | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ex_post_market_region_results is not None:
            self.ex_post_market_region_results = ex_post_market_region_results
