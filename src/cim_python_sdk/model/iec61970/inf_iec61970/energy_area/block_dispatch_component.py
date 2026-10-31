"""CIM class BlockDispatchComponent (TC57CIM/IEC61970/InfIEC61970/EnergyArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_component import EnergyComponent

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_order import (
        BlockDispatchOrder,
    )


class BlockDispatchComponent(EnergyComponent):
    """CIM class BlockDispatchComponent."""

    __slots__ = ("_block_dispatch_orders",)

    block_dispatch_orders: Many[BlockDispatchOrder] = Many(
        EndMeta(
            name="block_dispatch_orders",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.block_dispatch_order:BlockDispatchOrder",
            many=True,
            lower=1,
            upper=None,
            inverse="block_dispatch_component",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BlockDispatchComponent",
        package="TC57CIM/IEC61970/InfIEC61970/EnergyArea",
        guid="{0F1D4F85-15C3-4a05-A1B2-674CCE3BBBF0}",
        ends=(block_dispatch_orders.meta,),
    )

    def __init__(
        self,
        *,
        block_dispatch_orders: Iterable[BlockDispatchOrder] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if block_dispatch_orders is not None:
            BlockDispatchComponent.block_dispatch_orders.extend(self, block_dispatch_orders)

    def add_block_dispatch_order(self, block_dispatch_order: BlockDispatchOrder) -> Self:
        return BlockDispatchComponent.block_dispatch_orders.add(self, block_dispatch_order)

    def remove_block_dispatch_order(self, block_dispatch_order: BlockDispatchOrder) -> Self:
        return BlockDispatchComponent.block_dispatch_orders.remove(self, block_dispatch_order)

    def clear_block_dispatch_orders(self) -> Self:
        return BlockDispatchComponent.block_dispatch_orders.clear(self)

    def num_block_dispatch_order(self) -> int:
        return BlockDispatchComponent.block_dispatch_orders.count(self)

    def get_block_dispatch_order_by_mrid(self, mrid: str) -> BlockDispatchOrder | None:
        return BlockDispatchComponent.block_dispatch_orders.get_by_mrid(self, mrid)
