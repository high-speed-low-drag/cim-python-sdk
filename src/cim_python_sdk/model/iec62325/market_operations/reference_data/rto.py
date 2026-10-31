"""CIM class RTO (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_common.market_participant import MarketParticipant

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.resource_group_req import (
        ResourceGroupReq,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node import (
        MktConnectivityNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.commodity_definition import (
        CommodityDefinition,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.energy_market import (
        EnergyMarket,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraint_sum import (
        SecurityConstraintSum,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraints import (
        SecurityConstraints,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.adjacent_ca_set import (
        AdjacentCASet,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
        AggregateNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right import (
        ContractRight,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_region import (
        FuelRegion,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.local_reliability_area import (
        LocalReliabilityArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mss_aggregation import (
        MSSAggregation,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.transmission_right_chain import (
        TransmissionRightChain,
    )


class RTO(MarketParticipant):
    """Regional transmission operator."""

    __slots__ = (
        "_adjacent_ca_set",
        "_aggregate_node",
        "_commodity_definition",
        "_energy_markets",
        "_fuel_region",
        "_host_control_area",
        "_local_reliability_area",
        "_mkt_connectivity_node",
        "_mss_aggregation",
        "_pnodes",
        "_resource_group_reqs",
        "_security_constraints",
        "_security_constraints_linear",
        "_sub_control_area",
        "_transmission_contract_right",
        "_transmission_right_chain",
    )

    resource_group_reqs: Many[ResourceGroupReq] = Many(
        EndMeta(
            name="resource_group_reqs",
            cim_role="ResourceGroupReqs",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.resource_group_req:ResourceGroupReq",
            many=True,
            lower=0,
            upper=None,
            inverse="rtos",
            aggregation="none",
        )
    )
    transmission_right_chain: Many[TransmissionRightChain] = Many(
        EndMeta(
            name="transmission_right_chain",
            cim_role="TransmissionRightChain",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.transmission_right_chain:TransmissionRightChain",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    pnodes: Many[Pnode] = Many(
        EndMeta(
            name="pnodes",
            cim_role="Pnodes",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    mss_aggregation: Many[MSSAggregation] = Many(
        EndMeta(
            name="mss_aggregation",
            cim_role="MSSAggregation",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mss_aggregation:MSSAggregation",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    host_control_area: Many[HostControlArea] = Many(
        EndMeta(
            name="host_control_area",
            cim_role="HostControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    energy_markets: Many[EnergyMarket] = Many(
        EndMeta(
            name="energy_markets",
            cim_role="EnergyMarkets",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.energy_market:EnergyMarket",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    security_constraints_linear: Many[SecurityConstraintSum] = Many(
        EndMeta(
            name="security_constraints_linear",
            cim_role="SecurityConstraintsLinear",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraint_sum:SecurityConstraintSum",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    aggregate_node: Many[AggregateNode] = Many(
        EndMeta(
            name="aggregate_node",
            cim_role="AggregateNode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node:AggregateNode",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    commodity_definition: Many[CommodityDefinition] = Many(
        EndMeta(
            name="commodity_definition",
            cim_role="CommodityDefinition",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.commodity_definition:CommodityDefinition",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    transmission_contract_right: Many[ContractRight] = Many(
        EndMeta(
            name="transmission_contract_right",
            cim_role="TransmissionContractRight",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right:ContractRight",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    security_constraints: Many[SecurityConstraints] = Many(
        EndMeta(
            name="security_constraints",
            cim_role="SecurityConstraints",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraints:SecurityConstraints",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    sub_control_area: Many[SubControlArea] = Many(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    fuel_region: Many[FuelRegion] = Many(
        EndMeta(
            name="fuel_region",
            cim_role="FuelRegion",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_region:FuelRegion",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    mkt_connectivity_node: Many[MktConnectivityNode] = Many(
        EndMeta(
            name="mkt_connectivity_node",
            cim_role="MktConnectivityNode",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node:MktConnectivityNode",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    local_reliability_area: Many[LocalReliabilityArea] = Many(
        EndMeta(
            name="local_reliability_area",
            cim_role="LocalReliabilityArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.local_reliability_area:LocalReliabilityArea",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )
    adjacent_ca_set: Many[AdjacentCASet] = Many(
        EndMeta(
            name="adjacent_ca_set",
            cim_role="AdjacentCASet",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.adjacent_ca_set:AdjacentCASet",
            many=True,
            lower=0,
            upper=None,
            inverse="rto",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RTO",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{1E0CABAF-4ABF-4934-9F92-F65A765A8A0A}",
        ends=(
            resource_group_reqs.meta,
            transmission_right_chain.meta,
            pnodes.meta,
            mss_aggregation.meta,
            host_control_area.meta,
            energy_markets.meta,
            security_constraints_linear.meta,
            aggregate_node.meta,
            commodity_definition.meta,
            transmission_contract_right.meta,
            security_constraints.meta,
            sub_control_area.meta,
            fuel_region.meta,
            mkt_connectivity_node.meta,
            local_reliability_area.meta,
            adjacent_ca_set.meta,
        ),
    )

    def __init__(
        self,
        *,
        resource_group_reqs: Iterable[ResourceGroupReq] | None = None,
        transmission_right_chain: Iterable[TransmissionRightChain] | None = None,
        pnodes: Iterable[Pnode] | None = None,
        mss_aggregation: Iterable[MSSAggregation] | None = None,
        host_control_area: Iterable[HostControlArea] | None = None,
        energy_markets: Iterable[EnergyMarket] | None = None,
        security_constraints_linear: Iterable[SecurityConstraintSum] | None = None,
        aggregate_node: Iterable[AggregateNode] | None = None,
        commodity_definition: Iterable[CommodityDefinition] | None = None,
        transmission_contract_right: Iterable[ContractRight] | None = None,
        security_constraints: Iterable[SecurityConstraints] | None = None,
        sub_control_area: Iterable[SubControlArea] | None = None,
        fuel_region: Iterable[FuelRegion] | None = None,
        mkt_connectivity_node: Iterable[MktConnectivityNode] | None = None,
        local_reliability_area: Iterable[LocalReliabilityArea] | None = None,
        adjacent_ca_set: Iterable[AdjacentCASet] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if resource_group_reqs is not None:
            RTO.resource_group_reqs.extend(self, resource_group_reqs)
        if transmission_right_chain is not None:
            RTO.transmission_right_chain.extend(self, transmission_right_chain)
        if pnodes is not None:
            RTO.pnodes.extend(self, pnodes)
        if mss_aggregation is not None:
            RTO.mss_aggregation.extend(self, mss_aggregation)
        if host_control_area is not None:
            RTO.host_control_area.extend(self, host_control_area)
        if energy_markets is not None:
            RTO.energy_markets.extend(self, energy_markets)
        if security_constraints_linear is not None:
            RTO.security_constraints_linear.extend(self, security_constraints_linear)
        if aggregate_node is not None:
            RTO.aggregate_node.extend(self, aggregate_node)
        if commodity_definition is not None:
            RTO.commodity_definition.extend(self, commodity_definition)
        if transmission_contract_right is not None:
            RTO.transmission_contract_right.extend(self, transmission_contract_right)
        if security_constraints is not None:
            RTO.security_constraints.extend(self, security_constraints)
        if sub_control_area is not None:
            RTO.sub_control_area.extend(self, sub_control_area)
        if fuel_region is not None:
            RTO.fuel_region.extend(self, fuel_region)
        if mkt_connectivity_node is not None:
            RTO.mkt_connectivity_node.extend(self, mkt_connectivity_node)
        if local_reliability_area is not None:
            RTO.local_reliability_area.extend(self, local_reliability_area)
        if adjacent_ca_set is not None:
            RTO.adjacent_ca_set.extend(self, adjacent_ca_set)

    def add_resource_group_req(self, resource_group_req: ResourceGroupReq) -> Self:
        return RTO.resource_group_reqs.add(self, resource_group_req)

    def remove_resource_group_req(self, resource_group_req: ResourceGroupReq) -> Self:
        return RTO.resource_group_reqs.remove(self, resource_group_req)

    def clear_resource_group_reqs(self) -> Self:
        return RTO.resource_group_reqs.clear(self)

    def num_resource_group_req(self) -> int:
        return RTO.resource_group_reqs.count(self)

    def get_resource_group_req_by_mrid(self, mrid: str) -> ResourceGroupReq | None:
        return RTO.resource_group_reqs.get_by_mrid(self, mrid)

    def add_transmission_right_chain(
        self, transmission_right_chain: TransmissionRightChain
    ) -> Self:
        return RTO.transmission_right_chain.add(self, transmission_right_chain)

    def remove_transmission_right_chain(
        self, transmission_right_chain: TransmissionRightChain
    ) -> Self:
        return RTO.transmission_right_chain.remove(self, transmission_right_chain)

    def clear_transmission_right_chain(self) -> Self:
        return RTO.transmission_right_chain.clear(self)

    def num_transmission_right_chain(self) -> int:
        return RTO.transmission_right_chain.count(self)

    def get_transmission_right_chain_by_mrid(self, mrid: str) -> TransmissionRightChain | None:
        return RTO.transmission_right_chain.get_by_mrid(self, mrid)

    def add_pnode(self, pnode: Pnode) -> Self:
        return RTO.pnodes.add(self, pnode)

    def remove_pnode(self, pnode: Pnode) -> Self:
        return RTO.pnodes.remove(self, pnode)

    def clear_pnodes(self) -> Self:
        return RTO.pnodes.clear(self)

    def num_pnode(self) -> int:
        return RTO.pnodes.count(self)

    def get_pnode_by_mrid(self, mrid: str) -> Pnode | None:
        return RTO.pnodes.get_by_mrid(self, mrid)

    def add_mss_aggregation(self, mss_aggregation: MSSAggregation) -> Self:
        return RTO.mss_aggregation.add(self, mss_aggregation)

    def remove_mss_aggregation(self, mss_aggregation: MSSAggregation) -> Self:
        return RTO.mss_aggregation.remove(self, mss_aggregation)

    def clear_mss_aggregation(self) -> Self:
        return RTO.mss_aggregation.clear(self)

    def num_mss_aggregation(self) -> int:
        return RTO.mss_aggregation.count(self)

    def get_mss_aggregation_by_mrid(self, mrid: str) -> MSSAggregation | None:
        return RTO.mss_aggregation.get_by_mrid(self, mrid)

    def add_host_control_area(self, host_control_area: HostControlArea) -> Self:
        return RTO.host_control_area.add(self, host_control_area)

    def remove_host_control_area(self, host_control_area: HostControlArea) -> Self:
        return RTO.host_control_area.remove(self, host_control_area)

    def clear_host_control_area(self) -> Self:
        return RTO.host_control_area.clear(self)

    def num_host_control_area(self) -> int:
        return RTO.host_control_area.count(self)

    def get_host_control_area_by_mrid(self, mrid: str) -> HostControlArea | None:
        return RTO.host_control_area.get_by_mrid(self, mrid)

    def add_energy_market(self, energy_market: EnergyMarket) -> Self:
        return RTO.energy_markets.add(self, energy_market)

    def remove_energy_market(self, energy_market: EnergyMarket) -> Self:
        return RTO.energy_markets.remove(self, energy_market)

    def clear_energy_markets(self) -> Self:
        return RTO.energy_markets.clear(self)

    def num_energy_market(self) -> int:
        return RTO.energy_markets.count(self)

    def get_energy_market_by_mrid(self, mrid: str) -> EnergyMarket | None:
        return RTO.energy_markets.get_by_mrid(self, mrid)

    def add_security_constraints_linear(
        self, security_constraints_linear: SecurityConstraintSum
    ) -> Self:
        return RTO.security_constraints_linear.add(self, security_constraints_linear)

    def remove_security_constraints_linear(
        self, security_constraints_linear: SecurityConstraintSum
    ) -> Self:
        return RTO.security_constraints_linear.remove(self, security_constraints_linear)

    def clear_security_constraints_linear(self) -> Self:
        return RTO.security_constraints_linear.clear(self)

    def num_security_constraints_linear(self) -> int:
        return RTO.security_constraints_linear.count(self)

    def get_security_constraints_linear_by_mrid(self, mrid: str) -> SecurityConstraintSum | None:
        return RTO.security_constraints_linear.get_by_mrid(self, mrid)

    def add_aggregate_node(self, aggregate_node: AggregateNode) -> Self:
        return RTO.aggregate_node.add(self, aggregate_node)

    def remove_aggregate_node(self, aggregate_node: AggregateNode) -> Self:
        return RTO.aggregate_node.remove(self, aggregate_node)

    def clear_aggregate_node(self) -> Self:
        return RTO.aggregate_node.clear(self)

    def num_aggregate_node(self) -> int:
        return RTO.aggregate_node.count(self)

    def get_aggregate_node_by_mrid(self, mrid: str) -> AggregateNode | None:
        return RTO.aggregate_node.get_by_mrid(self, mrid)

    def add_commodity_definition(self, commodity_definition: CommodityDefinition) -> Self:
        return RTO.commodity_definition.add(self, commodity_definition)

    def remove_commodity_definition(self, commodity_definition: CommodityDefinition) -> Self:
        return RTO.commodity_definition.remove(self, commodity_definition)

    def clear_commodity_definition(self) -> Self:
        return RTO.commodity_definition.clear(self)

    def num_commodity_definition(self) -> int:
        return RTO.commodity_definition.count(self)

    def get_commodity_definition_by_mrid(self, mrid: str) -> CommodityDefinition | None:
        return RTO.commodity_definition.get_by_mrid(self, mrid)

    def add_transmission_contract_right(self, transmission_contract_right: ContractRight) -> Self:
        return RTO.transmission_contract_right.add(self, transmission_contract_right)

    def remove_transmission_contract_right(
        self, transmission_contract_right: ContractRight
    ) -> Self:
        return RTO.transmission_contract_right.remove(self, transmission_contract_right)

    def clear_transmission_contract_right(self) -> Self:
        return RTO.transmission_contract_right.clear(self)

    def num_transmission_contract_right(self) -> int:
        return RTO.transmission_contract_right.count(self)

    def get_transmission_contract_right_by_mrid(self, mrid: str) -> ContractRight | None:
        return RTO.transmission_contract_right.get_by_mrid(self, mrid)

    def add_security_constraint(self, security_constraint: SecurityConstraints) -> Self:
        return RTO.security_constraints.add(self, security_constraint)

    def remove_security_constraint(self, security_constraint: SecurityConstraints) -> Self:
        return RTO.security_constraints.remove(self, security_constraint)

    def clear_security_constraints(self) -> Self:
        return RTO.security_constraints.clear(self)

    def num_security_constraint(self) -> int:
        return RTO.security_constraints.count(self)

    def get_security_constraint_by_mrid(self, mrid: str) -> SecurityConstraints | None:
        return RTO.security_constraints.get_by_mrid(self, mrid)

    def add_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return RTO.sub_control_area.add(self, sub_control_area)

    def remove_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return RTO.sub_control_area.remove(self, sub_control_area)

    def clear_sub_control_area(self) -> Self:
        return RTO.sub_control_area.clear(self)

    def num_sub_control_area(self) -> int:
        return RTO.sub_control_area.count(self)

    def get_sub_control_area_by_mrid(self, mrid: str) -> SubControlArea | None:
        return RTO.sub_control_area.get_by_mrid(self, mrid)

    def add_fuel_region(self, fuel_region: FuelRegion) -> Self:
        return RTO.fuel_region.add(self, fuel_region)

    def remove_fuel_region(self, fuel_region: FuelRegion) -> Self:
        return RTO.fuel_region.remove(self, fuel_region)

    def clear_fuel_region(self) -> Self:
        return RTO.fuel_region.clear(self)

    def num_fuel_region(self) -> int:
        return RTO.fuel_region.count(self)

    def get_fuel_region_by_mrid(self, mrid: str) -> FuelRegion | None:
        return RTO.fuel_region.get_by_mrid(self, mrid)

    def add_mkt_connectivity_node(self, mkt_connectivity_node: MktConnectivityNode) -> Self:
        return RTO.mkt_connectivity_node.add(self, mkt_connectivity_node)

    def remove_mkt_connectivity_node(self, mkt_connectivity_node: MktConnectivityNode) -> Self:
        return RTO.mkt_connectivity_node.remove(self, mkt_connectivity_node)

    def clear_mkt_connectivity_node(self) -> Self:
        return RTO.mkt_connectivity_node.clear(self)

    def num_mkt_connectivity_node(self) -> int:
        return RTO.mkt_connectivity_node.count(self)

    def get_mkt_connectivity_node_by_mrid(self, mrid: str) -> MktConnectivityNode | None:
        return RTO.mkt_connectivity_node.get_by_mrid(self, mrid)

    def add_local_reliability_area(self, local_reliability_area: LocalReliabilityArea) -> Self:
        return RTO.local_reliability_area.add(self, local_reliability_area)

    def remove_local_reliability_area(self, local_reliability_area: LocalReliabilityArea) -> Self:
        return RTO.local_reliability_area.remove(self, local_reliability_area)

    def clear_local_reliability_area(self) -> Self:
        return RTO.local_reliability_area.clear(self)

    def num_local_reliability_area(self) -> int:
        return RTO.local_reliability_area.count(self)

    def get_local_reliability_area_by_mrid(self, mrid: str) -> LocalReliabilityArea | None:
        return RTO.local_reliability_area.get_by_mrid(self, mrid)

    def add_adjacent_ca_set(self, adjacent_ca_set: AdjacentCASet) -> Self:
        return RTO.adjacent_ca_set.add(self, adjacent_ca_set)

    def remove_adjacent_ca_set(self, adjacent_ca_set: AdjacentCASet) -> Self:
        return RTO.adjacent_ca_set.remove(self, adjacent_ca_set)

    def clear_adjacent_ca_set(self) -> Self:
        return RTO.adjacent_ca_set.clear(self)

    def num_adjacent_ca_set(self) -> int:
        return RTO.adjacent_ca_set.count(self)

    def get_adjacent_ca_set_by_mrid(self, mrid: str) -> AdjacentCASet | None:
        return RTO.adjacent_ca_set.get_by_mrid(self, mrid)
