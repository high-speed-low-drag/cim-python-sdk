"""CIM class DateAndOrTime (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.market_document import MarketDocument
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class DateAndOrTime(CimObject):
    """The date and/or the time."""

    __slots__ = ("_market_document", "_time_series", "date", "time")

    date: _dt.date | None
    time: _dt.time | None

    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="date_and_or_time",
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
            inverse="date_and_or_time",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DateAndOrTime",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{209EDF47-74BC-4a80-BCF8-42F3960FFE71}",
        attributes=(
            AttrMeta("date", "date", "date", 0, 1, "primitive"),
            AttrMeta("time", "time", "time", 0, 1, "primitive"),
        ),
        ends=(
            time_series.meta,
            market_document.meta,
        ),
    )

    def __init__(
        self,
        *,
        date: _dt.date | None = None,
        time: _dt.time | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        market_document: Iterable[MarketDocument] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.date = date
        self.time = time
        if time_series is not None:
            DateAndOrTime.time_series.extend(self, time_series)
        if market_document is not None:
            DateAndOrTime.market_document.extend(self, market_document)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return DateAndOrTime.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return DateAndOrTime.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return DateAndOrTime.time_series.clear(self)

    def num_time_series(self) -> int:
        return DateAndOrTime.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return DateAndOrTime.time_series.get_by_mrid(self, mrid)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return DateAndOrTime.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return DateAndOrTime.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return DateAndOrTime.market_document.clear(self)

    def num_market_document(self) -> int:
        return DateAndOrTime.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return DateAndOrTime.market_document.get_by_mrid(self, mrid)
