"""CIM class RegisteredResource (TC57CIM/IEC62325/MarketCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.resource_group import (
        ResourceGroup,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_market_operations.resource_certification import (
        ResourceCertification,
    )
    from cim_python_sdk.model.iec62325.market_common.market_participant import MarketParticipant
    from cim_python_sdk.model.iec62325.market_common.resource_capacity import ResourceCapacity
    from cim_python_sdk.model.iec62325.market_management.domain import Domain
    from cim_python_sdk.model.iec62325.market_management.market_object_status import (
        MarketObjectStatus,
    )
    from cim_python_sdk.model.iec62325.market_management.reason import Reason
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node import (
        MktConnectivityNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.energy_market import (
        EnergyMarket,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.allocation_result_values import (
        AllocationResultValues,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.expected_energy_values import (
        ExpectedEnergyValues,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.default_bid import (
        DefaultBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.intermittent_resource_eligibility import (
        IntermittentResourceEligibility,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commitments import (
        Commitments,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.dop_instruction import (
        DopInstruction,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.dot_instruction import (
        DotInstruction,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_resource_results import (
        ExPostResourceResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instructions import (
        Instructions,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.load_following_operator_input import (
        LoadFollowingOperatorInput,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_resource_status import (
        MPMResourceStatus,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_instruction import (
        ResourceAwardInstruction,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_dispatch_results import (
        ResourceDispatchResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_load_following_inst import (
        ResourceLoadFollowingInst,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.rmr_operator_input import (
        RMROperatorInput,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ruc_award_instruction import (
        RUCAwardInstruction,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.resource_registration_status import (
        ResourceRegistrationStatus,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.dispatch_inst_reply import (
        DispatchInstReply,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_following_inst import (
        LoadFollowingInst,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.ramp_rate_curve import (
        RampRateCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.adjacent_ca_set import (
        AdjacentCASet,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
        AggregateNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_distribution_factor import (
        ContractDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.control_area_designation import (
        ControlAreaDesignation,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.forbidden_region import (
        ForbiddenRegion,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.former_reference import (
        FormerReference,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_threshold import (
        MPMTestThreshold,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.org_res_ownership import (
        OrgResOwnership,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode
    from cim_python_sdk.model.iec62325.market_operations.reference_data.resource_certification import (
        ResourceCertification as ResourceCertification_dup1,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.resource_verifiable_costs import (
        ResourceVerifiableCosts,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_point import (
        SchedulingPoint,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.substitution_resource_list import (
        SubstitutionResourceList,
    )


class RegisteredResource(PowerSystemResource):
    """A resource that is registered through the market participant registration system.
    Examples include generating unit, load, and non-physical generator or load."""

    __slots__ = (
        "_adjacent_ca_set",
        "_aggregate_node",
        "_allocation_result_values",
        "_commitments",
        "_contract_distribution_factor",
        "_control_area_designation",
        "_default_bid",
        "_dispatch_inst_reply",
        "_domain",
        "_dop_instruction",
        "_dot_instruction",
        "_energy_markets",
        "_ex_post_resource_results",
        "_expected_energy_values",
        "_forbidden_region",
        "_former_reference",
        "_host_control_area",
        "_instructions",
        "_inter_tie",
        "_intermittent_resource_eligibility",
        "_load_following_inst",
        "_load_following_operator_input",
        "_market_object_status",
        "_market_participant",
        "_mkt_connectivity_node",
        "_mpm_resource_status",
        "_mpm_test_threshold",
        "_org_res_ownership",
        "_pnode",
        "_ramp_rate_curve",
        "_reason",
        "_resource_ancillary_service_qualification",
        "_resource_award_instruction",
        "_resource_capacity",
        "_resource_certification",
        "_resource_dispatch_results",
        "_resource_groups",
        "_resource_load_following_inst",
        "_resource_verifiable_costs",
        "_rmr_operator_input",
        "_ruc_award_instruction",
        "_sub_control_area",
        "_substitution_resource_list",
        "_time_series",
        "aca_flag",
        "assp_optimization_flag",
        "commercial_op_date",
        "contingency_avail_flag",
        "dispatchable",
        "eca_flag",
        "flexible_offer_flag",
        "hourly_predispatch",
        "is_aggregated_res",
        "last_modified",
        "lmpm_flag",
        "market_participation_flag",
        "max_base_self_sched_qty",
        "max_on_time",
        "min_dispatch_time",
        "min_off_time",
        "min_on_time",
        "must_offer_flag",
        "non_market",
        "point_of_delivery_flag",
        "price_set_flag_da",
        "price_set_flag_rt",
        "registration_status",
        "resource_adequacy_flag",
        "smpm_flag",
    )

    aca_flag: YesNo | None
    assp_optimization_flag: YesNo | None
    commercial_op_date: _dt.datetime | None
    contingency_avail_flag: YesNo | None
    dispatchable: bool | None
    eca_flag: YesNo | None
    flexible_offer_flag: YesNo | None
    hourly_predispatch: YesNo | None
    is_aggregated_res: YesNo | None
    last_modified: _dt.datetime | None
    lmpm_flag: YesNo | None
    market_participation_flag: YesNo | None
    max_base_self_sched_qty: float | None
    max_on_time: float | None
    min_dispatch_time: float | None  # Hours
    min_off_time: float | None
    min_on_time: float | None
    must_offer_flag: YesNo | None
    non_market: YesNo | None
    point_of_delivery_flag: YesNo | None
    price_set_flag_da: YesNo | None
    price_set_flag_rt: YesNo | None
    registration_status: ResourceRegistrationStatus | None
    resource_adequacy_flag: YesNo | None
    smpm_flag: YesNo | None

    dot_instruction: Many[DotInstruction] = Many(
        EndMeta(
            name="dot_instruction",
            cim_role="DotInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.dot_instruction:DotInstruction",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    dop_instruction: Many[DopInstruction] = Many(
        EndMeta(
            name="dop_instruction",
            cim_role="DopInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.dop_instruction:DopInstruction",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resouce",
            aggregation="none",
        )
    )
    resource_groups: Many[ResourceGroup] = Many(
        EndMeta(
            name="resource_groups",
            cim_role="ResourceGroups",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.resource_group:ResourceGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resources",
            aggregation="none",
        )
    )
    mkt_connectivity_node: One[MktConnectivityNode] = One(
        EndMeta(
            name="mkt_connectivity_node",
            cim_role="MktConnectivityNode",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node:MktConnectivityNode",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    inter_tie: Many[SchedulingPoint] = Many(
        EndMeta(
            name="inter_tie",
            cim_role="InterTie",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_point:SchedulingPoint",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    resource_certification: Many[ResourceCertification] = Many(
        EndMeta(
            name="resource_certification",
            cim_role="ResourceCertification",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_market_operations.resource_certification:ResourceCertification",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
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
            inverse="registered_resources",
            aggregation="none",
        )
    )
    resource_capacity: Many[ResourceCapacity] = Many(
        EndMeta(
            name="resource_capacity",
            cim_role="ResourceCapacity",
            target="cim_python_sdk.model.iec62325.market_common.resource_capacity:ResourceCapacity",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    reason: Many[Reason] = Many(
        EndMeta(
            name="reason",
            cim_role="Reason",
            target="cim_python_sdk.model.iec62325.market_management.reason:Reason",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    domain: Many[Domain] = Many(
        EndMeta(
            name="domain",
            cim_role="Domain",
            target="cim_python_sdk.model.iec62325.market_management.domain:Domain",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    expected_energy_values: Many[ExpectedEnergyValues] = Many(
        EndMeta(
            name="expected_energy_values",
            cim_role="ExpectedEnergyValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.expected_energy_values:ExpectedEnergyValues",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    resource_ancillary_service_qualification: Many[ResourceCertification_dup1] = Many(
        EndMeta(
            name="resource_ancillary_service_qualification",
            cim_role="ResourceAncillaryServiceQualification",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.resource_certification:ResourceCertification",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    resource_load_following_inst: Many[ResourceLoadFollowingInst] = Many(
        EndMeta(
            name="resource_load_following_inst",
            cim_role="ResourceLoadFollowingInst",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_load_following_inst:ResourceLoadFollowingInst",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    load_following_inst: Many[LoadFollowingInst] = Many(
        EndMeta(
            name="load_following_inst",
            cim_role="LoadFollowingInst",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.load_following_inst:LoadFollowingInst",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
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
            inverse="registered_resource",
            aggregation="none",
        )
    )
    allocation_result_values: Many[AllocationResultValues] = Many(
        EndMeta(
            name="allocation_result_values",
            cim_role="AllocationResultValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.allocation_result_values:AllocationResultValues",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    ruc_award_instruction: Many[RUCAwardInstruction] = Many(
        EndMeta(
            name="ruc_award_instruction",
            cim_role="RUCAwardInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ruc_award_instruction:RUCAwardInstruction",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    mpm_resource_status: Many[MPMResourceStatus] = Many(
        EndMeta(
            name="mpm_resource_status",
            cim_role="MPMResourceStatus",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_resource_status:MPMResourceStatus",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    commitments: Many[Commitments] = Many(
        EndMeta(
            name="commitments",
            cim_role="Commitments",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commitments:Commitments",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    pnode: One[Pnode] = One(
        EndMeta(
            name="pnode",
            cim_role="Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_resources",
            aggregation="none",
        )
    )
    former_reference: Many[FormerReference] = Many(
        EndMeta(
            name="former_reference",
            cim_role="FormerReference",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.former_reference:FormerReference",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    intermittent_resource_eligibility: Many[IntermittentResourceEligibility] = Many(
        EndMeta(
            name="intermittent_resource_eligibility",
            cim_role="IntermittentResourceEligibility",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.intermittent_resource_eligibility:IntermittentResourceEligibility",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    instructions: Many[Instructions] = Many(
        EndMeta(
            name="instructions",
            cim_role="Instructions",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instructions:Instructions",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    market_participant: One[MarketParticipant] = One(
        EndMeta(
            name="market_participant",
            cim_role="MarketParticipant",
            target="cim_python_sdk.model.iec62325.market_common.market_participant:MarketParticipant",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_resource",
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
            inverse="registered_resource",
            aggregation="none",
        )
    )
    adjacent_ca_set: One[AdjacentCASet] = One(
        EndMeta(
            name="adjacent_ca_set",
            cim_role="AdjacentCASet",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.adjacent_ca_set:AdjacentCASet",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    substitution_resource_list: Many[SubstitutionResourceList] = Many(
        EndMeta(
            name="substitution_resource_list",
            cim_role="SubstitutionResourceList",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.substitution_resource_list:SubstitutionResourceList",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    resource_dispatch_results: Many[ResourceDispatchResults] = Many(
        EndMeta(
            name="resource_dispatch_results",
            cim_role="ResourceDispatchResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_dispatch_results:ResourceDispatchResults",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    rmr_operator_input: Many[RMROperatorInput] = Many(
        EndMeta(
            name="rmr_operator_input",
            cim_role="RMROperatorInput",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.rmr_operator_input:RMROperatorInput",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    ex_post_resource_results: Many[ExPostResourceResults] = Many(
        EndMeta(
            name="ex_post_resource_results",
            cim_role="ExPostResourceResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_resource_results:ExPostResourceResults",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    org_res_ownership: Many[OrgResOwnership] = Many(
        EndMeta(
            name="org_res_ownership",
            cim_role="OrgResOwnership",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.org_res_ownership:OrgResOwnership",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    contract_distribution_factor: Many[ContractDistributionFactor] = Many(
        EndMeta(
            name="contract_distribution_factor",
            cim_role="ContractDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_distribution_factor:ContractDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    ramp_rate_curve: Many[RampRateCurve] = Many(
        EndMeta(
            name="ramp_rate_curve",
            cim_role="RampRateCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.ramp_rate_curve:RampRateCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    resource_award_instruction: Many[ResourceAwardInstruction] = Many(
        EndMeta(
            name="resource_award_instruction",
            cim_role="ResourceAwardInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_instruction:ResourceAwardInstruction",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    mpm_test_threshold: Many[MPMTestThreshold] = Many(
        EndMeta(
            name="mpm_test_threshold",
            cim_role="MPMTestThreshold",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_threshold:MPMTestThreshold",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    load_following_operator_input: Many[LoadFollowingOperatorInput] = Many(
        EndMeta(
            name="load_following_operator_input",
            cim_role="LoadFollowingOperatorInput",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.load_following_operator_input:LoadFollowingOperatorInput",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    control_area_designation: Many[ControlAreaDesignation] = Many(
        EndMeta(
            name="control_area_designation",
            cim_role="ControlAreaDesignation",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.control_area_designation:ControlAreaDesignation",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    dispatch_inst_reply: Many[DispatchInstReply] = Many(
        EndMeta(
            name="dispatch_inst_reply",
            cim_role="DispatchInstReply",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.dispatch_inst_reply:DispatchInstReply",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    market_object_status: Many[MarketObjectStatus] = Many(
        EndMeta(
            name="market_object_status",
            cim_role="MarketObjectStatus",
            target="cim_python_sdk.model.iec62325.market_management.market_object_status:MarketObjectStatus",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
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
            inverse="registered_resource",
            aggregation="none",
        )
    )
    default_bid: One[DefaultBid] = One(
        EndMeta(
            name="default_bid",
            cim_role="DefaultBid",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.default_bid:DefaultBid",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    resource_verifiable_costs: One[ResourceVerifiableCosts] = One(
        EndMeta(
            name="resource_verifiable_costs",
            cim_role="ResourceVerifiableCosts",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.resource_verifiable_costs:ResourceVerifiableCosts",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_resource",
            aggregation="none",
        )
    )
    forbidden_region: Many[ForbiddenRegion] = Many(
        EndMeta(
            name="forbidden_region",
            cim_role="ForbiddenRegion",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.forbidden_region:ForbiddenRegion",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_resource",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegisteredResource",
        package="TC57CIM/IEC62325/MarketCommon",
        guid="{920A6CB8-97C1-4c0a-8A7C-C20B85B04F7E}",
        attributes=(
            AttrMeta("aca_flag", "ACAFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "assp_optimization_flag", "ASSPOptimizationFlag", "YesNo", 0, 1, "enumeration"
            ),
            AttrMeta("commercial_op_date", "commercialOpDate", "datetime", 0, 1, "primitive"),
            AttrMeta(
                "contingency_avail_flag", "contingencyAvailFlag", "YesNo", 0, 1, "enumeration"
            ),
            AttrMeta("dispatchable", "dispatchable", "bool", 0, 1, "primitive"),
            AttrMeta("eca_flag", "ECAFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("flexible_offer_flag", "flexibleOfferFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("hourly_predispatch", "hourlyPredispatch", "YesNo", 0, 1, "enumeration"),
            AttrMeta("is_aggregated_res", "isAggregatedRes", "YesNo", 0, 1, "enumeration"),
            AttrMeta("last_modified", "lastModified", "datetime", 0, 1, "primitive"),
            AttrMeta("lmpm_flag", "LMPMFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "market_participation_flag", "marketParticipationFlag", "YesNo", 0, 1, "enumeration"
            ),
            AttrMeta("max_base_self_sched_qty", "maxBaseSelfSchedQty", "float", 0, 1, "primitive"),
            AttrMeta("max_on_time", "maxOnTime", "float", 0, 1, "primitive"),
            AttrMeta("min_dispatch_time", "minDispatchTime", "Hours", 0, 1, "cimdatatype"),
            AttrMeta("min_off_time", "minOffTime", "float", 0, 1, "primitive"),
            AttrMeta("min_on_time", "minOnTime", "float", 0, 1, "primitive"),
            AttrMeta("must_offer_flag", "mustOfferFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("non_market", "nonMarket", "YesNo", 0, 1, "enumeration"),
            AttrMeta("point_of_delivery_flag", "pointOfDeliveryFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("price_set_flag_da", "priceSetFlagDA", "YesNo", 0, 1, "enumeration"),
            AttrMeta("price_set_flag_rt", "priceSetFlagRT", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "registration_status",
                "registrationStatus",
                "ResourceRegistrationStatus",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "resource_adequacy_flag", "resourceAdequacyFlag", "YesNo", 0, 1, "enumeration"
            ),
            AttrMeta("smpm_flag", "SMPMFlag", "YesNo", 0, 1, "enumeration"),
        ),
        ends=(
            dot_instruction.meta,
            dop_instruction.meta,
            resource_groups.meta,
            mkt_connectivity_node.meta,
            inter_tie.meta,
            resource_certification.meta,
            energy_markets.meta,
            resource_capacity.meta,
            reason.meta,
            domain.meta,
            expected_energy_values.meta,
            resource_ancillary_service_qualification.meta,
            resource_load_following_inst.meta,
            load_following_inst.meta,
            host_control_area.meta,
            allocation_result_values.meta,
            ruc_award_instruction.meta,
            mpm_resource_status.meta,
            commitments.meta,
            pnode.meta,
            former_reference.meta,
            intermittent_resource_eligibility.meta,
            instructions.meta,
            market_participant.meta,
            sub_control_area.meta,
            adjacent_ca_set.meta,
            substitution_resource_list.meta,
            resource_dispatch_results.meta,
            rmr_operator_input.meta,
            ex_post_resource_results.meta,
            org_res_ownership.meta,
            contract_distribution_factor.meta,
            ramp_rate_curve.meta,
            resource_award_instruction.meta,
            mpm_test_threshold.meta,
            load_following_operator_input.meta,
            time_series.meta,
            control_area_designation.meta,
            dispatch_inst_reply.meta,
            market_object_status.meta,
            aggregate_node.meta,
            default_bid.meta,
            resource_verifiable_costs.meta,
            forbidden_region.meta,
        ),
    )

    def __init__(
        self,
        *,
        aca_flag: YesNo | None = None,
        assp_optimization_flag: YesNo | None = None,
        commercial_op_date: _dt.datetime | None = None,
        contingency_avail_flag: YesNo | None = None,
        dispatchable: bool | None = None,
        eca_flag: YesNo | None = None,
        flexible_offer_flag: YesNo | None = None,
        hourly_predispatch: YesNo | None = None,
        is_aggregated_res: YesNo | None = None,
        last_modified: _dt.datetime | None = None,
        lmpm_flag: YesNo | None = None,
        market_participation_flag: YesNo | None = None,
        max_base_self_sched_qty: float | None = None,
        max_on_time: float | None = None,
        min_dispatch_time: float | None = None,
        min_off_time: float | None = None,
        min_on_time: float | None = None,
        must_offer_flag: YesNo | None = None,
        non_market: YesNo | None = None,
        point_of_delivery_flag: YesNo | None = None,
        price_set_flag_da: YesNo | None = None,
        price_set_flag_rt: YesNo | None = None,
        registration_status: ResourceRegistrationStatus | None = None,
        resource_adequacy_flag: YesNo | None = None,
        smpm_flag: YesNo | None = None,
        dot_instruction: Iterable[DotInstruction] | None = None,
        dop_instruction: Iterable[DopInstruction] | None = None,
        resource_groups: Iterable[ResourceGroup] | None = None,
        mkt_connectivity_node: MktConnectivityNode | None = None,
        inter_tie: Iterable[SchedulingPoint] | None = None,
        resource_certification: Iterable[ResourceCertification] | None = None,
        energy_markets: Iterable[EnergyMarket] | None = None,
        resource_capacity: Iterable[ResourceCapacity] | None = None,
        reason: Iterable[Reason] | None = None,
        domain: Iterable[Domain] | None = None,
        expected_energy_values: Iterable[ExpectedEnergyValues] | None = None,
        resource_ancillary_service_qualification: Iterable[ResourceCertification_dup1]
        | None = None,
        resource_load_following_inst: Iterable[ResourceLoadFollowingInst] | None = None,
        load_following_inst: Iterable[LoadFollowingInst] | None = None,
        host_control_area: HostControlArea | None = None,
        allocation_result_values: Iterable[AllocationResultValues] | None = None,
        ruc_award_instruction: Iterable[RUCAwardInstruction] | None = None,
        mpm_resource_status: Iterable[MPMResourceStatus] | None = None,
        commitments: Iterable[Commitments] | None = None,
        pnode: Pnode | None = None,
        former_reference: Iterable[FormerReference] | None = None,
        intermittent_resource_eligibility: Iterable[IntermittentResourceEligibility] | None = None,
        instructions: Iterable[Instructions] | None = None,
        market_participant: MarketParticipant | None = None,
        sub_control_area: Iterable[SubControlArea] | None = None,
        adjacent_ca_set: AdjacentCASet | None = None,
        substitution_resource_list: Iterable[SubstitutionResourceList] | None = None,
        resource_dispatch_results: Iterable[ResourceDispatchResults] | None = None,
        rmr_operator_input: Iterable[RMROperatorInput] | None = None,
        ex_post_resource_results: Iterable[ExPostResourceResults] | None = None,
        org_res_ownership: Iterable[OrgResOwnership] | None = None,
        contract_distribution_factor: Iterable[ContractDistributionFactor] | None = None,
        ramp_rate_curve: Iterable[RampRateCurve] | None = None,
        resource_award_instruction: Iterable[ResourceAwardInstruction] | None = None,
        mpm_test_threshold: Iterable[MPMTestThreshold] | None = None,
        load_following_operator_input: Iterable[LoadFollowingOperatorInput] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        control_area_designation: Iterable[ControlAreaDesignation] | None = None,
        dispatch_inst_reply: Iterable[DispatchInstReply] | None = None,
        market_object_status: Iterable[MarketObjectStatus] | None = None,
        aggregate_node: AggregateNode | None = None,
        default_bid: DefaultBid | None = None,
        resource_verifiable_costs: ResourceVerifiableCosts | None = None,
        forbidden_region: Iterable[ForbiddenRegion] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.aca_flag = aca_flag
        self.assp_optimization_flag = assp_optimization_flag
        self.commercial_op_date = commercial_op_date
        self.contingency_avail_flag = contingency_avail_flag
        self.dispatchable = dispatchable
        self.eca_flag = eca_flag
        self.flexible_offer_flag = flexible_offer_flag
        self.hourly_predispatch = hourly_predispatch
        self.is_aggregated_res = is_aggregated_res
        self.last_modified = last_modified
        self.lmpm_flag = lmpm_flag
        self.market_participation_flag = market_participation_flag
        self.max_base_self_sched_qty = max_base_self_sched_qty
        self.max_on_time = max_on_time
        self.min_dispatch_time = min_dispatch_time
        self.min_off_time = min_off_time
        self.min_on_time = min_on_time
        self.must_offer_flag = must_offer_flag
        self.non_market = non_market
        self.point_of_delivery_flag = point_of_delivery_flag
        self.price_set_flag_da = price_set_flag_da
        self.price_set_flag_rt = price_set_flag_rt
        self.registration_status = registration_status
        self.resource_adequacy_flag = resource_adequacy_flag
        self.smpm_flag = smpm_flag
        if dot_instruction is not None:
            RegisteredResource.dot_instruction.extend(self, dot_instruction)
        if dop_instruction is not None:
            RegisteredResource.dop_instruction.extend(self, dop_instruction)
        if resource_groups is not None:
            RegisteredResource.resource_groups.extend(self, resource_groups)
        if mkt_connectivity_node is not None:
            self.mkt_connectivity_node = mkt_connectivity_node
        if inter_tie is not None:
            RegisteredResource.inter_tie.extend(self, inter_tie)
        if resource_certification is not None:
            RegisteredResource.resource_certification.extend(self, resource_certification)
        if energy_markets is not None:
            RegisteredResource.energy_markets.extend(self, energy_markets)
        if resource_capacity is not None:
            RegisteredResource.resource_capacity.extend(self, resource_capacity)
        if reason is not None:
            RegisteredResource.reason.extend(self, reason)
        if domain is not None:
            RegisteredResource.domain.extend(self, domain)
        if expected_energy_values is not None:
            RegisteredResource.expected_energy_values.extend(self, expected_energy_values)
        if resource_ancillary_service_qualification is not None:
            RegisteredResource.resource_ancillary_service_qualification.extend(
                self, resource_ancillary_service_qualification
            )
        if resource_load_following_inst is not None:
            RegisteredResource.resource_load_following_inst.extend(
                self, resource_load_following_inst
            )
        if load_following_inst is not None:
            RegisteredResource.load_following_inst.extend(self, load_following_inst)
        if host_control_area is not None:
            self.host_control_area = host_control_area
        if allocation_result_values is not None:
            RegisteredResource.allocation_result_values.extend(self, allocation_result_values)
        if ruc_award_instruction is not None:
            RegisteredResource.ruc_award_instruction.extend(self, ruc_award_instruction)
        if mpm_resource_status is not None:
            RegisteredResource.mpm_resource_status.extend(self, mpm_resource_status)
        if commitments is not None:
            RegisteredResource.commitments.extend(self, commitments)
        if pnode is not None:
            self.pnode = pnode
        if former_reference is not None:
            RegisteredResource.former_reference.extend(self, former_reference)
        if intermittent_resource_eligibility is not None:
            RegisteredResource.intermittent_resource_eligibility.extend(
                self, intermittent_resource_eligibility
            )
        if instructions is not None:
            RegisteredResource.instructions.extend(self, instructions)
        if market_participant is not None:
            self.market_participant = market_participant
        if sub_control_area is not None:
            RegisteredResource.sub_control_area.extend(self, sub_control_area)
        if adjacent_ca_set is not None:
            self.adjacent_ca_set = adjacent_ca_set
        if substitution_resource_list is not None:
            RegisteredResource.substitution_resource_list.extend(self, substitution_resource_list)
        if resource_dispatch_results is not None:
            RegisteredResource.resource_dispatch_results.extend(self, resource_dispatch_results)
        if rmr_operator_input is not None:
            RegisteredResource.rmr_operator_input.extend(self, rmr_operator_input)
        if ex_post_resource_results is not None:
            RegisteredResource.ex_post_resource_results.extend(self, ex_post_resource_results)
        if org_res_ownership is not None:
            RegisteredResource.org_res_ownership.extend(self, org_res_ownership)
        if contract_distribution_factor is not None:
            RegisteredResource.contract_distribution_factor.extend(
                self, contract_distribution_factor
            )
        if ramp_rate_curve is not None:
            RegisteredResource.ramp_rate_curve.extend(self, ramp_rate_curve)
        if resource_award_instruction is not None:
            RegisteredResource.resource_award_instruction.extend(self, resource_award_instruction)
        if mpm_test_threshold is not None:
            RegisteredResource.mpm_test_threshold.extend(self, mpm_test_threshold)
        if load_following_operator_input is not None:
            RegisteredResource.load_following_operator_input.extend(
                self, load_following_operator_input
            )
        if time_series is not None:
            RegisteredResource.time_series.extend(self, time_series)
        if control_area_designation is not None:
            RegisteredResource.control_area_designation.extend(self, control_area_designation)
        if dispatch_inst_reply is not None:
            RegisteredResource.dispatch_inst_reply.extend(self, dispatch_inst_reply)
        if market_object_status is not None:
            RegisteredResource.market_object_status.extend(self, market_object_status)
        if aggregate_node is not None:
            self.aggregate_node = aggregate_node
        if default_bid is not None:
            self.default_bid = default_bid
        if resource_verifiable_costs is not None:
            self.resource_verifiable_costs = resource_verifiable_costs
        if forbidden_region is not None:
            RegisteredResource.forbidden_region.extend(self, forbidden_region)

    def add_dot_instruction(self, dot_instruction: DotInstruction) -> Self:
        return RegisteredResource.dot_instruction.add(self, dot_instruction)

    def remove_dot_instruction(self, dot_instruction: DotInstruction) -> Self:
        return RegisteredResource.dot_instruction.remove(self, dot_instruction)

    def clear_dot_instruction(self) -> Self:
        return RegisteredResource.dot_instruction.clear(self)

    def num_dot_instruction(self) -> int:
        return RegisteredResource.dot_instruction.count(self)

    def add_dop_instruction(self, dop_instruction: DopInstruction) -> Self:
        return RegisteredResource.dop_instruction.add(self, dop_instruction)

    def remove_dop_instruction(self, dop_instruction: DopInstruction) -> Self:
        return RegisteredResource.dop_instruction.remove(self, dop_instruction)

    def clear_dop_instruction(self) -> Self:
        return RegisteredResource.dop_instruction.clear(self)

    def num_dop_instruction(self) -> int:
        return RegisteredResource.dop_instruction.count(self)

    def add_resource_group(self, resource_group: ResourceGroup) -> Self:
        return RegisteredResource.resource_groups.add(self, resource_group)

    def remove_resource_group(self, resource_group: ResourceGroup) -> Self:
        return RegisteredResource.resource_groups.remove(self, resource_group)

    def clear_resource_groups(self) -> Self:
        return RegisteredResource.resource_groups.clear(self)

    def num_resource_group(self) -> int:
        return RegisteredResource.resource_groups.count(self)

    def get_resource_group_by_mrid(self, mrid: str) -> ResourceGroup | None:
        return RegisteredResource.resource_groups.get_by_mrid(self, mrid)

    def add_inter_tie(self, inter_tie: SchedulingPoint) -> Self:
        return RegisteredResource.inter_tie.add(self, inter_tie)

    def remove_inter_tie(self, inter_tie: SchedulingPoint) -> Self:
        return RegisteredResource.inter_tie.remove(self, inter_tie)

    def clear_inter_tie(self) -> Self:
        return RegisteredResource.inter_tie.clear(self)

    def num_inter_tie(self) -> int:
        return RegisteredResource.inter_tie.count(self)

    def get_inter_tie_by_mrid(self, mrid: str) -> SchedulingPoint | None:
        return RegisteredResource.inter_tie.get_by_mrid(self, mrid)

    def add_resource_certification(self, resource_certification: ResourceCertification) -> Self:
        return RegisteredResource.resource_certification.add(self, resource_certification)

    def remove_resource_certification(self, resource_certification: ResourceCertification) -> Self:
        return RegisteredResource.resource_certification.remove(self, resource_certification)

    def clear_resource_certification(self) -> Self:
        return RegisteredResource.resource_certification.clear(self)

    def num_resource_certification(self) -> int:
        return RegisteredResource.resource_certification.count(self)

    def add_energy_market(self, energy_market: EnergyMarket) -> Self:
        return RegisteredResource.energy_markets.add(self, energy_market)

    def remove_energy_market(self, energy_market: EnergyMarket) -> Self:
        return RegisteredResource.energy_markets.remove(self, energy_market)

    def clear_energy_markets(self) -> Self:
        return RegisteredResource.energy_markets.clear(self)

    def num_energy_market(self) -> int:
        return RegisteredResource.energy_markets.count(self)

    def get_energy_market_by_mrid(self, mrid: str) -> EnergyMarket | None:
        return RegisteredResource.energy_markets.get_by_mrid(self, mrid)

    def add_resource_capacity(self, resource_capacity: ResourceCapacity) -> Self:
        return RegisteredResource.resource_capacity.add(self, resource_capacity)

    def remove_resource_capacity(self, resource_capacity: ResourceCapacity) -> Self:
        return RegisteredResource.resource_capacity.remove(self, resource_capacity)

    def clear_resource_capacity(self) -> Self:
        return RegisteredResource.resource_capacity.clear(self)

    def num_resource_capacity(self) -> int:
        return RegisteredResource.resource_capacity.count(self)

    def add_reason(self, reason: Reason) -> Self:
        return RegisteredResource.reason.add(self, reason)

    def remove_reason(self, reason: Reason) -> Self:
        return RegisteredResource.reason.remove(self, reason)

    def clear_reason(self) -> Self:
        return RegisteredResource.reason.clear(self)

    def num_reason(self) -> int:
        return RegisteredResource.reason.count(self)

    def add_domain(self, domain: Domain) -> Self:
        return RegisteredResource.domain.add(self, domain)

    def remove_domain(self, domain: Domain) -> Self:
        return RegisteredResource.domain.remove(self, domain)

    def clear_domain(self) -> Self:
        return RegisteredResource.domain.clear(self)

    def num_domain(self) -> int:
        return RegisteredResource.domain.count(self)

    def get_domain_by_mrid(self, mrid: str) -> Domain | None:
        return RegisteredResource.domain.get_by_mrid(self, mrid)

    def add_expected_energy_value(self, expected_energy_value: ExpectedEnergyValues) -> Self:
        return RegisteredResource.expected_energy_values.add(self, expected_energy_value)

    def remove_expected_energy_value(self, expected_energy_value: ExpectedEnergyValues) -> Self:
        return RegisteredResource.expected_energy_values.remove(self, expected_energy_value)

    def clear_expected_energy_values(self) -> Self:
        return RegisteredResource.expected_energy_values.clear(self)

    def num_expected_energy_value(self) -> int:
        return RegisteredResource.expected_energy_values.count(self)

    def add_resource_ancillary_service_qualification(
        self, resource_ancillary_service_qualification: ResourceCertification_dup1
    ) -> Self:
        return RegisteredResource.resource_ancillary_service_qualification.add(
            self, resource_ancillary_service_qualification
        )

    def remove_resource_ancillary_service_qualification(
        self, resource_ancillary_service_qualification: ResourceCertification_dup1
    ) -> Self:
        return RegisteredResource.resource_ancillary_service_qualification.remove(
            self, resource_ancillary_service_qualification
        )

    def clear_resource_ancillary_service_qualification(self) -> Self:
        return RegisteredResource.resource_ancillary_service_qualification.clear(self)

    def num_resource_ancillary_service_qualification(self) -> int:
        return RegisteredResource.resource_ancillary_service_qualification.count(self)

    def add_resource_load_following_inst(
        self, resource_load_following_inst: ResourceLoadFollowingInst
    ) -> Self:
        return RegisteredResource.resource_load_following_inst.add(
            self, resource_load_following_inst
        )

    def remove_resource_load_following_inst(
        self, resource_load_following_inst: ResourceLoadFollowingInst
    ) -> Self:
        return RegisteredResource.resource_load_following_inst.remove(
            self, resource_load_following_inst
        )

    def clear_resource_load_following_inst(self) -> Self:
        return RegisteredResource.resource_load_following_inst.clear(self)

    def num_resource_load_following_inst(self) -> int:
        return RegisteredResource.resource_load_following_inst.count(self)

    def add_load_following_inst(self, load_following_inst: LoadFollowingInst) -> Self:
        return RegisteredResource.load_following_inst.add(self, load_following_inst)

    def remove_load_following_inst(self, load_following_inst: LoadFollowingInst) -> Self:
        return RegisteredResource.load_following_inst.remove(self, load_following_inst)

    def clear_load_following_inst(self) -> Self:
        return RegisteredResource.load_following_inst.clear(self)

    def num_load_following_inst(self) -> int:
        return RegisteredResource.load_following_inst.count(self)

    def add_allocation_result_value(self, allocation_result_value: AllocationResultValues) -> Self:
        return RegisteredResource.allocation_result_values.add(self, allocation_result_value)

    def remove_allocation_result_value(
        self, allocation_result_value: AllocationResultValues
    ) -> Self:
        return RegisteredResource.allocation_result_values.remove(self, allocation_result_value)

    def clear_allocation_result_values(self) -> Self:
        return RegisteredResource.allocation_result_values.clear(self)

    def num_allocation_result_value(self) -> int:
        return RegisteredResource.allocation_result_values.count(self)

    def add_ruc_award_instruction(self, ruc_award_instruction: RUCAwardInstruction) -> Self:
        return RegisteredResource.ruc_award_instruction.add(self, ruc_award_instruction)

    def remove_ruc_award_instruction(self, ruc_award_instruction: RUCAwardInstruction) -> Self:
        return RegisteredResource.ruc_award_instruction.remove(self, ruc_award_instruction)

    def clear_ruc_award_instruction(self) -> Self:
        return RegisteredResource.ruc_award_instruction.clear(self)

    def num_ruc_award_instruction(self) -> int:
        return RegisteredResource.ruc_award_instruction.count(self)

    def add_mpm_resource_status(self, mpm_resource_status: MPMResourceStatus) -> Self:
        return RegisteredResource.mpm_resource_status.add(self, mpm_resource_status)

    def remove_mpm_resource_status(self, mpm_resource_status: MPMResourceStatus) -> Self:
        return RegisteredResource.mpm_resource_status.remove(self, mpm_resource_status)

    def clear_mpm_resource_status(self) -> Self:
        return RegisteredResource.mpm_resource_status.clear(self)

    def num_mpm_resource_status(self) -> int:
        return RegisteredResource.mpm_resource_status.count(self)

    def add_commitment(self, commitment: Commitments) -> Self:
        return RegisteredResource.commitments.add(self, commitment)

    def remove_commitment(self, commitment: Commitments) -> Self:
        return RegisteredResource.commitments.remove(self, commitment)

    def clear_commitments(self) -> Self:
        return RegisteredResource.commitments.clear(self)

    def num_commitment(self) -> int:
        return RegisteredResource.commitments.count(self)

    def add_former_reference(self, former_reference: FormerReference) -> Self:
        return RegisteredResource.former_reference.add(self, former_reference)

    def remove_former_reference(self, former_reference: FormerReference) -> Self:
        return RegisteredResource.former_reference.remove(self, former_reference)

    def clear_former_reference(self) -> Self:
        return RegisteredResource.former_reference.clear(self)

    def num_former_reference(self) -> int:
        return RegisteredResource.former_reference.count(self)

    def get_former_reference_by_mrid(self, mrid: str) -> FormerReference | None:
        return RegisteredResource.former_reference.get_by_mrid(self, mrid)

    def add_intermittent_resource_eligibility(
        self, intermittent_resource_eligibility: IntermittentResourceEligibility
    ) -> Self:
        return RegisteredResource.intermittent_resource_eligibility.add(
            self, intermittent_resource_eligibility
        )

    def remove_intermittent_resource_eligibility(
        self, intermittent_resource_eligibility: IntermittentResourceEligibility
    ) -> Self:
        return RegisteredResource.intermittent_resource_eligibility.remove(
            self, intermittent_resource_eligibility
        )

    def clear_intermittent_resource_eligibility(self) -> Self:
        return RegisteredResource.intermittent_resource_eligibility.clear(self)

    def num_intermittent_resource_eligibility(self) -> int:
        return RegisteredResource.intermittent_resource_eligibility.count(self)

    def get_intermittent_resource_eligibility_by_mrid(
        self, mrid: str
    ) -> IntermittentResourceEligibility | None:
        return RegisteredResource.intermittent_resource_eligibility.get_by_mrid(self, mrid)

    def add_instruction(self, instruction: Instructions) -> Self:
        return RegisteredResource.instructions.add(self, instruction)

    def remove_instruction(self, instruction: Instructions) -> Self:
        return RegisteredResource.instructions.remove(self, instruction)

    def clear_instructions(self) -> Self:
        return RegisteredResource.instructions.clear(self)

    def num_instruction(self) -> int:
        return RegisteredResource.instructions.count(self)

    def add_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return RegisteredResource.sub_control_area.add(self, sub_control_area)

    def remove_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return RegisteredResource.sub_control_area.remove(self, sub_control_area)

    def clear_sub_control_area(self) -> Self:
        return RegisteredResource.sub_control_area.clear(self)

    def num_sub_control_area(self) -> int:
        return RegisteredResource.sub_control_area.count(self)

    def get_sub_control_area_by_mrid(self, mrid: str) -> SubControlArea | None:
        return RegisteredResource.sub_control_area.get_by_mrid(self, mrid)

    def add_substitution_resource_list(
        self, substitution_resource_list: SubstitutionResourceList
    ) -> Self:
        return RegisteredResource.substitution_resource_list.add(self, substitution_resource_list)

    def remove_substitution_resource_list(
        self, substitution_resource_list: SubstitutionResourceList
    ) -> Self:
        return RegisteredResource.substitution_resource_list.remove(
            self, substitution_resource_list
        )

    def clear_substitution_resource_list(self) -> Self:
        return RegisteredResource.substitution_resource_list.clear(self)

    def num_substitution_resource_list(self) -> int:
        return RegisteredResource.substitution_resource_list.count(self)

    def add_resource_dispatch_result(
        self, resource_dispatch_result: ResourceDispatchResults
    ) -> Self:
        return RegisteredResource.resource_dispatch_results.add(self, resource_dispatch_result)

    def remove_resource_dispatch_result(
        self, resource_dispatch_result: ResourceDispatchResults
    ) -> Self:
        return RegisteredResource.resource_dispatch_results.remove(self, resource_dispatch_result)

    def clear_resource_dispatch_results(self) -> Self:
        return RegisteredResource.resource_dispatch_results.clear(self)

    def num_resource_dispatch_result(self) -> int:
        return RegisteredResource.resource_dispatch_results.count(self)

    def add_rmr_operator_input(self, rmr_operator_input: RMROperatorInput) -> Self:
        return RegisteredResource.rmr_operator_input.add(self, rmr_operator_input)

    def remove_rmr_operator_input(self, rmr_operator_input: RMROperatorInput) -> Self:
        return RegisteredResource.rmr_operator_input.remove(self, rmr_operator_input)

    def clear_rmr_operator_input(self) -> Self:
        return RegisteredResource.rmr_operator_input.clear(self)

    def num_rmr_operator_input(self) -> int:
        return RegisteredResource.rmr_operator_input.count(self)

    def get_rmr_operator_input_by_mrid(self, mrid: str) -> RMROperatorInput | None:
        return RegisteredResource.rmr_operator_input.get_by_mrid(self, mrid)

    def add_ex_post_resource_result(self, ex_post_resource_result: ExPostResourceResults) -> Self:
        return RegisteredResource.ex_post_resource_results.add(self, ex_post_resource_result)

    def remove_ex_post_resource_result(
        self, ex_post_resource_result: ExPostResourceResults
    ) -> Self:
        return RegisteredResource.ex_post_resource_results.remove(self, ex_post_resource_result)

    def clear_ex_post_resource_results(self) -> Self:
        return RegisteredResource.ex_post_resource_results.clear(self)

    def num_ex_post_resource_result(self) -> int:
        return RegisteredResource.ex_post_resource_results.count(self)

    def add_org_res_ownership(self, org_res_ownership: OrgResOwnership) -> Self:
        return RegisteredResource.org_res_ownership.add(self, org_res_ownership)

    def remove_org_res_ownership(self, org_res_ownership: OrgResOwnership) -> Self:
        return RegisteredResource.org_res_ownership.remove(self, org_res_ownership)

    def clear_org_res_ownership(self) -> Self:
        return RegisteredResource.org_res_ownership.clear(self)

    def num_org_res_ownership(self) -> int:
        return RegisteredResource.org_res_ownership.count(self)

    def get_org_res_ownership_by_mrid(self, mrid: str) -> OrgResOwnership | None:
        return RegisteredResource.org_res_ownership.get_by_mrid(self, mrid)

    def add_contract_distribution_factor(
        self, contract_distribution_factor: ContractDistributionFactor
    ) -> Self:
        return RegisteredResource.contract_distribution_factor.add(
            self, contract_distribution_factor
        )

    def remove_contract_distribution_factor(
        self, contract_distribution_factor: ContractDistributionFactor
    ) -> Self:
        return RegisteredResource.contract_distribution_factor.remove(
            self, contract_distribution_factor
        )

    def clear_contract_distribution_factor(self) -> Self:
        return RegisteredResource.contract_distribution_factor.clear(self)

    def num_contract_distribution_factor(self) -> int:
        return RegisteredResource.contract_distribution_factor.count(self)

    def add_ramp_rate_curve(self, ramp_rate_curve: RampRateCurve) -> Self:
        return RegisteredResource.ramp_rate_curve.add(self, ramp_rate_curve)

    def remove_ramp_rate_curve(self, ramp_rate_curve: RampRateCurve) -> Self:
        return RegisteredResource.ramp_rate_curve.remove(self, ramp_rate_curve)

    def clear_ramp_rate_curve(self) -> Self:
        return RegisteredResource.ramp_rate_curve.clear(self)

    def num_ramp_rate_curve(self) -> int:
        return RegisteredResource.ramp_rate_curve.count(self)

    def get_ramp_rate_curve_by_mrid(self, mrid: str) -> RampRateCurve | None:
        return RegisteredResource.ramp_rate_curve.get_by_mrid(self, mrid)

    def add_resource_award_instruction(
        self, resource_award_instruction: ResourceAwardInstruction
    ) -> Self:
        return RegisteredResource.resource_award_instruction.add(self, resource_award_instruction)

    def remove_resource_award_instruction(
        self, resource_award_instruction: ResourceAwardInstruction
    ) -> Self:
        return RegisteredResource.resource_award_instruction.remove(
            self, resource_award_instruction
        )

    def clear_resource_award_instruction(self) -> Self:
        return RegisteredResource.resource_award_instruction.clear(self)

    def num_resource_award_instruction(self) -> int:
        return RegisteredResource.resource_award_instruction.count(self)

    def add_mpm_test_threshold(self, mpm_test_threshold: MPMTestThreshold) -> Self:
        return RegisteredResource.mpm_test_threshold.add(self, mpm_test_threshold)

    def remove_mpm_test_threshold(self, mpm_test_threshold: MPMTestThreshold) -> Self:
        return RegisteredResource.mpm_test_threshold.remove(self, mpm_test_threshold)

    def clear_mpm_test_threshold(self) -> Self:
        return RegisteredResource.mpm_test_threshold.clear(self)

    def num_mpm_test_threshold(self) -> int:
        return RegisteredResource.mpm_test_threshold.count(self)

    def add_load_following_operator_input(
        self, load_following_operator_input: LoadFollowingOperatorInput
    ) -> Self:
        return RegisteredResource.load_following_operator_input.add(
            self, load_following_operator_input
        )

    def remove_load_following_operator_input(
        self, load_following_operator_input: LoadFollowingOperatorInput
    ) -> Self:
        return RegisteredResource.load_following_operator_input.remove(
            self, load_following_operator_input
        )

    def clear_load_following_operator_input(self) -> Self:
        return RegisteredResource.load_following_operator_input.clear(self)

    def num_load_following_operator_input(self) -> int:
        return RegisteredResource.load_following_operator_input.count(self)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return RegisteredResource.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return RegisteredResource.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return RegisteredResource.time_series.clear(self)

    def num_time_series(self) -> int:
        return RegisteredResource.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return RegisteredResource.time_series.get_by_mrid(self, mrid)

    def add_control_area_designation(
        self, control_area_designation: ControlAreaDesignation
    ) -> Self:
        return RegisteredResource.control_area_designation.add(self, control_area_designation)

    def remove_control_area_designation(
        self, control_area_designation: ControlAreaDesignation
    ) -> Self:
        return RegisteredResource.control_area_designation.remove(self, control_area_designation)

    def clear_control_area_designation(self) -> Self:
        return RegisteredResource.control_area_designation.clear(self)

    def num_control_area_designation(self) -> int:
        return RegisteredResource.control_area_designation.count(self)

    def add_dispatch_inst_reply(self, dispatch_inst_reply: DispatchInstReply) -> Self:
        return RegisteredResource.dispatch_inst_reply.add(self, dispatch_inst_reply)

    def remove_dispatch_inst_reply(self, dispatch_inst_reply: DispatchInstReply) -> Self:
        return RegisteredResource.dispatch_inst_reply.remove(self, dispatch_inst_reply)

    def clear_dispatch_inst_reply(self) -> Self:
        return RegisteredResource.dispatch_inst_reply.clear(self)

    def num_dispatch_inst_reply(self) -> int:
        return RegisteredResource.dispatch_inst_reply.count(self)

    def get_dispatch_inst_reply_by_mrid(self, mrid: str) -> DispatchInstReply | None:
        return RegisteredResource.dispatch_inst_reply.get_by_mrid(self, mrid)

    def add_market_object_status(self, market_object_status: MarketObjectStatus) -> Self:
        return RegisteredResource.market_object_status.add(self, market_object_status)

    def remove_market_object_status(self, market_object_status: MarketObjectStatus) -> Self:
        return RegisteredResource.market_object_status.remove(self, market_object_status)

    def clear_market_object_status(self) -> Self:
        return RegisteredResource.market_object_status.clear(self)

    def num_market_object_status(self) -> int:
        return RegisteredResource.market_object_status.count(self)

    def add_forbidden_region(self, forbidden_region: ForbiddenRegion) -> Self:
        return RegisteredResource.forbidden_region.add(self, forbidden_region)

    def remove_forbidden_region(self, forbidden_region: ForbiddenRegion) -> Self:
        return RegisteredResource.forbidden_region.remove(self, forbidden_region)

    def clear_forbidden_region(self) -> Self:
        return RegisteredResource.forbidden_region.clear(self)

    def num_forbidden_region(self) -> int:
        return RegisteredResource.forbidden_region.count(self)

    def get_forbidden_region_by_mrid(self, mrid: str) -> ForbiddenRegion | None:
        return RegisteredResource.forbidden_region.get_by_mrid(self, mrid)
