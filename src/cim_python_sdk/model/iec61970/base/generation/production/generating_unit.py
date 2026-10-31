"""CIM class GeneratingUnit (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.equipment import Equipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.control_area.control_area_generating_unit import (
        ControlAreaGeneratingUnit,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.gen_unit_op_cost_curve import (
        GenUnitOpCostCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.gen_unit_op_schedule import (
        GenUnitOpSchedule,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.generator_control_mode import (
        GeneratorControlMode,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.generator_control_source import (
        GeneratorControlSource,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.gross_to_net_active_power_curve import (
        GrossToNetActivePowerCurve,
    )
    from cim_python_sdk.model.iec61970.base.wires.rotating_machine import RotatingMachine


class GeneratingUnit(Equipment):
    """A single or set of synchronous machines for converting mechanical power into
    alternating-current power. For example, individual machines within a set may be defined
    for scheduling purposes while a single control signal is derived for the set. In this
    case there would be a GeneratingUnit for each member of the set and an additional
    GeneratingUnit corresponding to the set."""

    __slots__ = (
        "_control_area_generating_unit",
        "_gen_unit_op_cost_curves",
        "_gen_unit_op_schedule",
        "_gross_to_net_active_power_curves",
        "_rotating_machine",
        "alloc_spin_res_p",
        "auto_cntrl_margin_p",
        "base_p",
        "control_deadband",
        "control_pulse_high",
        "control_pulse_low",
        "control_response_rate",
        "efficiency",
        "gen_control_mode",
        "gen_control_source",
        "governor_mpl",
        "governor_scd",
        "high_control_limit",
        "initial_p",
        "long_pf",
        "low_control_limit",
        "lower_ramp_rate",
        "max_economic_p",
        "max_operating_p",
        "maximum_allowable_spinning_reserve",
        "min_economic_p",
        "min_operating_p",
        "minimum_off_time",
        "model_detail",
        "nominal_p",
        "normal_pf",
        "penalty_factor",
        "raise_ramp_rate",
        "rated_gross_max_p",
        "rated_gross_min_p",
        "rated_net_max_p",
        "short_pf",
        "startup_cost",
        "startup_time",
        "tie_line_pf",
        "total_efficiency",
        "variable_cost",
    )

    alloc_spin_res_p: float | None  # ActivePower
    auto_cntrl_margin_p: float | None  # ActivePower
    base_p: float | None  # ActivePower
    control_deadband: float | None  # ActivePower
    control_pulse_high: float | None  # Seconds
    control_pulse_low: float | None  # Seconds
    control_response_rate: float | None  # ActivePowerChangeRate
    efficiency: float | None  # PerCent
    gen_control_mode: GeneratorControlMode | None
    gen_control_source: GeneratorControlSource | None
    governor_mpl: float | None  # PU
    governor_scd: float | None  # PerCent
    high_control_limit: float | None  # ActivePower
    initial_p: float | None  # ActivePower
    long_pf: float | None
    low_control_limit: float | None  # ActivePower
    lower_ramp_rate: float | None  # ActivePowerChangeRate
    max_economic_p: float | None  # ActivePower
    maximum_allowable_spinning_reserve: float | None  # ActivePower
    max_operating_p: float | None  # ActivePower
    min_economic_p: float | None  # ActivePower
    minimum_off_time: float | None  # Seconds
    min_operating_p: float | None  # ActivePower
    model_detail: int | None  # Classification
    nominal_p: float | None  # ActivePower
    normal_pf: float | None
    penalty_factor: float | None
    raise_ramp_rate: float | None  # ActivePowerChangeRate
    rated_gross_max_p: float | None  # ActivePower
    rated_gross_min_p: float | None  # ActivePower
    rated_net_max_p: float | None  # ActivePower
    short_pf: float | None
    startup_cost: _decimal.Decimal | None  # Money
    startup_time: float | None  # Seconds
    tie_line_pf: float | None
    total_efficiency: float | None  # PerCent
    variable_cost: _decimal.Decimal | None  # Money

    rotating_machine: Many[RotatingMachine] = Many(
        EndMeta(
            name="rotating_machine",
            cim_role="RotatingMachine",
            target="cim_python_sdk.model.iec61970.base.wires.rotating_machine:RotatingMachine",
            many=True,
            lower=0,
            upper=None,
            inverse="generating_unit",
            aggregation="none",
        )
    )
    gross_to_net_active_power_curves: Many[GrossToNetActivePowerCurve] = Many(
        EndMeta(
            name="gross_to_net_active_power_curves",
            cim_role="GrossToNetActivePowerCurves",
            target="cim_python_sdk.model.iec61970.base.generation.production.gross_to_net_active_power_curve:GrossToNetActivePowerCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="generating_unit",
            aggregation="shared",
        )
    )
    control_area_generating_unit: Many[ControlAreaGeneratingUnit] = Many(
        EndMeta(
            name="control_area_generating_unit",
            cim_role="ControlAreaGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.control_area.control_area_generating_unit:ControlAreaGeneratingUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="generating_unit",
            aggregation="none",
        )
    )
    gen_unit_op_cost_curves: Many[GenUnitOpCostCurve] = Many(
        EndMeta(
            name="gen_unit_op_cost_curves",
            cim_role="GenUnitOpCostCurves",
            target="cim_python_sdk.model.iec61970.base.generation.production.gen_unit_op_cost_curve:GenUnitOpCostCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="generating_unit",
            aggregation="shared",
        )
    )
    gen_unit_op_schedule: One[GenUnitOpSchedule] = One(
        EndMeta(
            name="gen_unit_op_schedule",
            cim_role="GenUnitOpSchedule",
            target="cim_python_sdk.model.iec61970.base.generation.production.gen_unit_op_schedule:GenUnitOpSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="generating_unit",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GeneratingUnit",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{A4C4D1F8-0359-44b1-8F2A-521D3F9F3C28}",
        attributes=(
            AttrMeta("alloc_spin_res_p", "allocSpinResP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("auto_cntrl_margin_p", "autoCntrlMarginP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("base_p", "baseP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("control_deadband", "controlDeadband", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("control_pulse_high", "controlPulseHigh", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("control_pulse_low", "controlPulseLow", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta(
                "control_response_rate",
                "controlResponseRate",
                "ActivePowerChangeRate",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("efficiency", "efficiency", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta(
                "gen_control_mode", "genControlMode", "GeneratorControlMode", 0, 1, "enumeration"
            ),
            AttrMeta(
                "gen_control_source",
                "genControlSource",
                "GeneratorControlSource",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("governor_mpl", "governorMPL", "PU", 0, 1, "cimdatatype"),
            AttrMeta("governor_scd", "governorSCD", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("high_control_limit", "highControlLimit", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("initial_p", "initialP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("long_pf", "longPF", "float", 0, 1, "primitive"),
            AttrMeta("low_control_limit", "lowControlLimit", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "lower_ramp_rate", "lowerRampRate", "ActivePowerChangeRate", 0, 1, "cimdatatype"
            ),
            AttrMeta("max_economic_p", "maxEconomicP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "maximum_allowable_spinning_reserve",
                "maximumAllowableSpinningReserve",
                "ActivePower",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("max_operating_p", "maxOperatingP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_economic_p", "minEconomicP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("minimum_off_time", "minimumOffTime", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("min_operating_p", "minOperatingP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("model_detail", "modelDetail", "Classification", 0, 1, "cimdatatype"),
            AttrMeta("nominal_p", "nominalP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("normal_pf", "normalPF", "float", 0, 1, "primitive"),
            AttrMeta("penalty_factor", "penaltyFactor", "float", 0, 1, "primitive"),
            AttrMeta(
                "raise_ramp_rate", "raiseRampRate", "ActivePowerChangeRate", 0, 1, "cimdatatype"
            ),
            AttrMeta("rated_gross_max_p", "ratedGrossMaxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("rated_gross_min_p", "ratedGrossMinP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("rated_net_max_p", "ratedNetMaxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("short_pf", "shortPF", "float", 0, 1, "primitive"),
            AttrMeta("startup_cost", "startupCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("startup_time", "startupTime", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tie_line_pf", "tieLinePF", "float", 0, 1, "primitive"),
            AttrMeta("total_efficiency", "totalEfficiency", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("variable_cost", "variableCost", "Money", 0, 1, "cimdatatype"),
        ),
        ends=(
            rotating_machine.meta,
            gross_to_net_active_power_curves.meta,
            control_area_generating_unit.meta,
            gen_unit_op_cost_curves.meta,
            gen_unit_op_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        alloc_spin_res_p: float | None = None,
        auto_cntrl_margin_p: float | None = None,
        base_p: float | None = None,
        control_deadband: float | None = None,
        control_pulse_high: float | None = None,
        control_pulse_low: float | None = None,
        control_response_rate: float | None = None,
        efficiency: float | None = None,
        gen_control_mode: GeneratorControlMode | None = None,
        gen_control_source: GeneratorControlSource | None = None,
        governor_mpl: float | None = None,
        governor_scd: float | None = None,
        high_control_limit: float | None = None,
        initial_p: float | None = None,
        long_pf: float | None = None,
        low_control_limit: float | None = None,
        lower_ramp_rate: float | None = None,
        max_economic_p: float | None = None,
        maximum_allowable_spinning_reserve: float | None = None,
        max_operating_p: float | None = None,
        min_economic_p: float | None = None,
        minimum_off_time: float | None = None,
        min_operating_p: float | None = None,
        model_detail: int | None = None,
        nominal_p: float | None = None,
        normal_pf: float | None = None,
        penalty_factor: float | None = None,
        raise_ramp_rate: float | None = None,
        rated_gross_max_p: float | None = None,
        rated_gross_min_p: float | None = None,
        rated_net_max_p: float | None = None,
        short_pf: float | None = None,
        startup_cost: _decimal.Decimal | None = None,
        startup_time: float | None = None,
        tie_line_pf: float | None = None,
        total_efficiency: float | None = None,
        variable_cost: _decimal.Decimal | None = None,
        rotating_machine: Iterable[RotatingMachine] | None = None,
        gross_to_net_active_power_curves: Iterable[GrossToNetActivePowerCurve] | None = None,
        control_area_generating_unit: Iterable[ControlAreaGeneratingUnit] | None = None,
        gen_unit_op_cost_curves: Iterable[GenUnitOpCostCurve] | None = None,
        gen_unit_op_schedule: GenUnitOpSchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.alloc_spin_res_p = alloc_spin_res_p
        self.auto_cntrl_margin_p = auto_cntrl_margin_p
        self.base_p = base_p
        self.control_deadband = control_deadband
        self.control_pulse_high = control_pulse_high
        self.control_pulse_low = control_pulse_low
        self.control_response_rate = control_response_rate
        self.efficiency = efficiency
        self.gen_control_mode = gen_control_mode
        self.gen_control_source = gen_control_source
        self.governor_mpl = governor_mpl
        self.governor_scd = governor_scd
        self.high_control_limit = high_control_limit
        self.initial_p = initial_p
        self.long_pf = long_pf
        self.low_control_limit = low_control_limit
        self.lower_ramp_rate = lower_ramp_rate
        self.max_economic_p = max_economic_p
        self.maximum_allowable_spinning_reserve = maximum_allowable_spinning_reserve
        self.max_operating_p = max_operating_p
        self.min_economic_p = min_economic_p
        self.minimum_off_time = minimum_off_time
        self.min_operating_p = min_operating_p
        self.model_detail = model_detail
        self.nominal_p = nominal_p
        self.normal_pf = normal_pf
        self.penalty_factor = penalty_factor
        self.raise_ramp_rate = raise_ramp_rate
        self.rated_gross_max_p = rated_gross_max_p
        self.rated_gross_min_p = rated_gross_min_p
        self.rated_net_max_p = rated_net_max_p
        self.short_pf = short_pf
        self.startup_cost = startup_cost
        self.startup_time = startup_time
        self.tie_line_pf = tie_line_pf
        self.total_efficiency = total_efficiency
        self.variable_cost = variable_cost
        if rotating_machine is not None:
            GeneratingUnit.rotating_machine.extend(self, rotating_machine)
        if gross_to_net_active_power_curves is not None:
            GeneratingUnit.gross_to_net_active_power_curves.extend(
                self, gross_to_net_active_power_curves
            )
        if control_area_generating_unit is not None:
            GeneratingUnit.control_area_generating_unit.extend(self, control_area_generating_unit)
        if gen_unit_op_cost_curves is not None:
            GeneratingUnit.gen_unit_op_cost_curves.extend(self, gen_unit_op_cost_curves)
        if gen_unit_op_schedule is not None:
            self.gen_unit_op_schedule = gen_unit_op_schedule

    def add_rotating_machine(self, rotating_machine: RotatingMachine) -> Self:
        return GeneratingUnit.rotating_machine.add(self, rotating_machine)

    def remove_rotating_machine(self, rotating_machine: RotatingMachine) -> Self:
        return GeneratingUnit.rotating_machine.remove(self, rotating_machine)

    def clear_rotating_machine(self) -> Self:
        return GeneratingUnit.rotating_machine.clear(self)

    def num_rotating_machine(self) -> int:
        return GeneratingUnit.rotating_machine.count(self)

    def get_rotating_machine_by_mrid(self, mrid: str) -> RotatingMachine | None:
        return GeneratingUnit.rotating_machine.get_by_mrid(self, mrid)

    def add_gross_to_net_active_power_curve(
        self, gross_to_net_active_power_curve: GrossToNetActivePowerCurve
    ) -> Self:
        return GeneratingUnit.gross_to_net_active_power_curves.add(
            self, gross_to_net_active_power_curve
        )

    def remove_gross_to_net_active_power_curve(
        self, gross_to_net_active_power_curve: GrossToNetActivePowerCurve
    ) -> Self:
        return GeneratingUnit.gross_to_net_active_power_curves.remove(
            self, gross_to_net_active_power_curve
        )

    def clear_gross_to_net_active_power_curves(self) -> Self:
        return GeneratingUnit.gross_to_net_active_power_curves.clear(self)

    def num_gross_to_net_active_power_curve(self) -> int:
        return GeneratingUnit.gross_to_net_active_power_curves.count(self)

    def get_gross_to_net_active_power_curve_by_mrid(
        self, mrid: str
    ) -> GrossToNetActivePowerCurve | None:
        return GeneratingUnit.gross_to_net_active_power_curves.get_by_mrid(self, mrid)

    def add_control_area_generating_unit(
        self, control_area_generating_unit: ControlAreaGeneratingUnit
    ) -> Self:
        return GeneratingUnit.control_area_generating_unit.add(self, control_area_generating_unit)

    def remove_control_area_generating_unit(
        self, control_area_generating_unit: ControlAreaGeneratingUnit
    ) -> Self:
        return GeneratingUnit.control_area_generating_unit.remove(
            self, control_area_generating_unit
        )

    def clear_control_area_generating_unit(self) -> Self:
        return GeneratingUnit.control_area_generating_unit.clear(self)

    def num_control_area_generating_unit(self) -> int:
        return GeneratingUnit.control_area_generating_unit.count(self)

    def get_control_area_generating_unit_by_mrid(
        self, mrid: str
    ) -> ControlAreaGeneratingUnit | None:
        return GeneratingUnit.control_area_generating_unit.get_by_mrid(self, mrid)

    def add_gen_unit_op_cost_curve(self, gen_unit_op_cost_curve: GenUnitOpCostCurve) -> Self:
        return GeneratingUnit.gen_unit_op_cost_curves.add(self, gen_unit_op_cost_curve)

    def remove_gen_unit_op_cost_curve(self, gen_unit_op_cost_curve: GenUnitOpCostCurve) -> Self:
        return GeneratingUnit.gen_unit_op_cost_curves.remove(self, gen_unit_op_cost_curve)

    def clear_gen_unit_op_cost_curves(self) -> Self:
        return GeneratingUnit.gen_unit_op_cost_curves.clear(self)

    def num_gen_unit_op_cost_curve(self) -> int:
        return GeneratingUnit.gen_unit_op_cost_curves.count(self)

    def get_gen_unit_op_cost_curve_by_mrid(self, mrid: str) -> GenUnitOpCostCurve | None:
        return GeneratingUnit.gen_unit_op_cost_curves.get_by_mrid(self, mrid)
