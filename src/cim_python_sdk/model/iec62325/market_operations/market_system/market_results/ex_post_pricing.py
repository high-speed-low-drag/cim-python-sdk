"""CIM class ExPostPricing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_pricing_results import (
        ExPostPricingResults,
    )


class ExPostPricing(MarketFactors):
    """Model of ex-post pricing of nodes."""

    __slots__ = ("_ex_post_results", "energy_price")

    energy_price: float | None

    ex_post_results: Many[ExPostPricingResults] = Many(
        EndMeta(
            name="ex_post_results",
            cim_role="ExPostResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_pricing_results:ExPostPricingResults",
            many=True,
            lower=0,
            upper=None,
            inverse="ex_post_pricing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExPostPricing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{7126046F-1F0B-4a9e-8640-86396331A06C}",
        attributes=(AttrMeta("energy_price", "energyPrice", "float", 0, 1, "primitive"),),
        ends=(ex_post_results.meta,),
    )

    def __init__(
        self,
        *,
        energy_price: float | None = None,
        ex_post_results: Iterable[ExPostPricingResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.energy_price = energy_price
        if ex_post_results is not None:
            ExPostPricing.ex_post_results.extend(self, ex_post_results)

    def add_ex_post_result(self, ex_post_result: ExPostPricingResults) -> Self:
        return ExPostPricing.ex_post_results.add(self, ex_post_result)

    def remove_ex_post_result(self, ex_post_result: ExPostPricingResults) -> Self:
        return ExPostPricing.ex_post_results.remove(self, ex_post_result)

    def clear_ex_post_results(self) -> Self:
        return ExPostPricing.ex_post_results.clear(self)

    def num_ex_post_result(self) -> int:
        return ExPostPricing.ex_post_results.count(self)
