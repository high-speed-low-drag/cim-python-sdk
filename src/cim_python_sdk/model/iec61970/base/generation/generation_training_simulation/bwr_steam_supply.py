"""CIM class BWRSteamSupply (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.steam_supply import (
    SteamSupply,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class BWRSteamSupply(SteamSupply):
    """Boiling water reactor used as a steam supply to a steam turbine."""

    __slots__ = (
        "high_power_limit",
        "in_core_thermal_tc",
        "integral_gain",
        "low_power_limit",
        "lower_limit",
        "pressure_limit",
        "pressure_setpoint_ga",
        "pressure_setpoint_tc1",
        "pressure_setpoint_tc2",
        "proportional_gain",
        "rf_aux1",
        "rf_aux2",
        "rf_aux3",
        "rf_aux4",
        "rf_aux5",
        "rf_aux6",
        "rf_aux7",
        "rf_aux8",
        "rod_pattern",
        "rod_pattern_constant",
        "upper_limit",
    )

    high_power_limit: float | None  # PU
    in_core_thermal_tc: float | None  # Seconds
    integral_gain: float | None
    lower_limit: float | None  # PU
    low_power_limit: float | None  # PU
    pressure_limit: float | None  # PU
    pressure_setpoint_ga: float | None
    pressure_setpoint_tc1: float | None  # Seconds
    pressure_setpoint_tc2: float | None  # Seconds
    proportional_gain: float | None
    rf_aux1: float | None  # PU
    rf_aux2: float | None  # PU
    rf_aux3: float | None  # PU
    rf_aux4: float | None  # PU
    rf_aux5: float | None  # PU
    rf_aux6: float | None  # PU
    rf_aux7: float | None  # PU
    rf_aux8: float | None  # PU
    rod_pattern: float | None  # PU
    rod_pattern_constant: float | None
    upper_limit: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="BWRSteamSupply",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{0AF61476-B124-42e0-8DB8-09FDC27BA8EF}",
        attributes=(
            AttrMeta("high_power_limit", "highPowerLimit", "PU", 0, 1, "cimdatatype"),
            AttrMeta("in_core_thermal_tc", "inCoreThermalTC", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("integral_gain", "integralGain", "float", 0, 1, "primitive"),
            AttrMeta("lower_limit", "lowerLimit", "PU", 0, 1, "cimdatatype"),
            AttrMeta("low_power_limit", "lowPowerLimit", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pressure_limit", "pressureLimit", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pressure_setpoint_ga", "pressureSetpointGA", "float", 0, 1, "primitive"),
            AttrMeta(
                "pressure_setpoint_tc1", "pressureSetpointTC1", "Seconds", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "pressure_setpoint_tc2", "pressureSetpointTC2", "Seconds", 0, 1, "cimdatatype"
            ),
            AttrMeta("proportional_gain", "proportionalGain", "float", 0, 1, "primitive"),
            AttrMeta("rf_aux1", "rfAux1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rf_aux2", "rfAux2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rf_aux3", "rfAux3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rf_aux4", "rfAux4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rf_aux5", "rfAux5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rf_aux6", "rfAux6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rf_aux7", "rfAux7", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rf_aux8", "rfAux8", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rod_pattern", "rodPattern", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rod_pattern_constant", "rodPatternConstant", "float", 0, 1, "primitive"),
            AttrMeta("upper_limit", "upperLimit", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        high_power_limit: float | None = None,
        in_core_thermal_tc: float | None = None,
        integral_gain: float | None = None,
        lower_limit: float | None = None,
        low_power_limit: float | None = None,
        pressure_limit: float | None = None,
        pressure_setpoint_ga: float | None = None,
        pressure_setpoint_tc1: float | None = None,
        pressure_setpoint_tc2: float | None = None,
        proportional_gain: float | None = None,
        rf_aux1: float | None = None,
        rf_aux2: float | None = None,
        rf_aux3: float | None = None,
        rf_aux4: float | None = None,
        rf_aux5: float | None = None,
        rf_aux6: float | None = None,
        rf_aux7: float | None = None,
        rf_aux8: float | None = None,
        rod_pattern: float | None = None,
        rod_pattern_constant: float | None = None,
        upper_limit: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.high_power_limit = high_power_limit
        self.in_core_thermal_tc = in_core_thermal_tc
        self.integral_gain = integral_gain
        self.lower_limit = lower_limit
        self.low_power_limit = low_power_limit
        self.pressure_limit = pressure_limit
        self.pressure_setpoint_ga = pressure_setpoint_ga
        self.pressure_setpoint_tc1 = pressure_setpoint_tc1
        self.pressure_setpoint_tc2 = pressure_setpoint_tc2
        self.proportional_gain = proportional_gain
        self.rf_aux1 = rf_aux1
        self.rf_aux2 = rf_aux2
        self.rf_aux3 = rf_aux3
        self.rf_aux4 = rf_aux4
        self.rf_aux5 = rf_aux5
        self.rf_aux6 = rf_aux6
        self.rf_aux7 = rf_aux7
        self.rf_aux8 = rf_aux8
        self.rod_pattern = rod_pattern
        self.rod_pattern_constant = rod_pattern_constant
        self.upper_limit = upper_limit
