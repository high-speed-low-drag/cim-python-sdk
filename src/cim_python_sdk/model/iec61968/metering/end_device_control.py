"""CIM class EndDeviceControl (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.end_device import EndDevice
    from cim_python_sdk.model.iec61968.metering.end_device_action import EndDeviceAction
    from cim_python_sdk.model.iec61968.metering.end_device_control_type import EndDeviceControlType
    from cim_python_sdk.model.iec61968.metering.end_device_group import EndDeviceGroup
    from cim_python_sdk.model.iec61968.metering.end_device_timing import EndDeviceTiming
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61968.metering.usage_point_group import UsagePointGroup
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class EndDeviceControl(IdentifiedObject):
    """Instructs an end device (or an end device group) to perform a specified action."""

    __slots__ = (
        "_end_device_action",
        "_end_device_control_type",
        "_end_device_groups",
        "_end_devices",
        "_usage_point_groups",
        "_usage_points",
        "dr_program_level",
        "dr_program_mandatory",
        "issuer_id",
        "issuer_tracking_id",
        "price_signal",
        "primary_device_timing",
        "reason",
        "scheduled_interval",
        "secondary_device_timing",
    )

    issuer_tracking_id: str | None
    issuer_id: str | None
    reason: str | None
    scheduled_interval: DateTimeInterval | None
    price_signal: float | None
    dr_program_level: int | None
    dr_program_mandatory: bool | None
    primary_device_timing: EndDeviceTiming | None
    secondary_device_timing: EndDeviceTiming | None

    end_device_action: One[EndDeviceAction] = One(
        EndMeta(
            name="end_device_action",
            cim_role="EndDeviceAction",
            target="cim_python_sdk.model.iec61968.metering.end_device_action:EndDeviceAction",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device_control",
            aggregation="none",
        )
    )
    end_device_groups: Many[EndDeviceGroup] = Many(
        EndMeta(
            name="end_device_groups",
            cim_role="EndDeviceGroups",
            target="cim_python_sdk.model.iec61968.metering.end_device_group:EndDeviceGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_controls",
            aggregation="none",
        )
    )
    end_devices: Many[EndDevice] = Many(
        EndMeta(
            name="end_devices",
            cim_role="EndDevices",
            target="cim_python_sdk.model.iec61968.metering.end_device:EndDevice",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_controls",
            aggregation="none",
        )
    )
    usage_points: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_points",
            cim_role="UsagePoints",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_controls",
            aggregation="none",
        )
    )
    usage_point_groups: Many[UsagePointGroup] = Many(
        EndMeta(
            name="usage_point_groups",
            cim_role="UsagePointGroups",
            target="cim_python_sdk.model.iec61968.metering.usage_point_group:UsagePointGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_controls",
            aggregation="none",
        )
    )
    end_device_control_type: One[EndDeviceControlType] = One(
        EndMeta(
            name="end_device_control_type",
            cim_role="EndDeviceControlType",
            target="cim_python_sdk.model.iec61968.metering.end_device_control_type:EndDeviceControlType",
            many=False,
            lower=1,
            upper=1,
            inverse="end_device_controls",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDeviceControl",
        package="TC57CIM/IEC61968/Metering",
        guid="{8EBA0240-AFA2-4247-BD90-5F01BF12B58B}",
        attributes=(
            AttrMeta("issuer_tracking_id", "issuerTrackingID", "str", 0, 1, "primitive"),
            AttrMeta("issuer_id", "issuerID", "str", 0, 1, "primitive"),
            AttrMeta("reason", "reason", "str", 0, 1, "primitive"),
            AttrMeta(
                "scheduled_interval", "scheduledInterval", "DateTimeInterval", 0, 1, "compound"
            ),
            AttrMeta("price_signal", "priceSignal", "float", 0, 1, "primitive"),
            AttrMeta("dr_program_level", "drProgramLevel", "int", 0, 1, "primitive"),
            AttrMeta("dr_program_mandatory", "drProgramMandatory", "bool", 0, 1, "primitive"),
            AttrMeta(
                "primary_device_timing", "primaryDeviceTiming", "EndDeviceTiming", 0, 1, "compound"
            ),
            AttrMeta(
                "secondary_device_timing",
                "secondaryDeviceTiming",
                "EndDeviceTiming",
                0,
                1,
                "compound",
            ),
        ),
        ends=(
            end_device_action.meta,
            end_device_groups.meta,
            end_devices.meta,
            usage_points.meta,
            usage_point_groups.meta,
            end_device_control_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        issuer_tracking_id: str | None = None,
        issuer_id: str | None = None,
        reason: str | None = None,
        scheduled_interval: DateTimeInterval | None = None,
        price_signal: float | None = None,
        dr_program_level: int | None = None,
        dr_program_mandatory: bool | None = None,
        primary_device_timing: EndDeviceTiming | None = None,
        secondary_device_timing: EndDeviceTiming | None = None,
        end_device_action: EndDeviceAction | None = None,
        end_device_groups: Iterable[EndDeviceGroup] | None = None,
        end_devices: Iterable[EndDevice] | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        usage_point_groups: Iterable[UsagePointGroup] | None = None,
        end_device_control_type: EndDeviceControlType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.issuer_tracking_id = issuer_tracking_id
        self.issuer_id = issuer_id
        self.reason = reason
        self.scheduled_interval = scheduled_interval
        self.price_signal = price_signal
        self.dr_program_level = dr_program_level
        self.dr_program_mandatory = dr_program_mandatory
        self.primary_device_timing = primary_device_timing
        self.secondary_device_timing = secondary_device_timing
        if end_device_action is not None:
            self.end_device_action = end_device_action
        if end_device_groups is not None:
            EndDeviceControl.end_device_groups.extend(self, end_device_groups)
        if end_devices is not None:
            EndDeviceControl.end_devices.extend(self, end_devices)
        if usage_points is not None:
            EndDeviceControl.usage_points.extend(self, usage_points)
        if usage_point_groups is not None:
            EndDeviceControl.usage_point_groups.extend(self, usage_point_groups)
        if end_device_control_type is not None:
            self.end_device_control_type = end_device_control_type

    def add_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return EndDeviceControl.end_device_groups.add(self, end_device_group)

    def remove_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return EndDeviceControl.end_device_groups.remove(self, end_device_group)

    def clear_end_device_groups(self) -> Self:
        return EndDeviceControl.end_device_groups.clear(self)

    def num_end_device_group(self) -> int:
        return EndDeviceControl.end_device_groups.count(self)

    def get_end_device_group_by_mrid(self, mrid: str) -> EndDeviceGroup | None:
        return EndDeviceControl.end_device_groups.get_by_mrid(self, mrid)

    def add_end_device(self, end_device: EndDevice) -> Self:
        return EndDeviceControl.end_devices.add(self, end_device)

    def remove_end_device(self, end_device: EndDevice) -> Self:
        return EndDeviceControl.end_devices.remove(self, end_device)

    def clear_end_devices(self) -> Self:
        return EndDeviceControl.end_devices.clear(self)

    def num_end_device(self) -> int:
        return EndDeviceControl.end_devices.count(self)

    def get_end_device_by_mrid(self, mrid: str) -> EndDevice | None:
        return EndDeviceControl.end_devices.get_by_mrid(self, mrid)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return EndDeviceControl.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return EndDeviceControl.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return EndDeviceControl.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return EndDeviceControl.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return EndDeviceControl.usage_points.get_by_mrid(self, mrid)

    def add_usage_point_group(self, usage_point_group: UsagePointGroup) -> Self:
        return EndDeviceControl.usage_point_groups.add(self, usage_point_group)

    def remove_usage_point_group(self, usage_point_group: UsagePointGroup) -> Self:
        return EndDeviceControl.usage_point_groups.remove(self, usage_point_group)

    def clear_usage_point_groups(self) -> Self:
        return EndDeviceControl.usage_point_groups.clear(self)

    def num_usage_point_group(self) -> int:
        return EndDeviceControl.usage_point_groups.count(self)

    def get_usage_point_group_by_mrid(self, mrid: str) -> UsagePointGroup | None:
        return EndDeviceControl.usage_point_groups.get_by_mrid(self, mrid)
