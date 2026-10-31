"""CIM class MktConnectivityNode (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.connectivity_node import ConnectivityNode

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.loss_sensitivity import (
        LossSensitivity,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.node_constraint_term import (
        NodeConstraintTerm,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.sys_load_distribution_factor import (
        SysLoadDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.cnode_distribution_factor import (
        CnodeDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.individual_pnode import (
        IndividualPnode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class MktConnectivityNode(ConnectivityNode):
    """Subclass of IEC61970:Topology:ConnectivityNode."""

    __slots__ = (
        "_cnode_distribution_factor",
        "_individual_pnode",
        "_loss_penalty_factor",
        "_node_constraint_term",
        "_registered_resource",
        "_rto",
        "_sys_load_distribu_factor",
    )

    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_connectivity_node",
            aggregation="none",
        )
    )
    individual_pnode: One[IndividualPnode] = One(
        EndMeta(
            name="individual_pnode",
            cim_role="IndividualPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.individual_pnode:IndividualPnode",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_connectivity_node",
            aggregation="none",
        )
    )
    cnode_distribution_factor: Many[CnodeDistributionFactor] = Many(
        EndMeta(
            name="cnode_distribution_factor",
            cim_role="CnodeDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.cnode_distribution_factor:CnodeDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_connectivity_node",
            aggregation="none",
        )
    )
    loss_penalty_factor: Many[LossSensitivity] = Many(
        EndMeta(
            name="loss_penalty_factor",
            cim_role="LossPenaltyFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.loss_sensitivity:LossSensitivity",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_connectivity_node",
            aggregation="none",
        )
    )
    sys_load_distribu_factor: One[SysLoadDistributionFactor] = One(
        EndMeta(
            name="sys_load_distribu_factor",
            cim_role="SysLoadDistribuFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.sys_load_distribution_factor:SysLoadDistributionFactor",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_connectivity_node",
            aggregation="none",
        )
    )
    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=1,
            upper=1,
            inverse="mkt_connectivity_node",
            aggregation="none",
        )
    )
    node_constraint_term: Many[NodeConstraintTerm] = Many(
        EndMeta(
            name="node_constraint_term",
            cim_role="NodeConstraintTerm",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.node_constraint_term:NodeConstraintTerm",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_connectivity_node",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktConnectivityNode",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{C1B50235-BB57-46b1-8156-D728B377DB02}",
        ends=(
            registered_resource.meta,
            individual_pnode.meta,
            cnode_distribution_factor.meta,
            loss_penalty_factor.meta,
            sys_load_distribu_factor.meta,
            rto.meta,
            node_constraint_term.meta,
        ),
    )

    def __init__(
        self,
        *,
        registered_resource: Iterable[RegisteredResource] | None = None,
        individual_pnode: IndividualPnode | None = None,
        cnode_distribution_factor: Iterable[CnodeDistributionFactor] | None = None,
        loss_penalty_factor: Iterable[LossSensitivity] | None = None,
        sys_load_distribu_factor: SysLoadDistributionFactor | None = None,
        rto: RTO | None = None,
        node_constraint_term: Iterable[NodeConstraintTerm] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if registered_resource is not None:
            MktConnectivityNode.registered_resource.extend(self, registered_resource)
        if individual_pnode is not None:
            self.individual_pnode = individual_pnode
        if cnode_distribution_factor is not None:
            MktConnectivityNode.cnode_distribution_factor.extend(self, cnode_distribution_factor)
        if loss_penalty_factor is not None:
            MktConnectivityNode.loss_penalty_factor.extend(self, loss_penalty_factor)
        if sys_load_distribu_factor is not None:
            self.sys_load_distribu_factor = sys_load_distribu_factor
        if rto is not None:
            self.rto = rto
        if node_constraint_term is not None:
            MktConnectivityNode.node_constraint_term.extend(self, node_constraint_term)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return MktConnectivityNode.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return MktConnectivityNode.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return MktConnectivityNode.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return MktConnectivityNode.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return MktConnectivityNode.registered_resource.get_by_mrid(self, mrid)

    def add_cnode_distribution_factor(
        self, cnode_distribution_factor: CnodeDistributionFactor
    ) -> Self:
        return MktConnectivityNode.cnode_distribution_factor.add(self, cnode_distribution_factor)

    def remove_cnode_distribution_factor(
        self, cnode_distribution_factor: CnodeDistributionFactor
    ) -> Self:
        return MktConnectivityNode.cnode_distribution_factor.remove(self, cnode_distribution_factor)

    def clear_cnode_distribution_factor(self) -> Self:
        return MktConnectivityNode.cnode_distribution_factor.clear(self)

    def num_cnode_distribution_factor(self) -> int:
        return MktConnectivityNode.cnode_distribution_factor.count(self)

    def get_cnode_distribution_factor_by_mrid(self, mrid: str) -> CnodeDistributionFactor | None:
        return MktConnectivityNode.cnode_distribution_factor.get_by_mrid(self, mrid)

    def add_loss_penalty_factor(self, loss_penalty_factor: LossSensitivity) -> Self:
        return MktConnectivityNode.loss_penalty_factor.add(self, loss_penalty_factor)

    def remove_loss_penalty_factor(self, loss_penalty_factor: LossSensitivity) -> Self:
        return MktConnectivityNode.loss_penalty_factor.remove(self, loss_penalty_factor)

    def clear_loss_penalty_factor(self) -> Self:
        return MktConnectivityNode.loss_penalty_factor.clear(self)

    def num_loss_penalty_factor(self) -> int:
        return MktConnectivityNode.loss_penalty_factor.count(self)

    def get_loss_penalty_factor_by_mrid(self, mrid: str) -> LossSensitivity | None:
        return MktConnectivityNode.loss_penalty_factor.get_by_mrid(self, mrid)

    def add_node_constraint_term(self, node_constraint_term: NodeConstraintTerm) -> Self:
        return MktConnectivityNode.node_constraint_term.add(self, node_constraint_term)

    def remove_node_constraint_term(self, node_constraint_term: NodeConstraintTerm) -> Self:
        return MktConnectivityNode.node_constraint_term.remove(self, node_constraint_term)

    def clear_node_constraint_term(self) -> Self:
        return MktConnectivityNode.node_constraint_term.clear(self)

    def num_node_constraint_term(self) -> int:
        return MktConnectivityNode.node_constraint_term.count(self)

    def get_node_constraint_term_by_mrid(self, mrid: str) -> NodeConstraintTerm | None:
        return MktConnectivityNode.node_constraint_term.get_by_mrid(self, mrid)
