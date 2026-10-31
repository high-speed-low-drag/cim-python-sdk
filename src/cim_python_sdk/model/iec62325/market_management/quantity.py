"""CIM class Quantity (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

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


class Quantity(CimObject):
    """Description of quantities needed in the data exchange.

    The type of the quantity is described either by the role of the association or the type
    attribute.

    The quality attribute provides the information about the quality of the quantity
    (measured, estimated, etc.)."""

    __slots__ = (
        "_detail_quantity",
        "_domain",
        "_point",
        "_quantity_detail_quantity",
        "_time_series",
        "quality",
        "quantity",
        "type",
    )

    quantity: _decimal.Decimal | None
    type: str | None
    quality: str | None

    domain: Many[Domain] = Many(
        EndMeta(
            name="domain",
            cim_role="Domain",
            target="cim_python_sdk.model.iec62325.market_management.domain:Domain",
            many=True,
            lower=0,
            upper=None,
            inverse="quantity",
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
            inverse="quantity_point",
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
            inverse="quantity",
            aggregation="none",
        )
    )
    quantity_detail_quantity: One[Quantity] = One(
        EndMeta(
            name="quantity_detail_quantity",
            cim_role="quantity",
            target="cim_python_sdk.model.iec62325.market_management.quantity:Quantity",
            many=False,
            lower=0,
            upper=1,
            inverse="detail_quantity",
            aggregation="none",
        )
    )
    detail_quantity: Many[Quantity] = Many(
        EndMeta(
            name="detail_quantity",
            cim_role="Detail_Quantity",
            target="cim_python_sdk.model.iec62325.market_management.quantity:Quantity",
            many=True,
            lower=0,
            upper=None,
            inverse="quantity_detail_quantity",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Quantity",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{2FE8FA95-2C67-4b07-B3F9-86385F4D6CB3}",
        attributes=(
            AttrMeta("quantity", "quantity", "Decimal", 0, 1, "primitive"),
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("quality", "quality", "str", 0, 1, "primitive"),
        ),
        ends=(
            domain.meta,
            point.meta,
            time_series.meta,
            quantity_detail_quantity.meta,
            detail_quantity.meta,
        ),
    )

    def __init__(
        self,
        *,
        quantity: _decimal.Decimal | None = None,
        type: str | None = None,
        quality: str | None = None,
        domain: Iterable[Domain] | None = None,
        point: Iterable[Point] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        quantity_detail_quantity: Quantity | None = None,
        detail_quantity: Iterable[Quantity] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.quantity = quantity
        self.type = type
        self.quality = quality
        if domain is not None:
            Quantity.domain.extend(self, domain)
        if point is not None:
            Quantity.point.extend(self, point)
        if time_series is not None:
            Quantity.time_series.extend(self, time_series)
        if quantity_detail_quantity is not None:
            self.quantity_detail_quantity = quantity_detail_quantity
        if detail_quantity is not None:
            Quantity.detail_quantity.extend(self, detail_quantity)

    def add_domain(self, domain: Domain) -> Self:
        return Quantity.domain.add(self, domain)

    def remove_domain(self, domain: Domain) -> Self:
        return Quantity.domain.remove(self, domain)

    def clear_domain(self) -> Self:
        return Quantity.domain.clear(self)

    def num_domain(self) -> int:
        return Quantity.domain.count(self)

    def get_domain_by_mrid(self, mrid: str) -> Domain | None:
        return Quantity.domain.get_by_mrid(self, mrid)

    def add_point(self, point: Point) -> Self:
        return Quantity.point.add(self, point)

    def remove_point(self, point: Point) -> Self:
        return Quantity.point.remove(self, point)

    def clear_point(self) -> Self:
        return Quantity.point.clear(self)

    def num_point(self) -> int:
        return Quantity.point.count(self)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return Quantity.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return Quantity.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return Quantity.time_series.clear(self)

    def num_time_series(self) -> int:
        return Quantity.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return Quantity.time_series.get_by_mrid(self, mrid)

    def add_detail_quantity(self, detail_quantity: Quantity) -> Self:
        return Quantity.detail_quantity.add(self, detail_quantity)

    def remove_detail_quantity(self, detail_quantity: Quantity) -> Self:
        return Quantity.detail_quantity.remove(self, detail_quantity)

    def clear_detail_quantity(self) -> Self:
        return Quantity.detail_quantity.clear(self)

    def num_detail_quantity(self) -> int:
        return Quantity.detail_quantity.count(self)
