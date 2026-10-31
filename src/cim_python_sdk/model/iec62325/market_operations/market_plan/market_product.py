"""CIM class MarketProduct (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.reserve_req import (
        ReserveReq,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.commodity_definition import (
        CommodityDefinition,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.market import Market
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_region_results import (
        MarketRegionResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_instruction import (
        ResourceAwardInstruction,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_product_type import (
        MarketProductType,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_error import (
        BidError,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid import (
        ProductBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.bid_price_cap import (
        BidPriceCap,
    )


class MarketProduct(IdentifiedObject):
    """A product traded by an RTO (e.g. energy, 10 minute spinning reserve). Ancillary service
    product examples include: Regulation, Regulation Up, Regulation Down, Spinning Reserve,
    Non-Spinning Reserve, etc."""

    __slots__ = (
        "_bid_error",
        "_bid_price_cap",
        "_commodity_definition",
        "_market",
        "_market_region_results",
        "_product_bids",
        "_reserve_reqs",
        "_resource_award_instruction",
        "market_product_type",
        "ramp_interval",
    )

    market_product_type: MarketProductType | None
    ramp_interval: float | None

    commodity_definition: Many[CommodityDefinition] = Many(
        EndMeta(
            name="commodity_definition",
            cim_role="CommodityDefinition",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.commodity_definition:CommodityDefinition",
            many=True,
            lower=0,
            upper=None,
            inverse="market_product",
            aggregation="none",
        )
    )
    market_region_results: One[MarketRegionResults] = One(
        EndMeta(
            name="market_region_results",
            cim_role="MarketRegionResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_region_results:MarketRegionResults",
            many=False,
            lower=0,
            upper=1,
            inverse="market_product",
            aggregation="none",
        )
    )
    bid_price_cap: Many[BidPriceCap] = Many(
        EndMeta(
            name="bid_price_cap",
            cim_role="BidPriceCap",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.bid_price_cap:BidPriceCap",
            many=True,
            lower=0,
            upper=None,
            inverse="market_product",
            aggregation="none",
        )
    )
    market: One[Market] = One(
        EndMeta(
            name="market",
            cim_role="Market",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market:Market",
            many=False,
            lower=0,
            upper=1,
            inverse="market_products",
            aggregation="none",
        )
    )
    bid_error: Many[BidError] = Many(
        EndMeta(
            name="bid_error",
            cim_role="BidError",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_error:BidError",
            many=True,
            lower=0,
            upper=None,
            inverse="market_product",
            aggregation="none",
        )
    )
    reserve_reqs: Many[ReserveReq] = Many(
        EndMeta(
            name="reserve_reqs",
            cim_role="ReserveReqs",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.reserve_req:ReserveReq",
            many=True,
            lower=0,
            upper=None,
            inverse="market_product",
            aggregation="none",
        )
    )
    resource_award_instruction: Many[ResourceAwardInstruction] = Many(
        EndMeta(
            name="resource_award_instruction",
            cim_role="ResourceAwardInstruction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_instruction:ResourceAwardInstruction",
            many=True,
            lower=0,
            upper=None,
            inverse="market_product",
            aggregation="none",
        )
    )
    product_bids: Many[ProductBid] = Many(
        EndMeta(
            name="product_bids",
            cim_role="ProductBids",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid:ProductBid",
            many=True,
            lower=0,
            upper=None,
            inverse="market_product",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketProduct",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{181E8299-A6B5-4e02-AFC0-D1890C50FC39}",
        attributes=(
            AttrMeta(
                "market_product_type", "marketProductType", "MarketProductType", 0, 1, "enumeration"
            ),
            AttrMeta("ramp_interval", "rampInterval", "float", 0, 1, "primitive"),
        ),
        ends=(
            commodity_definition.meta,
            market_region_results.meta,
            bid_price_cap.meta,
            market.meta,
            bid_error.meta,
            reserve_reqs.meta,
            resource_award_instruction.meta,
            product_bids.meta,
        ),
    )

    def __init__(
        self,
        *,
        market_product_type: MarketProductType | None = None,
        ramp_interval: float | None = None,
        commodity_definition: Iterable[CommodityDefinition] | None = None,
        market_region_results: MarketRegionResults | None = None,
        bid_price_cap: Iterable[BidPriceCap] | None = None,
        market: Market | None = None,
        bid_error: Iterable[BidError] | None = None,
        reserve_reqs: Iterable[ReserveReq] | None = None,
        resource_award_instruction: Iterable[ResourceAwardInstruction] | None = None,
        product_bids: Iterable[ProductBid] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.market_product_type = market_product_type
        self.ramp_interval = ramp_interval
        if commodity_definition is not None:
            MarketProduct.commodity_definition.extend(self, commodity_definition)
        if market_region_results is not None:
            self.market_region_results = market_region_results
        if bid_price_cap is not None:
            MarketProduct.bid_price_cap.extend(self, bid_price_cap)
        if market is not None:
            self.market = market
        if bid_error is not None:
            MarketProduct.bid_error.extend(self, bid_error)
        if reserve_reqs is not None:
            MarketProduct.reserve_reqs.extend(self, reserve_reqs)
        if resource_award_instruction is not None:
            MarketProduct.resource_award_instruction.extend(self, resource_award_instruction)
        if product_bids is not None:
            MarketProduct.product_bids.extend(self, product_bids)

    def add_commodity_definition(self, commodity_definition: CommodityDefinition) -> Self:
        return MarketProduct.commodity_definition.add(self, commodity_definition)

    def remove_commodity_definition(self, commodity_definition: CommodityDefinition) -> Self:
        return MarketProduct.commodity_definition.remove(self, commodity_definition)

    def clear_commodity_definition(self) -> Self:
        return MarketProduct.commodity_definition.clear(self)

    def num_commodity_definition(self) -> int:
        return MarketProduct.commodity_definition.count(self)

    def get_commodity_definition_by_mrid(self, mrid: str) -> CommodityDefinition | None:
        return MarketProduct.commodity_definition.get_by_mrid(self, mrid)

    def add_bid_price_cap(self, bid_price_cap: BidPriceCap) -> Self:
        return MarketProduct.bid_price_cap.add(self, bid_price_cap)

    def remove_bid_price_cap(self, bid_price_cap: BidPriceCap) -> Self:
        return MarketProduct.bid_price_cap.remove(self, bid_price_cap)

    def clear_bid_price_cap(self) -> Self:
        return MarketProduct.bid_price_cap.clear(self)

    def num_bid_price_cap(self) -> int:
        return MarketProduct.bid_price_cap.count(self)

    def add_bid_error(self, bid_error: BidError) -> Self:
        return MarketProduct.bid_error.add(self, bid_error)

    def remove_bid_error(self, bid_error: BidError) -> Self:
        return MarketProduct.bid_error.remove(self, bid_error)

    def clear_bid_error(self) -> Self:
        return MarketProduct.bid_error.clear(self)

    def num_bid_error(self) -> int:
        return MarketProduct.bid_error.count(self)

    def get_bid_error_by_mrid(self, mrid: str) -> BidError | None:
        return MarketProduct.bid_error.get_by_mrid(self, mrid)

    def add_reserve_req(self, reserve_req: ReserveReq) -> Self:
        return MarketProduct.reserve_reqs.add(self, reserve_req)

    def remove_reserve_req(self, reserve_req: ReserveReq) -> Self:
        return MarketProduct.reserve_reqs.remove(self, reserve_req)

    def clear_reserve_reqs(self) -> Self:
        return MarketProduct.reserve_reqs.clear(self)

    def num_reserve_req(self) -> int:
        return MarketProduct.reserve_reqs.count(self)

    def get_reserve_req_by_mrid(self, mrid: str) -> ReserveReq | None:
        return MarketProduct.reserve_reqs.get_by_mrid(self, mrid)

    def add_resource_award_instruction(
        self, resource_award_instruction: ResourceAwardInstruction
    ) -> Self:
        return MarketProduct.resource_award_instruction.add(self, resource_award_instruction)

    def remove_resource_award_instruction(
        self, resource_award_instruction: ResourceAwardInstruction
    ) -> Self:
        return MarketProduct.resource_award_instruction.remove(self, resource_award_instruction)

    def clear_resource_award_instruction(self) -> Self:
        return MarketProduct.resource_award_instruction.clear(self)

    def num_resource_award_instruction(self) -> int:
        return MarketProduct.resource_award_instruction.count(self)

    def add_product_bid(self, product_bid: ProductBid) -> Self:
        return MarketProduct.product_bids.add(self, product_bid)

    def remove_product_bid(self, product_bid: ProductBid) -> Self:
        return MarketProduct.product_bids.remove(self, product_bid)

    def clear_product_bids(self) -> Self:
        return MarketProduct.product_bids.clear(self)

    def num_product_bid(self) -> int:
        return MarketProduct.product_bids.count(self)

    def get_product_bid_by_mrid(self, mrid: str) -> ProductBid | None:
        return MarketProduct.product_bids.get_by_mrid(self, mrid)
