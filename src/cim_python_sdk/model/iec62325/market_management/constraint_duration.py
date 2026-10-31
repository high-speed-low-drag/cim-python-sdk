"""CIM class ConstraintDuration (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class ConstraintDuration(CimObject):
    """Duration constraint to activate, to put in operation, to deactivate, ... a given event."""

    __slots__ = ("_time_series", "duration", "type")

    duration: str | None
    type: str | None

    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="constraint_duration",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConstraintDuration",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{4CD39F85-BB1B-4b04-BB68-CF9478CADBDF}",
        attributes=(
            AttrMeta("duration", "duration", "str", 0, 1, "primitive"),
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
        ),
        ends=(time_series.meta,),
    )

    def __init__(
        self,
        *,
        duration: str | None = None,
        type: str | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.duration = duration
        self.type = type
        if time_series is not None:
            ConstraintDuration.time_series.extend(self, time_series)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return ConstraintDuration.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return ConstraintDuration.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return ConstraintDuration.time_series.clear(self)

    def num_time_series(self) -> int:
        return ConstraintDuration.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return ConstraintDuration.time_series.get_by_mrid(self, mrid)
