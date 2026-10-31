"""CIM class PnodeDistributionFactor (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_distribution_factor import (
        BidDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode import (
        AggregatedPnode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.individual_pnode import (
        IndividualPnode,
    )


class PnodeDistributionFactor(CimObject):
    """This class allows SC to input different distribution factors for pricing node."""

    __slots__ = (
        "_aggregated_pnode",
        "_bid_distribution_factor",
        "_individual_pnode",
        "factor",
        "off_peak",
        "on_peak",
        "pod_loss_factor",
    )

    factor: float | None
    off_peak: YesNo | None
    on_peak: YesNo | None
    pod_loss_factor: float | None

    individual_pnode: One[IndividualPnode] = One(
        EndMeta(
            name="individual_pnode",
            cim_role="IndividualPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.individual_pnode:IndividualPnode",
            many=False,
            lower=1,
            upper=1,
            inverse="pnode_distribution_factor",
            aggregation="none",
        )
    )
    bid_distribution_factor: One[BidDistributionFactor] = One(
        EndMeta(
            name="bid_distribution_factor",
            cim_role="BidDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_distribution_factor:BidDistributionFactor",
            many=False,
            lower=0,
            upper=1,
            inverse="pnode_distribution_factor",
            aggregation="none",
        )
    )
    aggregated_pnode: One[AggregatedPnode] = One(
        EndMeta(
            name="aggregated_pnode",
            cim_role="AggregatedPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode:AggregatedPnode",
            many=False,
            lower=1,
            upper=1,
            inverse="pnode_distribution_factor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PnodeDistributionFactor",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{116353F7-F4CD-4f9d-8B45-BEE771C51F06}",
        attributes=(
            AttrMeta("factor", "factor", "float", 0, 1, "primitive"),
            AttrMeta("off_peak", "offPeak", "YesNo", 0, 1, "enumeration"),
            AttrMeta("on_peak", "onPeak", "YesNo", 0, 1, "enumeration"),
            AttrMeta("pod_loss_factor", "podLossFactor", "float", 0, 1, "primitive"),
        ),
        ends=(
            individual_pnode.meta,
            bid_distribution_factor.meta,
            aggregated_pnode.meta,
        ),
    )

    def __init__(
        self,
        *,
        factor: float | None = None,
        off_peak: YesNo | None = None,
        on_peak: YesNo | None = None,
        pod_loss_factor: float | None = None,
        individual_pnode: IndividualPnode | None = None,
        bid_distribution_factor: BidDistributionFactor | None = None,
        aggregated_pnode: AggregatedPnode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.factor = factor
        self.off_peak = off_peak
        self.on_peak = on_peak
        self.pod_loss_factor = pod_loss_factor
        if individual_pnode is not None:
            self.individual_pnode = individual_pnode
        if bid_distribution_factor is not None:
            self.bid_distribution_factor = bid_distribution_factor
        if aggregated_pnode is not None:
            self.aggregated_pnode = aggregated_pnode
