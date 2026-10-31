"""CIM class ResourceClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_dispatch_results import (
        ResourceDispatchResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_load_following_inst import (
        ResourceLoadFollowingInst,
    )


class ResourceClearing(MarketFactors):
    """Model of market results, including cleaing result of resources. Associated with
    ResourceDispatchResults."""

    __slots__ = ("_resource_dispatch_results", "_resource_load_following_inst")

    resource_dispatch_results: Many[ResourceDispatchResults] = Many(
        EndMeta(
            name="resource_dispatch_results",
            cim_role="ResourceDispatchResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_dispatch_results:ResourceDispatchResults",
            many=True,
            lower=1,
            upper=None,
            inverse="resource_clearing",
            aggregation="none",
        )
    )
    resource_load_following_inst: Many[ResourceLoadFollowingInst] = Many(
        EndMeta(
            name="resource_load_following_inst",
            cim_role="ResourceLoadFollowingInst",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_load_following_inst:ResourceLoadFollowingInst",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{AE7158B0-FBBB-42d1-8B34-0B98A9E2F777}",
        ends=(
            resource_dispatch_results.meta,
            resource_load_following_inst.meta,
        ),
    )

    def __init__(
        self,
        *,
        resource_dispatch_results: Iterable[ResourceDispatchResults] | None = None,
        resource_load_following_inst: Iterable[ResourceLoadFollowingInst] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if resource_dispatch_results is not None:
            ResourceClearing.resource_dispatch_results.extend(self, resource_dispatch_results)
        if resource_load_following_inst is not None:
            ResourceClearing.resource_load_following_inst.extend(self, resource_load_following_inst)

    def add_resource_dispatch_result(
        self, resource_dispatch_result: ResourceDispatchResults
    ) -> Self:
        return ResourceClearing.resource_dispatch_results.add(self, resource_dispatch_result)

    def remove_resource_dispatch_result(
        self, resource_dispatch_result: ResourceDispatchResults
    ) -> Self:
        return ResourceClearing.resource_dispatch_results.remove(self, resource_dispatch_result)

    def clear_resource_dispatch_results(self) -> Self:
        return ResourceClearing.resource_dispatch_results.clear(self)

    def num_resource_dispatch_result(self) -> int:
        return ResourceClearing.resource_dispatch_results.count(self)

    def add_resource_load_following_inst(
        self, resource_load_following_inst: ResourceLoadFollowingInst
    ) -> Self:
        return ResourceClearing.resource_load_following_inst.add(self, resource_load_following_inst)

    def remove_resource_load_following_inst(
        self, resource_load_following_inst: ResourceLoadFollowingInst
    ) -> Self:
        return ResourceClearing.resource_load_following_inst.remove(
            self, resource_load_following_inst
        )

    def clear_resource_load_following_inst(self) -> Self:
        return ResourceClearing.resource_load_following_inst.clear(self)

    def num_resource_load_following_inst(self) -> int:
        return ResourceClearing.resource_load_following_inst.count(self)
