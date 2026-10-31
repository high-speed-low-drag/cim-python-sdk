"""CIM class DCTopologicalNode (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.dc.dc_base_terminal import DCBaseTerminal
    from cim_python_sdk.model.iec61970.base.dc.dc_equipment_container import DCEquipmentContainer
    from cim_python_sdk.model.iec61970.base.dc.dc_node import DCNode
    from cim_python_sdk.model.iec61970.base.dc.dc_topological_island import DCTopologicalIsland


class DCTopologicalNode(IdentifiedObject):
    """DC bus."""

    __slots__ = ("_dc_equipment_container", "_dc_nodes", "_dc_terminals", "_dc_topological_island")

    dc_topological_island: One[DCTopologicalIsland] = One(
        EndMeta(
            name="dc_topological_island",
            cim_role="DCTopologicalIsland",
            target="cim_python_sdk.model.iec61970.base.dc.dc_topological_island:DCTopologicalIsland",
            many=False,
            lower=0,
            upper=1,
            inverse="dc_topological_nodes",
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
            inverse="dc_topological_node",
            aggregation="none",
        )
    )
    dc_equipment_container: One[DCEquipmentContainer] = One(
        EndMeta(
            name="dc_equipment_container",
            cim_role="DCEquipmentContainer",
            target="cim_python_sdk.model.iec61970.base.dc.dc_equipment_container:DCEquipmentContainer",
            many=False,
            lower=0,
            upper=1,
            inverse="dc_topological_node",
            aggregation="none",
        )
    )
    dc_terminals: Many[DCBaseTerminal] = Many(
        EndMeta(
            name="dc_terminals",
            cim_role="DCTerminals",
            target="cim_python_sdk.model.iec61970.base.dc.dc_base_terminal:DCBaseTerminal",
            many=True,
            lower=0,
            upper=None,
            inverse="dc_topological_node",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCTopologicalNode",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{36E96930-3FAF-4844-91D4-7103E3D68EAA}",
        ends=(
            dc_topological_island.meta,
            dc_nodes.meta,
            dc_equipment_container.meta,
            dc_terminals.meta,
        ),
    )

    def __init__(
        self,
        *,
        dc_topological_island: DCTopologicalIsland | None = None,
        dc_nodes: Iterable[DCNode] | None = None,
        dc_equipment_container: DCEquipmentContainer | None = None,
        dc_terminals: Iterable[DCBaseTerminal] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dc_topological_island is not None:
            self.dc_topological_island = dc_topological_island
        if dc_nodes is not None:
            DCTopologicalNode.dc_nodes.extend(self, dc_nodes)
        if dc_equipment_container is not None:
            self.dc_equipment_container = dc_equipment_container
        if dc_terminals is not None:
            DCTopologicalNode.dc_terminals.extend(self, dc_terminals)

    def add_dc_node(self, dc_node: DCNode) -> Self:
        return DCTopologicalNode.dc_nodes.add(self, dc_node)

    def remove_dc_node(self, dc_node: DCNode) -> Self:
        return DCTopologicalNode.dc_nodes.remove(self, dc_node)

    def clear_dc_nodes(self) -> Self:
        return DCTopologicalNode.dc_nodes.clear(self)

    def num_dc_node(self) -> int:
        return DCTopologicalNode.dc_nodes.count(self)

    def get_dc_node_by_mrid(self, mrid: str) -> DCNode | None:
        return DCTopologicalNode.dc_nodes.get_by_mrid(self, mrid)

    def add_dc_terminal(self, dc_terminal: DCBaseTerminal) -> Self:
        return DCTopologicalNode.dc_terminals.add(self, dc_terminal)

    def remove_dc_terminal(self, dc_terminal: DCBaseTerminal) -> Self:
        return DCTopologicalNode.dc_terminals.remove(self, dc_terminal)

    def clear_dc_terminals(self) -> Self:
        return DCTopologicalNode.dc_terminals.clear(self)

    def num_dc_terminal(self) -> int:
        return DCTopologicalNode.dc_terminals.count(self)

    def get_dc_terminal_by_mrid(self, mrid: str) -> DCBaseTerminal | None:
        return DCTopologicalNode.dc_terminals.get_by_mrid(self, mrid)
