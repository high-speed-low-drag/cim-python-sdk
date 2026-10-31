"""CIM class DistributedResourceActualEvent (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_actual_event import (
    MarketActualEvent,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing import (
        InstructionClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing_dot import (
        InstructionClearingDOT,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_evaluation import (
        ResourcePerformanceEvaluation,
    )


class DistributedResourceActualEvent(MarketActualEvent):
    """A demand response event is created when there is a need to call upon resources to
    respond to demand adjustment requests. These events are created by ISO/RTO system
    operations and managed by a demand response management system (DRMS). These events may
    or may not be coordinated with the Market Events and a defined Energy Market. The event
    will call for the deployment of a number of registered resources, or for deployment of
    resources within a zone (an organizational area within the power system that contains a
    number of resources)."""

    __slots__ = (
        "_instruction_clearing",
        "_instruction_clearing_dot",
        "_resource_performance_evaluations",
        "total_power_adjustment",
    )

    total_power_adjustment: float | None  # ActivePower

    instruction_clearing_dot: Many[InstructionClearingDOT] = Many(
        EndMeta(
            name="instruction_clearing_dot",
            cim_role="InstructionClearingDOT",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing_dot:InstructionClearingDOT",
            many=True,
            lower=0,
            upper=None,
            inverse="demand_response_actual_event",
            aggregation="none",
        )
    )
    resource_performance_evaluations: Many[ResourcePerformanceEvaluation] = Many(
        EndMeta(
            name="resource_performance_evaluations",
            cim_role="ResourcePerformanceEvaluations",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_performance_evaluation:ResourcePerformanceEvaluation",
            many=True,
            lower=0,
            upper=None,
            inverse="demand_response_actual_event",
            aggregation="none",
        )
    )
    instruction_clearing: Many[InstructionClearing] = Many(
        EndMeta(
            name="instruction_clearing",
            cim_role="InstructionClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing:InstructionClearing",
            many=True,
            lower=0,
            upper=None,
            inverse="actual_demand_response_event",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DistributedResourceActualEvent",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{846E5539-74A2-4faa-BCD9-B72523D08DFD}",
        attributes=(
            AttrMeta(
                "total_power_adjustment", "totalPowerAdjustment", "ActivePower", 0, 1, "cimdatatype"
            ),
        ),
        ends=(
            instruction_clearing_dot.meta,
            resource_performance_evaluations.meta,
            instruction_clearing.meta,
        ),
    )

    def __init__(
        self,
        *,
        total_power_adjustment: float | None = None,
        instruction_clearing_dot: Iterable[InstructionClearingDOT] | None = None,
        resource_performance_evaluations: Iterable[ResourcePerformanceEvaluation] | None = None,
        instruction_clearing: Iterable[InstructionClearing] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.total_power_adjustment = total_power_adjustment
        if instruction_clearing_dot is not None:
            DistributedResourceActualEvent.instruction_clearing_dot.extend(
                self, instruction_clearing_dot
            )
        if resource_performance_evaluations is not None:
            DistributedResourceActualEvent.resource_performance_evaluations.extend(
                self, resource_performance_evaluations
            )
        if instruction_clearing is not None:
            DistributedResourceActualEvent.instruction_clearing.extend(self, instruction_clearing)

    def add_instruction_clearing_dot(
        self, instruction_clearing_dot: InstructionClearingDOT
    ) -> Self:
        return DistributedResourceActualEvent.instruction_clearing_dot.add(
            self, instruction_clearing_dot
        )

    def remove_instruction_clearing_dot(
        self, instruction_clearing_dot: InstructionClearingDOT
    ) -> Self:
        return DistributedResourceActualEvent.instruction_clearing_dot.remove(
            self, instruction_clearing_dot
        )

    def clear_instruction_clearing_dot(self) -> Self:
        return DistributedResourceActualEvent.instruction_clearing_dot.clear(self)

    def num_instruction_clearing_dot(self) -> int:
        return DistributedResourceActualEvent.instruction_clearing_dot.count(self)

    def get_instruction_clearing_dot_by_mrid(self, mrid: str) -> InstructionClearingDOT | None:
        return DistributedResourceActualEvent.instruction_clearing_dot.get_by_mrid(self, mrid)

    def add_resource_performance_evaluation(
        self, resource_performance_evaluation: ResourcePerformanceEvaluation
    ) -> Self:
        return DistributedResourceActualEvent.resource_performance_evaluations.add(
            self, resource_performance_evaluation
        )

    def remove_resource_performance_evaluation(
        self, resource_performance_evaluation: ResourcePerformanceEvaluation
    ) -> Self:
        return DistributedResourceActualEvent.resource_performance_evaluations.remove(
            self, resource_performance_evaluation
        )

    def clear_resource_performance_evaluations(self) -> Self:
        return DistributedResourceActualEvent.resource_performance_evaluations.clear(self)

    def num_resource_performance_evaluation(self) -> int:
        return DistributedResourceActualEvent.resource_performance_evaluations.count(self)

    def get_resource_performance_evaluation_by_mrid(
        self, mrid: str
    ) -> ResourcePerformanceEvaluation | None:
        return DistributedResourceActualEvent.resource_performance_evaluations.get_by_mrid(
            self, mrid
        )

    def add_instruction_clearing(self, instruction_clearing: InstructionClearing) -> Self:
        return DistributedResourceActualEvent.instruction_clearing.add(self, instruction_clearing)

    def remove_instruction_clearing(self, instruction_clearing: InstructionClearing) -> Self:
        return DistributedResourceActualEvent.instruction_clearing.remove(
            self, instruction_clearing
        )

    def clear_instruction_clearing(self) -> Self:
        return DistributedResourceActualEvent.instruction_clearing.clear(self)

    def num_instruction_clearing(self) -> int:
        return DistributedResourceActualEvent.instruction_clearing.count(self)

    def get_instruction_clearing_by_mrid(self, mrid: str) -> InstructionClearing | None:
        return DistributedResourceActualEvent.instruction_clearing.get_by_mrid(self, mrid)
