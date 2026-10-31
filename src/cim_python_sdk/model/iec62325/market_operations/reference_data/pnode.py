"""CIM class Pnode (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.ftr import FTR
    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.crr_segment import (
        CRRSegment,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_measurement import (
        MktMeasurement,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.commodity_definition import (
        CommodityDefinition,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_pricing_results import (
        ExPostPricingResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pnode_results import (
        PnodeResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade import Trade
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.transaction_bid import (
        TransactionBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
        AggregateNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.org_pnode_allocation import (
        OrgPnodeAllocation,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class Pnode(IdentifiedObject):
    """A pricing node is directly associated with a connectivity node. It is a pricing location
    for which market participants submit their bids, offers, buy/sell CRRs, and settle."""

    __slots__ = (
        "_aggregate_node",
        "_commodity_definition",
        "_delivery_transaction_bids",
        "_ex_post_results",
        "_ftrs",
        "_mkt_measurement",
        "_org_pnode_allocation",
        "_pnode_results",
        "_receipt_transaction_bids",
        "_registered_resources",
        "_rto",
        "_sink_crr_segment",
        "_source_crr_segment",
        "_sub_control_area",
        "_trade",
        "is_public",
    )

    is_public: bool | None

    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=0,
            upper=1,
            inverse="pnodes",
            aggregation="none",
        )
    )
    pnode_results: Many[PnodeResults] = Many(
        EndMeta(
            name="pnode_results",
            cim_role="PnodeResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pnode_results:PnodeResults",
            many=True,
            lower=1,
            upper=None,
            inverse="pnode",
            aggregation="none",
        )
    )
    delivery_transaction_bids: Many[TransactionBid] = Many(
        EndMeta(
            name="delivery_transaction_bids",
            cim_role="DeliveryTransactionBids",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.transaction_bid:TransactionBid",
            many=True,
            lower=0,
            upper=None,
            inverse="delivery_pnode",
            aggregation="none",
        )
    )
    sink_crr_segment: Many[CRRSegment] = Many(
        EndMeta(
            name="sink_crr_segment",
            cim_role="SinkCRRSegment",
            target="cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.crr_segment:CRRSegment",
            many=True,
            lower=0,
            upper=None,
            inverse="sink",
            aggregation="none",
        )
    )
    registered_resources: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resources",
            cim_role="RegisteredResources",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="pnode",
            aggregation="none",
        )
    )
    mkt_measurement: Many[MktMeasurement] = Many(
        EndMeta(
            name="mkt_measurement",
            cim_role="MktMeasurement",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_measurement:MktMeasurement",
            many=True,
            lower=0,
            upper=None,
            inverse="pnode",
            aggregation="none",
        )
    )
    org_pnode_allocation: Many[OrgPnodeAllocation] = Many(
        EndMeta(
            name="org_pnode_allocation",
            cim_role="OrgPnodeAllocation",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.org_pnode_allocation:OrgPnodeAllocation",
            many=True,
            lower=0,
            upper=None,
            inverse="pnode",
            aggregation="none",
        )
    )
    ftrs: Many[FTR] = Many(
        EndMeta(
            name="ftrs",
            cim_role="FTRs",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.ftr:FTR",
            many=True,
            lower=0,
            upper=None,
            inverse="pnodes",
            aggregation="none",
        )
    )
    receipt_transaction_bids: Many[TransactionBid] = Many(
        EndMeta(
            name="receipt_transaction_bids",
            cim_role="ReceiptTransactionBids",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.transaction_bid:TransactionBid",
            many=True,
            lower=0,
            upper=None,
            inverse="receipt_pnode",
            aggregation="none",
        )
    )
    source_crr_segment: Many[CRRSegment] = Many(
        EndMeta(
            name="source_crr_segment",
            cim_role="SourceCRRSegment",
            target="cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.crr_segment:CRRSegment",
            many=True,
            lower=0,
            upper=None,
            inverse="source",
            aggregation="none",
        )
    )
    aggregate_node: Many[AggregateNode] = Many(
        EndMeta(
            name="aggregate_node",
            cim_role="AggregateNode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node:AggregateNode",
            many=True,
            lower=0,
            upper=None,
            inverse="pnode",
            aggregation="none",
        )
    )
    trade: Many[Trade] = Many(
        EndMeta(
            name="trade",
            cim_role="Trade",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade:Trade",
            many=True,
            lower=0,
            upper=None,
            inverse="pnode",
            aggregation="none",
        )
    )
    ex_post_results: Many[ExPostPricingResults] = Many(
        EndMeta(
            name="ex_post_results",
            cim_role="ExPostResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_pricing_results:ExPostPricingResults",
            many=True,
            lower=0,
            upper=None,
            inverse="pnode",
            aggregation="none",
        )
    )
    sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="pnode",
            aggregation="none",
        )
    )
    commodity_definition: Many[CommodityDefinition] = Many(
        EndMeta(
            name="commodity_definition",
            cim_role="CommodityDefinition",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.commodity_definition:CommodityDefinition",
            many=True,
            lower=0,
            upper=None,
            inverse="pnode",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Pnode",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{C8A89D1C-E63F-429c-B543-92BEB004BADD}",
        attributes=(AttrMeta("is_public", "isPublic", "bool", 0, 1, "primitive"),),
        ends=(
            rto.meta,
            pnode_results.meta,
            delivery_transaction_bids.meta,
            sink_crr_segment.meta,
            registered_resources.meta,
            mkt_measurement.meta,
            org_pnode_allocation.meta,
            ftrs.meta,
            receipt_transaction_bids.meta,
            source_crr_segment.meta,
            aggregate_node.meta,
            trade.meta,
            ex_post_results.meta,
            sub_control_area.meta,
            commodity_definition.meta,
        ),
    )

    def __init__(
        self,
        *,
        is_public: bool | None = None,
        rto: RTO | None = None,
        pnode_results: Iterable[PnodeResults] | None = None,
        delivery_transaction_bids: Iterable[TransactionBid] | None = None,
        sink_crr_segment: Iterable[CRRSegment] | None = None,
        registered_resources: Iterable[RegisteredResource] | None = None,
        mkt_measurement: Iterable[MktMeasurement] | None = None,
        org_pnode_allocation: Iterable[OrgPnodeAllocation] | None = None,
        ftrs: Iterable[FTR] | None = None,
        receipt_transaction_bids: Iterable[TransactionBid] | None = None,
        source_crr_segment: Iterable[CRRSegment] | None = None,
        aggregate_node: Iterable[AggregateNode] | None = None,
        trade: Iterable[Trade] | None = None,
        ex_post_results: Iterable[ExPostPricingResults] | None = None,
        sub_control_area: SubControlArea | None = None,
        commodity_definition: Iterable[CommodityDefinition] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_public = is_public
        if rto is not None:
            self.rto = rto
        if pnode_results is not None:
            Pnode.pnode_results.extend(self, pnode_results)
        if delivery_transaction_bids is not None:
            Pnode.delivery_transaction_bids.extend(self, delivery_transaction_bids)
        if sink_crr_segment is not None:
            Pnode.sink_crr_segment.extend(self, sink_crr_segment)
        if registered_resources is not None:
            Pnode.registered_resources.extend(self, registered_resources)
        if mkt_measurement is not None:
            Pnode.mkt_measurement.extend(self, mkt_measurement)
        if org_pnode_allocation is not None:
            Pnode.org_pnode_allocation.extend(self, org_pnode_allocation)
        if ftrs is not None:
            Pnode.ftrs.extend(self, ftrs)
        if receipt_transaction_bids is not None:
            Pnode.receipt_transaction_bids.extend(self, receipt_transaction_bids)
        if source_crr_segment is not None:
            Pnode.source_crr_segment.extend(self, source_crr_segment)
        if aggregate_node is not None:
            Pnode.aggregate_node.extend(self, aggregate_node)
        if trade is not None:
            Pnode.trade.extend(self, trade)
        if ex_post_results is not None:
            Pnode.ex_post_results.extend(self, ex_post_results)
        if sub_control_area is not None:
            self.sub_control_area = sub_control_area
        if commodity_definition is not None:
            Pnode.commodity_definition.extend(self, commodity_definition)

    def add_pnode_result(self, pnode_result: PnodeResults) -> Self:
        return Pnode.pnode_results.add(self, pnode_result)

    def remove_pnode_result(self, pnode_result: PnodeResults) -> Self:
        return Pnode.pnode_results.remove(self, pnode_result)

    def clear_pnode_results(self) -> Self:
        return Pnode.pnode_results.clear(self)

    def num_pnode_result(self) -> int:
        return Pnode.pnode_results.count(self)

    def add_delivery_transaction_bid(self, delivery_transaction_bid: TransactionBid) -> Self:
        return Pnode.delivery_transaction_bids.add(self, delivery_transaction_bid)

    def remove_delivery_transaction_bid(self, delivery_transaction_bid: TransactionBid) -> Self:
        return Pnode.delivery_transaction_bids.remove(self, delivery_transaction_bid)

    def clear_delivery_transaction_bids(self) -> Self:
        return Pnode.delivery_transaction_bids.clear(self)

    def num_delivery_transaction_bid(self) -> int:
        return Pnode.delivery_transaction_bids.count(self)

    def get_delivery_transaction_bid_by_mrid(self, mrid: str) -> TransactionBid | None:
        return Pnode.delivery_transaction_bids.get_by_mrid(self, mrid)

    def add_sink_crr_segment(self, sink_crr_segment: CRRSegment) -> Self:
        return Pnode.sink_crr_segment.add(self, sink_crr_segment)

    def remove_sink_crr_segment(self, sink_crr_segment: CRRSegment) -> Self:
        return Pnode.sink_crr_segment.remove(self, sink_crr_segment)

    def clear_sink_crr_segment(self) -> Self:
        return Pnode.sink_crr_segment.clear(self)

    def num_sink_crr_segment(self) -> int:
        return Pnode.sink_crr_segment.count(self)

    def get_sink_crr_segment_by_mrid(self, mrid: str) -> CRRSegment | None:
        return Pnode.sink_crr_segment.get_by_mrid(self, mrid)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return Pnode.registered_resources.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return Pnode.registered_resources.remove(self, registered_resource)

    def clear_registered_resources(self) -> Self:
        return Pnode.registered_resources.clear(self)

    def num_registered_resource(self) -> int:
        return Pnode.registered_resources.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return Pnode.registered_resources.get_by_mrid(self, mrid)

    def add_mkt_measurement(self, mkt_measurement: MktMeasurement) -> Self:
        return Pnode.mkt_measurement.add(self, mkt_measurement)

    def remove_mkt_measurement(self, mkt_measurement: MktMeasurement) -> Self:
        return Pnode.mkt_measurement.remove(self, mkt_measurement)

    def clear_mkt_measurement(self) -> Self:
        return Pnode.mkt_measurement.clear(self)

    def num_mkt_measurement(self) -> int:
        return Pnode.mkt_measurement.count(self)

    def get_mkt_measurement_by_mrid(self, mrid: str) -> MktMeasurement | None:
        return Pnode.mkt_measurement.get_by_mrid(self, mrid)

    def add_org_pnode_allocation(self, org_pnode_allocation: OrgPnodeAllocation) -> Self:
        return Pnode.org_pnode_allocation.add(self, org_pnode_allocation)

    def remove_org_pnode_allocation(self, org_pnode_allocation: OrgPnodeAllocation) -> Self:
        return Pnode.org_pnode_allocation.remove(self, org_pnode_allocation)

    def clear_org_pnode_allocation(self) -> Self:
        return Pnode.org_pnode_allocation.clear(self)

    def num_org_pnode_allocation(self) -> int:
        return Pnode.org_pnode_allocation.count(self)

    def get_org_pnode_allocation_by_mrid(self, mrid: str) -> OrgPnodeAllocation | None:
        return Pnode.org_pnode_allocation.get_by_mrid(self, mrid)

    def add_ftr(self, ftr: FTR) -> Self:
        return Pnode.ftrs.add(self, ftr)

    def remove_ftr(self, ftr: FTR) -> Self:
        return Pnode.ftrs.remove(self, ftr)

    def clear_ftrs(self) -> Self:
        return Pnode.ftrs.clear(self)

    def num_ftr(self) -> int:
        return Pnode.ftrs.count(self)

    def get_ftr_by_mrid(self, mrid: str) -> FTR | None:
        return Pnode.ftrs.get_by_mrid(self, mrid)

    def add_receipt_transaction_bid(self, receipt_transaction_bid: TransactionBid) -> Self:
        return Pnode.receipt_transaction_bids.add(self, receipt_transaction_bid)

    def remove_receipt_transaction_bid(self, receipt_transaction_bid: TransactionBid) -> Self:
        return Pnode.receipt_transaction_bids.remove(self, receipt_transaction_bid)

    def clear_receipt_transaction_bids(self) -> Self:
        return Pnode.receipt_transaction_bids.clear(self)

    def num_receipt_transaction_bid(self) -> int:
        return Pnode.receipt_transaction_bids.count(self)

    def get_receipt_transaction_bid_by_mrid(self, mrid: str) -> TransactionBid | None:
        return Pnode.receipt_transaction_bids.get_by_mrid(self, mrid)

    def add_source_crr_segment(self, source_crr_segment: CRRSegment) -> Self:
        return Pnode.source_crr_segment.add(self, source_crr_segment)

    def remove_source_crr_segment(self, source_crr_segment: CRRSegment) -> Self:
        return Pnode.source_crr_segment.remove(self, source_crr_segment)

    def clear_source_crr_segment(self) -> Self:
        return Pnode.source_crr_segment.clear(self)

    def num_source_crr_segment(self) -> int:
        return Pnode.source_crr_segment.count(self)

    def get_source_crr_segment_by_mrid(self, mrid: str) -> CRRSegment | None:
        return Pnode.source_crr_segment.get_by_mrid(self, mrid)

    def add_aggregate_node(self, aggregate_node: AggregateNode) -> Self:
        return Pnode.aggregate_node.add(self, aggregate_node)

    def remove_aggregate_node(self, aggregate_node: AggregateNode) -> Self:
        return Pnode.aggregate_node.remove(self, aggregate_node)

    def clear_aggregate_node(self) -> Self:
        return Pnode.aggregate_node.clear(self)

    def num_aggregate_node(self) -> int:
        return Pnode.aggregate_node.count(self)

    def get_aggregate_node_by_mrid(self, mrid: str) -> AggregateNode | None:
        return Pnode.aggregate_node.get_by_mrid(self, mrid)

    def add_trade(self, trade: Trade) -> Self:
        return Pnode.trade.add(self, trade)

    def remove_trade(self, trade: Trade) -> Self:
        return Pnode.trade.remove(self, trade)

    def clear_trade(self) -> Self:
        return Pnode.trade.clear(self)

    def num_trade(self) -> int:
        return Pnode.trade.count(self)

    def get_trade_by_mrid(self, mrid: str) -> Trade | None:
        return Pnode.trade.get_by_mrid(self, mrid)

    def add_ex_post_result(self, ex_post_result: ExPostPricingResults) -> Self:
        return Pnode.ex_post_results.add(self, ex_post_result)

    def remove_ex_post_result(self, ex_post_result: ExPostPricingResults) -> Self:
        return Pnode.ex_post_results.remove(self, ex_post_result)

    def clear_ex_post_results(self) -> Self:
        return Pnode.ex_post_results.clear(self)

    def num_ex_post_result(self) -> int:
        return Pnode.ex_post_results.count(self)

    def add_commodity_definition(self, commodity_definition: CommodityDefinition) -> Self:
        return Pnode.commodity_definition.add(self, commodity_definition)

    def remove_commodity_definition(self, commodity_definition: CommodityDefinition) -> Self:
        return Pnode.commodity_definition.remove(self, commodity_definition)

    def clear_commodity_definition(self) -> Self:
        return Pnode.commodity_definition.clear(self)

    def num_commodity_definition(self) -> int:
        return Pnode.commodity_definition.count(self)

    def get_commodity_definition_by_mrid(self, mrid: str) -> CommodityDefinition | None:
        return Pnode.commodity_definition.get_by_mrid(self, mrid)
