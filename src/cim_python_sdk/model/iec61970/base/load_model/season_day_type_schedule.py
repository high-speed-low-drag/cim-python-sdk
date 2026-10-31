"""CIM class SeasonDayTypeSchedule (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.load_model.day_type import DayType
    from cim_python_sdk.model.iec61970.base.load_model.season import Season


class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """A time schedule covering a 24 hour period, with curve data for a specific type of season
    and day."""

    __slots__ = ("_day_type", "_season")

    day_type: One[DayType] = One(
        EndMeta(
            name="day_type",
            cim_role="DayType",
            target="cim_python_sdk.model.iec61970.base.load_model.day_type:DayType",
            many=False,
            lower=0,
            upper=1,
            inverse="season_day_type_schedules",
            aggregation="none",
        )
    )
    season: One[Season] = One(
        EndMeta(
            name="season",
            cim_role="Season",
            target="cim_python_sdk.model.iec61970.base.load_model.season:Season",
            many=False,
            lower=0,
            upper=1,
            inverse="season_day_type_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SeasonDayTypeSchedule",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{56D10F07-3518-4dec-BAD8-82B5ED26C817}",
        ends=(
            day_type.meta,
            season.meta,
        ),
    )

    def __init__(
        self,
        *,
        day_type: DayType | None = None,
        season: Season | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if day_type is not None:
            self.day_type = day_type
        if season is not None:
            self.season = season
