"""CIM class BlockDispatchInstruction (TC57CIM/IEC61970/InfIEC61970/EnergyArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_order import (
        BlockDispatchOrder,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group import EnergyGroup


class BlockDispatchInstruction(IdentifiedObject):
    """CIM class BlockDispatchInstruction."""

    __slots__ = ("_block_dispatch_orders", "_energy_group")

    energy_group: One[EnergyGroup] = One(
        EndMeta(
            name="energy_group",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group:EnergyGroup",
            many=False,
            lower=1,
            upper=1,
            inverse="block_dispatch_instructions",
            aggregation="none",
        )
    )
    block_dispatch_orders: Many[BlockDispatchOrder] = Many(
        EndMeta(
            name="block_dispatch_orders",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_order:BlockDispatchOrder",
            many=True,
            lower=1,
            upper=None,
            inverse="block_dispatch_instruction",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BlockDispatchInstruction",
        package="TC57CIM/IEC61970/InfIEC61970/EnergyArea",
        guid="{A6360DD7-6199-496b-8468-7B7AEB2AC68F}",
        ends=(
            energy_group.meta,
            block_dispatch_orders.meta,
        ),
    )

    def __init__(
        self,
        *,
        energy_group: EnergyGroup | None = None,
        block_dispatch_orders: Iterable[BlockDispatchOrder] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if energy_group is not None:
            self.energy_group = energy_group
        if block_dispatch_orders is not None:
            BlockDispatchInstruction.block_dispatch_orders.extend(self, block_dispatch_orders)

    def add_block_dispatch_order(self, block_dispatch_order: BlockDispatchOrder) -> Self:
        return BlockDispatchInstruction.block_dispatch_orders.add(self, block_dispatch_order)

    def remove_block_dispatch_order(self, block_dispatch_order: BlockDispatchOrder) -> Self:
        return BlockDispatchInstruction.block_dispatch_orders.remove(self, block_dispatch_order)

    def clear_block_dispatch_orders(self) -> Self:
        return BlockDispatchInstruction.block_dispatch_orders.clear(self)

    def num_block_dispatch_order(self) -> int:
        return BlockDispatchInstruction.block_dispatch_orders.count(self)

    def get_block_dispatch_order_by_mrid(self, mrid: str) -> BlockDispatchOrder | None:
        return BlockDispatchInstruction.block_dispatch_orders.get_by_mrid(self, mrid)
