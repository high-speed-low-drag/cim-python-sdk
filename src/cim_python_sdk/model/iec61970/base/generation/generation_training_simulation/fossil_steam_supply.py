"""CIM class FossilSteamSupply (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.steam_supply import (
    SteamSupply,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.boiler_control_mode import (
        BoilerControlMode,
    )


class FossilSteamSupply(SteamSupply):
    """Fossil fuelled boiler (e.g., coal, oil, gas)."""

    __slots__ = (
        "aux_power_versus_frequency",
        "aux_power_versus_voltage",
        "boiler_control_mode",
        "control_error_bias_p",
        "control_ic",
        "control_pc",
        "control_peb",
        "control_ped",
        "control_tc",
        "feed_water_ig",
        "feed_water_pg",
        "feed_water_tc",
        "fuel_demand_limit",
        "fuel_supply_delay",
        "fuel_supply_tc",
        "max_error_rate_p",
        "mech_power_sensor_lag",
        "min_error_rate_p",
        "pressure_ctrl_dg",
        "pressure_ctrl_ig",
        "pressure_ctrl_pg",
        "pressure_feedback",
        "super_heater1_capacity",
        "super_heater2_capacity",
        "super_heater_pipe_pd",
        "throttle_pressure_sp",
    )

    aux_power_versus_frequency: float | None  # PU
    aux_power_versus_voltage: float | None  # PU
    boiler_control_mode: BoilerControlMode | None
    control_error_bias_p: float | None
    control_ic: float | None
    control_pc: float | None
    control_peb: float | None
    control_ped: float | None  # PU
    control_tc: float | None
    feed_water_ig: float | None
    feed_water_pg: float | None
    feed_water_tc: float | None  # Seconds
    fuel_demand_limit: float | None  # PU
    fuel_supply_delay: float | None  # Seconds
    fuel_supply_tc: float | None  # Seconds
    max_error_rate_p: float | None
    mech_power_sensor_lag: float | None  # Seconds
    min_error_rate_p: float | None
    pressure_ctrl_dg: float | None
    pressure_ctrl_ig: float | None
    pressure_ctrl_pg: float | None
    pressure_feedback: int | None
    super_heater1_capacity: float | None
    super_heater2_capacity: float | None
    super_heater_pipe_pd: float | None
    throttle_pressure_sp: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="FossilSteamSupply",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{47678786-032B-421a-A56B-CC5EFE4A269D}",
        attributes=(
            AttrMeta(
                "aux_power_versus_frequency", "auxPowerVersusFrequency", "PU", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "aux_power_versus_voltage", "auxPowerVersusVoltage", "PU", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "boiler_control_mode", "boilerControlMode", "BoilerControlMode", 0, 1, "enumeration"
            ),
            AttrMeta("control_error_bias_p", "controlErrorBiasP", "float", 0, 1, "primitive"),
            AttrMeta("control_ic", "controlIC", "float", 0, 1, "primitive"),
            AttrMeta("control_pc", "controlPC", "float", 0, 1, "primitive"),
            AttrMeta("control_peb", "controlPEB", "float", 0, 1, "primitive"),
            AttrMeta("control_ped", "controlPED", "PU", 0, 1, "cimdatatype"),
            AttrMeta("control_tc", "controlTC", "float", 0, 1, "primitive"),
            AttrMeta("feed_water_ig", "feedWaterIG", "float", 0, 1, "primitive"),
            AttrMeta("feed_water_pg", "feedWaterPG", "float", 0, 1, "primitive"),
            AttrMeta("feed_water_tc", "feedWaterTC", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("fuel_demand_limit", "fuelDemandLimit", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fuel_supply_delay", "fuelSupplyDelay", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("fuel_supply_tc", "fuelSupplyTC", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("max_error_rate_p", "maxErrorRateP", "float", 0, 1, "primitive"),
            AttrMeta("mech_power_sensor_lag", "mechPowerSensorLag", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("min_error_rate_p", "minErrorRateP", "float", 0, 1, "primitive"),
            AttrMeta("pressure_ctrl_dg", "pressureCtrlDG", "float", 0, 1, "primitive"),
            AttrMeta("pressure_ctrl_ig", "pressureCtrlIG", "float", 0, 1, "primitive"),
            AttrMeta("pressure_ctrl_pg", "pressureCtrlPG", "float", 0, 1, "primitive"),
            AttrMeta("pressure_feedback", "pressureFeedback", "int", 0, 1, "primitive"),
            AttrMeta("super_heater1_capacity", "superHeater1Capacity", "float", 0, 1, "primitive"),
            AttrMeta("super_heater2_capacity", "superHeater2Capacity", "float", 0, 1, "primitive"),
            AttrMeta("super_heater_pipe_pd", "superHeaterPipePD", "float", 0, 1, "primitive"),
            AttrMeta("throttle_pressure_sp", "throttlePressureSP", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        aux_power_versus_frequency: float | None = None,
        aux_power_versus_voltage: float | None = None,
        boiler_control_mode: BoilerControlMode | None = None,
        control_error_bias_p: float | None = None,
        control_ic: float | None = None,
        control_pc: float | None = None,
        control_peb: float | None = None,
        control_ped: float | None = None,
        control_tc: float | None = None,
        feed_water_ig: float | None = None,
        feed_water_pg: float | None = None,
        feed_water_tc: float | None = None,
        fuel_demand_limit: float | None = None,
        fuel_supply_delay: float | None = None,
        fuel_supply_tc: float | None = None,
        max_error_rate_p: float | None = None,
        mech_power_sensor_lag: float | None = None,
        min_error_rate_p: float | None = None,
        pressure_ctrl_dg: float | None = None,
        pressure_ctrl_ig: float | None = None,
        pressure_ctrl_pg: float | None = None,
        pressure_feedback: int | None = None,
        super_heater1_capacity: float | None = None,
        super_heater2_capacity: float | None = None,
        super_heater_pipe_pd: float | None = None,
        throttle_pressure_sp: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.aux_power_versus_frequency = aux_power_versus_frequency
        self.aux_power_versus_voltage = aux_power_versus_voltage
        self.boiler_control_mode = boiler_control_mode
        self.control_error_bias_p = control_error_bias_p
        self.control_ic = control_ic
        self.control_pc = control_pc
        self.control_peb = control_peb
        self.control_ped = control_ped
        self.control_tc = control_tc
        self.feed_water_ig = feed_water_ig
        self.feed_water_pg = feed_water_pg
        self.feed_water_tc = feed_water_tc
        self.fuel_demand_limit = fuel_demand_limit
        self.fuel_supply_delay = fuel_supply_delay
        self.fuel_supply_tc = fuel_supply_tc
        self.max_error_rate_p = max_error_rate_p
        self.mech_power_sensor_lag = mech_power_sensor_lag
        self.min_error_rate_p = min_error_rate_p
        self.pressure_ctrl_dg = pressure_ctrl_dg
        self.pressure_ctrl_ig = pressure_ctrl_ig
        self.pressure_ctrl_pg = pressure_ctrl_pg
        self.pressure_feedback = pressure_feedback
        self.super_heater1_capacity = super_heater1_capacity
        self.super_heater2_capacity = super_heater2_capacity
        self.super_heater_pipe_pd = super_heater_pipe_pd
        self.throttle_pressure_sp = throttle_pressure_sp
