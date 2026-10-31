"""CIM class LossClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing_results import (
        LossClearingResults,
    )


class LossClearing(MarketFactors):
    """RT only and is published on 5 minute intervals for the previous RT time interval
    results."""

    __slots__ = ("_loss_clearing_results",)

    loss_clearing_results: Many[LossClearingResults] = Many(
        EndMeta(
            name="loss_clearing_results",
            cim_role="LossClearingResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing_results:LossClearingResults",
            many=True,
            lower=0,
            upper=None,
            inverse="loss_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LossClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{A675112F-3536-4224-8DAA-0DEDEE9C8055}",
        ends=(loss_clearing_results.meta,),
    )

    def __init__(
        self,
        *,
        loss_clearing_results: Iterable[LossClearingResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if loss_clearing_results is not None:
            LossClearing.loss_clearing_results.extend(self, loss_clearing_results)

    def add_loss_clearing_result(self, loss_clearing_result: LossClearingResults) -> Self:
        return LossClearing.loss_clearing_results.add(self, loss_clearing_result)

    def remove_loss_clearing_result(self, loss_clearing_result: LossClearingResults) -> Self:
        return LossClearing.loss_clearing_results.remove(self, loss_clearing_result)

    def clear_loss_clearing_results(self) -> Self:
        return LossClearing.loss_clearing_results.clear(self)

    def num_loss_clearing_result(self) -> int:
        return LossClearing.loss_clearing_results.count(self)
