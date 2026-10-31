"""CIM class BidDistributionFactor (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid import (
        ProductBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode_distribution_factor import (
        PnodeDistributionFactor,
    )


class BidDistributionFactor(CimObject):
    """This class allows SC to input different time intervals for distribution factors."""

    __slots__ = (
        "_pnode_distribution_factor",
        "_product_bid",
        "time_interval_end",
        "time_interval_start",
    )

    time_interval_start: _dt.datetime | None
    time_interval_end: _dt.datetime | None

    product_bid: One[ProductBid] = One(
        EndMeta(
            name="product_bid",
            cim_role="ProductBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.product_bid:ProductBid",
            many=False,
            lower=1,
            upper=1,
            inverse="bid_distribution_factor",
            aggregation="none",
        )
    )
    pnode_distribution_factor: Many[PnodeDistributionFactor] = Many(
        EndMeta(
            name="pnode_distribution_factor",
            cim_role="PnodeDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode_distribution_factor:PnodeDistributionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="bid_distribution_factor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BidDistributionFactor",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{36444558-B7DA-402b-AF2C-2D4E99F67AE3}",
        attributes=(
            AttrMeta("time_interval_start", "timeIntervalStart", "datetime", 0, 1, "primitive"),
            AttrMeta("time_interval_end", "timeIntervalEnd", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            product_bid.meta,
            pnode_distribution_factor.meta,
        ),
    )

    def __init__(
        self,
        *,
        time_interval_start: _dt.datetime | None = None,
        time_interval_end: _dt.datetime | None = None,
        product_bid: ProductBid | None = None,
        pnode_distribution_factor: Iterable[PnodeDistributionFactor] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time_interval_start = time_interval_start
        self.time_interval_end = time_interval_end
        if product_bid is not None:
            self.product_bid = product_bid
        if pnode_distribution_factor is not None:
            BidDistributionFactor.pnode_distribution_factor.extend(self, pnode_distribution_factor)

    def add_pnode_distribution_factor(
        self, pnode_distribution_factor: PnodeDistributionFactor
    ) -> Self:
        return BidDistributionFactor.pnode_distribution_factor.add(self, pnode_distribution_factor)

    def remove_pnode_distribution_factor(
        self, pnode_distribution_factor: PnodeDistributionFactor
    ) -> Self:
        return BidDistributionFactor.pnode_distribution_factor.remove(
            self, pnode_distribution_factor
        )

    def clear_pnode_distribution_factor(self) -> Self:
        return BidDistributionFactor.pnode_distribution_factor.clear(self)

    def num_pnode_distribution_factor(self) -> int:
        return BidDistributionFactor.pnode_distribution_factor.count(self)
