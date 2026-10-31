"""CIM class MarketEvaluationPoint (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class MarketEvaluationPoint(UsagePoint):
    """The identification of an entity where energy products are measured or computed."""

    __slots__ = ("_time_series",)

    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="market_evaluation_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketEvaluationPoint",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{5C7856BA-008C-4e93-B0B0-80E339AB6A08}",
        ends=(time_series.meta,),
    )

    def __init__(
        self,
        *,
        time_series: Iterable[TimeSeries] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if time_series is not None:
            MarketEvaluationPoint.time_series.extend(self, time_series)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return MarketEvaluationPoint.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return MarketEvaluationPoint.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return MarketEvaluationPoint.time_series.clear(self)

    def num_time_series(self) -> int:
        return MarketEvaluationPoint.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return MarketEvaluationPoint.time_series.get_by_mrid(self, mrid)
