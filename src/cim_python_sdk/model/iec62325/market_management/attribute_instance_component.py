"""CIM class AttributeInstanceComponent (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.market_document import MarketDocument
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class AttributeInstanceComponent(CimObject):
    """A class used to provide information about an attribute."""

    __slots__ = ("_market_document", "_time_series", "attribute", "attribute_value", "position")

    attribute: str | None
    attribute_value: str | None
    position: int | None

    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="attribute_instance_component",
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
            inverse="attribute_instance_component",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AttributeInstanceComponent",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{908E7712-A11D-4b97-B631-3E0749BFF95D}",
        attributes=(
            AttrMeta("attribute", "attribute", "str", 0, 1, "primitive"),
            AttrMeta("attribute_value", "attributeValue", "str", 0, 1, "primitive"),
            AttrMeta("position", "position", "int", 0, 1, "primitive"),
        ),
        ends=(
            time_series.meta,
            market_document.meta,
        ),
    )

    def __init__(
        self,
        *,
        attribute: str | None = None,
        attribute_value: str | None = None,
        position: int | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        market_document: Iterable[MarketDocument] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.attribute = attribute
        self.attribute_value = attribute_value
        self.position = position
        if time_series is not None:
            AttributeInstanceComponent.time_series.extend(self, time_series)
        if market_document is not None:
            AttributeInstanceComponent.market_document.extend(self, market_document)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return AttributeInstanceComponent.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return AttributeInstanceComponent.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return AttributeInstanceComponent.time_series.clear(self)

    def num_time_series(self) -> int:
        return AttributeInstanceComponent.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return AttributeInstanceComponent.time_series.get_by_mrid(self, mrid)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return AttributeInstanceComponent.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return AttributeInstanceComponent.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return AttributeInstanceComponent.market_document.clear(self)

    def num_market_document(self) -> int:
        return AttributeInstanceComponent.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return AttributeInstanceComponent.market_document.get_by_mrid(self, mrid)
