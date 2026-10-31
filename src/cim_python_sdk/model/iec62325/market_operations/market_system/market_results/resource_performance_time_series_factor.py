"""CIM class ResourcePerformanceTimeSeriesFactor (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_evaluation import (
        ResourcePerformanceEvaluation,
    )


class ResourcePerformanceTimeSeriesFactor(RegularIntervalSchedule):
    """Represents the performance of a resource as time series data for a specified time
    period, time interval, and evaluation criteria."""

    __slots__ = (
        "_resource_performance_evaluation",
        "time_series_data_type",
        "time_series_description",
        "value1_description",
        "value2_description",
    )

    time_series_data_type: str | None
    time_series_description: str | None
    value1_description: str | None
    value2_description: str | None

    resource_performance_evaluation: One[ResourcePerformanceEvaluation] = One(
        EndMeta(
            name="resource_performance_evaluation",
            cim_role="ResourcePerformanceEvaluation",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_evaluation:ResourcePerformanceEvaluation",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_performance_time_series_factors",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourcePerformanceTimeSeriesFactor",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{BC04C5C3-2138-4b6f-B7B2-98C3905EB788}",
        attributes=(
            AttrMeta("time_series_data_type", "timeSeriesDataType", "str", 0, 1, "primitive"),
            AttrMeta("time_series_description", "timeSeriesDescription", "str", 0, 1, "primitive"),
            AttrMeta("value1_description", "value1Description", "str", 0, 1, "primitive"),
            AttrMeta("value2_description", "value2Description", "str", 0, 1, "primitive"),
        ),
        ends=(resource_performance_evaluation.meta,),
    )

    def __init__(
        self,
        *,
        time_series_data_type: str | None = None,
        time_series_description: str | None = None,
        value1_description: str | None = None,
        value2_description: str | None = None,
        resource_performance_evaluation: ResourcePerformanceEvaluation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time_series_data_type = time_series_data_type
        self.time_series_description = time_series_description
        self.value1_description = value1_description
        self.value2_description = value2_description
        if resource_performance_evaluation is not None:
            self.resource_performance_evaluation = resource_performance_evaluation
