"""CIM class RegisteredGenerator (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_object import (
        AuxiliaryObject,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_price_index import (
        EnergyPriceIndex,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.unit_initial_conditions import (
        UnitInitialConditions,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.cost_basis import CostBasis
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.flag_type_rmr import FlagTypeRMR
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.fuel_source import FuelSource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.ramp_curve_type import (
        RampCurveType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.unit_regulation_kind import (
        UnitRegulationKind,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.unit_type import UnitType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid import (
        GeneratingBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.start_up_cost_curve import (
        StartUpCostCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.start_up_time_curve import (
        StartUpTimeCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade import Trade
    from cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_cost_curve import (
        FuelCostCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_region import (
        FuelRegion,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.local_reliability_area import (
        LocalReliabilityArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_heat_rate_curve import (
        MktHeatRateCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.regulating_limit import (
        RegulatingLimit,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_heat_rate_curve import (
        RMRHeatRateCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_start_up_cost_curve import (
        RMRStartUpCostCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_start_up_energy_curve import (
        RMRStartUpEnergyCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_start_up_fuel_curve import (
        RMRStartUpFuelCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_start_up_time_curve import (
        RMRStartUpTimeCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.start_up_energy_curve import (
        StartUpEnergyCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.start_up_fuel_curve import (
        StartUpFuelCurve,
    )


class RegisteredGenerator(RegisteredResource):
    """Model of a generator that is registered to participate in the market."""

    __slots__ = (
        "_auxillary_object",
        "_energy_price_index",
        "_fuel_cost_curve",
        "_fuel_region",
        "_generating_bids",
        "_local_reliability_area",
        "_mkt_heat_rate_curve",
        "_regulating_limit",
        "_rmr_heat_rate_curve",
        "_rmr_start_up_cost_curve",
        "_rmr_start_up_energy_curve",
        "_rmr_start_up_fuel_curve",
        "_rmr_start_up_time_curve",
        "_start_up_cost_curves",
        "_start_up_energy_curve",
        "_start_up_fuel_curve",
        "_start_up_time_curve",
        "_trade",
        "_unit_initial_conditions",
        "capacity_factor",
        "cold_start_time",
        "combined_cycle_operating_mode",
        "commericial_operation_date",
        "constrained_output_flag",
        "energy_down_ramp_rate",
        "energy_up_ramp_rate",
        "extreme_long_start",
        "fuel_source",
        "high_control_limit",
        "hot_int_time",
        "hot_start_time",
        "int_cold_time",
        "int_start_time",
        "load_following_down_mss",
        "load_following_up_mss",
        "low_control_l_imit",
        "max_dependable_cap",
        "max_min_load_cost",
        "max_pumping_level",
        "max_shutdown_time",
        "max_start_ups_per_day",
        "max_weekly_energy",
        "max_weekly_starts",
        "maximum_allowable_spinning_reserve",
        "maximum_operating_limit",
        "min_load_cost",
        "minimum_load_cost_basis",
        "minimum_load_fuel_cost",
        "minimum_operating_limit",
        "must_offer_ra",
        "nameplate_capacity",
        "operating_maintenance_cost",
        "pump_min_down_time",
        "pump_min_up_time",
        "pump_shutdown_cost",
        "pump_shutdown_time",
        "pumping_cost",
        "pumping_factor",
        "quick_start_flag",
        "ramp_curve_type",
        "regulation_down_ramp_rate",
        "regulation_flag",
        "regulation_up_ramp_rate",
        "resource_sub_type",
        "river_system",
        "rmnr_flag",
        "rmr_flag",
        "rmr_manual_indicator",
        "rmt_flag",
        "spin_ramp_rate",
        "start_up_cost_basis",
        "sync_cond_capable",
        "unit_type",
        "use_limit_flag",
        "variable_energy_resource",
    )

    capacity_factor: float | None  # PerCent
    cold_start_time: float | None
    combined_cycle_operating_mode: str | None
    commericial_operation_date: _dt.datetime | None
    constrained_output_flag: YesNo | None
    energy_down_ramp_rate: float | None  # ActivePowerChangeRate
    energy_up_ramp_rate: float | None  # ActivePowerChangeRate
    extreme_long_start: YesNo | None
    fuel_source: FuelSource | None
    high_control_limit: float | None  # ActivePower
    hot_int_time: float | None
    hot_start_time: float | None
    int_cold_time: float | None
    int_start_time: float | None
    load_following_down_mss: YesNo | None
    load_following_up_mss: YesNo | None
    low_control_l_imit: float | None  # ActivePower
    max_dependable_cap: float | None  # ActivePower
    maximum_allowable_spinning_reserve: float | None  # ActivePower
    maximum_operating_limit: float | None  # ActivePower
    max_min_load_cost: float | None  # CostRate
    max_pumping_level: float | None  # ActivePower
    max_shutdown_time: _dt.datetime | None
    max_start_ups_per_day: int | None
    max_weekly_energy: float | None
    max_weekly_starts: int | None
    minimum_load_cost_basis: CostBasis | None
    minimum_load_fuel_cost: float | None  # CostPerHeatUnit
    minimum_operating_limit: float | None  # ActivePower
    min_load_cost: float | None  # CostRate
    must_offer_ra: YesNo | None
    nameplate_capacity: float | None  # ActivePower
    operating_maintenance_cost: float | None  # CostPerEnergyUnit
    pumping_cost: float | None  # CostRate
    pumping_factor: float | None
    pump_min_down_time: float | None
    pump_min_up_time: float | None
    pump_shutdown_cost: float | None
    pump_shutdown_time: int | None
    quick_start_flag: YesNo | None
    ramp_curve_type: RampCurveType | None
    regulation_down_ramp_rate: float | None  # ActivePowerChangeRate
    regulation_flag: UnitRegulationKind | None
    regulation_up_ramp_rate: float | None  # ActivePowerChangeRate
    resource_sub_type: str | None
    river_system: str | None
    rmnr_flag: YesNo | None
    rmr_flag: FlagTypeRMR | None
    rmr_manual_indicator: YesNo | None
    rmt_flag: YesNo | None
    spin_ramp_rate: float | None  # ActivePowerChangeRate
    start_up_cost_basis: CostBasis | None
    sync_cond_capable: YesNo | None
    unit_type: UnitType | None
    use_limit_flag: YesNo | None
    variable_energy_resource: YesNo | None

    trade: Many[Trade] = Many(
        EndMeta(
            name="trade",
            cim_role="Trade",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade:Trade",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    rmr_start_up_energy_curve: One[RMRStartUpEnergyCurve] = One(
        EndMeta(
            name="rmr_start_up_energy_curve",
            cim_role="RMRStartUpEnergyCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_start_up_energy_curve:RMRStartUpEnergyCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    mkt_heat_rate_curve: One[MktHeatRateCurve] = One(
        EndMeta(
            name="mkt_heat_rate_curve",
            cim_role="MktHeatRateCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_heat_rate_curve:MktHeatRateCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    fuel_region: One[FuelRegion] = One(
        EndMeta(
            name="fuel_region",
            cim_role="FuelRegion",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_region:FuelRegion",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    local_reliability_area: One[LocalReliabilityArea] = One(
        EndMeta(
            name="local_reliability_area",
            cim_role="LocalReliabilityArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.local_reliability_area:LocalReliabilityArea",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    rmr_start_up_time_curve: One[RMRStartUpTimeCurve] = One(
        EndMeta(
            name="rmr_start_up_time_curve",
            cim_role="RMRStartUpTimeCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_start_up_time_curve:RMRStartUpTimeCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    start_up_cost_curves: Many[StartUpCostCurve] = Many(
        EndMeta(
            name="start_up_cost_curves",
            cim_role="StartUpCostCurves",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.start_up_cost_curve:StartUpCostCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_generators",
            aggregation="none",
        )
    )
    start_up_energy_curve: One[StartUpEnergyCurve] = One(
        EndMeta(
            name="start_up_energy_curve",
            cim_role="StartUpEnergyCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.start_up_energy_curve:StartUpEnergyCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    start_up_time_curve: One[StartUpTimeCurve] = One(
        EndMeta(
            name="start_up_time_curve",
            cim_role="StartUpTimeCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.start_up_time_curve:StartUpTimeCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    energy_price_index: One[EnergyPriceIndex] = One(
        EndMeta(
            name="energy_price_index",
            cim_role="EnergyPriceIndex",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_price_index:EnergyPriceIndex",
            many=False,
            lower=1,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    regulating_limit: One[RegulatingLimit] = One(
        EndMeta(
            name="regulating_limit",
            cim_role="RegulatingLimit",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.regulating_limit:RegulatingLimit",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    start_up_fuel_curve: One[StartUpFuelCurve] = One(
        EndMeta(
            name="start_up_fuel_curve",
            cim_role="StartUpFuelCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.start_up_fuel_curve:StartUpFuelCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    auxillary_object: Many[AuxiliaryObject] = Many(
        EndMeta(
            name="auxillary_object",
            cim_role="AuxillaryObject",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_object:AuxiliaryObject",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    rmr_start_up_cost_curve: One[RMRStartUpCostCurve] = One(
        EndMeta(
            name="rmr_start_up_cost_curve",
            cim_role="RMRStartUpCostCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_start_up_cost_curve:RMRStartUpCostCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    generating_bids: Many[GeneratingBid] = Many(
        EndMeta(
            name="generating_bids",
            cim_role="GeneratingBids",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid:GeneratingBid",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    rmr_start_up_fuel_curve: One[RMRStartUpFuelCurve] = One(
        EndMeta(
            name="rmr_start_up_fuel_curve",
            cim_role="RMRStartUpFuelCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_start_up_fuel_curve:RMRStartUpFuelCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    fuel_cost_curve: One[FuelCostCurve] = One(
        EndMeta(
            name="fuel_cost_curve",
            cim_role="FuelCostCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.fuel_cost_curve:FuelCostCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    rmr_heat_rate_curve: One[RMRHeatRateCurve] = One(
        EndMeta(
            name="rmr_heat_rate_curve",
            cim_role="RMRHeatRateCurve",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rmr_heat_rate_curve:RMRHeatRateCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_generator",
            aggregation="none",
        )
    )
    unit_initial_conditions: Many[UnitInitialConditions] = Many(
        EndMeta(
            name="unit_initial_conditions",
            cim_role="UnitInitialConditions",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.unit_initial_conditions:UnitInitialConditions",
            many=True,
            lower=0,
            upper=None,
            inverse="generating_unit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegisteredGenerator",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{BB898438-F72C-40a5-9D06-3E70DAE96144}",
        attributes=(
            AttrMeta("capacity_factor", "capacityFactor", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("cold_start_time", "coldStartTime", "float", 0, 1, "primitive"),
            AttrMeta(
                "combined_cycle_operating_mode",
                "combinedCycleOperatingMode",
                "str",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "commericial_operation_date",
                "commericialOperationDate",
                "datetime",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "constrained_output_flag", "constrainedOutputFlag", "YesNo", 0, 1, "enumeration"
            ),
            AttrMeta(
                "energy_down_ramp_rate",
                "energyDownRampRate",
                "ActivePowerChangeRate",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "energy_up_ramp_rate",
                "energyUpRampRate",
                "ActivePowerChangeRate",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("extreme_long_start", "extremeLongStart", "YesNo", 0, 1, "enumeration"),
            AttrMeta("fuel_source", "fuelSource", "FuelSource", 0, 1, "enumeration"),
            AttrMeta("high_control_limit", "highControlLimit", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("hot_int_time", "hotIntTime", "float", 0, 1, "primitive"),
            AttrMeta("hot_start_time", "hotStartTime", "float", 0, 1, "primitive"),
            AttrMeta("int_cold_time", "intColdTime", "float", 0, 1, "primitive"),
            AttrMeta("int_start_time", "intStartTime", "float", 0, 1, "primitive"),
            AttrMeta(
                "load_following_down_mss", "loadFollowingDownMSS", "YesNo", 0, 1, "enumeration"
            ),
            AttrMeta("load_following_up_mss", "loadFollowingUpMSS", "YesNo", 0, 1, "enumeration"),
            AttrMeta("low_control_l_imit", "lowControlLImit", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_dependable_cap", "maxDependableCap", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "maximum_allowable_spinning_reserve",
                "maximumAllowableSpinningReserve",
                "ActivePower",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "maximum_operating_limit",
                "maximumOperatingLimit",
                "ActivePower",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("max_min_load_cost", "maxMinLoadCost", "CostRate", 0, 1, "cimdatatype"),
            AttrMeta("max_pumping_level", "maxPumpingLevel", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_shutdown_time", "maxShutdownTime", "datetime", 0, 1, "primitive"),
            AttrMeta("max_start_ups_per_day", "maxStartUpsPerDay", "int", 0, 1, "primitive"),
            AttrMeta("max_weekly_energy", "maxWeeklyEnergy", "float", 0, 1, "primitive"),
            AttrMeta("max_weekly_starts", "maxWeeklyStarts", "int", 0, 1, "primitive"),
            AttrMeta(
                "minimum_load_cost_basis", "minimumLoadCostBasis", "CostBasis", 0, 1, "enumeration"
            ),
            AttrMeta(
                "minimum_load_fuel_cost",
                "minimumLoadFuelCost",
                "CostPerHeatUnit",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "minimum_operating_limit",
                "minimumOperatingLimit",
                "ActivePower",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("min_load_cost", "minLoadCost", "CostRate", 0, 1, "cimdatatype"),
            AttrMeta("must_offer_ra", "mustOfferRA", "YesNo", 0, 1, "enumeration"),
            AttrMeta("nameplate_capacity", "nameplateCapacity", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "operating_maintenance_cost",
                "operatingMaintenanceCost",
                "CostPerEnergyUnit",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("pumping_cost", "pumpingCost", "CostRate", 0, 1, "cimdatatype"),
            AttrMeta("pumping_factor", "pumpingFactor", "float", 0, 1, "primitive"),
            AttrMeta("pump_min_down_time", "pumpMinDownTime", "float", 0, 1, "primitive"),
            AttrMeta("pump_min_up_time", "pumpMinUpTime", "float", 0, 1, "primitive"),
            AttrMeta("pump_shutdown_cost", "pumpShutdownCost", "float", 0, 1, "primitive"),
            AttrMeta("pump_shutdown_time", "pumpShutdownTime", "int", 0, 1, "primitive"),
            AttrMeta("quick_start_flag", "quickStartFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("ramp_curve_type", "rampCurveType", "RampCurveType", 0, 1, "enumeration"),
            AttrMeta(
                "regulation_down_ramp_rate",
                "regulationDownRampRate",
                "ActivePowerChangeRate",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "regulation_flag", "regulationFlag", "UnitRegulationKind", 0, 1, "enumeration"
            ),
            AttrMeta(
                "regulation_up_ramp_rate",
                "regulationUpRampRate",
                "ActivePowerChangeRate",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("resource_sub_type", "resourceSubType", "str", 0, 1, "primitive"),
            AttrMeta("river_system", "riverSystem", "str", 0, 1, "primitive"),
            AttrMeta("rmnr_flag", "RMNRFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("rmr_flag", "RMRFlag", "FlagTypeRMR", 0, 1, "enumeration"),
            AttrMeta("rmr_manual_indicator", "RMRManualIndicator", "YesNo", 0, 1, "enumeration"),
            AttrMeta("rmt_flag", "RMTFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "spin_ramp_rate", "spinRampRate", "ActivePowerChangeRate", 0, 1, "cimdatatype"
            ),
            AttrMeta("start_up_cost_basis", "startUpCostBasis", "CostBasis", 0, 1, "enumeration"),
            AttrMeta("sync_cond_capable", "syncCondCapable", "YesNo", 0, 1, "enumeration"),
            AttrMeta("unit_type", "unitType", "UnitType", 0, 1, "enumeration"),
            AttrMeta("use_limit_flag", "useLimitFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "variable_energy_resource", "variableEnergyResource", "YesNo", 0, 1, "enumeration"
            ),
        ),
        ends=(
            trade.meta,
            rmr_start_up_energy_curve.meta,
            mkt_heat_rate_curve.meta,
            fuel_region.meta,
            local_reliability_area.meta,
            rmr_start_up_time_curve.meta,
            start_up_cost_curves.meta,
            start_up_energy_curve.meta,
            start_up_time_curve.meta,
            energy_price_index.meta,
            regulating_limit.meta,
            start_up_fuel_curve.meta,
            auxillary_object.meta,
            rmr_start_up_cost_curve.meta,
            generating_bids.meta,
            rmr_start_up_fuel_curve.meta,
            fuel_cost_curve.meta,
            rmr_heat_rate_curve.meta,
            unit_initial_conditions.meta,
        ),
    )

    def __init__(
        self,
        *,
        capacity_factor: float | None = None,
        cold_start_time: float | None = None,
        combined_cycle_operating_mode: str | None = None,
        commericial_operation_date: _dt.datetime | None = None,
        constrained_output_flag: YesNo | None = None,
        energy_down_ramp_rate: float | None = None,
        energy_up_ramp_rate: float | None = None,
        extreme_long_start: YesNo | None = None,
        fuel_source: FuelSource | None = None,
        high_control_limit: float | None = None,
        hot_int_time: float | None = None,
        hot_start_time: float | None = None,
        int_cold_time: float | None = None,
        int_start_time: float | None = None,
        load_following_down_mss: YesNo | None = None,
        load_following_up_mss: YesNo | None = None,
        low_control_l_imit: float | None = None,
        max_dependable_cap: float | None = None,
        maximum_allowable_spinning_reserve: float | None = None,
        maximum_operating_limit: float | None = None,
        max_min_load_cost: float | None = None,
        max_pumping_level: float | None = None,
        max_shutdown_time: _dt.datetime | None = None,
        max_start_ups_per_day: int | None = None,
        max_weekly_energy: float | None = None,
        max_weekly_starts: int | None = None,
        minimum_load_cost_basis: CostBasis | None = None,
        minimum_load_fuel_cost: float | None = None,
        minimum_operating_limit: float | None = None,
        min_load_cost: float | None = None,
        must_offer_ra: YesNo | None = None,
        nameplate_capacity: float | None = None,
        operating_maintenance_cost: float | None = None,
        pumping_cost: float | None = None,
        pumping_factor: float | None = None,
        pump_min_down_time: float | None = None,
        pump_min_up_time: float | None = None,
        pump_shutdown_cost: float | None = None,
        pump_shutdown_time: int | None = None,
        quick_start_flag: YesNo | None = None,
        ramp_curve_type: RampCurveType | None = None,
        regulation_down_ramp_rate: float | None = None,
        regulation_flag: UnitRegulationKind | None = None,
        regulation_up_ramp_rate: float | None = None,
        resource_sub_type: str | None = None,
        river_system: str | None = None,
        rmnr_flag: YesNo | None = None,
        rmr_flag: FlagTypeRMR | None = None,
        rmr_manual_indicator: YesNo | None = None,
        rmt_flag: YesNo | None = None,
        spin_ramp_rate: float | None = None,
        start_up_cost_basis: CostBasis | None = None,
        sync_cond_capable: YesNo | None = None,
        unit_type: UnitType | None = None,
        use_limit_flag: YesNo | None = None,
        variable_energy_resource: YesNo | None = None,
        trade: Iterable[Trade] | None = None,
        rmr_start_up_energy_curve: RMRStartUpEnergyCurve | None = None,
        mkt_heat_rate_curve: MktHeatRateCurve | None = None,
        fuel_region: FuelRegion | None = None,
        local_reliability_area: LocalReliabilityArea | None = None,
        rmr_start_up_time_curve: RMRStartUpTimeCurve | None = None,
        start_up_cost_curves: Iterable[StartUpCostCurve] | None = None,
        start_up_energy_curve: StartUpEnergyCurve | None = None,
        start_up_time_curve: StartUpTimeCurve | None = None,
        energy_price_index: EnergyPriceIndex | None = None,
        regulating_limit: RegulatingLimit | None = None,
        start_up_fuel_curve: StartUpFuelCurve | None = None,
        auxillary_object: Iterable[AuxiliaryObject] | None = None,
        rmr_start_up_cost_curve: RMRStartUpCostCurve | None = None,
        generating_bids: Iterable[GeneratingBid] | None = None,
        rmr_start_up_fuel_curve: RMRStartUpFuelCurve | None = None,
        fuel_cost_curve: FuelCostCurve | None = None,
        rmr_heat_rate_curve: RMRHeatRateCurve | None = None,
        unit_initial_conditions: Iterable[UnitInitialConditions] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capacity_factor = capacity_factor
        self.cold_start_time = cold_start_time
        self.combined_cycle_operating_mode = combined_cycle_operating_mode
        self.commericial_operation_date = commericial_operation_date
        self.constrained_output_flag = constrained_output_flag
        self.energy_down_ramp_rate = energy_down_ramp_rate
        self.energy_up_ramp_rate = energy_up_ramp_rate
        self.extreme_long_start = extreme_long_start
        self.fuel_source = fuel_source
        self.high_control_limit = high_control_limit
        self.hot_int_time = hot_int_time
        self.hot_start_time = hot_start_time
        self.int_cold_time = int_cold_time
        self.int_start_time = int_start_time
        self.load_following_down_mss = load_following_down_mss
        self.load_following_up_mss = load_following_up_mss
        self.low_control_l_imit = low_control_l_imit
        self.max_dependable_cap = max_dependable_cap
        self.maximum_allowable_spinning_reserve = maximum_allowable_spinning_reserve
        self.maximum_operating_limit = maximum_operating_limit
        self.max_min_load_cost = max_min_load_cost
        self.max_pumping_level = max_pumping_level
        self.max_shutdown_time = max_shutdown_time
        self.max_start_ups_per_day = max_start_ups_per_day
        self.max_weekly_energy = max_weekly_energy
        self.max_weekly_starts = max_weekly_starts
        self.minimum_load_cost_basis = minimum_load_cost_basis
        self.minimum_load_fuel_cost = minimum_load_fuel_cost
        self.minimum_operating_limit = minimum_operating_limit
        self.min_load_cost = min_load_cost
        self.must_offer_ra = must_offer_ra
        self.nameplate_capacity = nameplate_capacity
        self.operating_maintenance_cost = operating_maintenance_cost
        self.pumping_cost = pumping_cost
        self.pumping_factor = pumping_factor
        self.pump_min_down_time = pump_min_down_time
        self.pump_min_up_time = pump_min_up_time
        self.pump_shutdown_cost = pump_shutdown_cost
        self.pump_shutdown_time = pump_shutdown_time
        self.quick_start_flag = quick_start_flag
        self.ramp_curve_type = ramp_curve_type
        self.regulation_down_ramp_rate = regulation_down_ramp_rate
        self.regulation_flag = regulation_flag
        self.regulation_up_ramp_rate = regulation_up_ramp_rate
        self.resource_sub_type = resource_sub_type
        self.river_system = river_system
        self.rmnr_flag = rmnr_flag
        self.rmr_flag = rmr_flag
        self.rmr_manual_indicator = rmr_manual_indicator
        self.rmt_flag = rmt_flag
        self.spin_ramp_rate = spin_ramp_rate
        self.start_up_cost_basis = start_up_cost_basis
        self.sync_cond_capable = sync_cond_capable
        self.unit_type = unit_type
        self.use_limit_flag = use_limit_flag
        self.variable_energy_resource = variable_energy_resource
        if trade is not None:
            RegisteredGenerator.trade.extend(self, trade)
        if rmr_start_up_energy_curve is not None:
            self.rmr_start_up_energy_curve = rmr_start_up_energy_curve
        if mkt_heat_rate_curve is not None:
            self.mkt_heat_rate_curve = mkt_heat_rate_curve
        if fuel_region is not None:
            self.fuel_region = fuel_region
        if local_reliability_area is not None:
            self.local_reliability_area = local_reliability_area
        if rmr_start_up_time_curve is not None:
            self.rmr_start_up_time_curve = rmr_start_up_time_curve
        if start_up_cost_curves is not None:
            RegisteredGenerator.start_up_cost_curves.extend(self, start_up_cost_curves)
        if start_up_energy_curve is not None:
            self.start_up_energy_curve = start_up_energy_curve
        if start_up_time_curve is not None:
            self.start_up_time_curve = start_up_time_curve
        if energy_price_index is not None:
            self.energy_price_index = energy_price_index
        if regulating_limit is not None:
            self.regulating_limit = regulating_limit
        if start_up_fuel_curve is not None:
            self.start_up_fuel_curve = start_up_fuel_curve
        if auxillary_object is not None:
            RegisteredGenerator.auxillary_object.extend(self, auxillary_object)
        if rmr_start_up_cost_curve is not None:
            self.rmr_start_up_cost_curve = rmr_start_up_cost_curve
        if generating_bids is not None:
            RegisteredGenerator.generating_bids.extend(self, generating_bids)
        if rmr_start_up_fuel_curve is not None:
            self.rmr_start_up_fuel_curve = rmr_start_up_fuel_curve
        if fuel_cost_curve is not None:
            self.fuel_cost_curve = fuel_cost_curve
        if rmr_heat_rate_curve is not None:
            self.rmr_heat_rate_curve = rmr_heat_rate_curve
        if unit_initial_conditions is not None:
            RegisteredGenerator.unit_initial_conditions.extend(self, unit_initial_conditions)

    def add_trade(self, trade: Trade) -> Self:
        return RegisteredGenerator.trade.add(self, trade)

    def remove_trade(self, trade: Trade) -> Self:
        return RegisteredGenerator.trade.remove(self, trade)

    def clear_trade(self) -> Self:
        return RegisteredGenerator.trade.clear(self)

    def num_trade(self) -> int:
        return RegisteredGenerator.trade.count(self)

    def get_trade_by_mrid(self, mrid: str) -> Trade | None:
        return RegisteredGenerator.trade.get_by_mrid(self, mrid)

    def add_start_up_cost_curve(self, start_up_cost_curve: StartUpCostCurve) -> Self:
        return RegisteredGenerator.start_up_cost_curves.add(self, start_up_cost_curve)

    def remove_start_up_cost_curve(self, start_up_cost_curve: StartUpCostCurve) -> Self:
        return RegisteredGenerator.start_up_cost_curves.remove(self, start_up_cost_curve)

    def clear_start_up_cost_curves(self) -> Self:
        return RegisteredGenerator.start_up_cost_curves.clear(self)

    def num_start_up_cost_curve(self) -> int:
        return RegisteredGenerator.start_up_cost_curves.count(self)

    def get_start_up_cost_curve_by_mrid(self, mrid: str) -> StartUpCostCurve | None:
        return RegisteredGenerator.start_up_cost_curves.get_by_mrid(self, mrid)

    def add_auxillary_object(self, auxillary_object: AuxiliaryObject) -> Self:
        return RegisteredGenerator.auxillary_object.add(self, auxillary_object)

    def remove_auxillary_object(self, auxillary_object: AuxiliaryObject) -> Self:
        return RegisteredGenerator.auxillary_object.remove(self, auxillary_object)

    def clear_auxillary_object(self) -> Self:
        return RegisteredGenerator.auxillary_object.clear(self)

    def num_auxillary_object(self) -> int:
        return RegisteredGenerator.auxillary_object.count(self)

    def add_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return RegisteredGenerator.generating_bids.add(self, generating_bid)

    def remove_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return RegisteredGenerator.generating_bids.remove(self, generating_bid)

    def clear_generating_bids(self) -> Self:
        return RegisteredGenerator.generating_bids.clear(self)

    def num_generating_bid(self) -> int:
        return RegisteredGenerator.generating_bids.count(self)

    def get_generating_bid_by_mrid(self, mrid: str) -> GeneratingBid | None:
        return RegisteredGenerator.generating_bids.get_by_mrid(self, mrid)

    def add_unit_initial_condition(self, unit_initial_condition: UnitInitialConditions) -> Self:
        return RegisteredGenerator.unit_initial_conditions.add(self, unit_initial_condition)

    def remove_unit_initial_condition(self, unit_initial_condition: UnitInitialConditions) -> Self:
        return RegisteredGenerator.unit_initial_conditions.remove(self, unit_initial_condition)

    def clear_unit_initial_conditions(self) -> Self:
        return RegisteredGenerator.unit_initial_conditions.clear(self)

    def num_unit_initial_condition(self) -> int:
        return RegisteredGenerator.unit_initial_conditions.count(self)

    def get_unit_initial_condition_by_mrid(self, mrid: str) -> UnitInitialConditions | None:
        return RegisteredGenerator.unit_initial_conditions.get_by_mrid(self, mrid)
