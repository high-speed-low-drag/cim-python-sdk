"""CIM class SelfScheduleBreakdown (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_instruction import (
        ResourceAwardInstruction,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.self_schedule_breakdown_type import (
        SelfScheduleBreakdownType,
    )


class SelfScheduleBreakdown(CimObject):
    """Model of Self Schedules Results. Includes self schedule MW,and type of self schedule for
    each self schedule type included in total self schedule MW value found in
    ResourceAwardInstruction."""

    __slots__ = ("_resource_award_instruction", "self_sched_mw", "self_sched_type")

    self_sched_mw: float | None
    self_sched_type: SelfScheduleBreakdownType | None

    resource_award_instruction: One[ResourceAwardInstruction] = One(
        EndMeta(
            name="resource_award_instruction",
            cim_role="ResourceAwardInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_instruction:ResourceAwardInstruction",
            many=False,
            lower=1,
            upper=1,
            inverse="self_schedule_breakdown",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SelfScheduleBreakdown",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{9134E482-78E1-4d37-9F1D-545330C38BDB}",
        attributes=(
            AttrMeta("self_sched_mw", "selfSchedMW", "float", 0, 1, "primitive"),
            AttrMeta(
                "self_sched_type", "selfSchedType", "SelfScheduleBreakdownType", 0, 1, "enumeration"
            ),
        ),
        ends=(resource_award_instruction.meta,),
    )

    def __init__(
        self,
        *,
        self_sched_mw: float | None = None,
        self_sched_type: SelfScheduleBreakdownType | None = None,
        resource_award_instruction: ResourceAwardInstruction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.self_sched_mw = self_sched_mw
        self.self_sched_type = self_sched_type
        if resource_award_instruction is not None:
            self.resource_award_instruction = resource_award_instruction
