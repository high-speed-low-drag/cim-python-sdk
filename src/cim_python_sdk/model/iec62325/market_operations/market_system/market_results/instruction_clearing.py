"""CIM class InstructionClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.distributed_resource_actual_event import (
        DistributedResourceActualEvent,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instructions import (
        Instructions,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_deployment_status import (
        ResourceDeploymentStatus,
    )


class InstructionClearing(MarketFactors):
    """Model of market clearing, relating to commitment instructions. Identifies interval."""

    __slots__ = ("_actual_demand_response_event", "_instructions", "_resource_deployment_status")

    resource_deployment_status: Many[ResourceDeploymentStatus] = Many(
        EndMeta(
            name="resource_deployment_status",
            cim_role="ResourceDeploymentStatus",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_deployment_status:ResourceDeploymentStatus",
            many=True,
            lower=0,
            upper=None,
            inverse="instruction_clearing",
            aggregation="none",
        )
    )
    actual_demand_response_event: One[DistributedResourceActualEvent] = One(
        EndMeta(
            name="actual_demand_response_event",
            cim_role="ActualDemandResponseEvent",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.distributed_resource_actual_event:DistributedResourceActualEvent",
            many=False,
            lower=0,
            upper=1,
            inverse="instruction_clearing",
            aggregation="none",
        )
    )
    instructions: Many[Instructions] = Many(
        EndMeta(
            name="instructions",
            cim_role="Instructions",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instructions:Instructions",
            many=True,
            lower=1,
            upper=None,
            inverse="instruction_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InstructionClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{EC8FBDD8-880A-49cb-9E58-39774488E1B5}",
        ends=(
            resource_deployment_status.meta,
            actual_demand_response_event.meta,
            instructions.meta,
        ),
    )

    def __init__(
        self,
        *,
        resource_deployment_status: Iterable[ResourceDeploymentStatus] | None = None,
        actual_demand_response_event: DistributedResourceActualEvent | None = None,
        instructions: Iterable[Instructions] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if resource_deployment_status is not None:
            InstructionClearing.resource_deployment_status.extend(self, resource_deployment_status)
        if actual_demand_response_event is not None:
            self.actual_demand_response_event = actual_demand_response_event
        if instructions is not None:
            InstructionClearing.instructions.extend(self, instructions)

    def add_resource_deployment_status(
        self, resource_deployment_status: ResourceDeploymentStatus
    ) -> Self:
        return InstructionClearing.resource_deployment_status.add(self, resource_deployment_status)

    def remove_resource_deployment_status(
        self, resource_deployment_status: ResourceDeploymentStatus
    ) -> Self:
        return InstructionClearing.resource_deployment_status.remove(
            self, resource_deployment_status
        )

    def clear_resource_deployment_status(self) -> Self:
        return InstructionClearing.resource_deployment_status.clear(self)

    def num_resource_deployment_status(self) -> int:
        return InstructionClearing.resource_deployment_status.count(self)

    def add_instruction(self, instruction: Instructions) -> Self:
        return InstructionClearing.instructions.add(self, instruction)

    def remove_instruction(self, instruction: Instructions) -> Self:
        return InstructionClearing.instructions.remove(self, instruction)

    def clear_instructions(self) -> Self:
        return InstructionClearing.instructions.clear(self)

    def num_instruction(self) -> int:
        return InstructionClearing.instructions.count(self)
