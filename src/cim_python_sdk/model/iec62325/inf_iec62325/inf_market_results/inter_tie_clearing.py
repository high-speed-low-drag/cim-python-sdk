"""CIM class InterTieClearing (TC57CIM/IEC62325/InfIEC62325/InfMarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_market_results.inter_tie_results import (
        InterTieResults,
    )


class InterTieClearing(MarketFactors):
    """Model of market clearing related to results at the inter-ties. Identifies interval"""

    __slots__ = ("_inter_tie_results",)

    inter_tie_results: Many[InterTieResults] = Many(
        EndMeta(
            name="inter_tie_results",
            cim_role="InterTieResults",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_market_results.inter_tie_results:InterTieResults",
            many=True,
            lower=0,
            upper=None,
            inverse="inter_tie_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InterTieClearing",
        package="TC57CIM/IEC62325/InfIEC62325/InfMarketResults",
        guid="{E25E8CDB-A8BF-4552-B0F3-0D52DBBB017A}",
        ends=(inter_tie_results.meta,),
    )

    def __init__(
        self,
        *,
        inter_tie_results: Iterable[InterTieResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if inter_tie_results is not None:
            InterTieClearing.inter_tie_results.extend(self, inter_tie_results)

    def add_inter_tie_result(self, inter_tie_result: InterTieResults) -> Self:
        return InterTieClearing.inter_tie_results.add(self, inter_tie_result)

    def remove_inter_tie_result(self, inter_tie_result: InterTieResults) -> Self:
        return InterTieClearing.inter_tie_results.remove(self, inter_tie_result)

    def clear_inter_tie_results(self) -> Self:
        return InterTieClearing.inter_tie_results.clear(self)

    def num_inter_tie_result(self) -> int:
        return InterTieClearing.inter_tie_results.count(self)
