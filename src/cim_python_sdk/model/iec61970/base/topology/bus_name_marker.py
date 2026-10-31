"""CIM class BusNameMarker (TC57CIM/IEC61970/Base/Topology). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.acdc_terminal import ACDCTerminal
    from cim_python_sdk.model.iec61970.base.core.reporting_group import ReportingGroup
    from cim_python_sdk.model.iec61970.base.topology.topological_node import TopologicalNode


class BusNameMarker(IdentifiedObject):
    """Used to apply user standard names to TopologicalNodes. Associated with one or more
    terminals that are normally connected with the bus name. The associated terminals are
    normally connected by non-retained switches. For a ring bus station configuration, all
    BusbarSection terminals in the ring are typically associated. For a breaker and a half
    scheme, both BusbarSections would normally be associated. For a ring bus, all
    BusbarSections would normally be associated. For a "straight" busbar configuration,
    normally only the main terminal at the BusbarSection would be associated."""

    __slots__ = ("_reporting_group", "_terminal", "_topological_node", "priority")

    priority: int | None

    topological_node: One[TopologicalNode] = One(
        EndMeta(
            name="topological_node",
            cim_role="TopologicalNode",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=False,
            lower=0,
            upper=1,
            inverse="bus_name_marker",
            aggregation="none",
        )
    )
    reporting_group: One[ReportingGroup] = One(
        EndMeta(
            name="reporting_group",
            cim_role="ReportingGroup",
            target="cim_python_sdk.model.iec61970.base.core.reporting_group:ReportingGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="bus_name_marker",
            aggregation="none",
        )
    )
    terminal: Many[ACDCTerminal] = Many(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.acdc_terminal:ACDCTerminal",
            many=True,
            lower=1,
            upper=None,
            inverse="bus_name_marker",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BusNameMarker",
        package="TC57CIM/IEC61970/Base/Topology",
        guid="{CC2E7414-F646-406e-BFE1-86C1E97305FA}",
        attributes=(AttrMeta("priority", "priority", "int", 0, 1, "primitive"),),
        ends=(
            topological_node.meta,
            reporting_group.meta,
            terminal.meta,
        ),
    )

    def __init__(
        self,
        *,
        priority: int | None = None,
        topological_node: TopologicalNode | None = None,
        reporting_group: ReportingGroup | None = None,
        terminal: Iterable[ACDCTerminal] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.priority = priority
        if topological_node is not None:
            self.topological_node = topological_node
        if reporting_group is not None:
            self.reporting_group = reporting_group
        if terminal is not None:
            BusNameMarker.terminal.extend(self, terminal)

    def add_terminal(self, terminal: ACDCTerminal) -> Self:
        return BusNameMarker.terminal.add(self, terminal)

    def remove_terminal(self, terminal: ACDCTerminal) -> Self:
        return BusNameMarker.terminal.remove(self, terminal)

    def clear_terminal(self) -> Self:
        return BusNameMarker.terminal.clear(self)

    def num_terminal(self) -> int:
        return BusNameMarker.terminal.count(self)

    def get_terminal_by_mrid(self, mrid: str) -> ACDCTerminal | None:
        return BusNameMarker.terminal.get_by_mrid(self, mrid)
