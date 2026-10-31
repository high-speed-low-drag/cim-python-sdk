"""CIM class EndDevice (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.assets.asset_container import AssetContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.customers.service_location import ServiceLocation
    from cim_python_sdk.model.iec61968.metering.end_device_control import EndDeviceControl
    from cim_python_sdk.model.iec61968.metering.end_device_event import EndDeviceEvent
    from cim_python_sdk.model.iec61968.metering.end_device_function import EndDeviceFunction
    from cim_python_sdk.model.iec61968.metering.end_device_group import EndDeviceGroup
    from cim_python_sdk.model.iec61968.metering.end_device_info import EndDeviceInfo
    from cim_python_sdk.model.iec61968.metering.meter_read_schedule import MeterReadSchedule
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint


class EndDevice(AssetContainer):
    """Asset container that performs one or more end device functions. One type of end device
    is a meter which can perform metering, load management, connect/disconnect, accounting
    functions, etc. Some end devices, such as ones monitoring and controlling air
    conditioners, refrigerators, pool pumps may be connected to a meter. All end devices may
    have communication capability defined by the associated communication function(s). An
    end device may be owned by a consumer, a service provider, utility or otherwise.

    There may be a related end device function that identifies a sensor or control point
    within a metering application or communications systems (e.g., water, gas, electricity).

    Some devices may use an optical port that conforms to the ANSI C12.18 standard for
    communications."""

    __slots__ = (
        "_customer",
        "_end_device_controls",
        "_end_device_events",
        "_end_device_functions",
        "_end_device_groups",
        "_end_device_info",
        "_meter_read_schedule",
        "_service_location_end_devices",
        "_usage_point",
        "amr_system",
        "install_code",
        "is_pan",
        "is_smart_inverter",
        "is_virtual",
        "time_zone_offset",
    )

    is_virtual: bool | None
    is_pan: bool | None
    install_code: str | None
    amr_system: str | None
    time_zone_offset: float | None  # Minutes
    is_smart_inverter: bool | None

    end_device_events: Many[EndDeviceEvent] = Many(
        EndMeta(
            name="end_device_events",
            cim_role="EndDeviceEvents",
            target="cim_python_sdk.model.iec61968.metering.end_device_event:EndDeviceEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device",
            aggregation="none",
        )
    )
    end_device_info: One[EndDeviceInfo] = One(
        EndMeta(
            name="end_device_info",
            cim_role="EndDeviceInfo",
            target="cim_python_sdk.model.iec61968.metering.end_device_info:EndDeviceInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="end_devices",
            aggregation="none",
        )
    )
    end_device_functions: Many[EndDeviceFunction] = Many(
        EndMeta(
            name="end_device_functions",
            cim_role="EndDeviceFunctions",
            target="cim_python_sdk.model.iec61968.metering.end_device_function:EndDeviceFunction",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device",
            aggregation="none",
        )
    )
    end_device_controls: Many[EndDeviceControl] = Many(
        EndMeta(
            name="end_device_controls",
            cim_role="EndDeviceControls",
            target="cim_python_sdk.model.iec61968.metering.end_device_control:EndDeviceControl",
            many=True,
            lower=0,
            upper=None,
            inverse="end_devices",
            aggregation="none",
        )
    )
    usage_point: One[UsagePoint] = One(
        EndMeta(
            name="usage_point",
            cim_role="UsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=False,
            lower=0,
            upper=1,
            inverse="end_devices",
            aggregation="none",
        )
    )
    customer: One[Customer] = One(
        EndMeta(
            name="customer",
            cim_role="Customer",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=False,
            lower=0,
            upper=1,
            inverse="end_devices",
            aggregation="none",
        )
    )
    meter_read_schedule: One[MeterReadSchedule] = One(
        EndMeta(
            name="meter_read_schedule",
            cim_role="MeterReadSchedule",
            target="cim_python_sdk.model.iec61968.metering.meter_read_schedule:MeterReadSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device",
            aggregation="none",
        )
    )
    service_location_end_devices: One[ServiceLocation] = One(
        EndMeta(
            name="service_location_end_devices",
            cim_role="ServiceLocation",
            target="cim_python_sdk.model.iec61968.customers.service_location:ServiceLocation",
            many=False,
            lower=0,
            upper=1,
            inverse="end_devices",
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
            inverse="end_devices",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDevice",
        package="TC57CIM/IEC61968/Metering",
        guid="{E17004EF-EA47-4c62-9520-DA35E34F44D8}",
        attributes=(
            AttrMeta("is_virtual", "isVirtual", "bool", 0, 1, "primitive"),
            AttrMeta("is_pan", "isPan", "bool", 0, 1, "primitive"),
            AttrMeta("install_code", "installCode", "str", 0, 1, "primitive"),
            AttrMeta("amr_system", "amrSystem", "str", 0, 1, "primitive"),
            AttrMeta("time_zone_offset", "timeZoneOffset", "Minutes", 0, 1, "cimdatatype"),
            AttrMeta("is_smart_inverter", "isSmartInverter", "bool", 0, 1, "primitive"),
        ),
        ends=(
            end_device_events.meta,
            end_device_info.meta,
            end_device_functions.meta,
            end_device_controls.meta,
            usage_point.meta,
            customer.meta,
            meter_read_schedule.meta,
            service_location_end_devices.meta,
            end_device_groups.meta,
        ),
    )

    def __init__(
        self,
        *,
        is_virtual: bool | None = None,
        is_pan: bool | None = None,
        install_code: str | None = None,
        amr_system: str | None = None,
        time_zone_offset: float | None = None,
        is_smart_inverter: bool | None = None,
        end_device_events: Iterable[EndDeviceEvent] | None = None,
        end_device_info: EndDeviceInfo | None = None,
        end_device_functions: Iterable[EndDeviceFunction] | None = None,
        end_device_controls: Iterable[EndDeviceControl] | None = None,
        usage_point: UsagePoint | None = None,
        customer: Customer | None = None,
        meter_read_schedule: MeterReadSchedule | None = None,
        service_location_end_devices: ServiceLocation | None = None,
        end_device_groups: Iterable[EndDeviceGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_virtual = is_virtual
        self.is_pan = is_pan
        self.install_code = install_code
        self.amr_system = amr_system
        self.time_zone_offset = time_zone_offset
        self.is_smart_inverter = is_smart_inverter
        if end_device_events is not None:
            EndDevice.end_device_events.extend(self, end_device_events)
        if end_device_info is not None:
            self.end_device_info = end_device_info
        if end_device_functions is not None:
            EndDevice.end_device_functions.extend(self, end_device_functions)
        if end_device_controls is not None:
            EndDevice.end_device_controls.extend(self, end_device_controls)
        if usage_point is not None:
            self.usage_point = usage_point
        if customer is not None:
            self.customer = customer
        if meter_read_schedule is not None:
            self.meter_read_schedule = meter_read_schedule
        if service_location_end_devices is not None:
            self.service_location_end_devices = service_location_end_devices
        if end_device_groups is not None:
            EndDevice.end_device_groups.extend(self, end_device_groups)

    def add_end_device_event(self, end_device_event: EndDeviceEvent) -> Self:
        return EndDevice.end_device_events.add(self, end_device_event)

    def remove_end_device_event(self, end_device_event: EndDeviceEvent) -> Self:
        return EndDevice.end_device_events.remove(self, end_device_event)

    def clear_end_device_events(self) -> Self:
        return EndDevice.end_device_events.clear(self)

    def num_end_device_event(self) -> int:
        return EndDevice.end_device_events.count(self)

    def get_end_device_event_by_mrid(self, mrid: str) -> EndDeviceEvent | None:
        return EndDevice.end_device_events.get_by_mrid(self, mrid)

    def add_end_device_function(self, end_device_function: EndDeviceFunction) -> Self:
        return EndDevice.end_device_functions.add(self, end_device_function)

    def remove_end_device_function(self, end_device_function: EndDeviceFunction) -> Self:
        return EndDevice.end_device_functions.remove(self, end_device_function)

    def clear_end_device_functions(self) -> Self:
        return EndDevice.end_device_functions.clear(self)

    def num_end_device_function(self) -> int:
        return EndDevice.end_device_functions.count(self)

    def get_end_device_function_by_mrid(self, mrid: str) -> EndDeviceFunction | None:
        return EndDevice.end_device_functions.get_by_mrid(self, mrid)

    def add_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return EndDevice.end_device_controls.add(self, end_device_control)

    def remove_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return EndDevice.end_device_controls.remove(self, end_device_control)

    def clear_end_device_controls(self) -> Self:
        return EndDevice.end_device_controls.clear(self)

    def num_end_device_control(self) -> int:
        return EndDevice.end_device_controls.count(self)

    def get_end_device_control_by_mrid(self, mrid: str) -> EndDeviceControl | None:
        return EndDevice.end_device_controls.get_by_mrid(self, mrid)

    def add_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return EndDevice.end_device_groups.add(self, end_device_group)

    def remove_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return EndDevice.end_device_groups.remove(self, end_device_group)

    def clear_end_device_groups(self) -> Self:
        return EndDevice.end_device_groups.clear(self)

    def num_end_device_group(self) -> int:
        return EndDevice.end_device_groups.count(self)

    def get_end_device_group_by_mrid(self, mrid: str) -> EndDeviceGroup | None:
        return EndDevice.end_device_groups.get_by_mrid(self, mrid)
