"""CIM class CombinedCycleLogicalConfiguration (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration import (
        CombinedCycleConfiguration,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_combined_cycle_plant import (
        MktCombinedCyclePlant,
    )


class CombinedCycleLogicalConfiguration(IdentifiedObject):
    """Logical Configuration of a Combined Cycle plant.

    Operating Combined Cycle Plant (CCP) configurations are represented as Logical CCP
    Resources. Logical representation shall be used for Market applications to optimize and
    control Market Operations. Logical representation is also necessary for controlling the
    number of CCP configurations and to temper performance issues that may otherwise occur.

    For example,(2CT configuration),(1CT + 1ST configuration) are examples of logical
    configuration, without specifying the specific CT and ST participating in the
    configuration."""

    __slots__ = ("_combined_cycle_configuration", "_mkt_combined_cycle_plant")

    combined_cycle_configuration: Many[CombinedCycleConfiguration] = Many(
        EndMeta(
            name="combined_cycle_configuration",
            cim_role="CombinedCycleConfiguration",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration:CombinedCycleConfiguration",
            many=True,
            lower=1,
            upper=None,
            inverse="combined_cycle_logical_configuration",
            aggregation="none",
        )
    )
    mkt_combined_cycle_plant: One[MktCombinedCyclePlant] = One(
        EndMeta(
            name="mkt_combined_cycle_plant",
            cim_role="MktCombinedCyclePlant",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_combined_cycle_plant:MktCombinedCyclePlant",
            many=False,
            lower=0,
            upper=1,
            inverse="combined_cycle_logical_configuration",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CombinedCycleLogicalConfiguration",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{C0FA5D45-3A6A-4642-B2F1-6DFC1FC762E7}",
        ends=(
            combined_cycle_configuration.meta,
            mkt_combined_cycle_plant.meta,
        ),
    )

    def __init__(
        self,
        *,
        combined_cycle_configuration: Iterable[CombinedCycleConfiguration] | None = None,
        mkt_combined_cycle_plant: MktCombinedCyclePlant | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if combined_cycle_configuration is not None:
            CombinedCycleLogicalConfiguration.combined_cycle_configuration.extend(
                self, combined_cycle_configuration
            )
        if mkt_combined_cycle_plant is not None:
            self.mkt_combined_cycle_plant = mkt_combined_cycle_plant

    def add_combined_cycle_configuration(
        self, combined_cycle_configuration: CombinedCycleConfiguration
    ) -> Self:
        return CombinedCycleLogicalConfiguration.combined_cycle_configuration.add(
            self, combined_cycle_configuration
        )

    def remove_combined_cycle_configuration(
        self, combined_cycle_configuration: CombinedCycleConfiguration
    ) -> Self:
        return CombinedCycleLogicalConfiguration.combined_cycle_configuration.remove(
            self, combined_cycle_configuration
        )

    def clear_combined_cycle_configuration(self) -> Self:
        return CombinedCycleLogicalConfiguration.combined_cycle_configuration.clear(self)

    def num_combined_cycle_configuration(self) -> int:
        return CombinedCycleLogicalConfiguration.combined_cycle_configuration.count(self)

    def get_combined_cycle_configuration_by_mrid(
        self, mrid: str
    ) -> CombinedCycleConfiguration | None:
        return CombinedCycleLogicalConfiguration.combined_cycle_configuration.get_by_mrid(
            self, mrid
        )
