"""CIM class CongestionRevenueRight (TC57CIM/IEC62325/MarketOperations/CongestionRevenueRights). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.crr_org_role import (
        CRROrgRole,
    )
    from cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.crr_segment import (
        CRRSegment,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.crr_market import CRRMarket
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.crr_category_type import (
        CRRCategoryType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.crr_hedge_type import (
        CRRHedgeType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.crr_segment_type import (
        CRRSegmentType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.time_of_use import TimeOfUse
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class CongestionRevenueRight(Document):
    """Congestion Revenue Rights (CRR) class that is inherited from a Document class.

    A CRR is a financial concept that is used to hedge congestion charges.

    The CRR is usually settled based on the Locational Marginal Prices (LMPs) that are
    calculated in the day-ahead market. These LMPs are determined by the Day-ahead resource
    schedules/bids. CRRs will not hedge against marginal losses. If the congestion component
    of LMP at the sink is greater than at the source, then the CRR owner is entitled to
    receive a portion of congestion revenues. If the congestion component at the sink is
    less than at the source, then an obligation-type CRR owner will be charged, but an
    option-type CRR owner will not."""

    __slots__ = (
        "_crr_market",
        "_crr_org_role",
        "_crr_segment",
        "_flowgate",
        "c_r_rcategory",
        "c_r_rtype",
        "hedge_type",
        "time_of_use",
        "trade_slice_id",
    )

    c_r_rcategory: CRRCategoryType | None
    c_r_rtype: CRRSegmentType | None
    hedge_type: CRRHedgeType | None
    time_of_use: TimeOfUse | None
    trade_slice_id: str | None

    crr_segment: Many[CRRSegment] = Many(
        EndMeta(
            name="crr_segment",
            cim_role="CRRSegment",
            target="cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.crr_segment:CRRSegment",
            many=True,
            lower=1,
            upper=None,
            inverse="congestion_revenue_right",
            aggregation="none",
        )
    )
    crr_org_role: Many[CRROrgRole] = Many(
        EndMeta(
            name="crr_org_role",
            cim_role="CRROrgRole",
            target="cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.crr_org_role:CRROrgRole",
            many=True,
            lower=1,
            upper=None,
            inverse="congestion_revenue_right",
            aggregation="none",
        )
    )
    crr_market: One[CRRMarket] = One(
        EndMeta(
            name="crr_market",
            cim_role="CRRMarket",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.crr_market:CRRMarket",
            many=False,
            lower=1,
            upper=1,
            inverse="congestion_revenue_right",
            aggregation="none",
        )
    )
    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=0,
            upper=1,
            inverse="congestion_revenue_right",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CongestionRevenueRight",
        package="TC57CIM/IEC62325/MarketOperations/CongestionRevenueRights",
        guid="{4F6C4284-2F00-40f9-82EB-B6723F0438FD}",
        attributes=(
            AttrMeta("c_r_rcategory", "cRRcategory", "CRRCategoryType", 0, 1, "enumeration"),
            AttrMeta("c_r_rtype", "cRRtype", "CRRSegmentType", 0, 1, "enumeration"),
            AttrMeta("hedge_type", "hedgeType", "CRRHedgeType", 0, 1, "enumeration"),
            AttrMeta("time_of_use", "timeOfUse", "TimeOfUse", 0, 1, "enumeration"),
            AttrMeta("trade_slice_id", "tradeSliceID", "str", 0, 1, "primitive"),
        ),
        ends=(
            crr_segment.meta,
            crr_org_role.meta,
            crr_market.meta,
            flowgate.meta,
        ),
    )

    def __init__(
        self,
        *,
        c_r_rcategory: CRRCategoryType | None = None,
        c_r_rtype: CRRSegmentType | None = None,
        hedge_type: CRRHedgeType | None = None,
        time_of_use: TimeOfUse | None = None,
        trade_slice_id: str | None = None,
        crr_segment: Iterable[CRRSegment] | None = None,
        crr_org_role: Iterable[CRROrgRole] | None = None,
        crr_market: CRRMarket | None = None,
        flowgate: Flowgate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.c_r_rcategory = c_r_rcategory
        self.c_r_rtype = c_r_rtype
        self.hedge_type = hedge_type
        self.time_of_use = time_of_use
        self.trade_slice_id = trade_slice_id
        if crr_segment is not None:
            CongestionRevenueRight.crr_segment.extend(self, crr_segment)
        if crr_org_role is not None:
            CongestionRevenueRight.crr_org_role.extend(self, crr_org_role)
        if crr_market is not None:
            self.crr_market = crr_market
        if flowgate is not None:
            self.flowgate = flowgate

    def add_crr_segment(self, crr_segment: CRRSegment) -> Self:
        return CongestionRevenueRight.crr_segment.add(self, crr_segment)

    def remove_crr_segment(self, crr_segment: CRRSegment) -> Self:
        return CongestionRevenueRight.crr_segment.remove(self, crr_segment)

    def clear_crr_segment(self) -> Self:
        return CongestionRevenueRight.crr_segment.clear(self)

    def num_crr_segment(self) -> int:
        return CongestionRevenueRight.crr_segment.count(self)

    def get_crr_segment_by_mrid(self, mrid: str) -> CRRSegment | None:
        return CongestionRevenueRight.crr_segment.get_by_mrid(self, mrid)

    def add_crr_org_role(self, crr_org_role: CRROrgRole) -> Self:
        return CongestionRevenueRight.crr_org_role.add(self, crr_org_role)

    def remove_crr_org_role(self, crr_org_role: CRROrgRole) -> Self:
        return CongestionRevenueRight.crr_org_role.remove(self, crr_org_role)

    def clear_crr_org_role(self) -> Self:
        return CongestionRevenueRight.crr_org_role.clear(self)

    def num_crr_org_role(self) -> int:
        return CongestionRevenueRight.crr_org_role.count(self)

    def get_crr_org_role_by_mrid(self, mrid: str) -> CRROrgRole | None:
        return CongestionRevenueRight.crr_org_role.get_by_mrid(self, mrid)
