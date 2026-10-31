"""CIM class LossSensitivity (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node import (
        MktConnectivityNode,
    )


class LossSensitivity(MarketFactors):
    """Loss sensitivity applied to a ConnectivityNode for a given time interval."""

    __slots__ = ("_mkt_connectivity_node", "loss_factor")

    loss_factor: float | None

    mkt_connectivity_node: One[MktConnectivityNode] = One(
        EndMeta(
            name="mkt_connectivity_node",
            cim_role="MktConnectivityNode",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node:MktConnectivityNode",
            many=False,
            lower=1,
            upper=1,
            inverse="loss_penalty_factor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LossSensitivity",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{E66C89D9-F387-4ef0-BF87-81874BCEB6CD}",
        attributes=(AttrMeta("loss_factor", "lossFactor", "float", 0, 1, "primitive"),),
        ends=(mkt_connectivity_node.meta,),
    )

    def __init__(
        self,
        *,
        loss_factor: float | None = None,
        mkt_connectivity_node: MktConnectivityNode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.loss_factor = loss_factor
        if mkt_connectivity_node is not None:
            self.mkt_connectivity_node = mkt_connectivity_node
