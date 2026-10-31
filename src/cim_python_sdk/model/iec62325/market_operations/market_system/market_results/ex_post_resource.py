"""CIM class ExPostResource (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_resource_results import (
        ExPostResourceResults,
    )


class ExPostResource(MarketFactors):
    """Model of ex-post pricing of resources."""

    __slots__ = ("_ex_post_resource_results",)

    ex_post_resource_results: Many[ExPostResourceResults] = Many(
        EndMeta(
            name="ex_post_resource_results",
            cim_role="ExPostResourceResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_resource_results:ExPostResourceResults",
            many=True,
            lower=0,
            upper=None,
            inverse="ex_post_resource",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExPostResource",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{F7E72241-5CBB-4cb7-B29B-FC4EC51F8F83}",
        ends=(ex_post_resource_results.meta,),
    )

    def __init__(
        self,
        *,
        ex_post_resource_results: Iterable[ExPostResourceResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ex_post_resource_results is not None:
            ExPostResource.ex_post_resource_results.extend(self, ex_post_resource_results)

    def add_ex_post_resource_result(self, ex_post_resource_result: ExPostResourceResults) -> Self:
        return ExPostResource.ex_post_resource_results.add(self, ex_post_resource_result)

    def remove_ex_post_resource_result(
        self, ex_post_resource_result: ExPostResourceResults
    ) -> Self:
        return ExPostResource.ex_post_resource_results.remove(self, ex_post_resource_result)

    def clear_ex_post_resource_results(self) -> Self:
        return ExPostResource.ex_post_resource_results.clear(self)

    def num_ex_post_resource_result(self) -> int:
        return ExPostResource.ex_post_resource_results.count(self)
