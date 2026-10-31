"""CIM class CRROrgRole (TC57CIM/IEC62325/MarketOperations/CongestionRevenueRights). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.congestion_revenue_right import (
        CongestionRevenueRight,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.crr_role_type import CRRRoleType


class CRROrgRole(OrganisationRole):
    """Identifies a way in which an organisation may participate with a defined Congestion
    Revenue Right (CRR)."""

    __slots__ = ("_congestion_revenue_right", "kind", "status")

    kind: CRRRoleType | None
    status: Status | None

    congestion_revenue_right: One[CongestionRevenueRight] = One(
        EndMeta(
            name="congestion_revenue_right",
            cim_role="CongestionRevenueRight",
            target="cim_python_sdk.model.iec62325.market_operations.congestion_revenue_rights.congestion_revenue_right:CongestionRevenueRight",
            many=False,
            lower=1,
            upper=1,
            inverse="crr_org_role",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CRROrgRole",
        package="TC57CIM/IEC62325/MarketOperations/CongestionRevenueRights",
        guid="{3806A99D-27A4-4019-B55D-288CA9D01F63}",
        attributes=(
            AttrMeta("kind", "kind", "CRRRoleType", 0, 1, "enumeration"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(congestion_revenue_right.meta,),
    )

    def __init__(
        self,
        *,
        kind: CRRRoleType | None = None,
        status: Status | None = None,
        congestion_revenue_right: CongestionRevenueRight | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.status = status
        if congestion_revenue_right is not None:
            self.congestion_revenue_right = congestion_revenue_right
