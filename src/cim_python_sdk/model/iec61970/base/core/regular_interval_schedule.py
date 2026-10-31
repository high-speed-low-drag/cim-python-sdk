"""CIM class RegularIntervalSchedule (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.basic_interval_schedule import BasicIntervalSchedule

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.regular_time_point import RegularTimePoint


class RegularIntervalSchedule(BasicIntervalSchedule):
    """The schedule has time points where the time between them is constant."""

    __slots__ = ("_time_points", "end_time", "time_step")

    end_time: _dt.datetime | None
    time_step: float | None  # Seconds

    time_points: Many[RegularTimePoint] = Many(
        EndMeta(
            name="time_points",
            cim_role="TimePoints",
            target="cim_python_sdk.model.iec61970.base.core.regular_time_point:RegularTimePoint",
            many=True,
            lower=1,
            upper=None,
            inverse="interval_schedule",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegularIntervalSchedule",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{A2B1A5C3-6129-4e3b-A1B5-1AC417DEF3AA}",
        attributes=(
            AttrMeta("end_time", "endTime", "datetime", 0, 1, "primitive"),
            AttrMeta("time_step", "timeStep", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(time_points.meta,),
    )

    def __init__(
        self,
        *,
        end_time: _dt.datetime | None = None,
        time_step: float | None = None,
        time_points: Iterable[RegularTimePoint] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.end_time = end_time
        self.time_step = time_step
        if time_points is not None:
            RegularIntervalSchedule.time_points.extend(self, time_points)

    def add_time_point(self, time_point: RegularTimePoint) -> Self:
        return RegularIntervalSchedule.time_points.add(self, time_point)

    def remove_time_point(self, time_point: RegularTimePoint) -> Self:
        return RegularIntervalSchedule.time_points.remove(self, time_point)

    def clear_time_points(self) -> Self:
        return RegularIntervalSchedule.time_points.clear(self)

    def num_time_point(self) -> int:
        return RegularIntervalSchedule.time_points.count(self)
