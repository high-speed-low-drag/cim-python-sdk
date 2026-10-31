"""CIM class MarketFactors (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_activity_record import (
        MktActivityRecord,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.market import Market


class MarketFactors(Document):
    """Aggregation of market information relative for a specific time interval."""

    __slots__ = ("_market", "_mkt_activity_record", "interval_end_time", "interval_start_time")

    interval_end_time: _dt.datetime | None
    interval_start_time: _dt.datetime | None

    mkt_activity_record: Many[MktActivityRecord] = Many(
        EndMeta(
            name="mkt_activity_record",
            cim_role="MktActivityRecord",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_activity_record:MktActivityRecord",
            many=True,
            lower=0,
            upper=None,
            inverse="market_factors",
            aggregation="none",
        )
    )
    market: One[Market] = One(
        EndMeta(
            name="market",
            cim_role="Market",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market:Market",
            many=False,
            lower=0,
            upper=1,
            inverse="market_factors",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketFactors",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{DC324B9D-14ED-47f5-8F9C-6779797D04F7}",
        attributes=(
            AttrMeta("interval_end_time", "intervalEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            mkt_activity_record.meta,
            market.meta,
        ),
    )

    def __init__(
        self,
        *,
        interval_end_time: _dt.datetime | None = None,
        interval_start_time: _dt.datetime | None = None,
        mkt_activity_record: Iterable[MktActivityRecord] | None = None,
        market: Market | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_end_time = interval_end_time
        self.interval_start_time = interval_start_time
        if mkt_activity_record is not None:
            MarketFactors.mkt_activity_record.extend(self, mkt_activity_record)
        if market is not None:
            self.market = market

    def add_mkt_activity_record(self, mkt_activity_record: MktActivityRecord) -> Self:
        return MarketFactors.mkt_activity_record.add(self, mkt_activity_record)

    def remove_mkt_activity_record(self, mkt_activity_record: MktActivityRecord) -> Self:
        return MarketFactors.mkt_activity_record.remove(self, mkt_activity_record)

    def clear_mkt_activity_record(self) -> Self:
        return MarketFactors.mkt_activity_record.clear(self)

    def num_mkt_activity_record(self) -> int:
        return MarketFactors.mkt_activity_record.count(self)

    def get_mkt_activity_record_by_mrid(self, mrid: str) -> MktActivityRecord | None:
        return MarketFactors.mkt_activity_record.get_by_mrid(self, mrid)
