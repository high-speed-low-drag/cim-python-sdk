"""CIM class MitigatedBidClearing (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid import (
        MitigatedBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_resource_status import (
        MPMResourceStatus,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.rmr_determination import (
        RMRDetermination,
    )


class MitigatedBidClearing(MarketFactors):
    """Model of market power mitigation through reference or mitigated bids. Interval based."""

    __slots__ = ("_mitigated_bid", "_mpm_resource_status", "_rmr_determination")

    rmr_determination: Many[RMRDetermination] = Many(
        EndMeta(
            name="rmr_determination",
            cim_role="RMRDetermination",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.rmr_determination:RMRDetermination",
            many=True,
            lower=0,
            upper=None,
            inverse="mitigated_bid_clearing",
            aggregation="none",
        )
    )
    mitigated_bid: Many[MitigatedBid] = Many(
        EndMeta(
            name="mitigated_bid",
            cim_role="MitigatedBid",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mitigated_bid:MitigatedBid",
            many=True,
            lower=0,
            upper=None,
            inverse="mitigated_bid_clearing",
            aggregation="none",
        )
    )
    mpm_resource_status: Many[MPMResourceStatus] = Many(
        EndMeta(
            name="mpm_resource_status",
            cim_role="MPMResourceStatus",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_resource_status:MPMResourceStatus",
            many=True,
            lower=0,
            upper=None,
            inverse="mitigated_bid_clearing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MitigatedBidClearing",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{70FE2C69-FAF0-43fa-8233-648A2E7ECC60}",
        ends=(
            rmr_determination.meta,
            mitigated_bid.meta,
            mpm_resource_status.meta,
        ),
    )

    def __init__(
        self,
        *,
        rmr_determination: Iterable[RMRDetermination] | None = None,
        mitigated_bid: Iterable[MitigatedBid] | None = None,
        mpm_resource_status: Iterable[MPMResourceStatus] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if rmr_determination is not None:
            MitigatedBidClearing.rmr_determination.extend(self, rmr_determination)
        if mitigated_bid is not None:
            MitigatedBidClearing.mitigated_bid.extend(self, mitigated_bid)
        if mpm_resource_status is not None:
            MitigatedBidClearing.mpm_resource_status.extend(self, mpm_resource_status)

    def add_rmr_determination(self, rmr_determination: RMRDetermination) -> Self:
        return MitigatedBidClearing.rmr_determination.add(self, rmr_determination)

    def remove_rmr_determination(self, rmr_determination: RMRDetermination) -> Self:
        return MitigatedBidClearing.rmr_determination.remove(self, rmr_determination)

    def clear_rmr_determination(self) -> Self:
        return MitigatedBidClearing.rmr_determination.clear(self)

    def num_rmr_determination(self) -> int:
        return MitigatedBidClearing.rmr_determination.count(self)

    def add_mitigated_bid(self, mitigated_bid: MitigatedBid) -> Self:
        return MitigatedBidClearing.mitigated_bid.add(self, mitigated_bid)

    def remove_mitigated_bid(self, mitigated_bid: MitigatedBid) -> Self:
        return MitigatedBidClearing.mitigated_bid.remove(self, mitigated_bid)

    def clear_mitigated_bid(self) -> Self:
        return MitigatedBidClearing.mitigated_bid.clear(self)

    def num_mitigated_bid(self) -> int:
        return MitigatedBidClearing.mitigated_bid.count(self)

    def get_mitigated_bid_by_mrid(self, mrid: str) -> MitigatedBid | None:
        return MitigatedBidClearing.mitigated_bid.get_by_mrid(self, mrid)

    def add_mpm_resource_status(self, mpm_resource_status: MPMResourceStatus) -> Self:
        return MitigatedBidClearing.mpm_resource_status.add(self, mpm_resource_status)

    def remove_mpm_resource_status(self, mpm_resource_status: MPMResourceStatus) -> Self:
        return MitigatedBidClearing.mpm_resource_status.remove(self, mpm_resource_status)

    def clear_mpm_resource_status(self) -> Self:
        return MitigatedBidClearing.mpm_resource_status.clear(self)

    def num_mpm_resource_status(self) -> int:
        return MitigatedBidClearing.mpm_resource_status.count(self)
