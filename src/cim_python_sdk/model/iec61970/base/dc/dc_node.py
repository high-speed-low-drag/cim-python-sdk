"""CIM class DCNode (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.dc.dc_base_terminal import DCBaseTerminal
    from cim_python_sdk.model.iec61970.base.dc.dc_equipment_container import DCEquipmentContainer
    from cim_python_sdk.model.iec61970.base.dc.dc_topological_node import DCTopologicalNode


class DCNode(IdentifiedObject):
    """DC nodes are points where terminals of DC conducting equipment are connected together
    with zero impedance."""

    __slots__ = ("_dc_equipment_container", "_dc_terminals", "_dc_topological_node")

    dc_topological_node: One[DCTopologicalNode] = One(
        EndMeta(
            name="dc_topological_node",
            cim_role="DCTopologicalNode",
            target="cim_python_sdk.model.iec61970.base.dc.dc_topological_node:DCTopologicalNode",
            many=False,
            lower=0,
            upper=1,
            inverse="dc_nodes",
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
            inverse="dc_node",
            aggregation="none",
        )
    )
    dc_equipment_container: One[DCEquipmentContainer] = One(
        EndMeta(
            name="dc_equipment_container",
            cim_role="DCEquipmentContainer",
            target="cim_python_sdk.model.iec61970.base.dc.dc_equipment_container:DCEquipmentContainer",
            many=False,
            lower=1,
            upper=1,
            inverse="dc_nodes",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCNode",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{203CCDC9-3887-4e57-8C59-B429AADB60F6}",
        ends=(
            dc_topological_node.meta,
            dc_terminals.meta,
            dc_equipment_container.meta,
        ),
    )

    def __init__(
        self,
        *,
        dc_topological_node: DCTopologicalNode | None = None,
        dc_terminals: Iterable[DCBaseTerminal] | None = None,
        dc_equipment_container: DCEquipmentContainer | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dc_topological_node is not None:
            self.dc_topological_node = dc_topological_node
        if dc_terminals is not None:
            DCNode.dc_terminals.extend(self, dc_terminals)
        if dc_equipment_container is not None:
            self.dc_equipment_container = dc_equipment_container

    def add_dc_terminal(self, dc_terminal: DCBaseTerminal) -> Self:
        return DCNode.dc_terminals.add(self, dc_terminal)

    def remove_dc_terminal(self, dc_terminal: DCBaseTerminal) -> Self:
        return DCNode.dc_terminals.remove(self, dc_terminal)

    def clear_dc_terminals(self) -> Self:
        return DCNode.dc_terminals.clear(self)

    def num_dc_terminal(self) -> int:
        return DCNode.dc_terminals.count(self)

    def get_dc_terminal_by_mrid(self, mrid: str) -> DCBaseTerminal | None:
        return DCNode.dc_terminals.get_by_mrid(self, mrid)
