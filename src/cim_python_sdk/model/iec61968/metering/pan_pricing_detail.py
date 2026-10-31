"""CIM class PanPricingDetail (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.pan_pricing import PanPricing


class PanPricingDetail(CimObject):
    """Detail for a single price command/action."""

    __slots__ = (
        "_pan_pricing",
        "alternate_cost_delivered",
        "alternate_cost_unit",
        "current_time_date",
        "generation_price",
        "generation_price_ratio",
        "price",
        "price_ratio",
        "price_tier",
        "price_tier_count",
        "price_tier_label",
        "rate_label",
        "register_tier",
        "unit_of_measure",
    )

    alternate_cost_delivered: float | None
    alternate_cost_unit: str | None
    current_time_date: _dt.datetime | None
    generation_price: _decimal.Decimal | None  # Money
    generation_price_ratio: float | None
    price_tier_count: int | None
    price: _decimal.Decimal | None  # Money
    price_ratio: float | None
    price_tier: int | None
    rate_label: str | None
    register_tier: str | None
    unit_of_measure: str | None
    price_tier_label: str | None

    pan_pricing: One[PanPricing] = One(
        EndMeta(
            name="pan_pricing",
            cim_role="PanPricing",
            target="cim_python_sdk.model.iec61968.metering.pan_pricing:PanPricing",
            many=False,
            lower=0,
            upper=1,
            inverse="pan_pricing_details",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PanPricingDetail",
        package="TC57CIM/IEC61968/Metering",
        guid="{FF9F96DE-88E6-4ca2-AD7C-DFE7D8DA5681}",
        attributes=(
            AttrMeta(
                "alternate_cost_delivered", "alternateCostDelivered", "float", 0, 1, "primitive"
            ),
            AttrMeta("alternate_cost_unit", "alternateCostUnit", "str", 0, 1, "primitive"),
            AttrMeta("current_time_date", "currentTimeDate", "datetime", 0, 1, "primitive"),
            AttrMeta("generation_price", "generationPrice", "Money", 0, 1, "cimdatatype"),
            AttrMeta("generation_price_ratio", "generationPriceRatio", "float", 0, 1, "primitive"),
            AttrMeta("price_tier_count", "priceTierCount", "int", 0, 1, "primitive"),
            AttrMeta("price", "price", "Money", 0, 1, "cimdatatype"),
            AttrMeta("price_ratio", "priceRatio", "float", 0, 1, "primitive"),
            AttrMeta("price_tier", "priceTier", "int", 0, 1, "primitive"),
            AttrMeta("rate_label", "rateLabel", "str", 0, 1, "primitive"),
            AttrMeta("register_tier", "registerTier", "str", 0, 1, "primitive"),
            AttrMeta("unit_of_measure", "unitOfMeasure", "str", 0, 1, "primitive"),
            AttrMeta("price_tier_label", "priceTierLabel", "str", 0, 1, "primitive"),
        ),
        ends=(pan_pricing.meta,),
    )

    def __init__(
        self,
        *,
        alternate_cost_delivered: float | None = None,
        alternate_cost_unit: str | None = None,
        current_time_date: _dt.datetime | None = None,
        generation_price: _decimal.Decimal | None = None,
        generation_price_ratio: float | None = None,
        price_tier_count: int | None = None,
        price: _decimal.Decimal | None = None,
        price_ratio: float | None = None,
        price_tier: int | None = None,
        rate_label: str | None = None,
        register_tier: str | None = None,
        unit_of_measure: str | None = None,
        price_tier_label: str | None = None,
        pan_pricing: PanPricing | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.alternate_cost_delivered = alternate_cost_delivered
        self.alternate_cost_unit = alternate_cost_unit
        self.current_time_date = current_time_date
        self.generation_price = generation_price
        self.generation_price_ratio = generation_price_ratio
        self.price_tier_count = price_tier_count
        self.price = price
        self.price_ratio = price_ratio
        self.price_tier = price_tier
        self.rate_label = rate_label
        self.register_tier = register_tier
        self.unit_of_measure = unit_of_measure
        self.price_tier_label = price_tier_label
        if pan_pricing is not None:
            self.pan_pricing = pan_pricing
