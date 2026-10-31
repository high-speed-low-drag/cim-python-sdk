"""CIM class EndDeviceGroup (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.common.version import Version
    from cim_python_sdk.model.iec61968.der.der_function import DERFunction
    from cim_python_sdk.model.iec61968.der.der_group_dispatch import DERGroupDispatch
    from cim_python_sdk.model.iec61968.der.der_group_forecast import DERGroupForecast
    from cim_python_sdk.model.iec61968.der.der_monitorable_parameter import DERMonitorableParameter
    from cim_python_sdk.model.iec61968.metering.demand_response_program import DemandResponseProgram
    from cim_python_sdk.model.iec61968.metering.end_device import EndDevice
    from cim_python_sdk.model.iec61968.metering.end_device_control import EndDeviceControl
    from cim_python_sdk.model.iec61968.metering.meter_read_schedule import MeterReadSchedule


class EndDeviceGroup(IdentifiedObject):
    """Abstraction for management of group communications within a two-way AMR system or the
    data for a group of related end devices. Commands can be issued to all of the end
    devices that belong to the group using a defined group address and the underlying AMR
    communication infrastructure. A DERGroup and a PANDeviceGroup is an EndDeviceGroup."""

    __slots__ = (
        "_demand_response_programs",
        "_der_function",
        "_der_function_end_device_group",
        "_der_group_dispatch",
        "_der_group_forecast",
        "_der_monitorable_parameter",
        "_end_device_controls",
        "_end_devices",
        "_meter_read_schedule",
        "status",
        "type",
        "version",
    )

    type: str | None
    status: Status | None
    version: Version | None

    meter_read_schedule: One[MeterReadSchedule] = One(
        EndMeta(
            name="meter_read_schedule",
            cim_role="MeterReadSchedule",
            target="cim_python_sdk.model.iec61968.metering.meter_read_schedule:MeterReadSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device_group",
            aggregation="none",
        )
    )
    demand_response_programs: Many[DemandResponseProgram] = Many(
        EndMeta(
            name="demand_response_programs",
            cim_role="DemandResponsePrograms",
            target="cim_python_sdk.model.iec61968.metering.demand_response_program:DemandResponseProgram",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_groups",
            aggregation="none",
        )
    )
    der_group_dispatch: Many[DERGroupDispatch] = Many(
        EndMeta(
            name="der_group_dispatch",
            cim_role="DERGroupDispatch",
            target="cim_python_sdk.model.iec61968.der.der_group_dispatch:DERGroupDispatch",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_group",
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
            inverse="end_device_groups",
            aggregation="none",
        )
    )
    der_monitorable_parameter: Many[DERMonitorableParameter] = Many(
        EndMeta(
            name="der_monitorable_parameter",
            cim_role="DERMonitorableParameter",
            target="cim_python_sdk.model.iec61968.der.der_monitorable_parameter:DERMonitorableParameter",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_group",
            aggregation="none",
        )
    )
    der_function: One[DERFunction] = One(
        EndMeta(
            name="der_function",
            cim_role="DERFunction",
            target="cim_python_sdk.model.iec61968.der.der_function:DERFunction",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device_group",
            aggregation="none",
        )
    )
    der_function_end_device_group: Many[DERFunction] = Many(
        EndMeta(
            name="der_function_end_device_group",
            cim_role="DER Function",
            target="cim_python_sdk.model.iec61968.der.der_function:DERFunction",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_group_der_function",
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
            inverse="end_device_groups",
            aggregation="none",
        )
    )
    der_group_forecast: Many[DERGroupForecast] = Many(
        EndMeta(
            name="der_group_forecast",
            cim_role="DERGroupForecast",
            target="cim_python_sdk.model.iec61968.der.der_group_forecast:DERGroupForecast",
            many=True,
            lower=1,
            upper=None,
            inverse="end_device_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDeviceGroup",
        package="TC57CIM/IEC61968/Metering",
        guid="{C8623B62-CFD3-4cf7-BFBD-65A72EA7A61E}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
            AttrMeta("version", "version", "Version", 0, 1, "compound"),
        ),
        ends=(
            meter_read_schedule.meta,
            demand_response_programs.meta,
            der_group_dispatch.meta,
            end_device_controls.meta,
            der_monitorable_parameter.meta,
            der_function.meta,
            der_function_end_device_group.meta,
            end_devices.meta,
            der_group_forecast.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        status: Status | None = None,
        version: Version | None = None,
        meter_read_schedule: MeterReadSchedule | None = None,
        demand_response_programs: Iterable[DemandResponseProgram] | None = None,
        der_group_dispatch: Iterable[DERGroupDispatch] | None = None,
        end_device_controls: Iterable[EndDeviceControl] | None = None,
        der_monitorable_parameter: Iterable[DERMonitorableParameter] | None = None,
        der_function: DERFunction | None = None,
        der_function_end_device_group: Iterable[DERFunction] | None = None,
        end_devices: Iterable[EndDevice] | None = None,
        der_group_forecast: Iterable[DERGroupForecast] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.status = status
        self.version = version
        if meter_read_schedule is not None:
            self.meter_read_schedule = meter_read_schedule
        if demand_response_programs is not None:
            EndDeviceGroup.demand_response_programs.extend(self, demand_response_programs)
        if der_group_dispatch is not None:
            EndDeviceGroup.der_group_dispatch.extend(self, der_group_dispatch)
        if end_device_controls is not None:
            EndDeviceGroup.end_device_controls.extend(self, end_device_controls)
        if der_monitorable_parameter is not None:
            EndDeviceGroup.der_monitorable_parameter.extend(self, der_monitorable_parameter)
        if der_function is not None:
            self.der_function = der_function
        if der_function_end_device_group is not None:
            EndDeviceGroup.der_function_end_device_group.extend(self, der_function_end_device_group)
        if end_devices is not None:
            EndDeviceGroup.end_devices.extend(self, end_devices)
        if der_group_forecast is not None:
            EndDeviceGroup.der_group_forecast.extend(self, der_group_forecast)

    def add_demand_response_program(self, demand_response_program: DemandResponseProgram) -> Self:
        return EndDeviceGroup.demand_response_programs.add(self, demand_response_program)

    def remove_demand_response_program(
        self, demand_response_program: DemandResponseProgram
    ) -> Self:
        return EndDeviceGroup.demand_response_programs.remove(self, demand_response_program)

    def clear_demand_response_programs(self) -> Self:
        return EndDeviceGroup.demand_response_programs.clear(self)

    def num_demand_response_program(self) -> int:
        return EndDeviceGroup.demand_response_programs.count(self)

    def get_demand_response_program_by_mrid(self, mrid: str) -> DemandResponseProgram | None:
        return EndDeviceGroup.demand_response_programs.get_by_mrid(self, mrid)

    def add_der_group_dispatch(self, der_group_dispatch: DERGroupDispatch) -> Self:
        return EndDeviceGroup.der_group_dispatch.add(self, der_group_dispatch)

    def remove_der_group_dispatch(self, der_group_dispatch: DERGroupDispatch) -> Self:
        return EndDeviceGroup.der_group_dispatch.remove(self, der_group_dispatch)

    def clear_der_group_dispatch(self) -> Self:
        return EndDeviceGroup.der_group_dispatch.clear(self)

    def num_der_group_dispatch(self) -> int:
        return EndDeviceGroup.der_group_dispatch.count(self)

    def get_der_group_dispatch_by_mrid(self, mrid: str) -> DERGroupDispatch | None:
        return EndDeviceGroup.der_group_dispatch.get_by_mrid(self, mrid)

    def add_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return EndDeviceGroup.end_device_controls.add(self, end_device_control)

    def remove_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return EndDeviceGroup.end_device_controls.remove(self, end_device_control)

    def clear_end_device_controls(self) -> Self:
        return EndDeviceGroup.end_device_controls.clear(self)

    def num_end_device_control(self) -> int:
        return EndDeviceGroup.end_device_controls.count(self)

    def get_end_device_control_by_mrid(self, mrid: str) -> EndDeviceControl | None:
        return EndDeviceGroup.end_device_controls.get_by_mrid(self, mrid)

    def add_der_monitorable_parameter(
        self, der_monitorable_parameter: DERMonitorableParameter
    ) -> Self:
        return EndDeviceGroup.der_monitorable_parameter.add(self, der_monitorable_parameter)

    def remove_der_monitorable_parameter(
        self, der_monitorable_parameter: DERMonitorableParameter
    ) -> Self:
        return EndDeviceGroup.der_monitorable_parameter.remove(self, der_monitorable_parameter)

    def clear_der_monitorable_parameter(self) -> Self:
        return EndDeviceGroup.der_monitorable_parameter.clear(self)

    def num_der_monitorable_parameter(self) -> int:
        return EndDeviceGroup.der_monitorable_parameter.count(self)

    def add_der_function_end_device_group(self, der_function_end_device_group: DERFunction) -> Self:
        return EndDeviceGroup.der_function_end_device_group.add(self, der_function_end_device_group)

    def remove_der_function_end_device_group(
        self, der_function_end_device_group: DERFunction
    ) -> Self:
        return EndDeviceGroup.der_function_end_device_group.remove(
            self, der_function_end_device_group
        )

    def clear_der_function_end_device_group(self) -> Self:
        return EndDeviceGroup.der_function_end_device_group.clear(self)

    def num_der_function_end_device_group(self) -> int:
        return EndDeviceGroup.der_function_end_device_group.count(self)

    def add_end_device(self, end_device: EndDevice) -> Self:
        return EndDeviceGroup.end_devices.add(self, end_device)

    def remove_end_device(self, end_device: EndDevice) -> Self:
        return EndDeviceGroup.end_devices.remove(self, end_device)

    def clear_end_devices(self) -> Self:
        return EndDeviceGroup.end_devices.clear(self)

    def num_end_device(self) -> int:
        return EndDeviceGroup.end_devices.count(self)

    def get_end_device_by_mrid(self, mrid: str) -> EndDevice | None:
        return EndDeviceGroup.end_devices.get_by_mrid(self, mrid)

    def add_der_group_forecast(self, der_group_forecast: DERGroupForecast) -> Self:
        return EndDeviceGroup.der_group_forecast.add(self, der_group_forecast)

    def remove_der_group_forecast(self, der_group_forecast: DERGroupForecast) -> Self:
        return EndDeviceGroup.der_group_forecast.remove(self, der_group_forecast)

    def clear_der_group_forecast(self) -> Self:
        return EndDeviceGroup.der_group_forecast.clear(self)

    def num_der_group_forecast(self) -> int:
        return EndDeviceGroup.der_group_forecast.count(self)

    def get_der_group_forecast_by_mrid(self, mrid: str) -> DERGroupForecast | None:
        return EndDeviceGroup.der_group_forecast.get_by_mrid(self, mrid)
