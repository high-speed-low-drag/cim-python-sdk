"""CIM class Domain (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_management.market_document import MarketDocument
    from cim_python_sdk.model.iec62325.market_management.price import Price
    from cim_python_sdk.model.iec62325.market_management.quantity import Quantity
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class Domain(IdentifiedObject):
    """An area of activity defined within the energy market."""

    __slots__ = ("_market_document", "_price", "_quantity", "_registered_resource", "_time_series")

    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="domain",
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
            inverse="domain",
            aggregation="none",
        )
    )
    quantity: Many[Quantity] = Many(
        EndMeta(
            name="quantity",
            cim_role="Quantity",
            target="cim_python_sdk.model.iec62325.market_management.quantity:Quantity",
            many=True,
            lower=0,
            upper=None,
            inverse="domain",
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
            inverse="domain",
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
            inverse="domain",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Domain",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{38DEC768-A35A-4213-BC91-5BA8187A564D}",
        ends=(
            registered_resource.meta,
            time_series.meta,
            quantity.meta,
            price.meta,
            market_document.meta,
        ),
    )

    def __init__(
        self,
        *,
        registered_resource: Iterable[RegisteredResource] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        quantity: Iterable[Quantity] | None = None,
        price: Iterable[Price] | None = None,
        market_document: Iterable[MarketDocument] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if registered_resource is not None:
            Domain.registered_resource.extend(self, registered_resource)
        if time_series is not None:
            Domain.time_series.extend(self, time_series)
        if quantity is not None:
            Domain.quantity.extend(self, quantity)
        if price is not None:
            Domain.price.extend(self, price)
        if market_document is not None:
            Domain.market_document.extend(self, market_document)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return Domain.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return Domain.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return Domain.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return Domain.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return Domain.registered_resource.get_by_mrid(self, mrid)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return Domain.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return Domain.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return Domain.time_series.clear(self)

    def num_time_series(self) -> int:
        return Domain.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return Domain.time_series.get_by_mrid(self, mrid)

    def add_quantity(self, quantity: Quantity) -> Self:
        return Domain.quantity.add(self, quantity)

    def remove_quantity(self, quantity: Quantity) -> Self:
        return Domain.quantity.remove(self, quantity)

    def clear_quantity(self) -> Self:
        return Domain.quantity.clear(self)

    def num_quantity(self) -> int:
        return Domain.quantity.count(self)

    def add_price(self, price: Price) -> Self:
        return Domain.price.add(self, price)

    def remove_price(self, price: Price) -> Self:
        return Domain.price.remove(self, price)

    def clear_price(self) -> Self:
        return Domain.price.clear(self)

    def num_price(self) -> int:
        return Domain.price.count(self)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return Domain.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return Domain.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return Domain.market_document.clear(self)

    def num_market_document(self) -> int:
        return Domain.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return Domain.market_document.get_by_mrid(self, mrid)
