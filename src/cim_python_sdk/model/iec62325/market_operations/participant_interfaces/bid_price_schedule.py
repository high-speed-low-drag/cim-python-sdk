"""CIM class BidPriceSchedule (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.bid_mitigation_status import (
        BidMitigationStatus,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.bid_mitigation_type import (
        BidMitigationType,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_price_curve import (
        BidPriceCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid import (
        ProductBid,
    )


class BidPriceSchedule(RegularIntervalSchedule):
    """Defines bid schedules to allow a product bid to use specified bid price curves for
    different time intervals."""

    __slots__ = ("_bid_price_curve", "_product_bid", "bid_type", "mitigation_status")

    bid_type: BidMitigationType | None
    mitigation_status: BidMitigationStatus | None

    bid_price_curve: One[BidPriceCurve] = One(
        EndMeta(
            name="bid_price_curve",
            cim_role="BidPriceCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_price_curve:BidPriceCurve",
            many=False,
            lower=1,
            upper=1,
            inverse="bid_schedule",
            aggregation="none",
        )
    )
    product_bid: One[ProductBid] = One(
        EndMeta(
            name="product_bid",
            cim_role="ProductBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid:ProductBid",
            many=False,
            lower=1,
            upper=1,
            inverse="bid_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BidPriceSchedule",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{8CAB15B6-4EE6-4027-8418-4703559C1BA8}",
        attributes=(
            AttrMeta("bid_type", "bidType", "BidMitigationType", 0, 1, "enumeration"),
            AttrMeta(
                "mitigation_status", "mitigationStatus", "BidMitigationStatus", 0, 1, "enumeration"
            ),
        ),
        ends=(
            bid_price_curve.meta,
            product_bid.meta,
        ),
    )

    def __init__(
        self,
        *,
        bid_type: BidMitigationType | None = None,
        mitigation_status: BidMitigationStatus | None = None,
        bid_price_curve: BidPriceCurve | None = None,
        product_bid: ProductBid | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bid_type = bid_type
        self.mitigation_status = mitigation_status
        if bid_price_curve is not None:
            self.bid_price_curve = bid_price_curve
        if product_bid is not None:
            self.product_bid = product_bid
