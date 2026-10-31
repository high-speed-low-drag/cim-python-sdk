"""CIM class TimePoint (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.common.time_schedule import TimeSchedule
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class TimePoint(IdentifiedObject):
    """A point in time within a sequence of points in time relative to a time schedule."""

    __slots__ = (
        "_time_schedule",
        "date_time",
        "relative_time_interval",
        "sequence_number",
        "status",
        "window",
    )

    date_time: _dt.datetime | None
    relative_time_interval: float | None  # Seconds
    sequence_number: int | None
    window: DateTimeInterval | None
    status: Status | None

    time_schedule: One[TimeSchedule] = One(
        EndMeta(
            name="time_schedule",
            cim_role="TimeSchedule",
            target="cim_python_sdk.model.iec61968.common.time_schedule:TimeSchedule",
            many=False,
            lower=1,
            upper=1,
            inverse="time_points",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TimePoint",
        package="TC57CIM/IEC61968/Common",
        guid="{336EA49A-BDDF-47d3-A9BC-B1B5BD070ED4}",
        attributes=(
            AttrMeta("date_time", "dateTime", "datetime", 0, 1, "primitive"),
            AttrMeta(
                "relative_time_interval", "relativeTimeInterval", "Seconds", 0, 1, "cimdatatype"
            ),
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("window", "window", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(time_schedule.meta,),
    )

    def __init__(
        self,
        *,
        date_time: _dt.datetime | None = None,
        relative_time_interval: float | None = None,
        sequence_number: int | None = None,
        window: DateTimeInterval | None = None,
        status: Status | None = None,
        time_schedule: TimeSchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.date_time = date_time
        self.relative_time_interval = relative_time_interval
        self.sequence_number = sequence_number
        self.window = window
        self.status = status
        if time_schedule is not None:
            self.time_schedule = time_schedule
