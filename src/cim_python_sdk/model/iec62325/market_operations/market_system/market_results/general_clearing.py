"""CIM class GeneralClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.general_clearing_results import (
        GeneralClearingResults,
    )


class GeneralClearing(MarketFactors):
    """Model of clearing result of the market run at the market level. Identifies interval."""

    __slots__ = ("_general_clearing_results",)

    general_clearing_results: Many[GeneralClearingResults] = Many(
        EndMeta(
            name="general_clearing_results",
            cim_role="GeneralClearingResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.general_clearing_results:GeneralClearingResults",
            many=True,
            lower=0,
            upper=None,
            inverse="general_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GeneralClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{7A9E03C5-840B-40fa-9E7E-61FDC21CB655}",
        ends=(general_clearing_results.meta,),
    )

    def __init__(
        self,
        *,
        general_clearing_results: Iterable[GeneralClearingResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if general_clearing_results is not None:
            GeneralClearing.general_clearing_results.extend(self, general_clearing_results)

    def add_general_clearing_result(self, general_clearing_result: GeneralClearingResults) -> Self:
        return GeneralClearing.general_clearing_results.add(self, general_clearing_result)

    def remove_general_clearing_result(
        self, general_clearing_result: GeneralClearingResults
    ) -> Self:
        return GeneralClearing.general_clearing_results.remove(self, general_clearing_result)

    def clear_general_clearing_results(self) -> Self:
        return GeneralClearing.general_clearing_results.clear(self)

    def num_general_clearing_result(self) -> int:
        return GeneralClearing.general_clearing_results.count(self)
