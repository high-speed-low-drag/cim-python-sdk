"""CIM enumeration MarketRoleKind (TC57CIM/IEC62325/InfIEC62325/InfMarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketRoleKind(CimEnum):
    """Kind of market role an organisation can have. This list is not exhausted, as other roles
    may exist."""

    energyServiceConsumer = "energyServiceConsumer"
    generatorOwner = "generatorOwner"
    generatorOperator = "generatorOperator"
    transmissionServiceProvider = "transmissionServiceProvider"
    transmissionOwner = "transmissionOwner"
    transmissionOperator = "transmissionOperator"
    distributionProvider = "distributionProvider"
    loadServingEntity = "loadServingEntity"
    purchasingSellingEntity = "purchasingSellingEntity"
    competitiveRetailer = "competitiveRetailer"
    reliabilityAuthority = "reliabilityAuthority"
    planningAuthority = "planningAuthority"
    balancingAuthority = "balancingAuthority"
    interchangeAuthority = "interchangeAuthority"
    transmissionPlanner = "transmissionPlanner"
    resourcePlanner = "resourcePlanner"
    standardsDeveloper = "standardsDeveloper"
    complianceMonitor = "complianceMonitor"
    BalanceResponsibleParty = "BalanceResponsibleParty"
    BalanceSupplier = "BalanceSupplier"
    BillingAgent = "BillingAgent"
    BlockEnergyTrader = "BlockEnergyTrader"
    CapacityCoordinator = "CapacityCoordinator"
    CapacityTrader = "CapacityTrader"
    Consumer = "Consumer"
    ConsumptionResponsibleParty = "ConsumptionResponsibleParty"
    ControlAreaOperator = "ControlAreaOperator"
    ControlBlockOperator = "ControlBlockOperator"
    CoordinationCenterOperator = "CoordinationCenterOperator"
    GridAccessProvider = "GridAccessProvider"
    GridOperator = "GridOperator"
    ImbalanceSettlementResponsible = "ImbalanceSettlementResponsible"
    InterconnectionTradeResponsible = "InterconnectionTradeResponsible"
    MarketInformationAggregator = "MarketInformationAggregator"
    MarketOperator = "MarketOperator"
    MeterAdministrator = "MeterAdministrator"
    MeterOperator = "MeterOperator"
    MeteredDataCollector = "MeteredDataCollector"
    MeteredDataResponsible = "MeteredDataResponsible"
    MeteredDataAggregator = "MeteredDataAggregator"
    MeteringPointAdministrator = "MeteringPointAdministrator"
    MOLResponsible = "MOLResponsible"
    NominationValidator = "NominationValidator"
    PartyConnectedToTheGrid = "PartyConnectedToTheGrid"
    Producer = "Producer"
    ProductionResponsibleParty = "ProductionResponsibleParty"
    ReconciliationAccountable = "ReconciliationAccountable"
    ReconciliationResponsible = "ReconciliationResponsible"
    ReserveAllocator = "ReserveAllocator"
    ResourceProvider = "ResourceProvider"
    SchedulingCoordinator = "SchedulingCoordinator"
    SystemOperator = "SystemOperator"
    TradeResponsibleParty = "TradeResponsibleParty"
    TransmissionCapacityAllocator = "TransmissionCapacityAllocator"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketRoleKind",
            package="TC57CIM/IEC62325/InfIEC62325/InfMarketOpCommon",
            guid="{86C84FDF-C303-49c7-827F-3EB7E7541C86}",
            kind="enumeration",
        )
    )
