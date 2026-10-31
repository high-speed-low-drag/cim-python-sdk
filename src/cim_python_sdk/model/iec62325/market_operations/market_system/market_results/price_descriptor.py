"""CIM class PriceDescriptor (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commodity_price import (
        CommodityPrice,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.price_type_kind import (
        PriceTypeKind,
    )


class PriceDescriptor(CimObject):
    """The price of a Commodity during a given time interval may change over time. For example,
    a price may be forecasted a year ahead, a month ahead, a day ahead, an hour ahead, and
    in real time; this is defined using the MarketType. Additionally a price may have one or
    more components. For example, a locational marginal energy price may be the arithmetic
    sum of the system price, the congestion price, and the loss price. The priceType
    enumeration is used determine if the price is the complete price (priceType="total") or
    one of potentially many constituent components."""

    __slots__ = ("_commodity_price", "market_type", "price_type")

    market_type: MarketType | None
    price_type: PriceTypeKind | None

    commodity_price: Many[CommodityPrice] = Many(
        EndMeta(
            name="commodity_price",
            cim_role="CommodityPrice",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commodity_price:CommodityPrice",
            many=True,
            lower=1,
            upper=None,
            inverse="price_descriptor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PriceDescriptor",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{2C266D06-8B90-4844-96BD-02735ACDC715}",
        attributes=(
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
            AttrMeta("price_type", "priceType", "PriceTypeKind", 0, 1, "enumeration"),
        ),
        ends=(commodity_price.meta,),
    )

    def __init__(
        self,
        *,
        market_type: MarketType | None = None,
        price_type: PriceTypeKind | None = None,
        commodity_price: Iterable[CommodityPrice] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.market_type = market_type
        self.price_type = price_type
        if commodity_price is not None:
            PriceDescriptor.commodity_price.extend(self, commodity_price)

    def add_commodity_price(self, commodity_price: CommodityPrice) -> Self:
        return PriceDescriptor.commodity_price.add(self, commodity_price)

    def remove_commodity_price(self, commodity_price: CommodityPrice) -> Self:
        return PriceDescriptor.commodity_price.remove(self, commodity_price)

    def clear_commodity_price(self) -> Self:
        return PriceDescriptor.commodity_price.clear(self)

    def num_commodity_price(self) -> int:
        return PriceDescriptor.commodity_price.count(self)
