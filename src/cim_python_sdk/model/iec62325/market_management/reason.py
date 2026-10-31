"""CIM class Reason (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_management.market_document import MarketDocument
    from cim_python_sdk.model.iec62325.market_management.period import Period
    from cim_python_sdk.model.iec62325.market_management.point import Point
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class Reason(CimObject):
    """The motivation of an act."""

    __slots__ = (
        "_market_document",
        "_period",
        "_point",
        "_registered_resource",
        "_time_series",
        "code",
        "text",
    )

    code: str | None
    text: str | None

    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="reason",
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
            inverse="reason",
            aggregation="none",
        )
    )
    market_document: Many[MarketDocument] = Many(
        EndMeta(
            name="market_document",
            cim_role="MarketDocument",
            target="cim_python_sdk.model.iec62325.market_management.market_document:MarketDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="reason",
            aggregation="none",
        )
    )
    period: Many[Period] = Many(
        EndMeta(
            name="period",
            cim_role="Period",
            target="cim_python_sdk.model.iec62325.market_management.period:Period",
            many=True,
            lower=0,
            upper=None,
            inverse="reason",
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
            inverse="reason",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Reason",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{D85ACC55-1B5A-4f2a-8083-9F533EC1B60A}",
        attributes=(
            AttrMeta("code", "code", "str", 0, 1, "primitive"),
            AttrMeta("text", "text", "str", 0, 1, "primitive"),
        ),
        ends=(
            registered_resource.meta,
            point.meta,
            market_document.meta,
            period.meta,
            time_series.meta,
        ),
    )

    def __init__(
        self,
        *,
        code: str | None = None,
        text: str | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        point: Iterable[Point] | None = None,
        market_document: Iterable[MarketDocument] | None = None,
        period: Iterable[Period] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.code = code
        self.text = text
        if registered_resource is not None:
            Reason.registered_resource.extend(self, registered_resource)
        if point is not None:
            Reason.point.extend(self, point)
        if market_document is not None:
            Reason.market_document.extend(self, market_document)
        if period is not None:
            Reason.period.extend(self, period)
        if time_series is not None:
            Reason.time_series.extend(self, time_series)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return Reason.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return Reason.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return Reason.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return Reason.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return Reason.registered_resource.get_by_mrid(self, mrid)

    def add_point(self, point: Point) -> Self:
        return Reason.point.add(self, point)

    def remove_point(self, point: Point) -> Self:
        return Reason.point.remove(self, point)

    def clear_point(self) -> Self:
        return Reason.point.clear(self)

    def num_point(self) -> int:
        return Reason.point.count(self)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return Reason.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return Reason.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return Reason.market_document.clear(self)

    def num_market_document(self) -> int:
        return Reason.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return Reason.market_document.get_by_mrid(self, mrid)

    def add_period(self, period: Period) -> Self:
        return Reason.period.add(self, period)

    def remove_period(self, period: Period) -> Self:
        return Reason.period.remove(self, period)

    def clear_period(self) -> Self:
        return Reason.period.clear(self)

    def num_period(self) -> int:
        return Reason.period.count(self)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return Reason.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return Reason.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return Reason.time_series.clear(self)

    def num_time_series(self) -> int:
        return Reason.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return Reason.time_series.get_by_mrid(self, mrid)
