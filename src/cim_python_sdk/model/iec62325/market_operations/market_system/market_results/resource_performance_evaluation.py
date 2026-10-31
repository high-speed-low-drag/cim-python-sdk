"""CIM class ResourcePerformanceEvaluation (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.distributed_resource_actual_event import (
        DistributedResourceActualEvent,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_global_factor import (
        ResourcePerformanceGlobalFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_time_series_factor import (
        ResourcePerformanceTimeSeriesFactor,
    )


class ResourcePerformanceEvaluation(IdentifiedObject):
    """Represents an the performance evaluation of a resource deployment. Every resource
    deployment may have many performance evaluations, using different evaluation metrics or
    algorithms, or produced by different evaluation authorities."""

    __slots__ = (
        "_demand_response_actual_event",
        "_resorce_performance_global_factor",
        "_resource_performance_time_series_factors",
        "effective_end_time",
        "effective_start_time",
        "evaluation_description",
        "evaluation_value",
    )

    effective_end_time: _dt.datetime | None
    effective_start_time: _dt.datetime | None
    evaluation_description: str | None
    evaluation_value: str | None

    demand_response_actual_event: One[DistributedResourceActualEvent] = One(
        EndMeta(
            name="demand_response_actual_event",
            cim_role="DemandResponseActualEvent",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.distributed_resource_actual_event:DistributedResourceActualEvent",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_performance_evaluations",
            aggregation="none",
        )
    )
    resource_performance_time_series_factors: Many[ResourcePerformanceTimeSeriesFactor] = Many(
        EndMeta(
            name="resource_performance_time_series_factors",
            cim_role="ResourcePerformanceTimeSeriesFactors",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_time_series_factor:ResourcePerformanceTimeSeriesFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_performance_evaluation",
            aggregation="none",
        )
    )
    resorce_performance_global_factor: Many[ResourcePerformanceGlobalFactor] = Many(
        EndMeta(
            name="resorce_performance_global_factor",
            cim_role="ResorcePerformanceGlobalFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_global_factor:ResourcePerformanceGlobalFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_performance_evaluation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourcePerformanceEvaluation",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{96F08A4F-48D6-4060-A348-291FA2C39A9D}",
        attributes=(
            AttrMeta("effective_end_time", "effectiveEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("effective_start_time", "effectiveStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("evaluation_description", "evaluationDescription", "str", 0, 1, "primitive"),
            AttrMeta("evaluation_value", "evaluationValue", "str", 0, 1, "primitive"),
        ),
        ends=(
            demand_response_actual_event.meta,
            resource_performance_time_series_factors.meta,
            resorce_performance_global_factor.meta,
        ),
    )

    def __init__(
        self,
        *,
        effective_end_time: _dt.datetime | None = None,
        effective_start_time: _dt.datetime | None = None,
        evaluation_description: str | None = None,
        evaluation_value: str | None = None,
        demand_response_actual_event: DistributedResourceActualEvent | None = None,
        resource_performance_time_series_factors: Iterable[ResourcePerformanceTimeSeriesFactor]
        | None = None,
        resorce_performance_global_factor: Iterable[ResourcePerformanceGlobalFactor] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.evaluation_description = evaluation_description
        self.evaluation_value = evaluation_value
        if demand_response_actual_event is not None:
            self.demand_response_actual_event = demand_response_actual_event
        if resource_performance_time_series_factors is not None:
            ResourcePerformanceEvaluation.resource_performance_time_series_factors.extend(
                self, resource_performance_time_series_factors
            )
        if resorce_performance_global_factor is not None:
            ResourcePerformanceEvaluation.resorce_performance_global_factor.extend(
                self, resorce_performance_global_factor
            )

    def add_resource_performance_time_series_factor(
        self, resource_performance_time_series_factor: ResourcePerformanceTimeSeriesFactor
    ) -> Self:
        return ResourcePerformanceEvaluation.resource_performance_time_series_factors.add(
            self, resource_performance_time_series_factor
        )

    def remove_resource_performance_time_series_factor(
        self, resource_performance_time_series_factor: ResourcePerformanceTimeSeriesFactor
    ) -> Self:
        return ResourcePerformanceEvaluation.resource_performance_time_series_factors.remove(
            self, resource_performance_time_series_factor
        )

    def clear_resource_performance_time_series_factors(self) -> Self:
        return ResourcePerformanceEvaluation.resource_performance_time_series_factors.clear(self)

    def num_resource_performance_time_series_factor(self) -> int:
        return ResourcePerformanceEvaluation.resource_performance_time_series_factors.count(self)

    def get_resource_performance_time_series_factor_by_mrid(
        self, mrid: str
    ) -> ResourcePerformanceTimeSeriesFactor | None:
        return ResourcePerformanceEvaluation.resource_performance_time_series_factors.get_by_mrid(
            self, mrid
        )

    def add_resorce_performance_global_factor(
        self, resorce_performance_global_factor: ResourcePerformanceGlobalFactor
    ) -> Self:
        return ResourcePerformanceEvaluation.resorce_performance_global_factor.add(
            self, resorce_performance_global_factor
        )

    def remove_resorce_performance_global_factor(
        self, resorce_performance_global_factor: ResourcePerformanceGlobalFactor
    ) -> Self:
        return ResourcePerformanceEvaluation.resorce_performance_global_factor.remove(
            self, resorce_performance_global_factor
        )

    def clear_resorce_performance_global_factor(self) -> Self:
        return ResourcePerformanceEvaluation.resorce_performance_global_factor.clear(self)

    def num_resorce_performance_global_factor(self) -> int:
        return ResourcePerformanceEvaluation.resorce_performance_global_factor.count(self)

    def get_resorce_performance_global_factor_by_mrid(
        self, mrid: str
    ) -> ResourcePerformanceGlobalFactor | None:
        return ResourcePerformanceEvaluation.resorce_performance_global_factor.get_by_mrid(
            self, mrid
        )
