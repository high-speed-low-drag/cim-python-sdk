"""CIM class Series (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self


class Series(TimeSeries):
    """A set of similar physical or conceptual objects defined for the same period or point of
    time."""

    __slots__ = ("_self_series", "_series", "last_update_date", "method_type", "registration_date")

    last_update_date: _dt.date | None
    method_type: str | None
    registration_date: _dt.date | None

    self_series: Many[Series] = Many(
        EndMeta(
            name="self_series",
            cim_role="SelfSeries",
            target="cim_python_sdk.model.iec62325.market_management.series:Series",
            many=True,
            lower=0,
            upper=None,
            inverse="series",
            aggregation="none",
        )
    )
    series: Many[Series] = Many(
        EndMeta(
            name="series",
            cim_role="Series",
            target="cim_python_sdk.model.iec62325.market_management.series:Series",
            many=True,
            lower=0,
            upper=None,
            inverse="self_series",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Series",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{CA5E8158-5348-4165-920A-1E02D29E4C7C}",
        attributes=(
            AttrMeta("last_update_date", "lastUpdateDate", "date", 0, 1, "primitive"),
            AttrMeta("method_type", "methodType", "str", 0, 1, "primitive"),
            AttrMeta("registration_date", "registrationDate", "date", 0, 1, "primitive"),
        ),
        ends=(
            self_series.meta,
            series.meta,
        ),
    )

    def __init__(
        self,
        *,
        last_update_date: _dt.date | None = None,
        method_type: str | None = None,
        registration_date: _dt.date | None = None,
        self_series: Iterable[Series] | None = None,
        series: Iterable[Series] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.last_update_date = last_update_date
        self.method_type = method_type
        self.registration_date = registration_date
        if self_series is not None:
            Series.self_series.extend(self, self_series)
        if series is not None:
            Series.series.extend(self, series)

    def add_self_series(self, self_series: Series) -> Self:
        return Series.self_series.add(self, self_series)

    def remove_self_series(self, self_series: Series) -> Self:
        return Series.self_series.remove(self, self_series)

    def clear_self_series(self) -> Self:
        return Series.self_series.clear(self)

    def num_self_series(self) -> int:
        return Series.self_series.count(self)

    def get_self_series_by_mrid(self, mrid: str) -> Series | None:
        return Series.self_series.get_by_mrid(self, mrid)

    def add_series(self, series: Series) -> Self:
        return Series.series.add(self, series)

    def remove_series(self, series: Series) -> Self:
        return Series.series.remove(self, series)

    def clear_series(self) -> Self:
        return Series.series.clear(self)

    def num_series(self) -> int:
        return Series.series.count(self)

    def get_series_by_mrid(self, mrid: str) -> Series | None:
        return Series.series.get_by_mrid(self, mrid)
