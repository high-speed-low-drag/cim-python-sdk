"""CIM class UsagePointGroup (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.demand_response_program import DemandResponseProgram
    from cim_python_sdk.model.iec61968.metering.end_device_control import EndDeviceControl
    from cim_python_sdk.model.iec61968.metering.meter_read_schedule import MeterReadSchedule
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint


class UsagePointGroup(IdentifiedObject):
    """Abstraction for management of group communications within a two-way AMR system or the
    data for a group of related usage points. Commands can be issued to all of the usage
    points that belong to a usage point group using a defined group address and the
    underlying AMR communication infrastructure."""

    __slots__ = (
        "_demand_response_programs",
        "_end_device_controls",
        "_meter_read_schedule",
        "_usage_points",
        "type",
    )

    type: str | None

    usage_points: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_points",
            cim_role="UsagePoints",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_point_groups",
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
            inverse="usage_point_groups",
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
            inverse="usage_point_group",
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
            inverse="usage_point_groups",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UsagePointGroup",
        package="TC57CIM/IEC61968/Metering",
        guid="{A13F73A0-CF45-42eb-8CDD-A7D37F059989}",
        attributes=(AttrMeta("type", "type", "str", 0, 1, "primitive"),),
        ends=(
            usage_points.meta,
            demand_response_programs.meta,
            meter_read_schedule.meta,
            end_device_controls.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        demand_response_programs: Iterable[DemandResponseProgram] | None = None,
        meter_read_schedule: MeterReadSchedule | None = None,
        end_device_controls: Iterable[EndDeviceControl] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        if usage_points is not None:
            UsagePointGroup.usage_points.extend(self, usage_points)
        if demand_response_programs is not None:
            UsagePointGroup.demand_response_programs.extend(self, demand_response_programs)
        if meter_read_schedule is not None:
            self.meter_read_schedule = meter_read_schedule
        if end_device_controls is not None:
            UsagePointGroup.end_device_controls.extend(self, end_device_controls)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return UsagePointGroup.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return UsagePointGroup.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return UsagePointGroup.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return UsagePointGroup.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return UsagePointGroup.usage_points.get_by_mrid(self, mrid)

    def add_demand_response_program(self, demand_response_program: DemandResponseProgram) -> Self:
        return UsagePointGroup.demand_response_programs.add(self, demand_response_program)

    def remove_demand_response_program(
        self, demand_response_program: DemandResponseProgram
    ) -> Self:
        return UsagePointGroup.demand_response_programs.remove(self, demand_response_program)

    def clear_demand_response_programs(self) -> Self:
        return UsagePointGroup.demand_response_programs.clear(self)

    def num_demand_response_program(self) -> int:
        return UsagePointGroup.demand_response_programs.count(self)

    def get_demand_response_program_by_mrid(self, mrid: str) -> DemandResponseProgram | None:
        return UsagePointGroup.demand_response_programs.get_by_mrid(self, mrid)

    def add_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return UsagePointGroup.end_device_controls.add(self, end_device_control)

    def remove_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return UsagePointGroup.end_device_controls.remove(self, end_device_control)

    def clear_end_device_controls(self) -> Self:
        return UsagePointGroup.end_device_controls.clear(self)

    def num_end_device_control(self) -> int:
        return UsagePointGroup.end_device_controls.count(self)

    def get_end_device_control_by_mrid(self, mrid: str) -> EndDeviceControl | None:
        return UsagePointGroup.end_device_controls.get_by_mrid(self, mrid)
