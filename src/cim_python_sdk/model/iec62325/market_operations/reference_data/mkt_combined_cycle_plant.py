"""CIM class MktCombinedCyclePlant (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.generation.production.combined_cycle_plant import (
    CombinedCyclePlant,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode import (
        AggregatedPnode,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_logical_configuration import (
        CombinedCycleLogicalConfiguration,
    )


class MktCombinedCyclePlant(CombinedCyclePlant):
    """Subclass of Production: CombinedCyclePlant from IEC 61970 package.

    A set of combustion turbines and steam turbines where the exhaust heat from the
    combustion turbines is recovered to make steam for the steam turbines, resulting in
    greater overall plant efficiency."""

    __slots__ = ("_aggregated_pnode", "_combined_cycle_logical_configuration")

    aggregated_pnode: One[AggregatedPnode] = One(
        EndMeta(
            name="aggregated_pnode",
            cim_role="AggregatedPnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.aggregated_pnode:AggregatedPnode",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_combined_cycle_plant",
            aggregation="none",
        )
    )
    combined_cycle_logical_configuration: Many[CombinedCycleLogicalConfiguration] = Many(
        EndMeta(
            name="combined_cycle_logical_configuration",
            cim_role="CombinedCycleLogicalConfiguration",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_logical_configuration:CombinedCycleLogicalConfiguration",
            many=True,
            lower=1,
            upper=None,
            inverse="mkt_combined_cycle_plant",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktCombinedCyclePlant",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{B0A0BCA1-2D6C-445f-9024-174B473927B8}",
        ends=(
            aggregated_pnode.meta,
            combined_cycle_logical_configuration.meta,
        ),
    )

    def __init__(
        self,
        *,
        aggregated_pnode: AggregatedPnode | None = None,
        combined_cycle_logical_configuration: Iterable[CombinedCycleLogicalConfiguration]
        | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if aggregated_pnode is not None:
            self.aggregated_pnode = aggregated_pnode
        if combined_cycle_logical_configuration is not None:
            MktCombinedCyclePlant.combined_cycle_logical_configuration.extend(
                self, combined_cycle_logical_configuration
            )

    def add_combined_cycle_logical_configuration(
        self, combined_cycle_logical_configuration: CombinedCycleLogicalConfiguration
    ) -> Self:
        return MktCombinedCyclePlant.combined_cycle_logical_configuration.add(
            self, combined_cycle_logical_configuration
        )

    def remove_combined_cycle_logical_configuration(
        self, combined_cycle_logical_configuration: CombinedCycleLogicalConfiguration
    ) -> Self:
        return MktCombinedCyclePlant.combined_cycle_logical_configuration.remove(
            self, combined_cycle_logical_configuration
        )

    def clear_combined_cycle_logical_configuration(self) -> Self:
        return MktCombinedCyclePlant.combined_cycle_logical_configuration.clear(self)

    def num_combined_cycle_logical_configuration(self) -> int:
        return MktCombinedCyclePlant.combined_cycle_logical_configuration.count(self)

    def get_combined_cycle_logical_configuration_by_mrid(
        self, mrid: str
    ) -> CombinedCycleLogicalConfiguration | None:
        return MktCombinedCyclePlant.combined_cycle_logical_configuration.get_by_mrid(self, mrid)
