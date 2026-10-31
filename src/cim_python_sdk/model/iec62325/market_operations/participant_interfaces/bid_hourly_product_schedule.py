"""CIM class BidHourlyProductSchedule (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid import (
        ProductBid,
    )


class BidHourlyProductSchedule(RegularIntervalSchedule):
    """Containment for bid parameters that are dependent on a market product type."""

    __slots__ = ("_product_bid",)

    product_bid: One[ProductBid] = One(
        EndMeta(
            name="product_bid",
            cim_role="ProductBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid:ProductBid",
            many=False,
            lower=1,
            upper=1,
            inverse="bid_hourly_product_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BidHourlyProductSchedule",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{49D7B906-B374-4e4c-A49F-18D8E096F5EC}",
        ends=(product_bid.meta,),
    )

    def __init__(
        self,
        *,
        product_bid: ProductBid | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if product_bid is not None:
            self.product_bid = product_bid
