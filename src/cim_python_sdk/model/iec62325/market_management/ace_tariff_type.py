"""CIM class AceTariffType (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.market_document import MarketDocument
    from cim_python_sdk.model.iec62325.market_management.point import Point
    from cim_python_sdk.model.iec62325.market_management.unit import Unit


class AceTariffType(CimObject):
    """The Area Control Error tariff type that is applied or used."""

    __slots__ = ("_market_document", "_point", "_unit", "type")

    type: str | None

    market_document: Many[MarketDocument] = Many(
        EndMeta(
            name="market_document",
            cim_role="MarketDocument",
            target="cim_python_sdk.model.iec62325.market_management.market_document:MarketDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="ace_tariff_type",
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
            inverse="ace_tariff_type",
            aggregation="none",
        )
    )
    unit: Many[Unit] = Many(
        EndMeta(
            name="unit",
            cim_role="Unit",
            target="cim_python_sdk.model.iec62325.market_management.unit:Unit",
            many=True,
            lower=0,
            upper=None,
            inverse="ace_tariff_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AceTariffType",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{155F5F4F-E3DE-4ba2-9B2C-FFE5461E84A0}",
        attributes=(AttrMeta("type", "type", "str", 0, 1, "primitive"),),
        ends=(
            market_document.meta,
            point.meta,
            unit.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        market_document: Iterable[MarketDocument] | None = None,
        point: Iterable[Point] | None = None,
        unit: Iterable[Unit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        if market_document is not None:
            AceTariffType.market_document.extend(self, market_document)
        if point is not None:
            AceTariffType.point.extend(self, point)
        if unit is not None:
            AceTariffType.unit.extend(self, unit)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return AceTariffType.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return AceTariffType.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return AceTariffType.market_document.clear(self)

    def num_market_document(self) -> int:
        return AceTariffType.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return AceTariffType.market_document.get_by_mrid(self, mrid)

    def add_point(self, point: Point) -> Self:
        return AceTariffType.point.add(self, point)

    def remove_point(self, point: Point) -> Self:
        return AceTariffType.point.remove(self, point)

    def clear_point(self) -> Self:
        return AceTariffType.point.clear(self)

    def num_point(self) -> int:
        return AceTariffType.point.count(self)

    def add_unit(self, unit: Unit) -> Self:
        return AceTariffType.unit.add(self, unit)

    def remove_unit(self, unit: Unit) -> Self:
        return AceTariffType.unit.remove(self, unit)

    def clear_unit(self) -> Self:
        return AceTariffType.unit.clear(self)

    def num_unit(self) -> int:
        return AceTariffType.unit.count(self)
