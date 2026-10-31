"""CIM class IrregularIntervalSchedule (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.basic_interval_schedule import BasicIntervalSchedule

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.irregular_time_point import IrregularTimePoint


class IrregularIntervalSchedule(BasicIntervalSchedule):
    """The schedule has time points where the time between them varies."""

    __slots__ = ("_time_points",)

    time_points: Many[IrregularTimePoint] = Many(
        EndMeta(
            name="time_points",
            cim_role="TimePoints",
            target="cim_python_sdk.model.iec61970.base.core.irregular_time_point:IrregularTimePoint",
            many=True,
            lower=1,
            upper=None,
            inverse="interval_schedule",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IrregularIntervalSchedule",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{3CCC0D33-A9DC-49c4-9A3A-7DCF4CF792DE}",
        ends=(time_points.meta,),
    )

    def __init__(
        self,
        *,
        time_points: Iterable[IrregularTimePoint] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if time_points is not None:
            IrregularIntervalSchedule.time_points.extend(self, time_points)

    def add_time_point(self, time_point: IrregularTimePoint) -> Self:
        return IrregularIntervalSchedule.time_points.add(self, time_point)

    def remove_time_point(self, time_point: IrregularTimePoint) -> Self:
        return IrregularIntervalSchedule.time_points.remove(self, time_point)

    def clear_time_points(self) -> Self:
        return IrregularIntervalSchedule.time_points.clear(self)

    def num_time_point(self) -> int:
        return IrregularIntervalSchedule.time_points.count(self)
