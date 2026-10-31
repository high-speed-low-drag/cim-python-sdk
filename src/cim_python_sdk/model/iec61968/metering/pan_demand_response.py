"""CIM class PanDemandResponse (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.metering.end_device_action import EndDeviceAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.controlled_appliance import ControlledAppliance


class PanDemandResponse(EndDeviceAction):
    """PAN control used to issue action/command to PAN devices during a demand response/load
    control event."""

    __slots__ = (
        "appliance",
        "avg_load_adjustment",
        "cancel_control_mode",
        "cancel_date_time",
        "cancel_now",
        "cooling_offset",
        "cooling_setpoint",
        "criticality_level",
        "duty_cycle",
        "enrollment_group",
        "heating_offset",
        "heating_setpoint",
    )

    appliance: ControlledAppliance | None
    avg_load_adjustment: float | None  # PerCent
    cooling_offset: float | None  # Temperature
    cooling_setpoint: float | None  # Temperature
    duty_cycle: float | None  # PerCent
    heating_offset: float | None  # Temperature
    heating_setpoint: float | None  # Temperature
    cancel_control_mode: str | None
    cancel_date_time: _dt.datetime | None
    cancel_now: bool | None
    criticality_level: str | None
    enrollment_group: str | None

    _cim_meta = ClassMeta(
        cim_name="PanDemandResponse",
        package="TC57CIM/IEC61968/Metering",
        guid="{6203B004-2A00-4ce1-A8ED-546B60C392C6}",
        attributes=(
            AttrMeta("appliance", "appliance", "ControlledAppliance", 0, 1, "compound"),
            AttrMeta("avg_load_adjustment", "avgLoadAdjustment", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("cooling_offset", "coolingOffset", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("cooling_setpoint", "coolingSetpoint", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("duty_cycle", "dutyCycle", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("heating_offset", "heatingOffset", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("heating_setpoint", "heatingSetpoint", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("cancel_control_mode", "cancelControlMode", "str", 0, 1, "primitive"),
            AttrMeta("cancel_date_time", "cancelDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("cancel_now", "cancelNow", "bool", 0, 1, "primitive"),
            AttrMeta("criticality_level", "criticalityLevel", "str", 0, 1, "primitive"),
            AttrMeta("enrollment_group", "enrollmentGroup", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        appliance: ControlledAppliance | None = None,
        avg_load_adjustment: float | None = None,
        cooling_offset: float | None = None,
        cooling_setpoint: float | None = None,
        duty_cycle: float | None = None,
        heating_offset: float | None = None,
        heating_setpoint: float | None = None,
        cancel_control_mode: str | None = None,
        cancel_date_time: _dt.datetime | None = None,
        cancel_now: bool | None = None,
        criticality_level: str | None = None,
        enrollment_group: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.appliance = appliance
        self.avg_load_adjustment = avg_load_adjustment
        self.cooling_offset = cooling_offset
        self.cooling_setpoint = cooling_setpoint
        self.duty_cycle = duty_cycle
        self.heating_offset = heating_offset
        self.heating_setpoint = heating_setpoint
        self.cancel_control_mode = cancel_control_mode
        self.cancel_date_time = cancel_date_time
        self.cancel_now = cancel_now
        self.criticality_level = criticality_level
        self.enrollment_group = enrollment_group
