"""CIM class TimeSchedule (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.time_point import TimePoint
    from cim_python_sdk.model.iec61968.metering.meter_read_schedule import MeterReadSchedule
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class TimeSchedule(Document):
    """Description of anything that changes through time. Time schedule is used to perform a
    single-valued function of time. Use inherited 'type' attribute to give additional
    information on this schedule, such as: periodic (hourly, daily, weekly, monthly, etc.),
    day of the month, by date, calendar (specific times and dates)."""

    __slots__ = (
        "_meter_read_schedule",
        "_time_points",
        "disabled",
        "offset",
        "recurrence_pattern",
        "recurrence_period",
        "schedule_interval",
    )

    disabled: bool | None
    schedule_interval: DateTimeInterval | None
    recurrence_pattern: str | None
    recurrence_period: float | None  # Seconds
    offset: float | None  # Seconds

    time_points: Many[TimePoint] = Many(
        EndMeta(
            name="time_points",
            cim_role="TimePoints",
            target="cim_python_sdk.model.iec61968.common.time_point:TimePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="time_schedule",
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
            inverse="time_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TimeSchedule",
        package="TC57CIM/IEC61968/Common",
        guid="{49D4B4E2-FF11-4a48-8418-7E660E6B34C8}",
        attributes=(
            AttrMeta("disabled", "disabled", "bool", 0, 1, "primitive"),
            AttrMeta("schedule_interval", "scheduleInterval", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("recurrence_pattern", "recurrencePattern", "str", 0, 1, "primitive"),
            AttrMeta("recurrence_period", "recurrencePeriod", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("offset", "offset", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(
            time_points.meta,
            meter_read_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        disabled: bool | None = None,
        schedule_interval: DateTimeInterval | None = None,
        recurrence_pattern: str | None = None,
        recurrence_period: float | None = None,
        offset: float | None = None,
        time_points: Iterable[TimePoint] | None = None,
        meter_read_schedule: MeterReadSchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.disabled = disabled
        self.schedule_interval = schedule_interval
        self.recurrence_pattern = recurrence_pattern
        self.recurrence_period = recurrence_period
        self.offset = offset
        if time_points is not None:
            TimeSchedule.time_points.extend(self, time_points)
        if meter_read_schedule is not None:
            self.meter_read_schedule = meter_read_schedule

    def add_time_point(self, time_point: TimePoint) -> Self:
        return TimeSchedule.time_points.add(self, time_point)

    def remove_time_point(self, time_point: TimePoint) -> Self:
        return TimeSchedule.time_points.remove(self, time_point)

    def clear_time_points(self) -> Self:
        return TimeSchedule.time_points.clear(self)

    def num_time_point(self) -> int:
        return TimeSchedule.time_points.count(self)

    def get_time_point_by_mrid(self, mrid: str) -> TimePoint | None:
        return TimeSchedule.time_points.get_by_mrid(self, mrid)
