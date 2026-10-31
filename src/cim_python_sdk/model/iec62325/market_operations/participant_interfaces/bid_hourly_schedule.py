"""CIM class BidHourlySchedule (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid


class BidHourlySchedule(RegularIntervalSchedule):
    """Containment for bid hourly parameters that are not product dependent."""

    __slots__ = ("_bid",)

    bid: One[Bid] = One(
        EndMeta(
            name="bid",
            cim_role="Bid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid:Bid",
            many=False,
            lower=1,
            upper=1,
            inverse="bid_hourly_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BidHourlySchedule",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{42A3622D-147E-432e-A47E-EDD16C015035}",
        ends=(bid.meta,),
    )

    def __init__(
        self,
        *,
        bid: Bid | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if bid is not None:
            self.bid = bid
