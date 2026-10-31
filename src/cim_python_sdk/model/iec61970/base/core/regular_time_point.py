"""CIM class RegularTimePoint (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
        RegularIntervalSchedule,
    )


class RegularTimePoint(CimObject):
    """Time point for a schedule where the time between the consecutive points is constant."""

    __slots__ = ("_interval_schedule", "sequence_number", "value1", "value2")

    sequence_number: int | None
    value1: float | None
    value2: float | None

    interval_schedule: One[RegularIntervalSchedule] = One(
        EndMeta(
            name="interval_schedule",
            cim_role="IntervalSchedule",
            target="cim_python_sdk.model.iec61970.base.core.regular_interval_schedule:RegularIntervalSchedule",
            many=False,
            lower=1,
            upper=1,
            inverse="time_points",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegularTimePoint",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{8E858A31-A91C-4e9f-BEFA-6604EE4A4E30}",
        attributes=(
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("value1", "value1", "float", 0, 1, "primitive"),
            AttrMeta("value2", "value2", "float", 0, 1, "primitive"),
        ),
        ends=(interval_schedule.meta,),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        value1: float | None = None,
        value2: float | None = None,
        interval_schedule: RegularIntervalSchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        self.value1 = value1
        self.value2 = value2
        if interval_schedule is not None:
            self.interval_schedule = interval_schedule
