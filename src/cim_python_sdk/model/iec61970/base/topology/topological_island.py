"""CIM class TopologicalIsland (TC57CIM/IEC61970/Base/Topology). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.topology.topological_node import TopologicalNode


class TopologicalIsland(IdentifiedObject):
    """An electrically connected subset of the network. Topological islands can change as the
    current network state changes, e.g. due to:

    - disconnect switches or breakers changing state in a SCADA/EMS.

    - manual creation, change or deletion of topological nodes in a planning tool.

    Only energised TopologicalNode-s shall be part of the topological island."""

    __slots__ = ("_angle_ref_topological_node", "_topological_nodes")

    angle_ref_topological_node: One[TopologicalNode] = One(
        EndMeta(
            name="angle_ref_topological_node",
            cim_role="AngleRefTopologicalNode",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=False,
            lower=0,
            upper=1,
            inverse="angle_ref_topological_island",
            aggregation="none",
        )
    )
    topological_nodes: Many[TopologicalNode] = Many(
        EndMeta(
            name="topological_nodes",
            cim_role="TopologicalNodes",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=True,
            lower=1,
            upper=None,
            inverse="topological_island",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TopologicalIsland",
        package="TC57CIM/IEC61970/Base/Topology",
        guid="{7AAF072C-6B81-4f1b-95F5-0BA3A3B7BE68}",
        ends=(
            angle_ref_topological_node.meta,
            topological_nodes.meta,
        ),
    )

    def __init__(
        self,
        *,
        angle_ref_topological_node: TopologicalNode | None = None,
        topological_nodes: Iterable[TopologicalNode] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if angle_ref_topological_node is not None:
            self.angle_ref_topological_node = angle_ref_topological_node
        if topological_nodes is not None:
            TopologicalIsland.topological_nodes.extend(self, topological_nodes)

    def add_topological_node(self, topological_node: TopologicalNode) -> Self:
        return TopologicalIsland.topological_nodes.add(self, topological_node)

    def remove_topological_node(self, topological_node: TopologicalNode) -> Self:
        return TopologicalIsland.topological_nodes.remove(self, topological_node)

    def clear_topological_nodes(self) -> Self:
        return TopologicalIsland.topological_nodes.clear(self)

    def num_topological_node(self) -> int:
        return TopologicalIsland.topological_nodes.count(self)

    def get_topological_node_by_mrid(self, mrid: str) -> TopologicalNode | None:
        return TopologicalIsland.topological_nodes.get_by_mrid(self, mrid)
