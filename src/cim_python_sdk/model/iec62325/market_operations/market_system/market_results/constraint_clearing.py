"""CIM class ConstraintClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.constraint_results import (
        ConstraintResults,
    )


class ConstraintClearing(MarketFactors):
    """Groups all items associated with Binding Constraints and Constraint Violations per
    interval and market."""

    __slots__ = ("_constraint_results",)

    constraint_results: Many[ConstraintResults] = Many(
        EndMeta(
            name="constraint_results",
            cim_role="ConstraintResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.constraint_results:ConstraintResults",
            many=True,
            lower=0,
            upper=None,
            inverse="constraint_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConstraintClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{BE695822-33D6-4b39-A212-B6C5B4EF7459}",
        ends=(constraint_results.meta,),
    )

    def __init__(
        self,
        *,
        constraint_results: Iterable[ConstraintResults] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if constraint_results is not None:
            ConstraintClearing.constraint_results.extend(self, constraint_results)

    def add_constraint_result(self, constraint_result: ConstraintResults) -> Self:
        return ConstraintClearing.constraint_results.add(self, constraint_result)

    def remove_constraint_result(self, constraint_result: ConstraintResults) -> Self:
        return ConstraintClearing.constraint_results.remove(self, constraint_result)

    def clear_constraint_results(self) -> Self:
        return ConstraintClearing.constraint_results.clear(self)

    def num_constraint_result(self) -> int:
        return ConstraintClearing.constraint_results.count(self)

    def get_constraint_result_by_mrid(self, mrid: str) -> ConstraintResults | None:
        return ConstraintClearing.constraint_results.get_by_mrid(self, mrid)
