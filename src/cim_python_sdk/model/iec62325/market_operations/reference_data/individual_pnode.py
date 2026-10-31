"""CIM class IndividualPnode (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node import (
        MktConnectivityNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.gen_distribution_factor import (
        GenDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.load_distribution_factor import (
        LoadDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.congestion_area import (
        CongestionArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode_distribution_factor import (
        PnodeDistributionFactor,
    )


class IndividualPnode(Pnode):
    """Individual pricing node based on Pnode."""

    __slots__ = (
        "_congestion_area",
        "_gen_distribution_factor",
        "_load_distribution_factor",
        "_mkt_connectivity_node",
        "_pnode_distribution_factor",
    )

    gen_distribution_factor: One[GenDistributionFactor] = One(
        EndMeta(
            name="gen_distribution_factor",
            cim_role="GenDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.gen_distribution_factor:GenDistributionFactor",
            many=False,
            lower=0,
            upper=1,
            inverse="individual_pnode",
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
            inverse="individual_pnode",
            aggregation="none",
        )
    )
    mkt_connectivity_node: One[MktConnectivityNode] = One(
        EndMeta(
            name="mkt_connectivity_node",
            cim_role="MktConnectivityNode",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node:MktConnectivityNode",
            many=False,
            lower=1,
            upper=1,
            inverse="individual_pnode",
            aggregation="none",
        )
    )
    load_distribution_factor: One[LoadDistributionFactor] = One(
        EndMeta(
            name="load_distribution_factor",
            cim_role="LoadDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.load_distribution_factor:LoadDistributionFactor",
            many=False,
            lower=0,
            upper=1,
            inverse="individual_pnode",
            aggregation="none",
        )
    )
    congestion_area: Many[CongestionArea] = Many(
        EndMeta(
            name="congestion_area",
            cim_role="CongestionArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.congestion_area:CongestionArea",
            many=True,
            lower=0,
            upper=None,
            inverse="individual_pnode",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IndividualPnode",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{E6B3566B-661A-4e6f-819E-67B18C815E70}",
        ends=(
            gen_distribution_factor.meta,
            pnode_distribution_factor.meta,
            mkt_connectivity_node.meta,
            load_distribution_factor.meta,
            congestion_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        gen_distribution_factor: GenDistributionFactor | None = None,
        pnode_distribution_factor: Iterable[PnodeDistributionFactor] | None = None,
        mkt_connectivity_node: MktConnectivityNode | None = None,
        load_distribution_factor: LoadDistributionFactor | None = None,
        congestion_area: Iterable[CongestionArea] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if gen_distribution_factor is not None:
            self.gen_distribution_factor = gen_distribution_factor
        if pnode_distribution_factor is not None:
            IndividualPnode.pnode_distribution_factor.extend(self, pnode_distribution_factor)
        if mkt_connectivity_node is not None:
            self.mkt_connectivity_node = mkt_connectivity_node
        if load_distribution_factor is not None:
            self.load_distribution_factor = load_distribution_factor
        if congestion_area is not None:
            IndividualPnode.congestion_area.extend(self, congestion_area)

    def add_pnode_distribution_factor(
        self, pnode_distribution_factor: PnodeDistributionFactor
    ) -> Self:
        return IndividualPnode.pnode_distribution_factor.add(self, pnode_distribution_factor)

    def remove_pnode_distribution_factor(
        self, pnode_distribution_factor: PnodeDistributionFactor
    ) -> Self:
        return IndividualPnode.pnode_distribution_factor.remove(self, pnode_distribution_factor)

    def clear_pnode_distribution_factor(self) -> Self:
        return IndividualPnode.pnode_distribution_factor.clear(self)

    def num_pnode_distribution_factor(self) -> int:
        return IndividualPnode.pnode_distribution_factor.count(self)

    def add_congestion_area(self, congestion_area: CongestionArea) -> Self:
        return IndividualPnode.congestion_area.add(self, congestion_area)

    def remove_congestion_area(self, congestion_area: CongestionArea) -> Self:
        return IndividualPnode.congestion_area.remove(self, congestion_area)

    def clear_congestion_area(self) -> Self:
        return IndividualPnode.congestion_area.clear(self)

    def num_congestion_area(self) -> int:
        return IndividualPnode.congestion_area.count(self)

    def get_congestion_area_by_mrid(self, mrid: str) -> CongestionArea | None:
        return IndividualPnode.congestion_area.get_by_mrid(self, mrid)
