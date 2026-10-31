"""CIM class ResourceAwardClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_instruction import (
        ResourceAwardInstruction,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ruc_award_instruction import (
        RUCAwardInstruction,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.automatic_dispatch_mode import (
        AutomaticDispatchMode,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class ResourceAwardClearing(MarketFactors):
    """Models details of bid and offer market clearing. Class indicates whether a contingency
    is active and whether the automatic dispatching system is active for this interval of
    the market solution."""

    __slots__ = (
        "_resource_award_instruction",
        "_ruc_award_instruction",
        "contingency_active",
        "dispatch_mode",
    )

    dispatch_mode: AutomaticDispatchMode | None
    contingency_active: YesNo | None

    ruc_award_instruction: Many[RUCAwardInstruction] = Many(
        EndMeta(
            name="ruc_award_instruction",
            cim_role="RUCAwardInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ruc_award_instruction:RUCAwardInstruction",
            many=True,
            lower=1,
            upper=None,
            inverse="clearing_resource_award",
            aggregation="none",
        )
    )
    resource_award_instruction: Many[ResourceAwardInstruction] = Many(
        EndMeta(
            name="resource_award_instruction",
            cim_role="ResourceAwardInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_instruction:ResourceAwardInstruction",
            many=True,
            lower=1,
            upper=None,
            inverse="clearing_resource_award",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceAwardClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{F58861DA-5DAC-4572-9D47-348DEC93315D}",
        attributes=(
            AttrMeta("dispatch_mode", "dispatchMode", "AutomaticDispatchMode", 0, 1, "enumeration"),
            AttrMeta("contingency_active", "contingencyActive", "YesNo", 0, 1, "enumeration"),
        ),
        ends=(
            ruc_award_instruction.meta,
            resource_award_instruction.meta,
        ),
    )

    def __init__(
        self,
        *,
        dispatch_mode: AutomaticDispatchMode | None = None,
        contingency_active: YesNo | None = None,
        ruc_award_instruction: Iterable[RUCAwardInstruction] | None = None,
        resource_award_instruction: Iterable[ResourceAwardInstruction] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dispatch_mode = dispatch_mode
        self.contingency_active = contingency_active
        if ruc_award_instruction is not None:
            ResourceAwardClearing.ruc_award_instruction.extend(self, ruc_award_instruction)
        if resource_award_instruction is not None:
            ResourceAwardClearing.resource_award_instruction.extend(
                self, resource_award_instruction
            )

    def add_ruc_award_instruction(self, ruc_award_instruction: RUCAwardInstruction) -> Self:
        return ResourceAwardClearing.ruc_award_instruction.add(self, ruc_award_instruction)

    def remove_ruc_award_instruction(self, ruc_award_instruction: RUCAwardInstruction) -> Self:
        return ResourceAwardClearing.ruc_award_instruction.remove(self, ruc_award_instruction)

    def clear_ruc_award_instruction(self) -> Self:
        return ResourceAwardClearing.ruc_award_instruction.clear(self)

    def num_ruc_award_instruction(self) -> int:
        return ResourceAwardClearing.ruc_award_instruction.count(self)

    def add_resource_award_instruction(
        self, resource_award_instruction: ResourceAwardInstruction
    ) -> Self:
        return ResourceAwardClearing.resource_award_instruction.add(
            self, resource_award_instruction
        )

    def remove_resource_award_instruction(
        self, resource_award_instruction: ResourceAwardInstruction
    ) -> Self:
        return ResourceAwardClearing.resource_award_instruction.remove(
            self, resource_award_instruction
        )

    def clear_resource_award_instruction(self) -> Self:
        return ResourceAwardClearing.resource_award_instruction.clear(self)

    def num_resource_award_instruction(self) -> int:
        return ResourceAwardClearing.resource_award_instruction.count(self)
