"""CIM class BidSet (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid import (
        GeneratingBid,
    )


class BidSet(IdentifiedObject):
    """As set of mutually exclusive bids for which a maximum of one may be scheduled.

    Of these generating bids, only one generating bid can be scheduled at a time."""

    __slots__ = ("_generating_bids",)

    generating_bids: Many[GeneratingBid] = Many(
        EndMeta(
            name="generating_bids",
            cim_role="GeneratingBids",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid:GeneratingBid",
            many=True,
            lower=1,
            upper=None,
            inverse="bid_set",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BidSet",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{4A2C7058-24F5-4782-9CFC-2CC12357DAD3}",
        ends=(generating_bids.meta,),
    )

    def __init__(
        self,
        *,
        generating_bids: Iterable[GeneratingBid] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if generating_bids is not None:
            BidSet.generating_bids.extend(self, generating_bids)

    def add_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return BidSet.generating_bids.add(self, generating_bid)

    def remove_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return BidSet.generating_bids.remove(self, generating_bid)

    def clear_generating_bids(self) -> Self:
        return BidSet.generating_bids.clear(self)

    def num_generating_bid(self) -> int:
        return BidSet.generating_bids.count(self)

    def get_generating_bid_by_mrid(self, mrid: str) -> GeneratingBid | None:
        return BidSet.generating_bids.get_by_mrid(self, mrid)
