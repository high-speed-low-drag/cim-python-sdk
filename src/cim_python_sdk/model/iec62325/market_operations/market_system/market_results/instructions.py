"""CIM class Instructions (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing import (
        InstructionClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.automatic_disp_inst_type_commitment import (
        AutomaticDispInstTypeCommitment,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqs_instruction_source import (
        MQSInstructionSource,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
        AggregateNode,
    )


class Instructions(CimObject):
    """Provides the necessary information (on a resource basis) to capture the Startup/Shutdown
    instruction results. This information is relevant to the DA Market (RUC only) as well as
    the RT Market (HASP, Pre-dispatch, and Interval)."""

    __slots__ = (
        "_aggregate_node",
        "_instruction_clearing",
        "_registered_resource",
        "binding_dod",
        "binding_dot",
        "binding_instruction",
        "instruction_cost",
        "instruction_source",
        "instruction_start_time",
        "instruction_type",
        "manually_blocked",
        "min_status_change_time",
        "update_time_stamp",
        "update_type",
        "update_user",
    )

    binding_dod: float | None
    binding_dot: float | None
    binding_instruction: YesNo | None
    instruction_cost: float | None
    instruction_source: MQSInstructionSource | None
    instruction_start_time: _dt.datetime | None
    instruction_type: AutomaticDispInstTypeCommitment | None
    manually_blocked: YesNo | None
    min_status_change_time: int | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None
    update_user: str | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="instructions",
            aggregation="none",
        )
    )
    aggregate_node: One[AggregateNode] = One(
        EndMeta(
            name="aggregate_node",
            cim_role="AggregateNode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node:AggregateNode",
            many=False,
            lower=0,
            upper=1,
            inverse="instruction",
            aggregation="none",
        )
    )
    instruction_clearing: Many[InstructionClearing] = Many(
        EndMeta(
            name="instruction_clearing",
            cim_role="InstructionClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing:InstructionClearing",
            many=True,
            lower=1,
            upper=None,
            inverse="instructions",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Instructions",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{78311B60-9E5A-4ea1-8ED7-B9A5A192FBCD}",
        attributes=(
            AttrMeta("binding_dod", "bindingDOD", "float", 0, 1, "primitive"),
            AttrMeta("binding_dot", "bindingDOT", "float", 0, 1, "primitive"),
            AttrMeta("binding_instruction", "bindingInstruction", "YesNo", 0, 1, "enumeration"),
            AttrMeta("instruction_cost", "instructionCost", "float", 0, 1, "primitive"),
            AttrMeta(
                "instruction_source",
                "instructionSource",
                "MQSInstructionSource",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "instruction_start_time", "instructionStartTime", "datetime", 0, 1, "primitive"
            ),
            AttrMeta(
                "instruction_type",
                "instructionType",
                "AutomaticDispInstTypeCommitment",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("manually_blocked", "manuallyBlocked", "YesNo", 0, 1, "enumeration"),
            AttrMeta("min_status_change_time", "minStatusChangeTime", "int", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
        ),
        ends=(
            registered_resource.meta,
            aggregate_node.meta,
            instruction_clearing.meta,
        ),
    )

    def __init__(
        self,
        *,
        binding_dod: float | None = None,
        binding_dot: float | None = None,
        binding_instruction: YesNo | None = None,
        instruction_cost: float | None = None,
        instruction_source: MQSInstructionSource | None = None,
        instruction_start_time: _dt.datetime | None = None,
        instruction_type: AutomaticDispInstTypeCommitment | None = None,
        manually_blocked: YesNo | None = None,
        min_status_change_time: int | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        update_user: str | None = None,
        registered_resource: RegisteredResource | None = None,
        aggregate_node: AggregateNode | None = None,
        instruction_clearing: Iterable[InstructionClearing] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.binding_dod = binding_dod
        self.binding_dot = binding_dot
        self.binding_instruction = binding_instruction
        self.instruction_cost = instruction_cost
        self.instruction_source = instruction_source
        self.instruction_start_time = instruction_start_time
        self.instruction_type = instruction_type
        self.manually_blocked = manually_blocked
        self.min_status_change_time = min_status_change_time
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        self.update_user = update_user
        if registered_resource is not None:
            self.registered_resource = registered_resource
        if aggregate_node is not None:
            self.aggregate_node = aggregate_node
        if instruction_clearing is not None:
            Instructions.instruction_clearing.extend(self, instruction_clearing)

    def add_instruction_clearing(self, instruction_clearing: InstructionClearing) -> Self:
        return Instructions.instruction_clearing.add(self, instruction_clearing)

    def remove_instruction_clearing(self, instruction_clearing: InstructionClearing) -> Self:
        return Instructions.instruction_clearing.remove(self, instruction_clearing)

    def clear_instruction_clearing(self) -> Self:
        return Instructions.instruction_clearing.clear(self)

    def num_instruction_clearing(self) -> int:
        return Instructions.instruction_clearing.count(self)

    def get_instruction_clearing_by_mrid(self, mrid: str) -> InstructionClearing | None:
        return Instructions.instruction_clearing.get_by_mrid(self, mrid)
