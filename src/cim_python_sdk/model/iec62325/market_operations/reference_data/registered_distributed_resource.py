"""CIM class RegisteredDistributedResource (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_rating import (
        ResourcePerformanceRating,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.response_method import (
        ResponseMethod,
    )


class RegisteredDistributedResource(RegisteredResource):
    """A registered resource that represents a distributed energy resource, such as a
    micro-generator, fuel cell, photo-voltaic energy source, etc."""

    __slots__ = ("_resource_performance_ratings", "_response_methods", "distributed_resource_type")

    distributed_resource_type: str | None

    resource_performance_ratings: Many[ResourcePerformanceRating] = Many(
        EndMeta(
            name="resource_performance_ratings",
            cim_role="ResourcePerformanceRatings",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_rating:ResourcePerformanceRating",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    response_methods: Many[ResponseMethod] = Many(
        EndMeta(
            name="response_methods",
            cim_role="ResponseMethods",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.response_method:ResponseMethod",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegisteredDistributedResource",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{797D2ABC-99D4-4f9a-92A7-E3816F614B08}",
        attributes=(
            AttrMeta(
                "distributed_resource_type", "distributedResourceType", "str", 0, 1, "primitive"
            ),
        ),
        ends=(
            resource_performance_ratings.meta,
            response_methods.meta,
        ),
    )

    def __init__(
        self,
        *,
        distributed_resource_type: str | None = None,
        resource_performance_ratings: Iterable[ResourcePerformanceRating] | None = None,
        response_methods: Iterable[ResponseMethod] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.distributed_resource_type = distributed_resource_type
        if resource_performance_ratings is not None:
            RegisteredDistributedResource.resource_performance_ratings.extend(
                self, resource_performance_ratings
            )
        if response_methods is not None:
            RegisteredDistributedResource.response_methods.extend(self, response_methods)

    def add_resource_performance_rating(
        self, resource_performance_rating: ResourcePerformanceRating
    ) -> Self:
        return RegisteredDistributedResource.resource_performance_ratings.add(
            self, resource_performance_rating
        )

    def remove_resource_performance_rating(
        self, resource_performance_rating: ResourcePerformanceRating
    ) -> Self:
        return RegisteredDistributedResource.resource_performance_ratings.remove(
            self, resource_performance_rating
        )

    def clear_resource_performance_ratings(self) -> Self:
        return RegisteredDistributedResource.resource_performance_ratings.clear(self)

    def num_resource_performance_rating(self) -> int:
        return RegisteredDistributedResource.resource_performance_ratings.count(self)

    def get_resource_performance_rating_by_mrid(
        self, mrid: str
    ) -> ResourcePerformanceRating | None:
        return RegisteredDistributedResource.resource_performance_ratings.get_by_mrid(self, mrid)

    def add_response_method(self, response_method: ResponseMethod) -> Self:
        return RegisteredDistributedResource.response_methods.add(self, response_method)

    def remove_response_method(self, response_method: ResponseMethod) -> Self:
        return RegisteredDistributedResource.response_methods.remove(self, response_method)

    def clear_response_methods(self) -> Self:
        return RegisteredDistributedResource.response_methods.clear(self)

    def num_response_method(self) -> int:
        return RegisteredDistributedResource.response_methods.count(self)

    def get_response_method_by_mrid(self, mrid: str) -> ResponseMethod | None:
        return RegisteredDistributedResource.response_methods.get_by_mrid(self, mrid)
