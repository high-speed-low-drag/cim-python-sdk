"""CIM class ReportingGroup (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource
    from cim_python_sdk.model.iec61970.base.core.reporting_super_group import ReportingSuperGroup
    from cim_python_sdk.model.iec61970.base.topology.bus_name_marker import BusNameMarker
    from cim_python_sdk.model.iec61970.base.topology.topological_node import TopologicalNode


class ReportingGroup(IdentifiedObject):
    """A reporting group is used for various ad-hoc groupings used for reporting."""

    __slots__ = (
        "_bus_name_marker",
        "_power_system_resource",
        "_reporting_super_group",
        "_topological_node",
    )

    topological_node: Many[TopologicalNode] = Many(
        EndMeta(
            name="topological_node",
            cim_role="TopologicalNode",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=True,
            lower=0,
            upper=None,
            inverse="reporting_group",
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
            inverse="reporting_group",
            aggregation="none",
        )
    )
    reporting_super_group: One[ReportingSuperGroup] = One(
        EndMeta(
            name="reporting_super_group",
            cim_role="ReportingSuperGroup",
            target="cim_python_sdk.model.iec61970.base.core.reporting_super_group:ReportingSuperGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="reporting_group",
            aggregation="none",
        )
    )
    power_system_resource: Many[PowerSystemResource] = Many(
        EndMeta(
            name="power_system_resource",
            cim_role="PowerSystemResource",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=True,
            lower=0,
            upper=None,
            inverse="reporting_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReportingGroup",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{EB1C81AA-89E4-44f4-8BA2-45FF36E88015}",
        ends=(
            topological_node.meta,
            bus_name_marker.meta,
            reporting_super_group.meta,
            power_system_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        topological_node: Iterable[TopologicalNode] | None = None,
        bus_name_marker: Iterable[BusNameMarker] | None = None,
        reporting_super_group: ReportingSuperGroup | None = None,
        power_system_resource: Iterable[PowerSystemResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if topological_node is not None:
            ReportingGroup.topological_node.extend(self, topological_node)
        if bus_name_marker is not None:
            ReportingGroup.bus_name_marker.extend(self, bus_name_marker)
        if reporting_super_group is not None:
            self.reporting_super_group = reporting_super_group
        if power_system_resource is not None:
            ReportingGroup.power_system_resource.extend(self, power_system_resource)

    def add_topological_node(self, topological_node: TopologicalNode) -> Self:
        return ReportingGroup.topological_node.add(self, topological_node)

    def remove_topological_node(self, topological_node: TopologicalNode) -> Self:
        return ReportingGroup.topological_node.remove(self, topological_node)

    def clear_topological_node(self) -> Self:
        return ReportingGroup.topological_node.clear(self)

    def num_topological_node(self) -> int:
        return ReportingGroup.topological_node.count(self)

    def get_topological_node_by_mrid(self, mrid: str) -> TopologicalNode | None:
        return ReportingGroup.topological_node.get_by_mrid(self, mrid)

    def add_bus_name_marker(self, bus_name_marker: BusNameMarker) -> Self:
        return ReportingGroup.bus_name_marker.add(self, bus_name_marker)

    def remove_bus_name_marker(self, bus_name_marker: BusNameMarker) -> Self:
        return ReportingGroup.bus_name_marker.remove(self, bus_name_marker)

    def clear_bus_name_marker(self) -> Self:
        return ReportingGroup.bus_name_marker.clear(self)

    def num_bus_name_marker(self) -> int:
        return ReportingGroup.bus_name_marker.count(self)

    def get_bus_name_marker_by_mrid(self, mrid: str) -> BusNameMarker | None:
        return ReportingGroup.bus_name_marker.get_by_mrid(self, mrid)

    def add_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return ReportingGroup.power_system_resource.add(self, power_system_resource)

    def remove_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return ReportingGroup.power_system_resource.remove(self, power_system_resource)

    def clear_power_system_resource(self) -> Self:
        return ReportingGroup.power_system_resource.clear(self)

    def num_power_system_resource(self) -> int:
        return ReportingGroup.power_system_resource.count(self)

    def get_power_system_resource_by_mrid(self, mrid: str) -> PowerSystemResource | None:
        return ReportingGroup.power_system_resource.get_by_mrid(self, mrid)
