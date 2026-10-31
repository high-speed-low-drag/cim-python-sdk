"""CIM class MktPSRType (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.psr_type import PSRType

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class MktPSRType(PSRType):
    """The type of a power system resource."""

    __slots__ = ("_time_series", "psr_type")

    psr_type: str | None

    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_psr_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktPSRType",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{A544B969-57EA-4bd1-9E5F-6127F5C9AB8F}",
        attributes=(AttrMeta("psr_type", "psrType", "str", 0, 1, "primitive"),),
        ends=(time_series.meta,),
    )

    def __init__(
        self,
        *,
        psr_type: str | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.psr_type = psr_type
        if time_series is not None:
            MktPSRType.time_series.extend(self, time_series)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return MktPSRType.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return MktPSRType.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return MktPSRType.time_series.clear(self)

    def num_time_series(self) -> int:
        return MktPSRType.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return MktPSRType.time_series.get_by_mrid(self, mrid)
