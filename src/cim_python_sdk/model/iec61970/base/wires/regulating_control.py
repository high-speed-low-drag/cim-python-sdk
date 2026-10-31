"""CIM class RegulatingControl (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode
    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.wires.regulating_cond_eq import RegulatingCondEq
    from cim_python_sdk.model.iec61970.base.wires.regulating_control_mode_kind import (
        RegulatingControlModeKind,
    )
    from cim_python_sdk.model.iec61970.base.wires.regulation_schedule import RegulationSchedule
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_regulation import (
        ProtectiveActionRegulation,
    )


class RegulatingControl(PowerSystemResource):
    """Specifies a set of equipment that works together to control a power system quantity such
    as voltage or flow.

    Remote bus voltage control is possible by specifying the controlled terminal located at
    some place remote from the controlling equipment.

    The specified terminal shall be associated with the connectivity node of the controlled
    point. The most specific subtype of RegulatingControl shall be used in case such
    equipment participate in the control, e.g. TapChangerControl for tap changers.

    For flow control, load sign convention is used, i.e. positive sign means flow out from a
    TopologicalNode (bus) into the conducting equipment.

    The attribute minAllowedTargetValue and maxAllowedTargetValue are required in the
    following cases:

    - For a power generating module operated in power factor control mode to specify maximum
    and minimum power factor values;

    - Whenever it is necessary to have an off center target voltage for the tap changer
    regulator. For instance, due to long cables to off shore wind farms and the need to have
    a simpler setup at the off shore transformer platform, the voltage is controlled from
    the land at the connection point for the off shore wind farm. Since there usually is a
    voltage rise along the cable, there is typical and overvoltage of up 3-4 kV compared to
    the on shore station. Thus in normal operation the tap changer on the on shore station
    is operated with a target set point, which is in the lower parts of the dead band.

    The attributes minAllowedTargetValue and maxAllowedTargetValue are not related to the
    attribute targetDeadband and thus they are not treated as an alternative of the
    targetDeadband. They are needed due to limitations in the local substation controller.
    The attribute targetDeadband is used to prevent the power flow from move the tap
    position in circles (hunting) that is to be used regardless of the attributes
    minAllowedTargetValue and maxAllowedTargetValue."""

    __slots__ = (
        "_protective_action_regulation",
        "_regulating_cond_eq",
        "_regulation_schedule",
        "_terminal",
        "discrete",
        "enabled",
        "max_allowed_target_value",
        "min_allowed_target_value",
        "mode",
        "monitored_phase",
        "target_deadband",
        "target_value",
        "target_value_unit_multiplier",
    )

    discrete: bool | None
    enabled: bool | None
    mode: RegulatingControlModeKind | None
    monitored_phase: PhaseCode | None
    target_deadband: float | None
    target_value: float | None
    target_value_unit_multiplier: UnitMultiplier | None
    max_allowed_target_value: float | None
    min_allowed_target_value: float | None

    protective_action_regulation: Many[ProtectiveActionRegulation] = Many(
        EndMeta(
            name="protective_action_regulation",
            cim_role="ProtectiveActionRegulation",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_regulation:ProtectiveActionRegulation",
            many=True,
            lower=0,
            upper=None,
            inverse="regulating_control",
            aggregation="none",
        )
    )
    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=0,
            upper=1,
            inverse="regulating_control",
            aggregation="none",
        )
    )
    regulation_schedule: Many[RegulationSchedule] = Many(
        EndMeta(
            name="regulation_schedule",
            cim_role="RegulationSchedule",
            target="cim_python_sdk.model.iec61970.base.wires.regulation_schedule:RegulationSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="regulating_control",
            aggregation="none",
        )
    )
    regulating_cond_eq: Many[RegulatingCondEq] = Many(
        EndMeta(
            name="regulating_cond_eq",
            cim_role="RegulatingCondEq",
            target="cim_python_sdk.model.iec61970.base.wires.regulating_cond_eq:RegulatingCondEq",
            many=True,
            lower=0,
            upper=None,
            inverse="regulating_control",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegulatingControl",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{8C28B28D-4735-4033-9F33-7D86F6819922}",
        attributes=(
            AttrMeta("discrete", "discrete", "bool", 0, 1, "primitive"),
            AttrMeta("enabled", "enabled", "bool", 0, 1, "primitive"),
            AttrMeta("mode", "mode", "RegulatingControlModeKind", 0, 1, "enumeration"),
            AttrMeta("monitored_phase", "monitoredPhase", "PhaseCode", 0, 1, "enumeration"),
            AttrMeta("target_deadband", "targetDeadband", "float", 0, 1, "primitive"),
            AttrMeta("target_value", "targetValue", "float", 0, 1, "primitive"),
            AttrMeta(
                "target_value_unit_multiplier",
                "targetValueUnitMultiplier",
                "UnitMultiplier",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "max_allowed_target_value", "maxAllowedTargetValue", "float", 0, 1, "primitive"
            ),
            AttrMeta(
                "min_allowed_target_value", "minAllowedTargetValue", "float", 0, 1, "primitive"
            ),
        ),
        ends=(
            protective_action_regulation.meta,
            terminal.meta,
            regulation_schedule.meta,
            regulating_cond_eq.meta,
        ),
    )

    def __init__(
        self,
        *,
        discrete: bool | None = None,
        enabled: bool | None = None,
        mode: RegulatingControlModeKind | None = None,
        monitored_phase: PhaseCode | None = None,
        target_deadband: float | None = None,
        target_value: float | None = None,
        target_value_unit_multiplier: UnitMultiplier | None = None,
        max_allowed_target_value: float | None = None,
        min_allowed_target_value: float | None = None,
        protective_action_regulation: Iterable[ProtectiveActionRegulation] | None = None,
        terminal: Terminal | None = None,
        regulation_schedule: Iterable[RegulationSchedule] | None = None,
        regulating_cond_eq: Iterable[RegulatingCondEq] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.discrete = discrete
        self.enabled = enabled
        self.mode = mode
        self.monitored_phase = monitored_phase
        self.target_deadband = target_deadband
        self.target_value = target_value
        self.target_value_unit_multiplier = target_value_unit_multiplier
        self.max_allowed_target_value = max_allowed_target_value
        self.min_allowed_target_value = min_allowed_target_value
        if protective_action_regulation is not None:
            RegulatingControl.protective_action_regulation.extend(
                self, protective_action_regulation
            )
        if terminal is not None:
            self.terminal = terminal
        if regulation_schedule is not None:
            RegulatingControl.regulation_schedule.extend(self, regulation_schedule)
        if regulating_cond_eq is not None:
            RegulatingControl.regulating_cond_eq.extend(self, regulating_cond_eq)

    def add_protective_action_regulation(
        self, protective_action_regulation: ProtectiveActionRegulation
    ) -> Self:
        return RegulatingControl.protective_action_regulation.add(
            self, protective_action_regulation
        )

    def remove_protective_action_regulation(
        self, protective_action_regulation: ProtectiveActionRegulation
    ) -> Self:
        return RegulatingControl.protective_action_regulation.remove(
            self, protective_action_regulation
        )

    def clear_protective_action_regulation(self) -> Self:
        return RegulatingControl.protective_action_regulation.clear(self)

    def num_protective_action_regulation(self) -> int:
        return RegulatingControl.protective_action_regulation.count(self)

    def get_protective_action_regulation_by_mrid(
        self, mrid: str
    ) -> ProtectiveActionRegulation | None:
        return RegulatingControl.protective_action_regulation.get_by_mrid(self, mrid)

    def add_regulation_schedule(self, regulation_schedule: RegulationSchedule) -> Self:
        return RegulatingControl.regulation_schedule.add(self, regulation_schedule)

    def remove_regulation_schedule(self, regulation_schedule: RegulationSchedule) -> Self:
        return RegulatingControl.regulation_schedule.remove(self, regulation_schedule)

    def clear_regulation_schedule(self) -> Self:
        return RegulatingControl.regulation_schedule.clear(self)

    def num_regulation_schedule(self) -> int:
        return RegulatingControl.regulation_schedule.count(self)

    def get_regulation_schedule_by_mrid(self, mrid: str) -> RegulationSchedule | None:
        return RegulatingControl.regulation_schedule.get_by_mrid(self, mrid)

    def add_regulating_cond_eq(self, regulating_cond_eq: RegulatingCondEq) -> Self:
        return RegulatingControl.regulating_cond_eq.add(self, regulating_cond_eq)

    def remove_regulating_cond_eq(self, regulating_cond_eq: RegulatingCondEq) -> Self:
        return RegulatingControl.regulating_cond_eq.remove(self, regulating_cond_eq)

    def clear_regulating_cond_eq(self) -> Self:
        return RegulatingControl.regulating_cond_eq.clear(self)

    def num_regulating_cond_eq(self) -> int:
        return RegulatingControl.regulating_cond_eq.count(self)

    def get_regulating_cond_eq_by_mrid(self, mrid: str) -> RegulatingCondEq | None:
        return RegulatingControl.regulating_cond_eq.get_by_mrid(self, mrid)
