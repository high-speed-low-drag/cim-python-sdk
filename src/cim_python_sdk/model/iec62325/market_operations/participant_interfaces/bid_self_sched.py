"""CIM class BidSelfSched (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.bid_type_rmr import BidTypeRMR
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_product_self_sched_type import (
        MarketProductSelfSchedType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.self_sched_reference_type import (
        SelfSchedReferenceType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid import (
        ProductBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.adjacent_ca_set import (
        AdjacentCASet,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right import (
        ContractRight,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class BidSelfSched(RegularIntervalSchedule):
    """Defines self schedule values to be used for specified time intervals."""

    __slots__ = (
        "_adjacent_ca_set",
        "_host_control_area",
        "_product_bid",
        "_sub_control_area",
        "_transmission_contract_right",
        "balancing_flag",
        "bid_type",
        "priority_flag",
        "pump_self_sched_mw",
        "reference_type",
        "self_sched_mw",
        "self_sched_spt_resource",
        "self_sched_type",
        "update_type",
        "wheeling_transaction_reference",
    )

    balancing_flag: YesNo | None
    bid_type: BidTypeRMR | None
    priority_flag: YesNo | None
    pump_self_sched_mw: float | None
    reference_type: SelfSchedReferenceType | None
    self_sched_mw: float | None
    self_sched_spt_resource: str | None
    self_sched_type: MarketProductSelfSchedType | None
    update_type: MQSCHGType | None
    wheeling_transaction_reference: str | None

    product_bid: One[ProductBid] = One(
        EndMeta(
            name="product_bid",
            cim_role="ProductBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid:ProductBid",
            many=False,
            lower=1,
            upper=1,
            inverse="bid_self_sched",
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
            inverse="bid_self_sched",
            aggregation="none",
        )
    )
    host_control_area: One[HostControlArea] = One(
        EndMeta(
            name="host_control_area",
            cim_role="HostControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="bid_self_sched",
            aggregation="none",
        )
    )
    adjacent_ca_set: One[AdjacentCASet] = One(
        EndMeta(
            name="adjacent_ca_set",
            cim_role="AdjacentCASet",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.adjacent_ca_set:AdjacentCASet",
            many=False,
            lower=0,
            upper=1,
            inverse="bid_self_sched",
            aggregation="none",
        )
    )
    transmission_contract_right: One[ContractRight] = One(
        EndMeta(
            name="transmission_contract_right",
            cim_role="TransmissionContractRight",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right:ContractRight",
            many=False,
            lower=0,
            upper=1,
            inverse="bid_self_sched",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BidSelfSched",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{2D9F58A7-8C03-43fa-95EB-C1B928777C1F}",
        attributes=(
            AttrMeta("balancing_flag", "balancingFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("bid_type", "bidType", "BidTypeRMR", 0, 1, "enumeration"),
            AttrMeta("priority_flag", "priorityFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("pump_self_sched_mw", "pumpSelfSchedMw", "float", 0, 1, "primitive"),
            AttrMeta(
                "reference_type", "referenceType", "SelfSchedReferenceType", 0, 1, "enumeration"
            ),
            AttrMeta("self_sched_mw", "selfSchedMw", "float", 0, 1, "primitive"),
            AttrMeta("self_sched_spt_resource", "selfSchedSptResource", "str", 0, 1, "primitive"),
            AttrMeta(
                "self_sched_type",
                "selfSchedType",
                "MarketProductSelfSchedType",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
            AttrMeta(
                "wheeling_transaction_reference",
                "wheelingTransactionReference",
                "str",
                0,
                1,
                "primitive",
            ),
        ),
        ends=(
            product_bid.meta,
            sub_control_area.meta,
            host_control_area.meta,
            adjacent_ca_set.meta,
            transmission_contract_right.meta,
        ),
    )

    def __init__(
        self,
        *,
        balancing_flag: YesNo | None = None,
        bid_type: BidTypeRMR | None = None,
        priority_flag: YesNo | None = None,
        pump_self_sched_mw: float | None = None,
        reference_type: SelfSchedReferenceType | None = None,
        self_sched_mw: float | None = None,
        self_sched_spt_resource: str | None = None,
        self_sched_type: MarketProductSelfSchedType | None = None,
        update_type: MQSCHGType | None = None,
        wheeling_transaction_reference: str | None = None,
        product_bid: ProductBid | None = None,
        sub_control_area: SubControlArea | None = None,
        host_control_area: HostControlArea | None = None,
        adjacent_ca_set: AdjacentCASet | None = None,
        transmission_contract_right: ContractRight | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.balancing_flag = balancing_flag
        self.bid_type = bid_type
        self.priority_flag = priority_flag
        self.pump_self_sched_mw = pump_self_sched_mw
        self.reference_type = reference_type
        self.self_sched_mw = self_sched_mw
        self.self_sched_spt_resource = self_sched_spt_resource
        self.self_sched_type = self_sched_type
        self.update_type = update_type
        self.wheeling_transaction_reference = wheeling_transaction_reference
        if product_bid is not None:
            self.product_bid = product_bid
        if sub_control_area is not None:
            self.sub_control_area = sub_control_area
        if host_control_area is not None:
            self.host_control_area = host_control_area
        if adjacent_ca_set is not None:
            self.adjacent_ca_set = adjacent_ca_set
        if transmission_contract_right is not None:
            self.transmission_contract_right = transmission_contract_right
