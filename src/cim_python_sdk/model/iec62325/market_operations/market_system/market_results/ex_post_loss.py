"""CIM class ExPostLoss (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_loss_results import (
        ExPostLossResults,
    )


class ExPostLoss(MarketFactors):
    """Model of ex-post calcultion of MW losses."""

    __slots__ = ("_ex_post_loss_results",)

    ex_post_loss_results: Many[ExPostLossResults] = Many(
        EndMeta(
            name="ex_post_loss_results",
            cim_role="ExPostLossResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_loss_results:ExPostLossResults",
            many=True,
            lower=0,
            upper=None,
            inverse="ex_post_loss",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExPostLoss",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{DD74E80C-6CA3-40a5-A955-6DF08D937754}",
        ends=(ex_post_loss_results.meta,),
    )

    def __init__(
        self,
        *,
        ex_post_loss_results: Iterable[ExPostLossResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ex_post_loss_results is not None:
            ExPostLoss.ex_post_loss_results.extend(self, ex_post_loss_results)

    def add_ex_post_loss_result(self, ex_post_loss_result: ExPostLossResults) -> Self:
        return ExPostLoss.ex_post_loss_results.add(self, ex_post_loss_result)

    def remove_ex_post_loss_result(self, ex_post_loss_result: ExPostLossResults) -> Self:
        return ExPostLoss.ex_post_loss_results.remove(self, ex_post_loss_result)

    def clear_ex_post_loss_results(self) -> Self:
        return ExPostLoss.ex_post_loss_results.clear(self)

    def num_ex_post_loss_result(self) -> int:
        return ExPostLoss.ex_post_loss_results.count(self)
