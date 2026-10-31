"""CIM class Period (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec62325.market_management.market_document import MarketDocument
    from cim_python_sdk.model.iec62325.market_management.point import Point
    from cim_python_sdk.model.iec62325.market_management.reason import Reason
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class Period(CimObject):
    """An identification of a time interval that may have a given resolution."""

    __slots__ = (
        "_market_document",
        "_point",
        "_reason",
        "_time_series",
        "resolution",
        "time_interval",
    )

    resolution: str | None
    time_interval: DateTimeInterval | None

    market_document: Many[MarketDocument] = Many(
        EndMeta(
            name="market_document",
            cim_role="MarketDocument",
            target="cim_python_sdk.model.iec62325.market_management.market_document:MarketDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="period",
            aggregation="none",
        )
    )
    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="period",
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
            inverse="period",
            aggregation="none",
        )
    )
    reason: Many[Reason] = Many(
        EndMeta(
            name="reason",
            cim_role="Reason",
            target="cim_python_sdk.model.iec62325.market_management.reason:Reason",
            many=True,
            lower=0,
            upper=None,
            inverse="period",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Period",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{CF8ACB5F-11D6-4e05-9699-7D122B1DA29C}",
        attributes=(
            AttrMeta("resolution", "resolution", "str", 0, 1, "primitive"),
            AttrMeta("time_interval", "timeInterval", "DateTimeInterval", 0, 1, "compound"),
        ),
        ends=(
            market_document.meta,
            time_series.meta,
            point.meta,
            reason.meta,
        ),
    )

    def __init__(
        self,
        *,
        resolution: str | None = None,
        time_interval: DateTimeInterval | None = None,
        market_document: Iterable[MarketDocument] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        point: Iterable[Point] | None = None,
        reason: Iterable[Reason] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.resolution = resolution
        self.time_interval = time_interval
        if market_document is not None:
            Period.market_document.extend(self, market_document)
        if time_series is not None:
            Period.time_series.extend(self, time_series)
        if point is not None:
            Period.point.extend(self, point)
        if reason is not None:
            Period.reason.extend(self, reason)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return Period.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return Period.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return Period.market_document.clear(self)

    def num_market_document(self) -> int:
        return Period.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return Period.market_document.get_by_mrid(self, mrid)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return Period.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return Period.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return Period.time_series.clear(self)

    def num_time_series(self) -> int:
        return Period.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return Period.time_series.get_by_mrid(self, mrid)

    def add_point(self, point: Point) -> Self:
        return Period.point.add(self, point)

    def remove_point(self, point: Point) -> Self:
        return Period.point.remove(self, point)

    def clear_point(self) -> Self:
        return Period.point.clear(self)

    def num_point(self) -> int:
        return Period.point.count(self)

    def add_reason(self, reason: Reason) -> Self:
        return Period.reason.add(self, reason)

    def remove_reason(self, reason: Reason) -> Self:
        return Period.reason.remove(self, reason)

    def clear_reason(self) -> Self:
        return Period.reason.clear(self)

    def num_reason(self) -> int:
        return Period.reason.count(self)
