"""CIM class SysLoadDistributionFactor (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_connectivity_node import (
        MktConnectivityNode,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.distribution_factor_set import (
        DistributionFactorSet,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )


class SysLoadDistributionFactor(CimObject):
    """This class models the system distribution factors. This class needs to be used along
    with the HostControlArea and the ConnectivityNode to show the distribution of each
    individual party."""

    __slots__ = (
        "_distribution_factor_set",
        "_host_control_area",
        "_mkt_connectivity_node",
        "factor",
    )

    factor: float | None

    host_control_area: One[HostControlArea] = One(
        EndMeta(
            name="host_control_area",
            cim_role="HostControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="sys_load_distribu_factor",
            aggregation="none",
        )
    )
    distribution_factor_set: Many[DistributionFactorSet] = Many(
        EndMeta(
            name="distribution_factor_set",
            cim_role="DistributionFactorSet",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.distribution_factor_set:DistributionFactorSet",
            many=True,
            lower=0,
            upper=None,
            inverse="sys_load_distribu_factor",
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
            inverse="sys_load_distribu_factor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SysLoadDistributionFactor",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{1F407B8B-0DCD-4440-A23A-2571F2009882}",
        attributes=(AttrMeta("factor", "factor", "float", 0, 1, "primitive"),),
        ends=(
            host_control_area.meta,
            distribution_factor_set.meta,
            mkt_connectivity_node.meta,
        ),
    )

    def __init__(
        self,
        *,
        factor: float | None = None,
        host_control_area: HostControlArea | None = None,
        distribution_factor_set: Iterable[DistributionFactorSet] | None = None,
        mkt_connectivity_node: MktConnectivityNode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.factor = factor
        if host_control_area is not None:
            self.host_control_area = host_control_area
        if distribution_factor_set is not None:
            SysLoadDistributionFactor.distribution_factor_set.extend(self, distribution_factor_set)
        if mkt_connectivity_node is not None:
            self.mkt_connectivity_node = mkt_connectivity_node

    def add_distribution_factor_set(self, distribution_factor_set: DistributionFactorSet) -> Self:
        return SysLoadDistributionFactor.distribution_factor_set.add(self, distribution_factor_set)

    def remove_distribution_factor_set(
        self, distribution_factor_set: DistributionFactorSet
    ) -> Self:
        return SysLoadDistributionFactor.distribution_factor_set.remove(
            self, distribution_factor_set
        )

    def clear_distribution_factor_set(self) -> Self:
        return SysLoadDistributionFactor.distribution_factor_set.clear(self)

    def num_distribution_factor_set(self) -> int:
        return SysLoadDistributionFactor.distribution_factor_set.count(self)
