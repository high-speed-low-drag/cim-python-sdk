"""CIM class TopologicalNode (TC57CIM/IEC61970/Base/Topology). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.base_voltage import BaseVoltage
    from cim_python_sdk.model.iec61970.base.core.connectivity_node import ConnectivityNode
    from cim_python_sdk.model.iec61970.base.core.connectivity_node_container import (
        ConnectivityNodeContainer,
    )
    from cim_python_sdk.model.iec61970.base.core.reporting_group import ReportingGroup
    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.base.state_variables.sv_injection import SvInjection
    from cim_python_sdk.model.iec61970.base.state_variables.sv_voltage import SvVoltage
    from cim_python_sdk.model.iec61970.base.topology.bus_name_marker import BusNameMarker
    from cim_python_sdk.model.iec61970.base.topology.topological_island import TopologicalIsland


class TopologicalNode(IdentifiedObject):
    """For a detailed substation model a topological node is a set of connectivity nodes that,
    in the current network state, are connected together through any type of closed
    switches, including jumpers. Topological nodes change as the current network state
    changes (i.e., switches, breakers, etc. change state).

    For a planning model, switch statuses are not used to form topological nodes. Instead
    they are manually created or deleted in a model builder tool. Topological nodes
    maintained this way are also called "busses"."""

    __slots__ = (
        "_angle_ref_topological_island",
        "_base_voltage",
        "_bus_name_marker",
        "_connectivity_node_container",
        "_connectivity_nodes",
        "_reporting_group",
        "_sv_injection",
        "_sv_voltage",
        "_terminal",
        "_topological_island",
        "p_injection",
        "q_injection",
    )

    p_injection: float | None  # ActivePower
    q_injection: float | None  # ReactivePower

    reporting_group: One[ReportingGroup] = One(
        EndMeta(
            name="reporting_group",
            cim_role="ReportingGroup",
            target="cim_python_sdk.model.iec61970.base.core.reporting_group:ReportingGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="topological_node",
            aggregation="none",
        )
    )
    bus_name_marker: Many[BusNameMarker] = Many(
        EndMeta(
            name="bus_name_marker",
            cim_role="BusNameMarker",
            target="cim_python_sdk.model.iec61970.base.topology.bus_name_marker:BusNameMarker",
            many=True,
            lower=0,
            upper=None,
            inverse="topological_node",
            aggregation="none",
        )
    )
    sv_voltage: Many[SvVoltage] = Many(
        EndMeta(
            name="sv_voltage",
            cim_role="SvVoltage",
            target="cim_python_sdk.model.iec61970.base.state_variables.sv_voltage:SvVoltage",
            many=True,
            lower=0,
            upper=None,
            inverse="topological_node",
            aggregation="none",
        )
    )
    sv_injection: Many[SvInjection] = Many(
        EndMeta(
            name="sv_injection",
            cim_role="SvInjection",
            target="cim_python_sdk.model.iec61970.base.state_variables.sv_injection:SvInjection",
            many=True,
            lower=0,
            upper=None,
            inverse="topological_node",
            aggregation="none",
        )
    )
    base_voltage: One[BaseVoltage] = One(
        EndMeta(
            name="base_voltage",
            cim_role="BaseVoltage",
            target="cim_python_sdk.model.iec61970.base.core.base_voltage:BaseVoltage",
            many=False,
            lower=0,
            upper=1,
            inverse="topological_node",
            aggregation="none",
        )
    )
    angle_ref_topological_island: One[TopologicalIsland] = One(
        EndMeta(
            name="angle_ref_topological_island",
            cim_role="AngleRefTopologicalIsland",
            target="cim_python_sdk.model.iec61970.base.topology.topological_island:TopologicalIsland",
            many=False,
            lower=0,
            upper=1,
            inverse="angle_ref_topological_node",
            aggregation="none",
        )
    )
    connectivity_node_container: One[ConnectivityNodeContainer] = One(
        EndMeta(
            name="connectivity_node_container",
            cim_role="ConnectivityNodeContainer",
            target="cim_python_sdk.model.iec61970.base.core.connectivity_node_container:ConnectivityNodeContainer",
            many=False,
            lower=0,
            upper=1,
            inverse="topological_node",
            aggregation="none",
        )
    )
    connectivity_nodes: Many[ConnectivityNode] = Many(
        EndMeta(
            name="connectivity_nodes",
            cim_role="ConnectivityNodes",
            target="cim_python_sdk.model.iec61970.base.core.connectivity_node:ConnectivityNode",
            many=True,
            lower=0,
            upper=None,
            inverse="topological_node",
            aggregation="shared",
        )
    )
    topological_island: One[TopologicalIsland] = One(
        EndMeta(
            name="topological_island",
            cim_role="TopologicalIsland",
            target="cim_python_sdk.model.iec61970.base.topology.topological_island:TopologicalIsland",
            many=False,
            lower=0,
            upper=1,
            inverse="topological_nodes",
            aggregation="none",
        )
    )
    terminal: Many[Terminal] = Many(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=True,
            lower=0,
            upper=None,
            inverse="topological_node",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TopologicalNode",
        package="TC57CIM/IEC61970/Base/Topology",
        guid="{82489582-0ECB-4066-970D-A265B1065315}",
        attributes=(
            AttrMeta("p_injection", "pInjection", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("q_injection", "qInjection", "ReactivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            reporting_group.meta,
            bus_name_marker.meta,
            sv_voltage.meta,
            sv_injection.meta,
            base_voltage.meta,
            angle_ref_topological_island.meta,
            connectivity_node_container.meta,
            connectivity_nodes.meta,
            topological_island.meta,
            terminal.meta,
        ),
    )

    def __init__(
        self,
        *,
        p_injection: float | None = None,
        q_injection: float | None = None,
        reporting_group: ReportingGroup | None = None,
        bus_name_marker: Iterable[BusNameMarker] | None = None,
        sv_voltage: Iterable[SvVoltage] | None = None,
        sv_injection: Iterable[SvInjection] | None = None,
        base_voltage: BaseVoltage | None = None,
        angle_ref_topological_island: TopologicalIsland | None = None,
        connectivity_node_container: ConnectivityNodeContainer | None = None,
        connectivity_nodes: Iterable[ConnectivityNode] | None = None,
        topological_island: TopologicalIsland | None = None,
        terminal: Iterable[Terminal] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.p_injection = p_injection
        self.q_injection = q_injection
        if reporting_group is not None:
            self.reporting_group = reporting_group
        if bus_name_marker is not None:
            TopologicalNode.bus_name_marker.extend(self, bus_name_marker)
        if sv_voltage is not None:
            TopologicalNode.sv_voltage.extend(self, sv_voltage)
        if sv_injection is not None:
            TopologicalNode.sv_injection.extend(self, sv_injection)
        if base_voltage is not None:
            self.base_voltage = base_voltage
        if angle_ref_topological_island is not None:
            self.angle_ref_topological_island = angle_ref_topological_island
        if connectivity_node_container is not None:
            self.connectivity_node_container = connectivity_node_container
        if connectivity_nodes is not None:
            TopologicalNode.connectivity_nodes.extend(self, connectivity_nodes)
        if topological_island is not None:
            self.topological_island = topological_island
        if terminal is not None:
            TopologicalNode.terminal.extend(self, terminal)

    def add_bus_name_marker(self, bus_name_marker: BusNameMarker) -> Self:
        return TopologicalNode.bus_name_marker.add(self, bus_name_marker)

    def remove_bus_name_marker(self, bus_name_marker: BusNameMarker) -> Self:
        return TopologicalNode.bus_name_marker.remove(self, bus_name_marker)

    def clear_bus_name_marker(self) -> Self:
        return TopologicalNode.bus_name_marker.clear(self)

    def num_bus_name_marker(self) -> int:
        return TopologicalNode.bus_name_marker.count(self)

    def get_bus_name_marker_by_mrid(self, mrid: str) -> BusNameMarker | None:
        return TopologicalNode.bus_name_marker.get_by_mrid(self, mrid)

    def add_sv_voltage(self, sv_voltage: SvVoltage) -> Self:
        return TopologicalNode.sv_voltage.add(self, sv_voltage)

    def remove_sv_voltage(self, sv_voltage: SvVoltage) -> Self:
        return TopologicalNode.sv_voltage.remove(self, sv_voltage)

    def clear_sv_voltage(self) -> Self:
        return TopologicalNode.sv_voltage.clear(self)

    def num_sv_voltage(self) -> int:
        return TopologicalNode.sv_voltage.count(self)

    def add_sv_injection(self, sv_injection: SvInjection) -> Self:
        return TopologicalNode.sv_injection.add(self, sv_injection)

    def remove_sv_injection(self, sv_injection: SvInjection) -> Self:
        return TopologicalNode.sv_injection.remove(self, sv_injection)

    def clear_sv_injection(self) -> Self:
        return TopologicalNode.sv_injection.clear(self)

    def num_sv_injection(self) -> int:
        return TopologicalNode.sv_injection.count(self)

    def add_connectivity_node(self, connectivity_node: ConnectivityNode) -> Self:
        return TopologicalNode.connectivity_nodes.add(self, connectivity_node)

    def remove_connectivity_node(self, connectivity_node: ConnectivityNode) -> Self:
        return TopologicalNode.connectivity_nodes.remove(self, connectivity_node)

    def clear_connectivity_nodes(self) -> Self:
        return TopologicalNode.connectivity_nodes.clear(self)

    def num_connectivity_node(self) -> int:
        return TopologicalNode.connectivity_nodes.count(self)

    def get_connectivity_node_by_mrid(self, mrid: str) -> ConnectivityNode | None:
        return TopologicalNode.connectivity_nodes.get_by_mrid(self, mrid)

    def add_terminal(self, terminal: Terminal) -> Self:
        return TopologicalNode.terminal.add(self, terminal)

    def remove_terminal(self, terminal: Terminal) -> Self:
        return TopologicalNode.terminal.remove(self, terminal)

    def clear_terminal(self) -> Self:
        return TopologicalNode.terminal.clear(self)

    def num_terminal(self) -> int:
        return TopologicalNode.terminal.count(self)

    def get_terminal_by_mrid(self, mrid: str) -> Terminal | None:
        return TopologicalNode.terminal.get_by_mrid(self, mrid)
