"""CIM class ResourceVerifiableCosts (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_heat_rate_curve import (
        MktHeatRateCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.resource_operation_maintenance_cost import (
        ResourceOperationMaintenanceCost,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.resource_startup_cost import (
        ResourceStartupCost,
    )


class ResourceVerifiableCosts(CimObject):
    """This class is defined to describe the verifiable costs associated with a generation
    resource."""

    __slots__ = (
        "_mkt_heat_rate_curve",
        "_registered_resource",
        "_resource_operation_maintenance_cost",
        "_resource_startup_cost",
    )

    mkt_heat_rate_curve: One[MktHeatRateCurve] = One(
        EndMeta(
            name="mkt_heat_rate_curve",
            cim_role="MktHeatRateCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_heat_rate_curve:MktHeatRateCurve",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_verifiable_costs",
            aggregation="none",
        )
    )
    resource_startup_cost: Many[ResourceStartupCost] = Many(
        EndMeta(
            name="resource_startup_cost",
            cim_role="ResourceStartupCost",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.resource_startup_cost:ResourceStartupCost",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_verifiable_costs",
            aggregation="shared",
        )
    )
    resource_operation_maintenance_cost: One[ResourceOperationMaintenanceCost] = One(
        EndMeta(
            name="resource_operation_maintenance_cost",
            cim_role="ResourceOperationMaintenanceCost",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.resource_operation_maintenance_cost:ResourceOperationMaintenanceCost",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_verifiable_costs",
            aggregation="none",
        )
    )
    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_verifiable_costs",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceVerifiableCosts",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{9B7A2594-4808-491e-8A57-C917B16AE913}",
        ends=(
            mkt_heat_rate_curve.meta,
            resource_startup_cost.meta,
            resource_operation_maintenance_cost.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        mkt_heat_rate_curve: MktHeatRateCurve | None = None,
        resource_startup_cost: Iterable[ResourceStartupCost] | None = None,
        resource_operation_maintenance_cost: ResourceOperationMaintenanceCost | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if mkt_heat_rate_curve is not None:
            self.mkt_heat_rate_curve = mkt_heat_rate_curve
        if resource_startup_cost is not None:
            ResourceVerifiableCosts.resource_startup_cost.extend(self, resource_startup_cost)
        if resource_operation_maintenance_cost is not None:
            self.resource_operation_maintenance_cost = resource_operation_maintenance_cost
        if registered_resource is not None:
            self.registered_resource = registered_resource

    def add_resource_startup_cost(self, resource_startup_cost: ResourceStartupCost) -> Self:
        return ResourceVerifiableCosts.resource_startup_cost.add(self, resource_startup_cost)

    def remove_resource_startup_cost(self, resource_startup_cost: ResourceStartupCost) -> Self:
        return ResourceVerifiableCosts.resource_startup_cost.remove(self, resource_startup_cost)

    def clear_resource_startup_cost(self) -> Self:
        return ResourceVerifiableCosts.resource_startup_cost.clear(self)

    def num_resource_startup_cost(self) -> int:
        return ResourceVerifiableCosts.resource_startup_cost.count(self)
