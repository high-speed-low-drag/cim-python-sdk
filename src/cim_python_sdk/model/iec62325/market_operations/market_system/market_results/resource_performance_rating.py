"""CIM class ResourcePerformanceRating (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_distributed_resource import (
        RegisteredDistributedResource,
    )


class ResourcePerformanceRating(IdentifiedObject):
    """Rating of a resource for its demand response performance. e.g. given a set on monthly
    resource demand response performance evaluations, the resource may be rated with
    excellent, average, or poor performance for the sample set."""

    __slots__ = (
        "_registered_resource",
        "effective_end_time",
        "effective_start_time",
        "rating_description",
        "rating_type",
        "rating_value",
    )

    effective_end_time: _dt.datetime | None
    effective_start_time: _dt.datetime | None
    rating_description: str | None
    rating_type: str | None
    rating_value: str | None

    registered_resource: One[RegisteredDistributedResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_distributed_resource:RegisteredDistributedResource",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_performance_ratings",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourcePerformanceRating",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{A0F02391-DA9F-41dd-8539-9D4A34696690}",
        attributes=(
            AttrMeta("effective_end_time", "effectiveEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("effective_start_time", "effectiveStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("rating_description", "ratingDescription", "str", 0, 1, "primitive"),
            AttrMeta("rating_type", "ratingType", "str", 1, 1, "primitive"),
            AttrMeta("rating_value", "ratingValue", "str", 0, 1, "primitive"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        effective_end_time: _dt.datetime | None = None,
        effective_start_time: _dt.datetime | None = None,
        rating_description: str | None = None,
        rating_type: str | None = None,
        rating_value: str | None = None,
        registered_resource: RegisteredDistributedResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.rating_description = rating_description
        self.rating_type = rating_type
        self.rating_value = rating_value
        if registered_resource is not None:
            self.registered_resource = registered_resource
