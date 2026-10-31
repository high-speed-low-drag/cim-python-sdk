"""CIM class CnodeDistributionFactor (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node import (
        MktConnectivityNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
        AggregateNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class CnodeDistributionFactor(IdentifiedObject):
    """Participation factors per Cnode. Used to calculate "participation" of Cnode in an
    AggregateNode. Each Cnode associated to an AggregateNode would be assigned a
    participation factor for its participation within the AggregateNode."""

    __slots__ = (
        "_aggregate_node",
        "_host_control_area",
        "_mkt_connectivity_node",
        "_sub_control_area",
        "factor",
        "pod_loss_factor",
    )

    factor: float | None
    pod_loss_factor: float | None

    mkt_connectivity_node: One[MktConnectivityNode] = One(
        EndMeta(
            name="mkt_connectivity_node",
            cim_role="MktConnectivityNode",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node:MktConnectivityNode",
            many=False,
            lower=1,
            upper=1,
            inverse="cnode_distribution_factor",
            aggregation="none",
        )
    )
    host_control_area: One[HostControlArea] = One(
        EndMeta(
            name="host_control_area",
            cim_role="HostControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="cnode_distribution_factor",
            aggregation="none",
        )
    )
    aggregate_node: One[AggregateNode] = One(
        EndMeta(
            name="aggregate_node",
            cim_role="AggregateNode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node:AggregateNode",
            many=False,
            lower=0,
            upper=1,
            inverse="cnode_distribution_factor",
            aggregation="none",
        )
    )
    sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="cnode_distribution_factor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CnodeDistributionFactor",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{75C2DA55-16A0-4a0f-877B-84D86388AE49}",
        attributes=(
            AttrMeta("factor", "factor", "float", 0, 1, "primitive"),
            AttrMeta("pod_loss_factor", "podLossFactor", "float", 0, 1, "primitive"),
        ),
        ends=(
            mkt_connectivity_node.meta,
            host_control_area.meta,
            aggregate_node.meta,
            sub_control_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        factor: float | None = None,
        pod_loss_factor: float | None = None,
        mkt_connectivity_node: MktConnectivityNode | None = None,
        host_control_area: HostControlArea | None = None,
        aggregate_node: AggregateNode | None = None,
        sub_control_area: SubControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.factor = factor
        self.pod_loss_factor = pod_loss_factor
        if mkt_connectivity_node is not None:
            self.mkt_connectivity_node = mkt_connectivity_node
        if host_control_area is not None:
            self.host_control_area = host_control_area
        if aggregate_node is not None:
            self.aggregate_node = aggregate_node
        if sub_control_area is not None:
            self.sub_control_area = sub_control_area
