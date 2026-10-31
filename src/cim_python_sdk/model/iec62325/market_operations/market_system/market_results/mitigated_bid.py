"""CIM class MitigatedBid (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid_clearing import (
        MitigatedBidClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid


class MitigatedBid(IdentifiedObject):
    """Mitigated bid results posted for a given settlement period."""

    __slots__ = ("_bid", "_mitigated_bid_clearing")

    bid: One[Bid] = One(
        EndMeta(
            name="bid",
            cim_role="Bid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid:Bid",
            many=False,
            lower=0,
            upper=1,
            inverse="mitigated_bid",
            aggregation="none",
        )
    )
    mitigated_bid_clearing: Many[MitigatedBidClearing] = Many(
        EndMeta(
            name="mitigated_bid_clearing",
            cim_role="MitigatedBidClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid_clearing:MitigatedBidClearing",
            many=True,
            lower=1,
            upper=None,
            inverse="mitigated_bid",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MitigatedBid",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{BB03E840-974D-42d2-889C-538806C4467D}",
        ends=(
            bid.meta,
            mitigated_bid_clearing.meta,
        ),
    )

    def __init__(
        self,
        *,
        bid: Bid | None = None,
        mitigated_bid_clearing: Iterable[MitigatedBidClearing] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if bid is not None:
            self.bid = bid
        if mitigated_bid_clearing is not None:
            MitigatedBid.mitigated_bid_clearing.extend(self, mitigated_bid_clearing)

    def add_mitigated_bid_clearing(self, mitigated_bid_clearing: MitigatedBidClearing) -> Self:
        return MitigatedBid.mitigated_bid_clearing.add(self, mitigated_bid_clearing)

    def remove_mitigated_bid_clearing(self, mitigated_bid_clearing: MitigatedBidClearing) -> Self:
        return MitigatedBid.mitigated_bid_clearing.remove(self, mitigated_bid_clearing)

    def clear_mitigated_bid_clearing(self) -> Self:
        return MitigatedBid.mitigated_bid_clearing.clear(self)

    def num_mitigated_bid_clearing(self) -> int:
        return MitigatedBid.mitigated_bid_clearing.count(self)

    def get_mitigated_bid_clearing_by_mrid(self, mrid: str) -> MitigatedBidClearing | None:
        return MitigatedBid.mitigated_bid_clearing.get_by_mrid(self, mrid)
