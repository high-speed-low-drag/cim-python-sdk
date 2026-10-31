"""CIM class Season (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.load_model.season_day_type_schedule import (
        SeasonDayTypeSchedule,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_value import (
        ScheduledLimitValue,
    )


class Season(IdentifiedObject):
    """A specified time period of the year."""

    __slots__ = ("_scheduled_limits", "_season_day_type_schedules", "end_date", "start_date")

    end_date: str | None
    start_date: str | None

    scheduled_limits: Many[ScheduledLimitValue] = Many(
        EndMeta(
            name="scheduled_limits",
            cim_role="ScheduledLimits",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_value:ScheduledLimitValue",
            many=True,
            lower=0,
            upper=None,
            inverse="season",
            aggregation="none",
        )
    )
    season_day_type_schedules: Many[SeasonDayTypeSchedule] = Many(
        EndMeta(
            name="season_day_type_schedules",
            cim_role="SeasonDayTypeSchedules",
            target="cim_python_sdk.model.iec61970.base.load_model.season_day_type_schedule:SeasonDayTypeSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="season",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Season",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{34DC6AAA-A359-4408-9348-0305AB9E9E9A}",
        attributes=(
            AttrMeta("end_date", "endDate", "str", 0, 1, "primitive"),
            AttrMeta("start_date", "startDate", "str", 0, 1, "primitive"),
        ),
        ends=(
            scheduled_limits.meta,
            season_day_type_schedules.meta,
        ),
    )

    def __init__(
        self,
        *,
        end_date: str | None = None,
        start_date: str | None = None,
        scheduled_limits: Iterable[ScheduledLimitValue] | None = None,
        season_day_type_schedules: Iterable[SeasonDayTypeSchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.end_date = end_date
        self.start_date = start_date
        if scheduled_limits is not None:
            Season.scheduled_limits.extend(self, scheduled_limits)
        if season_day_type_schedules is not None:
            Season.season_day_type_schedules.extend(self, season_day_type_schedules)

    def add_scheduled_limit(self, scheduled_limit: ScheduledLimitValue) -> Self:
        return Season.scheduled_limits.add(self, scheduled_limit)

    def remove_scheduled_limit(self, scheduled_limit: ScheduledLimitValue) -> Self:
        return Season.scheduled_limits.remove(self, scheduled_limit)

    def clear_scheduled_limits(self) -> Self:
        return Season.scheduled_limits.clear(self)

    def num_scheduled_limit(self) -> int:
        return Season.scheduled_limits.count(self)

    def get_scheduled_limit_by_mrid(self, mrid: str) -> ScheduledLimitValue | None:
        return Season.scheduled_limits.get_by_mrid(self, mrid)

    def add_season_day_type_schedule(self, season_day_type_schedule: SeasonDayTypeSchedule) -> Self:
        return Season.season_day_type_schedules.add(self, season_day_type_schedule)

    def remove_season_day_type_schedule(
        self, season_day_type_schedule: SeasonDayTypeSchedule
    ) -> Self:
        return Season.season_day_type_schedules.remove(self, season_day_type_schedule)

    def clear_season_day_type_schedules(self) -> Self:
        return Season.season_day_type_schedules.clear(self)

    def num_season_day_type_schedule(self) -> int:
        return Season.season_day_type_schedules.count(self)

    def get_season_day_type_schedule_by_mrid(self, mrid: str) -> SeasonDayTypeSchedule | None:
        return Season.season_day_type_schedules.get_by_mrid(self, mrid)
