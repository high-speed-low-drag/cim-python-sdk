"""CIM class ConnectivityNodeContainer (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.connectivity_node import ConnectivityNode
    from cim_python_sdk.model.iec61970.base.topology.topological_node import TopologicalNode


class ConnectivityNodeContainer(PowerSystemResource):
    """A base class for all objects that may contain connectivity nodes or topological nodes."""

    __slots__ = ("_connectivity_nodes", "_topological_node")

    connectivity_nodes: Many[ConnectivityNode] = Many(
        EndMeta(
            name="connectivity_nodes",
            cim_role="ConnectivityNodes",
            target="cim_python_sdk.model.iec61970.base.core.connectivity_node:ConnectivityNode",
            many=True,
            lower=0,
            upper=None,
            inverse="connectivity_node_container",
            aggregation="none",
        )
    )
    topological_node: Many[TopologicalNode] = Many(
        EndMeta(
            name="topological_node",
            cim_role="TopologicalNode",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=True,
            lower=0,
            upper=None,
            inverse="connectivity_node_container",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConnectivityNodeContainer",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{B985C03E-46A3-4aec-B5B6-FDD983EBE621}",
        ends=(
            connectivity_nodes.meta,
            topological_node.meta,
        ),
    )

    def __init__(
        self,
        *,
        connectivity_nodes: Iterable[ConnectivityNode] | None = None,
        topological_node: Iterable[TopologicalNode] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if connectivity_nodes is not None:
            ConnectivityNodeContainer.connectivity_nodes.extend(self, connectivity_nodes)
        if topological_node is not None:
            ConnectivityNodeContainer.topological_node.extend(self, topological_node)

    def add_connectivity_node(self, connectivity_node: ConnectivityNode) -> Self:
        return ConnectivityNodeContainer.connectivity_nodes.add(self, connectivity_node)

    def remove_connectivity_node(self, connectivity_node: ConnectivityNode) -> Self:
        return ConnectivityNodeContainer.connectivity_nodes.remove(self, connectivity_node)

    def clear_connectivity_nodes(self) -> Self:
        return ConnectivityNodeContainer.connectivity_nodes.clear(self)

    def num_connectivity_node(self) -> int:
        return ConnectivityNodeContainer.connectivity_nodes.count(self)

    def get_connectivity_node_by_mrid(self, mrid: str) -> ConnectivityNode | None:
        return ConnectivityNodeContainer.connectivity_nodes.get_by_mrid(self, mrid)

    def add_topological_node(self, topological_node: TopologicalNode) -> Self:
        return ConnectivityNodeContainer.topological_node.add(self, topological_node)

    def remove_topological_node(self, topological_node: TopologicalNode) -> Self:
        return ConnectivityNodeContainer.topological_node.remove(self, topological_node)

    def clear_topological_node(self) -> Self:
        return ConnectivityNodeContainer.topological_node.clear(self)

    def num_topological_node(self) -> int:
        return ConnectivityNodeContainer.topological_node.count(self)

    def get_topological_node_by_mrid(self, mrid: str) -> TopologicalNode | None:
        return ConnectivityNodeContainer.topological_node.get_by_mrid(self, mrid)
