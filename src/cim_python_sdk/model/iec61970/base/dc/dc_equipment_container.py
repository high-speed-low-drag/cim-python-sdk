"""CIM class DCEquipmentContainer (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.equipment_container import EquipmentContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.dc.dc_node import DCNode
    from cim_python_sdk.model.iec61970.base.dc.dc_topological_node import DCTopologicalNode


class DCEquipmentContainer(EquipmentContainer):
    """A modelling construct to provide a root class for containment of DC as well as AC
    equipment. The class differ from the EquipmentContaner for AC in that it may also
    contain DCNode-s. Hence it can contain both AC and DC equipment."""

    __slots__ = ("_dc_nodes", "_dc_topological_node")

    dc_topological_node: Many[DCTopologicalNode] = Many(
        EndMeta(
            name="dc_topological_node",
            cim_role="DCTopologicalNode",
            target="cim_python_sdk.model.iec61970.base.dc.dc_topological_node:DCTopologicalNode",
            many=True,
            lower=0,
            upper=None,
            inverse="dc_equipment_container",
            aggregation="none",
        )
    )
    dc_nodes: Many[DCNode] = Many(
        EndMeta(
            name="dc_nodes",
            cim_role="DCNodes",
            target="cim_python_sdk.model.iec61970.base.dc.dc_node:DCNode",
            many=True,
            lower=0,
            upper=None,
            inverse="dc_equipment_container",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCEquipmentContainer",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{B7EB57A9-3AD6-40e2-9D5D-F391283E63B3}",
        ends=(
            dc_topological_node.meta,
            dc_nodes.meta,
        ),
    )

    def __init__(
        self,
        *,
        dc_topological_node: Iterable[DCTopologicalNode] | None = None,
        dc_nodes: Iterable[DCNode] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dc_topological_node is not None:
            DCEquipmentContainer.dc_topological_node.extend(self, dc_topological_node)
        if dc_nodes is not None:
            DCEquipmentContainer.dc_nodes.extend(self, dc_nodes)

    def add_dc_topological_node(self, dc_topological_node: DCTopologicalNode) -> Self:
        return DCEquipmentContainer.dc_topological_node.add(self, dc_topological_node)

    def remove_dc_topological_node(self, dc_topological_node: DCTopologicalNode) -> Self:
        return DCEquipmentContainer.dc_topological_node.remove(self, dc_topological_node)

    def clear_dc_topological_node(self) -> Self:
        return DCEquipmentContainer.dc_topological_node.clear(self)

    def num_dc_topological_node(self) -> int:
        return DCEquipmentContainer.dc_topological_node.count(self)

    def get_dc_topological_node_by_mrid(self, mrid: str) -> DCTopologicalNode | None:
        return DCEquipmentContainer.dc_topological_node.get_by_mrid(self, mrid)

    def add_dc_node(self, dc_node: DCNode) -> Self:
        return DCEquipmentContainer.dc_nodes.add(self, dc_node)

    def remove_dc_node(self, dc_node: DCNode) -> Self:
        return DCEquipmentContainer.dc_nodes.remove(self, dc_node)

    def clear_dc_nodes(self) -> Self:
        return DCEquipmentContainer.dc_nodes.clear(self)

    def num_dc_node(self) -> int:
        return DCEquipmentContainer.dc_nodes.count(self)

    def get_dc_node_by_mrid(self, mrid: str) -> DCNode | None:
        return DCEquipmentContainer.dc_nodes.get_by_mrid(self, mrid)
