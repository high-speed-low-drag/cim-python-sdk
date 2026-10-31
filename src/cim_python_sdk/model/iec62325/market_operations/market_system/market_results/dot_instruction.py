"""CIM class DotInstruction (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing_dot import (
        InstructionClearingDOT,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class DotInstruction(CimObject):
    """Provides the necessary information (on a resource basis) to capture the Dispatch
    Operating Target (DOT) results on a Dispatch interval. This information is only relevant
    to the RT interval market."""

    __slots__ = (
        "_instruction_clearing_dot",
        "_registered_resource",
        "actual_ramp_rate",
        "compliant_indicator",
        "dot",
        "economic_max_override",
        "expected_energy",
        "generator_performance_degree",
        "hour_ahead_sched_energy",
        "hourly_schedule",
        "instruction_time",
        "maximum_emergency_ind",
        "meter_load_following",
        "non_ramp_restricted_mw",
        "non_spin_reserve",
        "previous_dot_time_stamp",
        "ramp_rate_limit",
        "regulation_status",
        "spin_reserve",
        "standard_ramp_energy",
        "supplemental_energy",
        "unit_status",
    )

    actual_ramp_rate: float | None
    compliant_indicator: YesNo | None
    dot: float | None
    economic_max_override: float | None
    expected_energy: float | None
    generator_performance_degree: float | None
    hour_ahead_sched_energy: float | None
    hourly_schedule: float | None
    instruction_time: _dt.datetime | None
    maximum_emergency_ind: bool | None
    meter_load_following: float | None
    non_ramp_restricted_mw: float | None
    non_spin_reserve: float | None
    previous_dot_time_stamp: _dt.datetime | None
    ramp_rate_limit: float | None
    regulation_status: YesNo | None
    spin_reserve: float | None
    standard_ramp_energy: float | None
    supplemental_energy: float | None
    unit_status: int | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="dot_instruction",
            aggregation="none",
        )
    )
    instruction_clearing_dot: Many[InstructionClearingDOT] = Many(
        EndMeta(
            name="instruction_clearing_dot",
            cim_role="InstructionClearingDOT",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing_dot:InstructionClearingDOT",
            many=True,
            lower=1,
            upper=None,
            inverse="dot_instruction",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DotInstruction",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{09D2117F-38CF-4cb5-BCFC-82787ED71AAA}",
        attributes=(
            AttrMeta("actual_ramp_rate", "actualRampRate", "float", 0, 1, "primitive"),
            AttrMeta("compliant_indicator", "compliantIndicator", "YesNo", 0, 1, "enumeration"),
            AttrMeta("dot", "DOT", "float", 0, 1, "primitive"),
            AttrMeta("economic_max_override", "economicMaxOverride", "float", 0, 1, "primitive"),
            AttrMeta("expected_energy", "expectedEnergy", "float", 0, 1, "primitive"),
            AttrMeta(
                "generator_performance_degree",
                "generatorPerformanceDegree",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta("hour_ahead_sched_energy", "hourAheadSchedEnergy", "float", 0, 1, "primitive"),
            AttrMeta("hourly_schedule", "hourlySchedule", "float", 0, 1, "primitive"),
            AttrMeta("instruction_time", "instructionTime", "datetime", 0, 1, "primitive"),
            AttrMeta("maximum_emergency_ind", "maximumEmergencyInd", "bool", 0, 1, "primitive"),
            AttrMeta("meter_load_following", "meterLoadFollowing", "float", 0, 1, "primitive"),
            AttrMeta("non_ramp_restricted_mw", "nonRampRestrictedMW", "float", 0, 1, "primitive"),
            AttrMeta("non_spin_reserve", "nonSpinReserve", "float", 0, 1, "primitive"),
            AttrMeta(
                "previous_dot_time_stamp", "previousDOTTimeStamp", "datetime", 0, 1, "primitive"
            ),
            AttrMeta("ramp_rate_limit", "rampRateLimit", "float", 0, 1, "primitive"),
            AttrMeta("regulation_status", "regulationStatus", "YesNo", 0, 1, "enumeration"),
            AttrMeta("spin_reserve", "spinReserve", "float", 0, 1, "primitive"),
            AttrMeta("standard_ramp_energy", "standardRampEnergy", "float", 0, 1, "primitive"),
            AttrMeta("supplemental_energy", "supplementalEnergy", "float", 0, 1, "primitive"),
            AttrMeta("unit_status", "unitStatus", "int", 0, 1, "primitive"),
        ),
        ends=(
            registered_resource.meta,
            instruction_clearing_dot.meta,
        ),
    )

    def __init__(
        self,
        *,
        actual_ramp_rate: float | None = None,
        compliant_indicator: YesNo | None = None,
        dot: float | None = None,
        economic_max_override: float | None = None,
        expected_energy: float | None = None,
        generator_performance_degree: float | None = None,
        hour_ahead_sched_energy: float | None = None,
        hourly_schedule: float | None = None,
        instruction_time: _dt.datetime | None = None,
        maximum_emergency_ind: bool | None = None,
        meter_load_following: float | None = None,
        non_ramp_restricted_mw: float | None = None,
        non_spin_reserve: float | None = None,
        previous_dot_time_stamp: _dt.datetime | None = None,
        ramp_rate_limit: float | None = None,
        regulation_status: YesNo | None = None,
        spin_reserve: float | None = None,
        standard_ramp_energy: float | None = None,
        supplemental_energy: float | None = None,
        unit_status: int | None = None,
        registered_resource: RegisteredResource | None = None,
        instruction_clearing_dot: Iterable[InstructionClearingDOT] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.actual_ramp_rate = actual_ramp_rate
        self.compliant_indicator = compliant_indicator
        self.dot = dot
        self.economic_max_override = economic_max_override
        self.expected_energy = expected_energy
        self.generator_performance_degree = generator_performance_degree
        self.hour_ahead_sched_energy = hour_ahead_sched_energy
        self.hourly_schedule = hourly_schedule
        self.instruction_time = instruction_time
        self.maximum_emergency_ind = maximum_emergency_ind
        self.meter_load_following = meter_load_following
        self.non_ramp_restricted_mw = non_ramp_restricted_mw
        self.non_spin_reserve = non_spin_reserve
        self.previous_dot_time_stamp = previous_dot_time_stamp
        self.ramp_rate_limit = ramp_rate_limit
        self.regulation_status = regulation_status
        self.spin_reserve = spin_reserve
        self.standard_ramp_energy = standard_ramp_energy
        self.supplemental_energy = supplemental_energy
        self.unit_status = unit_status
        if registered_resource is not None:
            self.registered_resource = registered_resource
        if instruction_clearing_dot is not None:
            DotInstruction.instruction_clearing_dot.extend(self, instruction_clearing_dot)

    def add_instruction_clearing_dot(
        self, instruction_clearing_dot: InstructionClearingDOT
    ) -> Self:
        return DotInstruction.instruction_clearing_dot.add(self, instruction_clearing_dot)

    def remove_instruction_clearing_dot(
        self, instruction_clearing_dot: InstructionClearingDOT
    ) -> Self:
        return DotInstruction.instruction_clearing_dot.remove(self, instruction_clearing_dot)

    def clear_instruction_clearing_dot(self) -> Self:
        return DotInstruction.instruction_clearing_dot.clear(self)

    def num_instruction_clearing_dot(self) -> int:
        return DotInstruction.instruction_clearing_dot.count(self)

    def get_instruction_clearing_dot_by_mrid(self, mrid: str) -> InstructionClearingDOT | None:
        return DotInstruction.instruction_clearing_dot.get_by_mrid(self, mrid)
