"""CIM class MitigatedBidSegment (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid


class MitigatedBidSegment(CimObject):
    """Model of mitigated bid. Indicates segment of piece-wise linear bid, that has been
    mitigated."""

    __slots__ = ("_bid", "interval_start_time", "segment_mw", "segment_number", "threshold_type")

    interval_start_time: _dt.datetime | None
    threshold_type: str | None
    segment_number: int | None
    segment_mw: float | None

    bid: One[Bid] = One(
        EndMeta(
            name="bid",
            cim_role="Bid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid:Bid",
            many=False,
            lower=1,
            upper=1,
            inverse="mitigated_bid_segment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MitigatedBidSegment",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{8283C8BB-51F6-4b6e-9165-F0720FBAEA71}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("threshold_type", "thresholdType", "str", 0, 1, "primitive"),
            AttrMeta("segment_number", "segmentNumber", "int", 0, 1, "primitive"),
            AttrMeta("segment_mw", "segmentMW", "float", 0, 1, "primitive"),
        ),
        ends=(bid.meta,),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        threshold_type: str | None = None,
        segment_number: int | None = None,
        segment_mw: float | None = None,
        bid: Bid | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        self.threshold_type = threshold_type
        self.segment_number = segment_number
        self.segment_mw = segment_mw
        if bid is not None:
            self.bid = bid
