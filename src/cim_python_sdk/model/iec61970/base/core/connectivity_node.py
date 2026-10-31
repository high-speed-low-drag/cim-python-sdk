"""CIM class ConnectivityNode (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_core.boundary_point import (
        BoundaryPoint,
    )
    from cim_python_sdk.model.iec61970.base.core.connectivity_node_container import (
        ConnectivityNodeContainer,
    )
    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.base.topology.topological_node import TopologicalNode


class ConnectivityNode(IdentifiedObject):
    """Connectivity nodes are points where terminals of AC conducting equipment are connected
    together with zero impedance."""

    __slots__ = (
        "_boundary_point",
        "_connectivity_node_container",
        "_terminals",
        "_topological_node",
    )

    connectivity_node_container: One[ConnectivityNodeContainer] = One(
        EndMeta(
            name="connectivity_node_container",
            cim_role="ConnectivityNodeContainer",
            target="cim_python_sdk.model.iec61970.base.core.connectivity_node_container:ConnectivityNodeContainer",
            many=False,
            lower=1,
            upper=1,
            inverse="connectivity_nodes",
            aggregation="none",
        )
    )
    topological_node: One[TopologicalNode] = One(
        EndMeta(
            name="topological_node",
            cim_role="TopologicalNode",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=False,
            lower=0,
            upper=1,
            inverse="connectivity_nodes",
            aggregation="none",
        )
    )
    terminals: Many[Terminal] = Many(
        EndMeta(
            name="terminals",
            cim_role="Terminals",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=True,
            lower=0,
            upper=None,
            inverse="connectivity_node",
            aggregation="none",
        )
    )
    boundary_point: One[BoundaryPoint] = One(
        EndMeta(
            name="boundary_point",
            cim_role="BoundaryPoint",
            target="cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_core.boundary_point:BoundaryPoint",
            many=False,
            lower=0,
            upper=1,
            inverse="connectivity_node",
            aggregation="none",
            namespace="eu",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConnectivityNode",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{8BCACC36-B2DD-4c2a-A2AE-CFDF43731FC2}",
        ends=(
            connectivity_node_container.meta,
            topological_node.meta,
            terminals.meta,
            boundary_point.meta,
        ),
    )

    def __init__(
        self,
        *,
        connectivity_node_container: ConnectivityNodeContainer | None = None,
        topological_node: TopologicalNode | None = None,
        terminals: Iterable[Terminal] | None = None,
        boundary_point: BoundaryPoint | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if connectivity_node_container is not None:
            self.connectivity_node_container = connectivity_node_container
        if topological_node is not None:
            self.topological_node = topological_node
        if terminals is not None:
            ConnectivityNode.terminals.extend(self, terminals)
        if boundary_point is not None:
            self.boundary_point = boundary_point

    def add_terminal(self, terminal: Terminal) -> Self:
        return ConnectivityNode.terminals.add(self, terminal)

    def remove_terminal(self, terminal: Terminal) -> Self:
        return ConnectivityNode.terminals.remove(self, terminal)

    def clear_terminals(self) -> Self:
        return ConnectivityNode.terminals.clear(self)

    def num_terminal(self) -> int:
        return ConnectivityNode.terminals.count(self)

    def get_terminal_by_mrid(self, mrid: str) -> Terminal | None:
        return ConnectivityNode.terminals.get_by_mrid(self, mrid)
