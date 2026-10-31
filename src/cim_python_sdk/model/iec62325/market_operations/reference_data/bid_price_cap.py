"""CIM class BidPriceCap (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_product import (
        MarketProduct,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType


class BidPriceCap(CimObject):
    """This class represent the bid price cap."""

    __slots__ = (
        "_market_product",
        "bid_ceiling",
        "bid_ceiling_as",
        "bid_floor",
        "bid_floor_as",
        "default_price",
        "market_type",
    )

    market_type: MarketType | None
    bid_floor: float | None  # CostPerEnergyUnit
    bid_ceiling: float | None  # CostPerEnergyUnit
    default_price: float | None  # CostPerEnergyUnit
    bid_floor_as: float | None  # CostPerEnergyUnit
    bid_ceiling_as: float | None  # CostPerEnergyUnit

    market_product: One[MarketProduct] = One(
        EndMeta(
            name="market_product",
            cim_role="MarketProduct",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_product:MarketProduct",
            many=False,
            lower=0,
            upper=1,
            inverse="bid_price_cap",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BidPriceCap",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{C9E06915-50FD-41b5-B96F-0BA132B19F8A}",
        attributes=(
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
            AttrMeta("bid_floor", "bidFloor", "CostPerEnergyUnit", 0, 1, "cimdatatype"),
            AttrMeta("bid_ceiling", "bidCeiling", "CostPerEnergyUnit", 0, 1, "cimdatatype"),
            AttrMeta("default_price", "defaultPrice", "CostPerEnergyUnit", 0, 1, "cimdatatype"),
            AttrMeta("bid_floor_as", "bidFloorAS", "CostPerEnergyUnit", 0, 1, "cimdatatype"),
            AttrMeta("bid_ceiling_as", "bidCeilingAS", "CostPerEnergyUnit", 0, 1, "cimdatatype"),
        ),
        ends=(market_product.meta,),
    )

    def __init__(
        self,
        *,
        market_type: MarketType | None = None,
        bid_floor: float | None = None,
        bid_ceiling: float | None = None,
        default_price: float | None = None,
        bid_floor_as: float | None = None,
        bid_ceiling_as: float | None = None,
        market_product: MarketProduct | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.market_type = market_type
        self.bid_floor = bid_floor
        self.bid_ceiling = bid_ceiling
        self.default_price = default_price
        self.bid_floor_as = bid_floor_as
        self.bid_ceiling_as = bid_ceiling_as
        if market_product is not None:
            self.market_product = market_product
