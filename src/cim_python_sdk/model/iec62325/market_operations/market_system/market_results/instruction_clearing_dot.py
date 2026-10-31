"""CIM class InstructionClearingDOT (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.distributed_resource_actual_event import (
        DistributedResourceActualEvent,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.dot_instruction import (
        DotInstruction,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.automatic_dispatch_mode import (
        AutomaticDispatchMode,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class InstructionClearingDOT(MarketFactors):
    """Model of market clearing, related to Dispatch Operating Target (model of anticipatory
    dispatch). Identifies interval."""

    __slots__ = (
        "_demand_response_actual_event",
        "_dot_instruction",
        "contingency_active",
        "dispatch_mode",
    )

    contingency_active: YesNo | None
    dispatch_mode: AutomaticDispatchMode | None

    demand_response_actual_event: One[DistributedResourceActualEvent] = One(
        EndMeta(
            name="demand_response_actual_event",
            cim_role="DemandResponseActualEvent",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.distributed_resource_actual_event:DistributedResourceActualEvent",
            many=False,
            lower=0,
            upper=1,
            inverse="instruction_clearing_dot",
            aggregation="none",
        )
    )
    dot_instruction: Many[DotInstruction] = Many(
        EndMeta(
            name="dot_instruction",
            cim_role="DotInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.dot_instruction:DotInstruction",
            many=True,
            lower=1,
            upper=None,
            inverse="instruction_clearing_dot",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InstructionClearingDOT",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{6C295531-7D62-45ee-AB5F-46533D1F413B}",
        attributes=(
            AttrMeta("contingency_active", "contingencyActive", "YesNo", 0, 1, "enumeration"),
            AttrMeta("dispatch_mode", "dispatchMode", "AutomaticDispatchMode", 0, 1, "enumeration"),
        ),
        ends=(
            demand_response_actual_event.meta,
            dot_instruction.meta,
        ),
    )

    def __init__(
        self,
        *,
        contingency_active: YesNo | None = None,
        dispatch_mode: AutomaticDispatchMode | None = None,
        demand_response_actual_event: DistributedResourceActualEvent | None = None,
        dot_instruction: Iterable[DotInstruction] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.contingency_active = contingency_active
        self.dispatch_mode = dispatch_mode
        if demand_response_actual_event is not None:
            self.demand_response_actual_event = demand_response_actual_event
        if dot_instruction is not None:
            InstructionClearingDOT.dot_instruction.extend(self, dot_instruction)

    def add_dot_instruction(self, dot_instruction: DotInstruction) -> Self:
        return InstructionClearingDOT.dot_instruction.add(self, dot_instruction)

    def remove_dot_instruction(self, dot_instruction: DotInstruction) -> Self:
        return InstructionClearingDOT.dot_instruction.remove(self, dot_instruction)

    def clear_dot_instruction(self) -> Self:
        return InstructionClearingDOT.dot_instruction.clear(self)

    def num_dot_instruction(self) -> int:
        return InstructionClearingDOT.dot_instruction.count(self)
