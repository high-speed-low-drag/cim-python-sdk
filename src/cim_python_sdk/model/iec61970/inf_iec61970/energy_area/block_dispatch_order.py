"""CIM class BlockDispatchOrder (TC57CIM/IEC61970/InfIEC61970/EnergyArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_component import (
        BlockDispatchComponent,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_instruction import (
        BlockDispatchInstruction,
    )


class BlockDispatchOrder(IdentifiedObject):
    """CIM class BlockDispatchOrder."""

    __slots__ = ("_block_dispatch_component", "_block_dispatch_instruction", "p", "sequence")

    p: float | None  # ActivePower
    sequence: int | None

    block_dispatch_component: One[BlockDispatchComponent] = One(
        EndMeta(
            name="block_dispatch_component",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_component:BlockDispatchComponent",
            many=False,
            lower=1,
            upper=1,
            inverse="block_dispatch_orders",
            aggregation="none",
        )
    )
    block_dispatch_instruction: One[BlockDispatchInstruction] = One(
        EndMeta(
            name="block_dispatch_instruction",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_instruction:BlockDispatchInstruction",
            many=False,
            lower=1,
            upper=1,
            inverse="block_dispatch_orders",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BlockDispatchOrder",
        package="TC57CIM/IEC61970/InfIEC61970/EnergyArea",
        guid="{47F3F95D-63E2-4377-B322-31F18349B271}",
        attributes=(
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("sequence", "sequence", "int", 0, 1, "primitive"),
        ),
        ends=(
            block_dispatch_component.meta,
            block_dispatch_instruction.meta,
        ),
    )

    def __init__(
        self,
        *,
        p: float | None = None,
        sequence: int | None = None,
        block_dispatch_component: BlockDispatchComponent | None = None,
        block_dispatch_instruction: BlockDispatchInstruction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.p = p
        self.sequence = sequence
        if block_dispatch_component is not None:
            self.block_dispatch_component = block_dispatch_component
        if block_dispatch_instruction is not None:
            self.block_dispatch_instruction = block_dispatch_instruction
