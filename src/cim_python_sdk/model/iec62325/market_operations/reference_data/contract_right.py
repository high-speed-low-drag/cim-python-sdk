"""CIM class ContractRight (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.tr_entitlement import (
        TREntitlement,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_interface_right_entitlement import (
        TransmissionInterfaceRightEntitlement,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.contract_type import (
        ContractType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.tr_type import TRType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_self_sched import (
        BidSelfSched,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_distribution_factor import (
        ContractDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO
    from cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator import (
        SchedulingCoordinator,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.substitution_resource_list import (
        SubstitutionResourceList,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.transmission_right_chain import (
        TransmissionRightChain,
    )


class ContractRight(IdentifiedObject):
    """Provides definition of Transmission Ownership Right and Existing Transmission Contract
    identifiers for use by SCUC. RMR contract hosting: Startup lead time, Contract Service
    Limits, Max Service Hours, Max MWhs, Max Start-ups, Ramp Rate, Max Net Dependable
    Capacity, Min Capacity and Unit Substitution for DAM/RTM to retrieve."""

    __slots__ = (
        "_bid_self_sched",
        "_chain_transmission_right_chain",
        "_contract_distribution_factor",
        "_ind_transmission_right_chain",
        "_rto",
        "_scheduling_coordinator",
        "_substitution_resource_list",
        "_tr_entitlement",
        "_transmission_interface_entitlement",
        "chain_order",
        "contract_mw",
        "contract_price",
        "contract_priority",
        "contract_status",
        "contract_type",
        "financial_location",
        "financial_rights_dam",
        "financial_rights_rtm",
        "fuel_adder",
        "latest_sched_minutes",
        "latest_sched_mkt_type",
        "max_net_dependable_capacity",
        "maximum_schedule_quantity",
        "maximum_service_hours",
        "maximum_startups",
        "minimum_load",
        "minimum_schedule_quantity",
        "physical_rights_dam",
        "physical_rights_rtm",
        "startup_lead_time",
        "tr_type",
    )

    chain_order: int | None
    contract_mw: float | None
    contract_price: float | None  # CostPerEnergyUnit
    contract_priority: int | None
    contract_status: str | None
    contract_type: ContractType | None
    financial_location: YesNo | None
    financial_rights_dam: YesNo | None
    financial_rights_rtm: YesNo | None
    fuel_adder: float | None
    latest_sched_minutes: int | None
    latest_sched_mkt_type: MarketType | None
    maximum_schedule_quantity: float | None
    maximum_service_hours: int | None
    maximum_startups: int | None
    max_net_dependable_capacity: float | None
    minimum_load: float | None
    minimum_schedule_quantity: float | None
    physical_rights_dam: YesNo | None
    physical_rights_rtm: YesNo | None
    startup_lead_time: int | None
    tr_type: TRType | None

    chain_transmission_right_chain: One[TransmissionRightChain] = One(
        EndMeta(
            name="chain_transmission_right_chain",
            cim_role="Chain_TransmissionRightChain",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.transmission_right_chain:TransmissionRightChain",
            many=False,
            lower=0,
            upper=1,
            inverse="chain_contract_right",
            aggregation="none",
        )
    )
    ind_transmission_right_chain: One[TransmissionRightChain] = One(
        EndMeta(
            name="ind_transmission_right_chain",
            cim_role="Ind_TransmissionRightChain",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.transmission_right_chain:TransmissionRightChain",
            many=False,
            lower=0,
            upper=1,
            inverse="ind_contract_right",
            aggregation="none",
        )
    )
    tr_entitlement: Many[TREntitlement] = Many(
        EndMeta(
            name="tr_entitlement",
            cim_role="TREntitlement",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.tr_entitlement:TREntitlement",
            many=True,
            lower=0,
            upper=None,
            inverse="transmission_contract_right",
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
            inverse="transmission_contract_right",
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
            inverse="transmission_contract_right",
            aggregation="none",
        )
    )
    scheduling_coordinator: One[SchedulingCoordinator] = One(
        EndMeta(
            name="scheduling_coordinator",
            cim_role="SchedulingCoordinator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator:SchedulingCoordinator",
            many=False,
            lower=1,
            upper=1,
            inverse="transmission_contract_right",
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
            inverse="transmission_contract_right",
            aggregation="none",
        )
    )
    transmission_interface_entitlement: Many[TransmissionInterfaceRightEntitlement] = Many(
        EndMeta(
            name="transmission_interface_entitlement",
            cim_role="TransmissionInterfaceEntitlement",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_interface_right_entitlement:TransmissionInterfaceRightEntitlement",
            many=True,
            lower=0,
            upper=None,
            inverse="contract_right",
            aggregation="none",
        )
    )
    bid_self_sched: Many[BidSelfSched] = Many(
        EndMeta(
            name="bid_self_sched",
            cim_role="BidSelfSched",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_self_sched:BidSelfSched",
            many=True,
            lower=0,
            upper=None,
            inverse="transmission_contract_right",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ContractRight",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{FD1F57F3-DF0A-4e41-89FB-568A0D56E562}",
        attributes=(
            AttrMeta("chain_order", "chainOrder", "int", 0, 1, "primitive"),
            AttrMeta("contract_mw", "contractMW", "float", 0, 1, "primitive"),
            AttrMeta("contract_price", "contractPrice", "CostPerEnergyUnit", 0, 1, "cimdatatype"),
            AttrMeta("contract_priority", "contractPriority", "int", 0, 1, "primitive"),
            AttrMeta("contract_status", "contractStatus", "str", 0, 1, "primitive"),
            AttrMeta("contract_type", "contractType", "ContractType", 0, 1, "enumeration"),
            AttrMeta("financial_location", "financialLocation", "YesNo", 0, 1, "enumeration"),
            AttrMeta("financial_rights_dam", "financialRightsDAM", "YesNo", 0, 1, "enumeration"),
            AttrMeta("financial_rights_rtm", "financialRightsRTM", "YesNo", 0, 1, "enumeration"),
            AttrMeta("fuel_adder", "fuelAdder", "float", 0, 1, "primitive"),
            AttrMeta("latest_sched_minutes", "latestSchedMinutes", "int", 0, 1, "primitive"),
            AttrMeta(
                "latest_sched_mkt_type", "latestSchedMktType", "MarketType", 0, 1, "enumeration"
            ),
            AttrMeta(
                "maximum_schedule_quantity", "maximumScheduleQuantity", "float", 0, 1, "primitive"
            ),
            AttrMeta("maximum_service_hours", "maximumServiceHours", "int", 0, 1, "primitive"),
            AttrMeta("maximum_startups", "maximumStartups", "int", 0, 1, "primitive"),
            AttrMeta(
                "max_net_dependable_capacity",
                "maxNetDependableCapacity",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta("minimum_load", "minimumLoad", "float", 0, 1, "primitive"),
            AttrMeta(
                "minimum_schedule_quantity", "minimumScheduleQuantity", "float", 0, 1, "primitive"
            ),
            AttrMeta("physical_rights_dam", "physicalRightsDAM", "YesNo", 0, 1, "enumeration"),
            AttrMeta("physical_rights_rtm", "physicalRightsRTM", "YesNo", 0, 1, "enumeration"),
            AttrMeta("startup_lead_time", "startupLeadTime", "int", 0, 1, "primitive"),
            AttrMeta("tr_type", "TRType", "TRType", 0, 1, "enumeration"),
        ),
        ends=(
            chain_transmission_right_chain.meta,
            ind_transmission_right_chain.meta,
            tr_entitlement.meta,
            contract_distribution_factor.meta,
            substitution_resource_list.meta,
            scheduling_coordinator.meta,
            rto.meta,
            transmission_interface_entitlement.meta,
            bid_self_sched.meta,
        ),
    )

    def __init__(
        self,
        *,
        chain_order: int | None = None,
        contract_mw: float | None = None,
        contract_price: float | None = None,
        contract_priority: int | None = None,
        contract_status: str | None = None,
        contract_type: ContractType | None = None,
        financial_location: YesNo | None = None,
        financial_rights_dam: YesNo | None = None,
        financial_rights_rtm: YesNo | None = None,
        fuel_adder: float | None = None,
        latest_sched_minutes: int | None = None,
        latest_sched_mkt_type: MarketType | None = None,
        maximum_schedule_quantity: float | None = None,
        maximum_service_hours: int | None = None,
        maximum_startups: int | None = None,
        max_net_dependable_capacity: float | None = None,
        minimum_load: float | None = None,
        minimum_schedule_quantity: float | None = None,
        physical_rights_dam: YesNo | None = None,
        physical_rights_rtm: YesNo | None = None,
        startup_lead_time: int | None = None,
        tr_type: TRType | None = None,
        chain_transmission_right_chain: TransmissionRightChain | None = None,
        ind_transmission_right_chain: TransmissionRightChain | None = None,
        tr_entitlement: Iterable[TREntitlement] | None = None,
        contract_distribution_factor: Iterable[ContractDistributionFactor] | None = None,
        substitution_resource_list: Iterable[SubstitutionResourceList] | None = None,
        scheduling_coordinator: SchedulingCoordinator | None = None,
        rto: RTO | None = None,
        transmission_interface_entitlement: Iterable[TransmissionInterfaceRightEntitlement]
        | None = None,
        bid_self_sched: Iterable[BidSelfSched] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.chain_order = chain_order
        self.contract_mw = contract_mw
        self.contract_price = contract_price
        self.contract_priority = contract_priority
        self.contract_status = contract_status
        self.contract_type = contract_type
        self.financial_location = financial_location
        self.financial_rights_dam = financial_rights_dam
        self.financial_rights_rtm = financial_rights_rtm
        self.fuel_adder = fuel_adder
        self.latest_sched_minutes = latest_sched_minutes
        self.latest_sched_mkt_type = latest_sched_mkt_type
        self.maximum_schedule_quantity = maximum_schedule_quantity
        self.maximum_service_hours = maximum_service_hours
        self.maximum_startups = maximum_startups
        self.max_net_dependable_capacity = max_net_dependable_capacity
        self.minimum_load = minimum_load
        self.minimum_schedule_quantity = minimum_schedule_quantity
        self.physical_rights_dam = physical_rights_dam
        self.physical_rights_rtm = physical_rights_rtm
        self.startup_lead_time = startup_lead_time
        self.tr_type = tr_type
        if chain_transmission_right_chain is not None:
            self.chain_transmission_right_chain = chain_transmission_right_chain
        if ind_transmission_right_chain is not None:
            self.ind_transmission_right_chain = ind_transmission_right_chain
        if tr_entitlement is not None:
            ContractRight.tr_entitlement.extend(self, tr_entitlement)
        if contract_distribution_factor is not None:
            ContractRight.contract_distribution_factor.extend(self, contract_distribution_factor)
        if substitution_resource_list is not None:
            ContractRight.substitution_resource_list.extend(self, substitution_resource_list)
        if scheduling_coordinator is not None:
            self.scheduling_coordinator = scheduling_coordinator
        if rto is not None:
            self.rto = rto
        if transmission_interface_entitlement is not None:
            ContractRight.transmission_interface_entitlement.extend(
                self, transmission_interface_entitlement
            )
        if bid_self_sched is not None:
            ContractRight.bid_self_sched.extend(self, bid_self_sched)

    def add_tr_entitlement(self, tr_entitlement: TREntitlement) -> Self:
        return ContractRight.tr_entitlement.add(self, tr_entitlement)

    def remove_tr_entitlement(self, tr_entitlement: TREntitlement) -> Self:
        return ContractRight.tr_entitlement.remove(self, tr_entitlement)

    def clear_tr_entitlement(self) -> Self:
        return ContractRight.tr_entitlement.clear(self)

    def num_tr_entitlement(self) -> int:
        return ContractRight.tr_entitlement.count(self)

    def add_contract_distribution_factor(
        self, contract_distribution_factor: ContractDistributionFactor
    ) -> Self:
        return ContractRight.contract_distribution_factor.add(self, contract_distribution_factor)

    def remove_contract_distribution_factor(
        self, contract_distribution_factor: ContractDistributionFactor
    ) -> Self:
        return ContractRight.contract_distribution_factor.remove(self, contract_distribution_factor)

    def clear_contract_distribution_factor(self) -> Self:
        return ContractRight.contract_distribution_factor.clear(self)

    def num_contract_distribution_factor(self) -> int:
        return ContractRight.contract_distribution_factor.count(self)

    def add_substitution_resource_list(
        self, substitution_resource_list: SubstitutionResourceList
    ) -> Self:
        return ContractRight.substitution_resource_list.add(self, substitution_resource_list)

    def remove_substitution_resource_list(
        self, substitution_resource_list: SubstitutionResourceList
    ) -> Self:
        return ContractRight.substitution_resource_list.remove(self, substitution_resource_list)

    def clear_substitution_resource_list(self) -> Self:
        return ContractRight.substitution_resource_list.clear(self)

    def num_substitution_resource_list(self) -> int:
        return ContractRight.substitution_resource_list.count(self)

    def add_transmission_interface_entitlement(
        self, transmission_interface_entitlement: TransmissionInterfaceRightEntitlement
    ) -> Self:
        return ContractRight.transmission_interface_entitlement.add(
            self, transmission_interface_entitlement
        )

    def remove_transmission_interface_entitlement(
        self, transmission_interface_entitlement: TransmissionInterfaceRightEntitlement
    ) -> Self:
        return ContractRight.transmission_interface_entitlement.remove(
            self, transmission_interface_entitlement
        )

    def clear_transmission_interface_entitlement(self) -> Self:
        return ContractRight.transmission_interface_entitlement.clear(self)

    def num_transmission_interface_entitlement(self) -> int:
        return ContractRight.transmission_interface_entitlement.count(self)

    def add_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return ContractRight.bid_self_sched.add(self, bid_self_sched)

    def remove_bid_self_sched(self, bid_self_sched: BidSelfSched) -> Self:
        return ContractRight.bid_self_sched.remove(self, bid_self_sched)

    def clear_bid_self_sched(self) -> Self:
        return ContractRight.bid_self_sched.clear(self)

    def num_bid_self_sched(self) -> int:
        return ContractRight.bid_self_sched.count(self)

    def get_bid_self_sched_by_mrid(self, mrid: str) -> BidSelfSched | None:
        return ContractRight.bid_self_sched.get_by_mrid(self, mrid)
