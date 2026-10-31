"""CIM class NotificationTimeCurve (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid import (
        GeneratingBid,
    )


class NotificationTimeCurve(Curve):
    """Notification time curve as a function of down time. Relationship between crew
    notification time (Y1-axis) and unit startup time (Y2-axis) vs. unit elapsed down time
    (X-axis)."""

    __slots__ = ("_generating_bids",)

    generating_bids: Many[GeneratingBid] = Many(
        EndMeta(
            name="generating_bids",
            cim_role="GeneratingBids",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid:GeneratingBid",
            many=True,
            lower=0,
            upper=None,
            inverse="notification_time_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NotificationTimeCurve",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{985F418D-3104-422d-A6F4-39C1CBEEFF69}",
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
            NotificationTimeCurve.generating_bids.extend(self, generating_bids)

    def add_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return NotificationTimeCurve.generating_bids.add(self, generating_bid)

    def remove_generating_bid(self, generating_bid: GeneratingBid) -> Self:
        return NotificationTimeCurve.generating_bids.remove(self, generating_bid)

    def clear_generating_bids(self) -> Self:
        return NotificationTimeCurve.generating_bids.clear(self)

    def num_generating_bid(self) -> int:
        return NotificationTimeCurve.generating_bids.count(self)

    def get_generating_bid_by_mrid(self, mrid: str) -> GeneratingBid | None:
        return NotificationTimeCurve.generating_bids.get_by_mrid(self, mrid)
