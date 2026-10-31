"""CIM class EndDeviceAction (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.end_device_control import EndDeviceControl


class EndDeviceAction(CimObject):
    """Action/command performed by an end device on a device other than the end device."""

    __slots__ = (
        "_end_device_control",
        "command",
        "duration",
        "duration_indefinite",
        "start_date_time",
    )

    command: str | None
    duration: float | None  # Minutes
    duration_indefinite: bool | None
    start_date_time: _dt.datetime | None

    end_device_control: One[EndDeviceControl] = One(
        EndMeta(
            name="end_device_control",
            cim_role="EndDeviceControl",
            target="cim_python_sdk.model.iec61968.metering.end_device_control:EndDeviceControl",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDeviceAction",
        package="TC57CIM/IEC61968/Metering",
        guid="{B4547927-0523-404d-85BF-4BA4176B2AD4}",
        attributes=(
            AttrMeta("command", "command", "str", 0, 1, "primitive"),
            AttrMeta("duration", "duration", "Minutes", 0, 1, "cimdatatype"),
            AttrMeta("duration_indefinite", "durationIndefinite", "bool", 0, 1, "primitive"),
            AttrMeta("start_date_time", "startDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(end_device_control.meta,),
    )

    def __init__(
        self,
        *,
        command: str | None = None,
        duration: float | None = None,
        duration_indefinite: bool | None = None,
        start_date_time: _dt.datetime | None = None,
        end_device_control: EndDeviceControl | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.command = command
        self.duration = duration
        self.duration_indefinite = duration_indefinite
        self.start_date_time = start_date_time
        if end_device_control is not None:
            self.end_device_control = end_device_control
