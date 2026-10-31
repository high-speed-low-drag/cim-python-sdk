"""CIM class Point (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.ace_tariff_type import AceTariffType
    from cim_python_sdk.model.iec62325.market_management.flow_direction import FlowDirection
    from cim_python_sdk.model.iec62325.market_management.period import Period
    from cim_python_sdk.model.iec62325.market_management.price import Price
    from cim_python_sdk.model.iec62325.market_management.quantity import Quantity
    from cim_python_sdk.model.iec62325.market_management.reason import Reason
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class Point(CimObject):
    """An identification of a set of values beeing adressed within a specific interval of time."""

    __slots__ = (
        "_ace_tariff_type",
        "_flow_direction",
        "_period",
        "_price",
        "_quantity_point",
        "_reason",
        "_time_series",
        "position",
        "quality",
        "quantity",
        "secondary_quantity",
    )

    position: int | None
    quality: str | None
    quantity: _decimal.Decimal | None
    secondary_quantity: _decimal.Decimal | None

    period: One[Period] = One(
        EndMeta(
            name="period",
            cim_role="Period",
            target="cim_python_sdk.model.iec62325.market_management.period:Period",
            many=False,
            lower=1,
            upper=1,
            inverse="point",
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
            inverse="point",
            aggregation="none",
        )
    )
    quantity_point: Many[Quantity] = Many(
        EndMeta(
            name="quantity_point",
            cim_role="Quantity",
            target="cim_python_sdk.model.iec62325.market_management.quantity:Quantity",
            many=True,
            lower=0,
            upper=None,
            inverse="point",
            aggregation="none",
        )
    )
    ace_tariff_type: Many[AceTariffType] = Many(
        EndMeta(
            name="ace_tariff_type",
            cim_role="AceTariffType",
            target="cim_python_sdk.model.iec62325.market_management.ace_tariff_type:AceTariffType",
            many=True,
            lower=0,
            upper=None,
            inverse="point",
            aggregation="none",
        )
    )
    flow_direction: Many[FlowDirection] = Many(
        EndMeta(
            name="flow_direction",
            cim_role="FlowDirection",
            target="cim_python_sdk.model.iec62325.market_management.flow_direction:FlowDirection",
            many=True,
            lower=0,
            upper=None,
            inverse="point",
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
            inverse="point",
            aggregation="none",
        )
    )
    price: Many[Price] = Many(
        EndMeta(
            name="price",
            cim_role="Price",
            target="cim_python_sdk.model.iec62325.market_management.price:Price",
            many=True,
            lower=0,
            upper=None,
            inverse="point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Point",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{82841BAA-3085-432f-AD5E-3F87056F550F}",
        attributes=(
            AttrMeta("position", "position", "int", 0, 1, "primitive"),
            AttrMeta("quality", "quality", "str", 0, 1, "primitive"),
            AttrMeta("quantity", "quantity", "Decimal", 0, 1, "primitive"),
            AttrMeta("secondary_quantity", "secondaryQuantity", "Decimal", 0, 1, "primitive"),
        ),
        ends=(
            period.meta,
            reason.meta,
            quantity_point.meta,
            ace_tariff_type.meta,
            flow_direction.meta,
            time_series.meta,
            price.meta,
        ),
    )

    def __init__(
        self,
        *,
        position: int | None = None,
        quality: str | None = None,
        quantity: _decimal.Decimal | None = None,
        secondary_quantity: _decimal.Decimal | None = None,
        period: Period | None = None,
        reason: Iterable[Reason] | None = None,
        quantity_point: Iterable[Quantity] | None = None,
        ace_tariff_type: Iterable[AceTariffType] | None = None,
        flow_direction: Iterable[FlowDirection] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        price: Iterable[Price] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.position = position
        self.quality = quality
        self.quantity = quantity
        self.secondary_quantity = secondary_quantity
        if period is not None:
            self.period = period
        if reason is not None:
            Point.reason.extend(self, reason)
        if quantity_point is not None:
            Point.quantity_point.extend(self, quantity_point)
        if ace_tariff_type is not None:
            Point.ace_tariff_type.extend(self, ace_tariff_type)
        if flow_direction is not None:
            Point.flow_direction.extend(self, flow_direction)
        if time_series is not None:
            Point.time_series.extend(self, time_series)
        if price is not None:
            Point.price.extend(self, price)

    def add_reason(self, reason: Reason) -> Self:
        return Point.reason.add(self, reason)

    def remove_reason(self, reason: Reason) -> Self:
        return Point.reason.remove(self, reason)

    def clear_reason(self) -> Self:
        return Point.reason.clear(self)

    def num_reason(self) -> int:
        return Point.reason.count(self)

    def add_quantity_point(self, quantity_point: Quantity) -> Self:
        return Point.quantity_point.add(self, quantity_point)

    def remove_quantity_point(self, quantity_point: Quantity) -> Self:
        return Point.quantity_point.remove(self, quantity_point)

    def clear_quantity_point(self) -> Self:
        return Point.quantity_point.clear(self)

    def num_quantity_point(self) -> int:
        return Point.quantity_point.count(self)

    def add_ace_tariff_type(self, ace_tariff_type: AceTariffType) -> Self:
        return Point.ace_tariff_type.add(self, ace_tariff_type)

    def remove_ace_tariff_type(self, ace_tariff_type: AceTariffType) -> Self:
        return Point.ace_tariff_type.remove(self, ace_tariff_type)

    def clear_ace_tariff_type(self) -> Self:
        return Point.ace_tariff_type.clear(self)

    def num_ace_tariff_type(self) -> int:
        return Point.ace_tariff_type.count(self)

    def add_flow_direction(self, flow_direction: FlowDirection) -> Self:
        return Point.flow_direction.add(self, flow_direction)

    def remove_flow_direction(self, flow_direction: FlowDirection) -> Self:
        return Point.flow_direction.remove(self, flow_direction)

    def clear_flow_direction(self) -> Self:
        return Point.flow_direction.clear(self)

    def num_flow_direction(self) -> int:
        return Point.flow_direction.count(self)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return Point.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return Point.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return Point.time_series.clear(self)

    def num_time_series(self) -> int:
        return Point.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return Point.time_series.get_by_mrid(self, mrid)

    def add_price(self, price: Price) -> Self:
        return Point.price.add(self, price)

    def remove_price(self, price: Price) -> Self:
        return Point.price.remove(self, price)

    def clear_price(self) -> Self:
        return Point.price.clear(self)

    def num_price(self) -> int:
        return Point.price.count(self)
