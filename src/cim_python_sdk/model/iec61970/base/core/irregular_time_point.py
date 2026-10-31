"""CIM class IrregularTimePoint (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.irregular_interval_schedule import (
        IrregularIntervalSchedule,
    )


class IrregularTimePoint(CimObject):
    """TimePoints for a schedule where the time between the points varies."""

    __slots__ = ("_interval_schedule", "time", "value1", "value2")

    time: float | None  # Seconds
    value1: float | None
    value2: float | None

    interval_schedule: One[IrregularIntervalSchedule] = One(
        EndMeta(
            name="interval_schedule",
            cim_role="IntervalSchedule",
            target="cim_python_sdk.model.iec61970.base.core.irregular_interval_schedule:IrregularIntervalSchedule",
            many=False,
            lower=1,
            upper=1,
            inverse="time_points",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IrregularTimePoint",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{F3BCC51E-D829-45c1-BC79-9A6E463EFB0F}",
        attributes=(
            AttrMeta("time", "time", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("value1", "value1", "float", 0, 1, "primitive"),
            AttrMeta("value2", "value2", "float", 0, 1, "primitive"),
        ),
        ends=(interval_schedule.meta,),
    )

    def __init__(
        self,
        *,
        time: float | None = None,
        value1: float | None = None,
        value2: float | None = None,
        interval_schedule: IrregularIntervalSchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time = time
        self.value1 = value1
        self.value2 = value2
        if interval_schedule is not None:
            self.interval_schedule = interval_schedule
