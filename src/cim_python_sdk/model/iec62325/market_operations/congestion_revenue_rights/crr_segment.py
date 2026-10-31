"""CIM class CRRSegment (TC57CIM/IEC62325/MarketOperations/CongestionRevenueRights). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.congestion_revenue_right import (
        CongestionRevenueRight,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode


class CRRSegment(IdentifiedObject):
    """CRRSegment represents a segment of a CRR in a particular time frame.

    The segment class contains amount, clearing price, start date and time, end date and
    time."""

    __slots__ = (
        "_congestion_revenue_right",
        "_sink",
        "_source",
        "amount",
        "clearing_price",
        "end_date_time",
        "quantity",
        "start_date_time",
    )

    amount: _decimal.Decimal | None  # Money
    clearing_price: _decimal.Decimal | None  # Money
    end_date_time: _dt.datetime | None
    quantity: float | None
    start_date_time: _dt.datetime | None

    congestion_revenue_right: One[CongestionRevenueRight] = One(
        EndMeta(
            name="congestion_revenue_right",
            cim_role="CongestionRevenueRight",
            target="cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.congestion_revenue_right:CongestionRevenueRight",
            many=False,
            lower=1,
            upper=1,
            inverse="crr_segment",
            aggregation="none",
        )
    )
    sink: Many[Pnode] = Many(
        EndMeta(
            name="sink",
            cim_role="Sink",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=True,
            lower=0,
            upper=None,
            inverse="sink_crr_segment",
            aggregation="none",
        )
    )
    source: Many[Pnode] = Many(
        EndMeta(
            name="source",
            cim_role="Source",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=True,
            lower=0,
            upper=None,
            inverse="source_crr_segment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CRRSegment",
        package="TC57CIM/IEC62325/MarketOperations/CongestionRevenueRights",
        guid="{69DF78D3-49D3-476f-9D61-3F42EDB836BA}",
        attributes=(
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("clearing_price", "clearingPrice", "Money", 0, 1, "cimdatatype"),
            AttrMeta("end_date_time", "endDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("quantity", "quantity", "float", 0, 1, "primitive"),
            AttrMeta("start_date_time", "startDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            congestion_revenue_right.meta,
            sink.meta,
            source.meta,
        ),
    )

    def __init__(
        self,
        *,
        amount: _decimal.Decimal | None = None,
        clearing_price: _decimal.Decimal | None = None,
        end_date_time: _dt.datetime | None = None,
        quantity: float | None = None,
        start_date_time: _dt.datetime | None = None,
        congestion_revenue_right: CongestionRevenueRight | None = None,
        sink: Iterable[Pnode] | None = None,
        source: Iterable[Pnode] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.amount = amount
        self.clearing_price = clearing_price
        self.end_date_time = end_date_time
        self.quantity = quantity
        self.start_date_time = start_date_time
        if congestion_revenue_right is not None:
            self.congestion_revenue_right = congestion_revenue_right
        if sink is not None:
            CRRSegment.sink.extend(self, sink)
        if source is not None:
            CRRSegment.source.extend(self, source)

    def add_sink(self, sink: Pnode) -> Self:
        return CRRSegment.sink.add(self, sink)

    def remove_sink(self, sink: Pnode) -> Self:
        return CRRSegment.sink.remove(self, sink)

    def clear_sink(self) -> Self:
        return CRRSegment.sink.clear(self)

    def num_sink(self) -> int:
        return CRRSegment.sink.count(self)

    def get_sink_by_mrid(self, mrid: str) -> Pnode | None:
        return CRRSegment.sink.get_by_mrid(self, mrid)

    def add_source(self, source: Pnode) -> Self:
        return CRRSegment.source.add(self, source)

    def remove_source(self, source: Pnode) -> Self:
        return CRRSegment.source.remove(self, source)

    def clear_source(self) -> Self:
        return CRRSegment.source.clear(self)

    def num_source(self) -> int:
        return CRRSegment.source.count(self)

    def get_source_by_mrid(self, mrid: str) -> Pnode | None:
        return CRRSegment.source.get_by_mrid(self, mrid)
