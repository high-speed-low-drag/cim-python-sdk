"""CIM class Price (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.domain import Domain
    from cim_python_sdk.model.iec62325.market_management.point import Point
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class Price(CimObject):
    """The cost corresponding to a specific measure and expressed in a currency."""

    __slots__ = ("_domain", "_point", "_time_series", "amount", "category", "direction")

    amount: _decimal.Decimal | None
    category: str | None
    direction: str | None

    domain: Many[Domain] = Many(
        EndMeta(
            name="domain",
            cim_role="Domain",
            target="cim_python_sdk.model.iec62325.market_management.domain:Domain",
            many=True,
            lower=0,
            upper=None,
            inverse="price",
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
            inverse="price",
            aggregation="none",
        )
    )
    point: One[Point] = One(
        EndMeta(
            name="point",
            cim_role="Point",
            target="cim_python_sdk.model.iec62325.market_management.point:Point",
            many=False,
            lower=0,
            upper=1,
            inverse="price",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Price",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{BA13415E-3C31-4522-8171-7B6F728A03D8}",
        attributes=(
            AttrMeta("amount", "amount", "Decimal", 0, 1, "primitive"),
            AttrMeta("category", "category", "str", 0, 1, "primitive"),
            AttrMeta("direction", "direction", "str", 0, 1, "primitive"),
        ),
        ends=(
            domain.meta,
            time_series.meta,
            point.meta,
        ),
    )

    def __init__(
        self,
        *,
        amount: _decimal.Decimal | None = None,
        category: str | None = None,
        direction: str | None = None,
        domain: Iterable[Domain] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        point: Point | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.amount = amount
        self.category = category
        self.direction = direction
        if domain is not None:
            Price.domain.extend(self, domain)
        if time_series is not None:
            Price.time_series.extend(self, time_series)
        if point is not None:
            self.point = point

    def add_domain(self, domain: Domain) -> Self:
        return Price.domain.add(self, domain)

    def remove_domain(self, domain: Domain) -> Self:
        return Price.domain.remove(self, domain)

    def clear_domain(self) -> Self:
        return Price.domain.clear(self)

    def num_domain(self) -> int:
        return Price.domain.count(self)

    def get_domain_by_mrid(self, mrid: str) -> Domain | None:
        return Price.domain.get_by_mrid(self, mrid)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return Price.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return Price.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return Price.time_series.clear(self)

    def num_time_series(self) -> int:
        return Price.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return Price.time_series.get_by_mrid(self, mrid)
