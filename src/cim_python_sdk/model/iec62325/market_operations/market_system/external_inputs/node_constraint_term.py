"""CIM class NodeConstraintTerm (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.constraint_term import (
    ConstraintTerm,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node import (
        MktConnectivityNode,
    )


class NodeConstraintTerm(ConstraintTerm):
    """To be used only to constrain a quantity that cannot be associated with a terminal. For
    example, a registered generating unit that is not electrically connected to the network."""

    __slots__ = ("_mkt_connectivity_node",)

    mkt_connectivity_node: One[MktConnectivityNode] = One(
        EndMeta(
            name="mkt_connectivity_node",
            cim_role="MktConnectivityNode",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node:MktConnectivityNode",
            many=False,
            lower=1,
            upper=1,
            inverse="node_constraint_term",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NodeConstraintTerm",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{76D61CB8-3AC6-4380-912C-3A7D776DC872}",
        ends=(mkt_connectivity_node.meta,),
    )

    def __init__(
        self,
        *,
        mkt_connectivity_node: MktConnectivityNode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if mkt_connectivity_node is not None:
            self.mkt_connectivity_node = mkt_connectivity_node
