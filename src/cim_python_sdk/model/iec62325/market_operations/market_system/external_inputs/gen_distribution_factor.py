"""CIM class GenDistributionFactor (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

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


class GenDistributionFactor(CimObject):
    """This class models the generation distribution factors. This class needs to be used along
    with the AggregatedPnode and the IndividualPnode to show the distribution of each
    individual party."""

    __slots__ = ("_aggregated_pnode", "_distribution_factor_set", "_individual_pnode", "factor")

    factor: float | None

    individual_pnode: One[IndividualPnode] = One(
        EndMeta(
            name="individual_pnode",
            cim_role="IndividualPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.individual_pnode:IndividualPnode",
            many=False,
            lower=0,
            upper=1,
            inverse="gen_distribution_factor",
            aggregation="none",
        )
    )
    aggregated_pnode: One[AggregatedPnode] = One(
        EndMeta(
            name="aggregated_pnode",
            cim_role="AggregatedPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode:AggregatedPnode",
            many=False,
            lower=0,
            upper=1,
            inverse="gen_distribution_factor",
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
            inverse="gen_distribution_factor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GenDistributionFactor",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{8BFC9A50-2A30-454c-9906-8F95A9A88057}",
        attributes=(AttrMeta("factor", "factor", "float", 0, 1, "primitive"),),
        ends=(
            individual_pnode.meta,
            aggregated_pnode.meta,
            distribution_factor_set.meta,
        ),
    )

    def __init__(
        self,
        *,
        factor: float | None = None,
        individual_pnode: IndividualPnode | None = None,
        aggregated_pnode: AggregatedPnode | None = None,
        distribution_factor_set: Iterable[DistributionFactorSet] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.factor = factor
        if individual_pnode is not None:
            self.individual_pnode = individual_pnode
        if aggregated_pnode is not None:
            self.aggregated_pnode = aggregated_pnode
        if distribution_factor_set is not None:
            GenDistributionFactor.distribution_factor_set.extend(self, distribution_factor_set)

    def add_distribution_factor_set(self, distribution_factor_set: DistributionFactorSet) -> Self:
        return GenDistributionFactor.distribution_factor_set.add(self, distribution_factor_set)

    def remove_distribution_factor_set(
        self, distribution_factor_set: DistributionFactorSet
    ) -> Self:
        return GenDistributionFactor.distribution_factor_set.remove(self, distribution_factor_set)

    def clear_distribution_factor_set(self) -> Self:
        return GenDistributionFactor.distribution_factor_set.clear(self)

    def num_distribution_factor_set(self) -> int:
        return GenDistributionFactor.distribution_factor_set.count(self)
