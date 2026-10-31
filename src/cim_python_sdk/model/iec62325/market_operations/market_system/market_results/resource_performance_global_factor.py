"""CIM class ResourcePerformanceGlobalFactor (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_evaluation import (
        ResourcePerformanceEvaluation,
    )


class ResourcePerformanceGlobalFactor(IdentifiedObject):
    """Global factors are property/value pairs that are used to adjust resource performance
    values. Example include scale factors (e.g. scale a baseline up or down), adders
    (positive or negative), etc."""

    __slots__ = ("_resource_performance_evaluation", "factor_description", "factor_value")

    factor_description: str | None
    factor_value: str | None

    resource_performance_evaluation: Many[ResourcePerformanceEvaluation] = Many(
        EndMeta(
            name="resource_performance_evaluation",
            cim_role="ResourcePerformanceEvaluation",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_evaluation:ResourcePerformanceEvaluation",
            many=True,
            lower=0,
            upper=None,
            inverse="resorce_performance_global_factor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourcePerformanceGlobalFactor",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{DCBD23CE-0574-4fa9-ABB2-7BA5C3E7BE63}",
        attributes=(
            AttrMeta("factor_description", "factorDescription", "str", 0, 1, "primitive"),
            AttrMeta("factor_value", "factorValue", "str", 0, 1, "primitive"),
        ),
        ends=(resource_performance_evaluation.meta,),
    )

    def __init__(
        self,
        *,
        factor_description: str | None = None,
        factor_value: str | None = None,
        resource_performance_evaluation: Iterable[ResourcePerformanceEvaluation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.factor_description = factor_description
        self.factor_value = factor_value
        if resource_performance_evaluation is not None:
            ResourcePerformanceGlobalFactor.resource_performance_evaluation.extend(
                self, resource_performance_evaluation
            )

    def add_resource_performance_evaluation(
        self, resource_performance_evaluation: ResourcePerformanceEvaluation
    ) -> Self:
        return ResourcePerformanceGlobalFactor.resource_performance_evaluation.add(
            self, resource_performance_evaluation
        )

    def remove_resource_performance_evaluation(
        self, resource_performance_evaluation: ResourcePerformanceEvaluation
    ) -> Self:
        return ResourcePerformanceGlobalFactor.resource_performance_evaluation.remove(
            self, resource_performance_evaluation
        )

    def clear_resource_performance_evaluation(self) -> Self:
        return ResourcePerformanceGlobalFactor.resource_performance_evaluation.clear(self)

    def num_resource_performance_evaluation(self) -> int:
        return ResourcePerformanceGlobalFactor.resource_performance_evaluation.count(self)

    def get_resource_performance_evaluation_by_mrid(
        self, mrid: str
    ) -> ResourcePerformanceEvaluation | None:
        return ResourcePerformanceGlobalFactor.resource_performance_evaluation.get_by_mrid(
            self, mrid
        )
