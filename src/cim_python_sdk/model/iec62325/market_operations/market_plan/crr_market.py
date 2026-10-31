"""CIM class CRRMarket (TC57CIM/IEC62325/MarketOperations/MarketPlan). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market import Market

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.congestion_revenue_right import (
        CongestionRevenueRight,
    )


class CRRMarket(Market):
    """Model that describes the Congestion Revenue Rights Auction Market."""

    __slots__ = ("_congestion_revenue_right", "label_id")

    label_id: str | None

    congestion_revenue_right: Many[CongestionRevenueRight] = Many(
        EndMeta(
            name="congestion_revenue_right",
            cim_role="CongestionRevenueRight",
            target="cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.congestion_revenue_right:CongestionRevenueRight",
            many=True,
            lower=1,
            upper=None,
            inverse="crr_market",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CRRMarket",
        package="TC57CIM/IEC62325/MarketOperations/MarketPlan",
        guid="{C1414DA4-19B7-40a3-82D2-07730A10ED6F}",
        attributes=(AttrMeta("label_id", "labelID", "str", 0, 1, "primitive"),),
        ends=(congestion_revenue_right.meta,),
    )

    def __init__(
        self,
        *,
        label_id: str | None = None,
        congestion_revenue_right: Iterable[CongestionRevenueRight] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.label_id = label_id
        if congestion_revenue_right is not None:
            CRRMarket.congestion_revenue_right.extend(self, congestion_revenue_right)

    def add_congestion_revenue_right(
        self, congestion_revenue_right: CongestionRevenueRight
    ) -> Self:
        return CRRMarket.congestion_revenue_right.add(self, congestion_revenue_right)

    def remove_congestion_revenue_right(
        self, congestion_revenue_right: CongestionRevenueRight
    ) -> Self:
        return CRRMarket.congestion_revenue_right.remove(self, congestion_revenue_right)

    def clear_congestion_revenue_right(self) -> Self:
        return CRRMarket.congestion_revenue_right.clear(self)

    def num_congestion_revenue_right(self) -> int:
        return CRRMarket.congestion_revenue_right.count(self)

    def get_congestion_revenue_right_by_mrid(self, mrid: str) -> CongestionRevenueRight | None:
        return CRRMarket.congestion_revenue_right.get_by_mrid(self, mrid)
