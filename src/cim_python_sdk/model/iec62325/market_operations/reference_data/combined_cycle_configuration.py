"""CIM class CombinedCycleConfiguration (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
    RegisteredGenerator,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration_member import (
        CombinedCycleConfigurationMember,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_logical_configuration import (
        CombinedCycleLogicalConfiguration,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_transition_state import (
        CombinedCycleTransitionState,
    )


class CombinedCycleConfiguration(RegisteredGenerator):
    """Configuration options for combined cycle units.

    For example, a Combined Cycle with (CT1, CT2, ST1) will have (CT1, ST1) and (CT2, ST1)
    configurations as part of(1CT + 1STlogicalconfiguration)."""

    __slots__ = (
        "_combined_cycle_configuration_member",
        "_combined_cycle_logical_configuration",
        "_from_transition_state",
        "_to_transition_state",
        "primary_configuration",
        "shutdown_flag",
        "startup_flag",
    )

    primary_configuration: bool | None
    shutdown_flag: bool | None
    startup_flag: bool | None

    from_transition_state: Many[CombinedCycleTransitionState] = Many(
        EndMeta(
            name="from_transition_state",
            cim_role="FromTransitionState",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_transition_state:CombinedCycleTransitionState",
            many=True,
            lower=0,
            upper=None,
            inverse="from_configuration",
            aggregation="none",
        )
    )
    to_transition_state: Many[CombinedCycleTransitionState] = Many(
        EndMeta(
            name="to_transition_state",
            cim_role="ToTransitionState",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_transition_state:CombinedCycleTransitionState",
            many=True,
            lower=0,
            upper=None,
            inverse="to_configuration",
            aggregation="none",
        )
    )
    combined_cycle_logical_configuration: One[CombinedCycleLogicalConfiguration] = One(
        EndMeta(
            name="combined_cycle_logical_configuration",
            cim_role="CombinedCycleLogicalConfiguration",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_logical_configuration:CombinedCycleLogicalConfiguration",
            many=False,
            lower=0,
            upper=1,
            inverse="combined_cycle_configuration",
            aggregation="none",
        )
    )
    combined_cycle_configuration_member: Many[CombinedCycleConfigurationMember] = Many(
        EndMeta(
            name="combined_cycle_configuration_member",
            cim_role="CombinedCycleConfigurationMember",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration_member:CombinedCycleConfigurationMember",
            many=True,
            lower=0,
            upper=None,
            inverse="combined_cycle_configuration",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CombinedCycleConfiguration",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{7F2322C7-014A-4fc7-9F69-3474C0B89F7B}",
        attributes=(
            AttrMeta("primary_configuration", "primaryConfiguration", "bool", 0, 1, "primitive"),
            AttrMeta("shutdown_flag", "ShutdownFlag", "bool", 0, 1, "primitive"),
            AttrMeta("startup_flag", "StartupFlag", "bool", 0, 1, "primitive"),
        ),
        ends=(
            from_transition_state.meta,
            to_transition_state.meta,
            combined_cycle_logical_configuration.meta,
            combined_cycle_configuration_member.meta,
        ),
    )

    def __init__(
        self,
        *,
        primary_configuration: bool | None = None,
        shutdown_flag: bool | None = None,
        startup_flag: bool | None = None,
        from_transition_state: Iterable[CombinedCycleTransitionState] | None = None,
        to_transition_state: Iterable[CombinedCycleTransitionState] | None = None,
        combined_cycle_logical_configuration: CombinedCycleLogicalConfiguration | None = None,
        combined_cycle_configuration_member: Iterable[CombinedCycleConfigurationMember]
        | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.primary_configuration = primary_configuration
        self.shutdown_flag = shutdown_flag
        self.startup_flag = startup_flag
        if from_transition_state is not None:
            CombinedCycleConfiguration.from_transition_state.extend(self, from_transition_state)
        if to_transition_state is not None:
            CombinedCycleConfiguration.to_transition_state.extend(self, to_transition_state)
        if combined_cycle_logical_configuration is not None:
            self.combined_cycle_logical_configuration = combined_cycle_logical_configuration
        if combined_cycle_configuration_member is not None:
            CombinedCycleConfiguration.combined_cycle_configuration_member.extend(
                self, combined_cycle_configuration_member
            )

    def add_from_transition_state(
        self, from_transition_state: CombinedCycleTransitionState
    ) -> Self:
        return CombinedCycleConfiguration.from_transition_state.add(self, from_transition_state)

    def remove_from_transition_state(
        self, from_transition_state: CombinedCycleTransitionState
    ) -> Self:
        return CombinedCycleConfiguration.from_transition_state.remove(self, from_transition_state)

    def clear_from_transition_state(self) -> Self:
        return CombinedCycleConfiguration.from_transition_state.clear(self)

    def num_from_transition_state(self) -> int:
        return CombinedCycleConfiguration.from_transition_state.count(self)

    def add_to_transition_state(self, to_transition_state: CombinedCycleTransitionState) -> Self:
        return CombinedCycleConfiguration.to_transition_state.add(self, to_transition_state)

    def remove_to_transition_state(self, to_transition_state: CombinedCycleTransitionState) -> Self:
        return CombinedCycleConfiguration.to_transition_state.remove(self, to_transition_state)

    def clear_to_transition_state(self) -> Self:
        return CombinedCycleConfiguration.to_transition_state.clear(self)

    def num_to_transition_state(self) -> int:
        return CombinedCycleConfiguration.to_transition_state.count(self)

    def add_combined_cycle_configuration_member(
        self, combined_cycle_configuration_member: CombinedCycleConfigurationMember
    ) -> Self:
        return CombinedCycleConfiguration.combined_cycle_configuration_member.add(
            self, combined_cycle_configuration_member
        )

    def remove_combined_cycle_configuration_member(
        self, combined_cycle_configuration_member: CombinedCycleConfigurationMember
    ) -> Self:
        return CombinedCycleConfiguration.combined_cycle_configuration_member.remove(
            self, combined_cycle_configuration_member
        )

    def clear_combined_cycle_configuration_member(self) -> Self:
        return CombinedCycleConfiguration.combined_cycle_configuration_member.clear(self)

    def num_combined_cycle_configuration_member(self) -> int:
        return CombinedCycleConfiguration.combined_cycle_configuration_member.count(self)

    def get_combined_cycle_configuration_member_by_mrid(
        self, mrid: str
    ) -> CombinedCycleConfigurationMember | None:
        return CombinedCycleConfiguration.combined_cycle_configuration_member.get_by_mrid(
            self, mrid
        )
