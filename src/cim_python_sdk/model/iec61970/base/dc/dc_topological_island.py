"""CIM class DCTopologicalIsland (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.dc.dc_topological_node import DCTopologicalNode


class DCTopologicalIsland(IdentifiedObject):
    """An electrically connected subset of the network. DC topological islands can change as
    the current network state changes, e.g. due to:

    - disconnect switches or breakers changing state in a SCADA/EMS.

    - manual creation, change or deletion of topological nodes in a planning tool.

    Only energised TopologicalNode-s shall be part of the topological island."""

    __slots__ = ("_dc_topological_nodes",)

    dc_topological_nodes: Many[DCTopologicalNode] = Many(
        EndMeta(
            name="dc_topological_nodes",
            cim_role="DCTopologicalNodes",
            target="cim_python_sdk.model.iec61970.base.dc.dc_topological_node:DCTopologicalNode",
            many=True,
            lower=1,
            upper=None,
            inverse="dc_topological_island",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCTopologicalIsland",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{85B3B225-BD9B-4689-8878-0CEE3E06231B}",
        ends=(dc_topological_nodes.meta,),
    )

    def __init__(
        self,
        *,
        dc_topological_nodes: Iterable[DCTopologicalNode] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dc_topological_nodes is not None:
            DCTopologicalIsland.dc_topological_nodes.extend(self, dc_topological_nodes)

    def add_dc_topological_node(self, dc_topological_node: DCTopologicalNode) -> Self:
        return DCTopologicalIsland.dc_topological_nodes.add(self, dc_topological_node)

    def remove_dc_topological_node(self, dc_topological_node: DCTopologicalNode) -> Self:
        return DCTopologicalIsland.dc_topological_nodes.remove(self, dc_topological_node)

    def clear_dc_topological_nodes(self) -> Self:
        return DCTopologicalIsland.dc_topological_nodes.clear(self)

    def num_dc_topological_node(self) -> int:
        return DCTopologicalIsland.dc_topological_nodes.count(self)

    def get_dc_topological_node_by_mrid(self, mrid: str) -> DCTopologicalNode | None:
        return DCTopologicalIsland.dc_topological_nodes.get_by_mrid(self, mrid)
