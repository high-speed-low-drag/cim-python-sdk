"""CIM class DCBaseTerminal (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.acdc_terminal import ACDCTerminal

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.dc.dc_node import DCNode
    from cim_python_sdk.model.iec61970.base.dc.dc_topological_node import DCTopologicalNode


class DCBaseTerminal(ACDCTerminal):
    """An electrical connection point at a piece of DC conducting equipment. DC terminals are
    connected at one physical DC node that may have multiple DC terminals connected. A DC
    node is similar to an AC connectivity node. The model requires that DC connections are
    distinct from AC connections."""

    __slots__ = ("_dc_node", "_dc_topological_node")

    dc_node: One[DCNode] = One(
        EndMeta(
            name="dc_node",
            cim_role="DCNode",
            target="cim_python_sdk.model.iec61970.base.dc.dc_node:DCNode",
            many=False,
            lower=0,
            upper=1,
            inverse="dc_terminals",
            aggregation="none",
        )
    )
    dc_topological_node: One[DCTopologicalNode] = One(
        EndMeta(
            name="dc_topological_node",
            cim_role="DCTopologicalNode",
            target="cim_python_sdk.model.iec61970.base.dc.dc_topological_node:DCTopologicalNode",
            many=False,
            lower=0,
            upper=1,
            inverse="dc_terminals",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCBaseTerminal",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{F76397E4-74A4-4178-9434-E33C9EBC5E7C}",
        ends=(
            dc_node.meta,
            dc_topological_node.meta,
        ),
    )

    def __init__(
        self,
        *,
        dc_node: DCNode | None = None,
        dc_topological_node: DCTopologicalNode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dc_node is not None:
            self.dc_node = dc_node
        if dc_topological_node is not None:
            self.dc_topological_node = dc_topological_node
