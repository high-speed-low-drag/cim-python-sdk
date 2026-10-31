"""CIM class InstructionClearingDOP (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.dop_instruction import (
        DopInstruction,
    )


class InstructionClearingDOP(MarketFactors):
    """Model of market clearing, related to Dispatch Operating Point. Identifies interval."""

    __slots__ = ("_dop_instruction",)

    dop_instruction: Many[DopInstruction] = Many(
        EndMeta(
            name="dop_instruction",
            cim_role="DopInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.dop_instruction:DopInstruction",
            many=True,
            lower=1,
            upper=None,
            inverse="instruction_clearing_dop",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InstructionClearingDOP",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{64C614BD-1170-49a3-93A0-464AA289153B}",
        ends=(dop_instruction.meta,),
    )

    def __init__(
        self,
        *,
        dop_instruction: Iterable[DopInstruction] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dop_instruction is not None:
            InstructionClearingDOP.dop_instruction.extend(self, dop_instruction)

    def add_dop_instruction(self, dop_instruction: DopInstruction) -> Self:
        return InstructionClearingDOP.dop_instruction.add(self, dop_instruction)

    def remove_dop_instruction(self, dop_instruction: DopInstruction) -> Self:
        return InstructionClearingDOP.dop_instruction.remove(self, dop_instruction)

    def clear_dop_instruction(self) -> Self:
        return InstructionClearingDOP.dop_instruction.clear(self)

    def num_dop_instruction(self) -> int:
        return InstructionClearingDOP.dop_instruction.count(self)
