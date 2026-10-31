"""CIM class DayType (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.load_model.season_day_type_schedule import (
        SeasonDayTypeSchedule,
    )


class DayType(IdentifiedObject):
    """Group of similar days. For example it could be used to represent weekdays, weekend, or
    holidays."""

    __slots__ = ("_season_day_type_schedules",)

    season_day_type_schedules: Many[SeasonDayTypeSchedule] = Many(
        EndMeta(
            name="season_day_type_schedules",
            cim_role="SeasonDayTypeSchedules",
            target="cim_python_sdk.model.iec61970.base.load_model.season_day_type_schedule:SeasonDayTypeSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="day_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DayType",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{FC479F3A-125F-4b0c-835F-6BE1361D1378}",
        ends=(season_day_type_schedules.meta,),
    )

    def __init__(
        self,
        *,
        season_day_type_schedules: Iterable[SeasonDayTypeSchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if season_day_type_schedules is not None:
            DayType.season_day_type_schedules.extend(self, season_day_type_schedules)

    def add_season_day_type_schedule(self, season_day_type_schedule: SeasonDayTypeSchedule) -> Self:
        return DayType.season_day_type_schedules.add(self, season_day_type_schedule)

    def remove_season_day_type_schedule(
        self, season_day_type_schedule: SeasonDayTypeSchedule
    ) -> Self:
        return DayType.season_day_type_schedules.remove(self, season_day_type_schedule)

    def clear_season_day_type_schedules(self) -> Self:
        return DayType.season_day_type_schedules.clear(self)

    def num_season_day_type_schedule(self) -> int:
        return DayType.season_day_type_schedules.count(self)

    def get_season_day_type_schedule_by_mrid(self, mrid: str) -> SeasonDayTypeSchedule | None:
        return DayType.season_day_type_schedules.get_by_mrid(self, mrid)
