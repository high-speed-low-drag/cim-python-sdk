"""CIM class Auction (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class Auction(IdentifiedObject):
    """A class providing the identification and type of an auction."""

    __slots__ = (
        "_time_series",
        "allocation_mode",
        "cancelled",
        "category",
        "payment_terms",
        "rights",
        "type",
    )

    allocation_mode: str | None
    cancelled: str | None
    category: str | None
    payment_terms: str | None
    rights: str | None
    type: str | None

    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="auction",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Auction",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{0BEEB3F1-7308-4074-9B32-36BAB2F54807}",
        attributes=(
            AttrMeta("allocation_mode", "allocationMode", "str", 0, 1, "primitive"),
            AttrMeta("cancelled", "cancelled", "str", 0, 1, "primitive"),
            AttrMeta("category", "category", "str", 0, 1, "primitive"),
            AttrMeta("payment_terms", "paymentTerms", "str", 0, 1, "primitive"),
            AttrMeta("rights", "rights", "str", 0, 1, "primitive"),
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
        ),
        ends=(time_series.meta,),
    )

    def __init__(
        self,
        *,
        allocation_mode: str | None = None,
        cancelled: str | None = None,
        category: str | None = None,
        payment_terms: str | None = None,
        rights: str | None = None,
        type: str | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.allocation_mode = allocation_mode
        self.cancelled = cancelled
        self.category = category
        self.payment_terms = payment_terms
        self.rights = rights
        self.type = type
        if time_series is not None:
            Auction.time_series.extend(self, time_series)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return Auction.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return Auction.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return Auction.time_series.clear(self)

    def num_time_series(self) -> int:
        return Auction.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return Auction.time_series.get_by_mrid(self, mrid)
