"""CIM class AggregatedPnode (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.trading_hub_values import (
        TradingHubValues,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.gen_distribution_factor import (
        GenDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.load_distribution_factor import (
        LoadDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_test_results import (
        MPMTestResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.apnode_type import ApnodeType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.participation_category_mpm import (
        ParticipationCategoryMPM,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_combined_cycle_plant import (
        MktCombinedCyclePlant,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_threshold import (
        MPMTestThreshold,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode_distribution_factor import (
        PnodeDistributionFactor,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.tac_area import TACArea


class AggregatedPnode(Pnode):
    """An aggregated pricing node is a specialized type of pricing node used to model items
    such as System Zone, Default Price Zone, Custom Price Zone, Control Area, Aggregated
    Generation, Aggregated Particpating Load, Aggregated Non-Participating Load, Trading
    Hub, Designated Control Area(DCA) Zone."""

    __slots__ = (
        "_gen_distribution_factor",
        "_load_distribution_factor",
        "_mkt_combined_cycle_plant",
        "_mpm_test_results",
        "_mpm_test_threshold",
        "_pnode_distribution_factor",
        "_tac_area",
        "_trading_hub_values",
        "apnode_type",
        "participation_category",
    )

    apnode_type: ApnodeType | None
    participation_category: ParticipationCategoryMPM | None

    tac_area: Many[TACArea] = Many(
        EndMeta(
            name="tac_area",
            cim_role="TACArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.tac_area:TACArea",
            many=True,
            lower=0,
            upper=None,
            inverse="aggregated_pnode",
            aggregation="none",
        )
    )
    load_distribution_factor: Many[LoadDistributionFactor] = Many(
        EndMeta(
            name="load_distribution_factor",
            cim_role="LoadDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.load_distribution_factor:LoadDistributionFactor",
            many=True,
            lower=1,
            upper=None,
            inverse="aggregated_pnode",
            aggregation="none",
        )
    )
    trading_hub_values: Many[TradingHubValues] = Many(
        EndMeta(
            name="trading_hub_values",
            cim_role="TradingHubValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.trading_hub_values:TradingHubValues",
            many=True,
            lower=0,
            upper=None,
            inverse="aggregated_pnode",
            aggregation="none",
        )
    )
    mpm_test_threshold: Many[MPMTestThreshold] = Many(
        EndMeta(
            name="mpm_test_threshold",
            cim_role="MPMTestThreshold",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mpm_test_threshold:MPMTestThreshold",
            many=True,
            lower=1,
            upper=None,
            inverse="aggregated_pnode",
            aggregation="none",
        )
    )
    mkt_combined_cycle_plant: Many[MktCombinedCyclePlant] = Many(
        EndMeta(
            name="mkt_combined_cycle_plant",
            cim_role="MktCombinedCyclePlant",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_combined_cycle_plant:MktCombinedCyclePlant",
            many=True,
            lower=0,
            upper=None,
            inverse="aggregated_pnode",
            aggregation="none",
        )
    )
    gen_distribution_factor: Many[GenDistributionFactor] = Many(
        EndMeta(
            name="gen_distribution_factor",
            cim_role="GenDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.gen_distribution_factor:GenDistributionFactor",
            many=True,
            lower=1,
            upper=None,
            inverse="aggregated_pnode",
            aggregation="none",
        )
    )
    mpm_test_results: Many[MPMTestResults] = Many(
        EndMeta(
            name="mpm_test_results",
            cim_role="MPMTestResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.mpm_test_results:MPMTestResults",
            many=True,
            lower=1,
            upper=None,
            inverse="aggregated_pnode",
            aggregation="none",
        )
    )
    pnode_distribution_factor: Many[PnodeDistributionFactor] = Many(
        EndMeta(
            name="pnode_distribution_factor",
            cim_role="PnodeDistributionFactor",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode_distribution_factor:PnodeDistributionFactor",
            many=True,
            lower=1,
            upper=None,
            inverse="aggregated_pnode",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AggregatedPnode",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{175E9723-D1D7-497a-A5BF-82FFBC0CC3D4}",
        attributes=(
            AttrMeta("apnode_type", "apnodeType", "ApnodeType", 0, 1, "enumeration"),
            AttrMeta(
                "participation_category",
                "participationCategory",
                "ParticipationCategoryMPM",
                0,
                1,
                "enumeration",
            ),
        ),
        ends=(
            tac_area.meta,
            load_distribution_factor.meta,
            trading_hub_values.meta,
            mpm_test_threshold.meta,
            mkt_combined_cycle_plant.meta,
            gen_distribution_factor.meta,
            mpm_test_results.meta,
            pnode_distribution_factor.meta,
        ),
    )

    def __init__(
        self,
        *,
        apnode_type: ApnodeType | None = None,
        participation_category: ParticipationCategoryMPM | None = None,
        tac_area: Iterable[TACArea] | None = None,
        load_distribution_factor: Iterable[LoadDistributionFactor] | None = None,
        trading_hub_values: Iterable[TradingHubValues] | None = None,
        mpm_test_threshold: Iterable[MPMTestThreshold] | None = None,
        mkt_combined_cycle_plant: Iterable[MktCombinedCyclePlant] | None = None,
        gen_distribution_factor: Iterable[GenDistributionFactor] | None = None,
        mpm_test_results: Iterable[MPMTestResults] | None = None,
        pnode_distribution_factor: Iterable[PnodeDistributionFactor] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.apnode_type = apnode_type
        self.participation_category = participation_category
        if tac_area is not None:
            AggregatedPnode.tac_area.extend(self, tac_area)
        if load_distribution_factor is not None:
            AggregatedPnode.load_distribution_factor.extend(self, load_distribution_factor)
        if trading_hub_values is not None:
            AggregatedPnode.trading_hub_values.extend(self, trading_hub_values)
        if mpm_test_threshold is not None:
            AggregatedPnode.mpm_test_threshold.extend(self, mpm_test_threshold)
        if mkt_combined_cycle_plant is not None:
            AggregatedPnode.mkt_combined_cycle_plant.extend(self, mkt_combined_cycle_plant)
        if gen_distribution_factor is not None:
            AggregatedPnode.gen_distribution_factor.extend(self, gen_distribution_factor)
        if mpm_test_results is not None:
            AggregatedPnode.mpm_test_results.extend(self, mpm_test_results)
        if pnode_distribution_factor is not None:
            AggregatedPnode.pnode_distribution_factor.extend(self, pnode_distribution_factor)

    def add_tac_area(self, tac_area: TACArea) -> Self:
        return AggregatedPnode.tac_area.add(self, tac_area)

    def remove_tac_area(self, tac_area: TACArea) -> Self:
        return AggregatedPnode.tac_area.remove(self, tac_area)

    def clear_tac_area(self) -> Self:
        return AggregatedPnode.tac_area.clear(self)

    def num_tac_area(self) -> int:
        return AggregatedPnode.tac_area.count(self)

    def get_tac_area_by_mrid(self, mrid: str) -> TACArea | None:
        return AggregatedPnode.tac_area.get_by_mrid(self, mrid)

    def add_load_distribution_factor(
        self, load_distribution_factor: LoadDistributionFactor
    ) -> Self:
        return AggregatedPnode.load_distribution_factor.add(self, load_distribution_factor)

    def remove_load_distribution_factor(
        self, load_distribution_factor: LoadDistributionFactor
    ) -> Self:
        return AggregatedPnode.load_distribution_factor.remove(self, load_distribution_factor)

    def clear_load_distribution_factor(self) -> Self:
        return AggregatedPnode.load_distribution_factor.clear(self)

    def num_load_distribution_factor(self) -> int:
        return AggregatedPnode.load_distribution_factor.count(self)

    def add_trading_hub_value(self, trading_hub_value: TradingHubValues) -> Self:
        return AggregatedPnode.trading_hub_values.add(self, trading_hub_value)

    def remove_trading_hub_value(self, trading_hub_value: TradingHubValues) -> Self:
        return AggregatedPnode.trading_hub_values.remove(self, trading_hub_value)

    def clear_trading_hub_values(self) -> Self:
        return AggregatedPnode.trading_hub_values.clear(self)

    def num_trading_hub_value(self) -> int:
        return AggregatedPnode.trading_hub_values.count(self)

    def add_mpm_test_threshold(self, mpm_test_threshold: MPMTestThreshold) -> Self:
        return AggregatedPnode.mpm_test_threshold.add(self, mpm_test_threshold)

    def remove_mpm_test_threshold(self, mpm_test_threshold: MPMTestThreshold) -> Self:
        return AggregatedPnode.mpm_test_threshold.remove(self, mpm_test_threshold)

    def clear_mpm_test_threshold(self) -> Self:
        return AggregatedPnode.mpm_test_threshold.clear(self)

    def num_mpm_test_threshold(self) -> int:
        return AggregatedPnode.mpm_test_threshold.count(self)

    def add_mkt_combined_cycle_plant(self, mkt_combined_cycle_plant: MktCombinedCyclePlant) -> Self:
        return AggregatedPnode.mkt_combined_cycle_plant.add(self, mkt_combined_cycle_plant)

    def remove_mkt_combined_cycle_plant(
        self, mkt_combined_cycle_plant: MktCombinedCyclePlant
    ) -> Self:
        return AggregatedPnode.mkt_combined_cycle_plant.remove(self, mkt_combined_cycle_plant)

    def clear_mkt_combined_cycle_plant(self) -> Self:
        return AggregatedPnode.mkt_combined_cycle_plant.clear(self)

    def num_mkt_combined_cycle_plant(self) -> int:
        return AggregatedPnode.mkt_combined_cycle_plant.count(self)

    def get_mkt_combined_cycle_plant_by_mrid(self, mrid: str) -> MktCombinedCyclePlant | None:
        return AggregatedPnode.mkt_combined_cycle_plant.get_by_mrid(self, mrid)

    def add_gen_distribution_factor(self, gen_distribution_factor: GenDistributionFactor) -> Self:
        return AggregatedPnode.gen_distribution_factor.add(self, gen_distribution_factor)

    def remove_gen_distribution_factor(
        self, gen_distribution_factor: GenDistributionFactor
    ) -> Self:
        return AggregatedPnode.gen_distribution_factor.remove(self, gen_distribution_factor)

    def clear_gen_distribution_factor(self) -> Self:
        return AggregatedPnode.gen_distribution_factor.clear(self)

    def num_gen_distribution_factor(self) -> int:
        return AggregatedPnode.gen_distribution_factor.count(self)

    def add_mpm_test_result(self, mpm_test_result: MPMTestResults) -> Self:
        return AggregatedPnode.mpm_test_results.add(self, mpm_test_result)

    def remove_mpm_test_result(self, mpm_test_result: MPMTestResults) -> Self:
        return AggregatedPnode.mpm_test_results.remove(self, mpm_test_result)

    def clear_mpm_test_results(self) -> Self:
        return AggregatedPnode.mpm_test_results.clear(self)

    def num_mpm_test_result(self) -> int:
        return AggregatedPnode.mpm_test_results.count(self)

    def add_pnode_distribution_factor(
        self, pnode_distribution_factor: PnodeDistributionFactor
    ) -> Self:
        return AggregatedPnode.pnode_distribution_factor.add(self, pnode_distribution_factor)

    def remove_pnode_distribution_factor(
        self, pnode_distribution_factor: PnodeDistributionFactor
    ) -> Self:
        return AggregatedPnode.pnode_distribution_factor.remove(self, pnode_distribution_factor)

    def clear_pnode_distribution_factor(self) -> Self:
        return AggregatedPnode.pnode_distribution_factor.clear(self)

    def num_pnode_distribution_factor(self) -> int:
        return AggregatedPnode.pnode_distribution_factor.count(self)
