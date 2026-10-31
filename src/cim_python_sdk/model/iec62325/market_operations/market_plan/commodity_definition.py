"""CIM class CommodityDefinition (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.domain.currency import Currency
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol
    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_product import (
        MarketProduct,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commodity_price import (
        CommodityPrice,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class CommodityDefinition(IdentifiedObject):
    """Commodities in the context of IEC 62325 are MarketProducts (energy, regulation, reserve,
    etc) traded at a specific location, which in this case is a Pnode (either a specific
    pricing node or a pricing area or zone defined as a collection of pricing nodes). The
    CommodityDefinition is a container for these two parameters, plus the unit of measure
    and the currency in which the Commodity is traded. Each CommodityDefinition should be
    relatively static; defined once and rarely changed."""

    __slots__ = (
        "_commodity_price",
        "_market_product",
        "_pnode",
        "_rto",
        "commodity_currency",
        "commodity_unit",
        "commodity_unit_multiplier",
    )

    commodity_currency: Currency | None
    commodity_unit: UnitSymbol | None
    commodity_unit_multiplier: UnitMultiplier | None

    market_product: One[MarketProduct] = One(
        EndMeta(
            name="market_product",
            cim_role="MarketProduct",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_product:MarketProduct",
            many=False,
            lower=1,
            upper=1,
            inverse="commodity_definition",
            aggregation="none",
        )
    )
    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=1,
            upper=1,
            inverse="commodity_definition",
            aggregation="none",
        )
    )
    commodity_price: Many[CommodityPrice] = Many(
        EndMeta(
            name="commodity_price",
            cim_role="CommodityPrice",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commodity_price:CommodityPrice",
            many=True,
            lower=1,
            upper=None,
            inverse="commodity_definition",
            aggregation="none",
        )
    )
    pnode: One[Pnode] = One(
        EndMeta(
            name="pnode",
            cim_role="Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=False,
            lower=1,
            upper=1,
            inverse="commodity_definition",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CommodityDefinition",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{686D0DA4-E33A-423d-A375-8D61508FDA8C}",
        attributes=(
            AttrMeta("commodity_currency", "commodityCurrency", "Currency", 0, 1, "enumeration"),
            AttrMeta("commodity_unit", "commodityUnit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta(
                "commodity_unit_multiplier",
                "commodityUnitMultiplier",
                "UnitMultiplier",
                0,
                1,
                "enumeration",
            ),
        ),
        ends=(
            market_product.meta,
            rto.meta,
            commodity_price.meta,
            pnode.meta,
        ),
    )

    def __init__(
        self,
        *,
        commodity_currency: Currency | None = None,
        commodity_unit: UnitSymbol | None = None,
        commodity_unit_multiplier: UnitMultiplier | None = None,
        market_product: MarketProduct | None = None,
        rto: RTO | None = None,
        commodity_price: Iterable[CommodityPrice] | None = None,
        pnode: Pnode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.commodity_currency = commodity_currency
        self.commodity_unit = commodity_unit
        self.commodity_unit_multiplier = commodity_unit_multiplier
        if market_product is not None:
            self.market_product = market_product
        if rto is not None:
            self.rto = rto
        if commodity_price is not None:
            CommodityDefinition.commodity_price.extend(self, commodity_price)
        if pnode is not None:
            self.pnode = pnode

    def add_commodity_price(self, commodity_price: CommodityPrice) -> Self:
        return CommodityDefinition.commodity_price.add(self, commodity_price)

    def remove_commodity_price(self, commodity_price: CommodityPrice) -> Self:
        return CommodityDefinition.commodity_price.remove(self, commodity_price)

    def clear_commodity_price(self) -> Self:
        return CommodityDefinition.commodity_price.clear(self)

    def num_commodity_price(self) -> int:
        return CommodityDefinition.commodity_price.count(self)
