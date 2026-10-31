"""CIM class DefaultBid (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.default_bid_curve import (
        DefaultBidCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.bid_type import BidType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.on_off import OnOff


class DefaultBid(Bid):
    """DefaultBid is a generic class to hold Default Energy Bid, Default Startup Bid, and
    Default Minimum Load Bid:

    Default Energy Bid

    A Default Energy Bid is a monotonically increasing staircase function consisting at
    maximum 10 economic bid segments, or 10 ($/MW, MW) pairs. There are three methods for
    determining the Default Energy Bid:

    - Cost Based: derived from the Heat Rate or Average Cost multiplied by the Gas Price
    Index plus 10%.

    - LMP Based: a weighted average of LMPs in the preceding 90 days.

    - Negotiated: an amount negotiated with the designated Independent Entity.

    Default Startup Bid

    A Default Startup Bid (DSUB) shall be calculated for each RMR unit based on the Startup
    Cost stored in the Master File and the applicable GPI and EPI.

    Default Minimum Load Bid

    A Default Minimum Load Bid (DMLB) shall be calculated for each RMR unit based on the
    Minimum Load Cost stored in the Master File and the applicable GPI."""

    __slots__ = (
        "_default_bid_curve",
        "_registered_resource",
        "bid_type",
        "min_load_cost",
        "peak_flag",
    )

    bid_type: BidType | None
    min_load_cost: float | None  # CostRate
    peak_flag: OnOff | None

    default_bid_curve: One[DefaultBidCurve] = One(
        EndMeta(
            name="default_bid_curve",
            cim_role="DefaultBidCurve",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.default_bid_curve:DefaultBidCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="default_bid",
            aggregation="none",
        )
    )
    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="default_bid",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DefaultBid",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{F22AD717-92CC-402d-B153-F7611EBA24A1}",
        attributes=(
            AttrMeta("bid_type", "bidType", "BidType", 0, 1, "enumeration"),
            AttrMeta("min_load_cost", "minLoadCost", "CostRate", 0, 1, "cimdatatype"),
            AttrMeta("peak_flag", "peakFlag", "OnOff", 0, 1, "enumeration"),
        ),
        ends=(
            default_bid_curve.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        bid_type: BidType | None = None,
        min_load_cost: float | None = None,
        peak_flag: OnOff | None = None,
        default_bid_curve: DefaultBidCurve | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bid_type = bid_type
        self.min_load_cost = min_load_cost
        self.peak_flag = peak_flag
        if default_bid_curve is not None:
            self.default_bid_curve = default_bid_curve
        if registered_resource is not None:
            self.registered_resource = registered_resource
