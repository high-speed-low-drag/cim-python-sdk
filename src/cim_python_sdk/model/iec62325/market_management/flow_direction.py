"""CIM class FlowDirection (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.point import Point
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class FlowDirection(CimObject):
    """The coded identification of the direction of energy flow."""

    __slots__ = ("_point", "_time_series", "direction")

    direction: str | None

    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="flow_direction",
            aggregation="none",
        )
    )
    point: Many[Point] = Many(
        EndMeta(
            name="point",
            cim_role="Point",
            target="cim_python_sdk.model.iec62325.market_management.point:Point",
            many=True,
            lower=0,
            upper=None,
            inverse="flow_direction",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FlowDirection",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{C724715B-5A1F-4393-859C-459860DB9419}",
        attributes=(AttrMeta("direction", "direction", "str", 0, 1, "primitive"),),
        ends=(
            time_series.meta,
            point.meta,
        ),
    )

    def __init__(
        self,
        *,
        direction: str | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        point: Iterable[Point] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.direction = direction
        if time_series is not None:
            FlowDirection.time_series.extend(self, time_series)
        if point is not None:
            FlowDirection.point.extend(self, point)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return FlowDirection.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return FlowDirection.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return FlowDirection.time_series.clear(self)

    def num_time_series(self) -> int:
        return FlowDirection.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return FlowDirection.time_series.get_by_mrid(self, mrid)

    def add_point(self, point: Point) -> Self:
        return FlowDirection.point.add(self, point)

    def remove_point(self, point: Point) -> Self:
        return FlowDirection.point.remove(self, point)

    def clear_point(self) -> Self:
        return FlowDirection.point.clear(self)

    def num_point(self) -> int:
        return FlowDirection.point.count(self)
