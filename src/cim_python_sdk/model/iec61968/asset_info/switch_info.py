"""CIM class SwitchInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class SwitchInfo(AssetInfo):
    """<was Switch data.>

    Switch datasheet information."""

    __slots__ = (
        "breaking_capacity",
        "gas_weight_per_tank",
        "is_single_phase",
        "is_unganged",
        "low_pressure_alarm",
        "low_pressure_lock_out",
        "oil_volume_per_tank",
        "rated_current",
        "rated_frequency",
        "rated_impulse_withstand_voltage",
        "rated_interrupting_time",
        "rated_voltage",
    )

    rated_voltage: float | None  # Voltage
    rated_current: float | None  # CurrentFlow
    breaking_capacity: float | None  # CurrentFlow
    is_single_phase: bool | None
    is_unganged: bool | None
    rated_impulse_withstand_voltage: float | None  # Voltage
    rated_frequency: float | None  # Frequency
    rated_interrupting_time: float | None  # Seconds
    low_pressure_alarm: float | None  # Pressure
    low_pressure_lock_out: float | None  # Pressure
    oil_volume_per_tank: float | None  # Volume
    gas_weight_per_tank: float | None  # Mass

    _cim_meta = ClassMeta(
        cim_name="SwitchInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{1F119DDF-DDDB-463e-8712-CA1343550B9A}",
        attributes=(
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("breaking_capacity", "breakingCapacity", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("is_single_phase", "isSinglePhase", "bool", 0, 1, "primitive"),
            AttrMeta("is_unganged", "isUnganged", "bool", 0, 1, "primitive"),
            AttrMeta(
                "rated_impulse_withstand_voltage",
                "ratedImpulseWithstandVoltage",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("rated_frequency", "ratedFrequency", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta(
                "rated_interrupting_time", "ratedInterruptingTime", "Seconds", 0, 1, "cimdatatype"
            ),
            AttrMeta("low_pressure_alarm", "lowPressureAlarm", "Pressure", 0, 1, "cimdatatype"),
            AttrMeta(
                "low_pressure_lock_out", "lowPressureLockOut", "Pressure", 0, 1, "cimdatatype"
            ),
            AttrMeta("oil_volume_per_tank", "oilVolumePerTank", "Volume", 0, 1, "cimdatatype"),
            AttrMeta("gas_weight_per_tank", "gasWeightPerTank", "Mass", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        rated_voltage: float | None = None,
        rated_current: float | None = None,
        breaking_capacity: float | None = None,
        is_single_phase: bool | None = None,
        is_unganged: bool | None = None,
        rated_impulse_withstand_voltage: float | None = None,
        rated_frequency: float | None = None,
        rated_interrupting_time: float | None = None,
        low_pressure_alarm: float | None = None,
        low_pressure_lock_out: float | None = None,
        oil_volume_per_tank: float | None = None,
        gas_weight_per_tank: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rated_voltage = rated_voltage
        self.rated_current = rated_current
        self.breaking_capacity = breaking_capacity
        self.is_single_phase = is_single_phase
        self.is_unganged = is_unganged
        self.rated_impulse_withstand_voltage = rated_impulse_withstand_voltage
        self.rated_frequency = rated_frequency
        self.rated_interrupting_time = rated_interrupting_time
        self.low_pressure_alarm = low_pressure_alarm
        self.low_pressure_lock_out = low_pressure_lock_out
        self.oil_volume_per_tank = oil_volume_per_tank
        self.gas_weight_per_tank = gas_weight_per_tank
