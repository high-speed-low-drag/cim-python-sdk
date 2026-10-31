"""CIM class LoadDistributionFactor (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.distribution_factor_set import (
        DistributionFactorSet,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode import (
        AggregatedPnode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.individual_pnode import (
        IndividualPnode,
    )


class LoadDistributionFactor(CimObject):
    """This class models the load distribution factors. This class should be used in one of two
    ways:

    Use it along with the AggregatedPnode and the IndividualPnode to show the distriubtion
    of each individual party

    OR

    Use it with Mkt_EnergyConsumer to represent the current MW/Mvar distribution within it's
    parnet load group."""

    __slots__ = (
        "_aggregated_pnode",
        "_distribution_factor_set",
        "_individual_pnode",
        "p_dist_factor",
        "q_dist_factor",
    )

    p_dist_factor: float | None
    q_dist_factor: float | None

    aggregated_pnode: One[AggregatedPnode] = One(
        EndMeta(
            name="aggregated_pnode",
            cim_role="AggregatedPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode:AggregatedPnode",
            many=False,
            lower=0,
            upper=1,
            inverse="load_distribution_factor",
            aggregation="none",
        )
    )
    individual_pnode: One[IndividualPnode] = One(
        EndMeta(
            name="individual_pnode",
            cim_role="IndividualPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.individual_pnode:IndividualPnode",
            many=False,
            lower=0,
            upper=1,
            inverse="load_distribution_factor",
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
            inverse="load_distribution_factor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadDistributionFactor",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{5F30ADF0-511F-460c-BA44-39A90062F536}",
        attributes=(
            AttrMeta("p_dist_factor", "pDistFactor", "float", 0, 1, "primitive"),
            AttrMeta("q_dist_factor", "qDistFactor", "float", 0, 1, "primitive"),
        ),
        ends=(
            aggregated_pnode.meta,
            individual_pnode.meta,
            distribution_factor_set.meta,
        ),
    )

    def __init__(
        self,
        *,
        p_dist_factor: float | None = None,
        q_dist_factor: float | None = None,
        aggregated_pnode: AggregatedPnode | None = None,
        individual_pnode: IndividualPnode | None = None,
        distribution_factor_set: Iterable[DistributionFactorSet] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.p_dist_factor = p_dist_factor
        self.q_dist_factor = q_dist_factor
        if aggregated_pnode is not None:
            self.aggregated_pnode = aggregated_pnode
        if individual_pnode is not None:
            self.individual_pnode = individual_pnode
        if distribution_factor_set is not None:
            LoadDistributionFactor.distribution_factor_set.extend(self, distribution_factor_set)

    def add_distribution_factor_set(self, distribution_factor_set: DistributionFactorSet) -> Self:
        return LoadDistributionFactor.distribution_factor_set.add(self, distribution_factor_set)

    def remove_distribution_factor_set(
        self, distribution_factor_set: DistributionFactorSet
    ) -> Self:
        return LoadDistributionFactor.distribution_factor_set.remove(self, distribution_factor_set)

    def clear_distribution_factor_set(self) -> Self:
        return LoadDistributionFactor.distribution_factor_set.clear(self)

    def num_distribution_factor_set(self) -> int:
        return LoadDistributionFactor.distribution_factor_set.count(self)
