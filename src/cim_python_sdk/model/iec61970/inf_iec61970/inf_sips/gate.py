"""CIM class Gate (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate_input_pin import GateInputPin
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate_logic_kind import GateLogicKind
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_gate import PinGate
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action import (
        ProtectiveAction,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.remedial_action_scheme import (
        RemedialActionScheme,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage_trigger import StageTrigger
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.trigger_condition import (
        TriggerCondition,
    )


class Gate(IdentifiedObject):
    """Logical gate than support logical operation based on the input."""

    __slots__ = (
        "_gate_input_pin",
        "_pin_gate",
        "_protective_action_com",
        "_protective_action_enabled",
        "_remedial_action_scheme",
        "_stage_trigger",
        "_stage_trigger_armed",
        "_stage_trigger_com",
        "_trigger_condition",
        "kind",
    )

    kind: GateLogicKind | None

    gate_input_pin: Many[GateInputPin] = Many(
        EndMeta(
            name="gate_input_pin",
            cim_role="GateInputPin",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate_input_pin:GateInputPin",
            many=True,
            lower=1,
            upper=None,
            inverse="gate",
            aggregation="shared",
        )
    )
    protective_action_enabled: Many[ProtectiveAction] = Many(
        EndMeta(
            name="protective_action_enabled",
            cim_role="ProtectiveActionEnabled",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action:ProtectiveAction",
            many=True,
            lower=0,
            upper=None,
            inverse="gate_enabled_condition",
            aggregation="none",
        )
    )
    trigger_condition: Many[TriggerCondition] = Many(
        EndMeta(
            name="trigger_condition",
            cim_role="TriggerCondition",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.trigger_condition:TriggerCondition",
            many=True,
            lower=0,
            upper=None,
            inverse="gate_trigger",
            aggregation="none",
        )
    )
    stage_trigger: Many[StageTrigger] = Many(
        EndMeta(
            name="stage_trigger",
            cim_role="StageTrigger",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage_trigger:StageTrigger",
            many=True,
            lower=0,
            upper=None,
            inverse="gate_trigger",
            aggregation="none",
        )
    )
    stage_trigger_com: Many[StageTrigger] = Many(
        EndMeta(
            name="stage_trigger_com",
            cim_role="StageTriggerCom",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage_trigger:StageTrigger",
            many=True,
            lower=0,
            upper=None,
            inverse="gate_com_condition",
            aggregation="none",
        )
    )
    pin_gate: Many[PinGate] = Many(
        EndMeta(
            name="pin_gate",
            cim_role="PinGate",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_gate:PinGate",
            many=True,
            lower=0,
            upper=None,
            inverse="gate_output",
            aggregation="shared",
        )
    )
    protective_action_com: Many[ProtectiveAction] = Many(
        EndMeta(
            name="protective_action_com",
            cim_role="ProtectiveActionCom",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action:ProtectiveAction",
            many=True,
            lower=0,
            upper=None,
            inverse="gate_com_condition",
            aggregation="none",
        )
    )
    stage_trigger_armed: Many[StageTrigger] = Many(
        EndMeta(
            name="stage_trigger_armed",
            cim_role="StageTriggerArmed",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage_trigger:StageTrigger",
            many=True,
            lower=0,
            upper=None,
            inverse="gate_armed",
            aggregation="none",
        )
    )
    remedial_action_scheme: Many[RemedialActionScheme] = Many(
        EndMeta(
            name="remedial_action_scheme",
            cim_role="RemedialActionScheme",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.remedial_action_scheme:RemedialActionScheme",
            many=True,
            lower=0,
            upper=None,
            inverse="gate_armed",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Gate",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{EE0C575D-1F3F-4034-96EB-EB4B493B9788}",
        attributes=(AttrMeta("kind", "kind", "GateLogicKind", 0, 1, "enumeration"),),
        ends=(
            gate_input_pin.meta,
            protective_action_enabled.meta,
            trigger_condition.meta,
            stage_trigger.meta,
            stage_trigger_com.meta,
            pin_gate.meta,
            protective_action_com.meta,
            stage_trigger_armed.meta,
            remedial_action_scheme.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: GateLogicKind | None = None,
        gate_input_pin: Iterable[GateInputPin] | None = None,
        protective_action_enabled: Iterable[ProtectiveAction] | None = None,
        trigger_condition: Iterable[TriggerCondition] | None = None,
        stage_trigger: Iterable[StageTrigger] | None = None,
        stage_trigger_com: Iterable[StageTrigger] | None = None,
        pin_gate: Iterable[PinGate] | None = None,
        protective_action_com: Iterable[ProtectiveAction] | None = None,
        stage_trigger_armed: Iterable[StageTrigger] | None = None,
        remedial_action_scheme: Iterable[RemedialActionScheme] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if gate_input_pin is not None:
            Gate.gate_input_pin.extend(self, gate_input_pin)
        if protective_action_enabled is not None:
            Gate.protective_action_enabled.extend(self, protective_action_enabled)
        if trigger_condition is not None:
            Gate.trigger_condition.extend(self, trigger_condition)
        if stage_trigger is not None:
            Gate.stage_trigger.extend(self, stage_trigger)
        if stage_trigger_com is not None:
            Gate.stage_trigger_com.extend(self, stage_trigger_com)
        if pin_gate is not None:
            Gate.pin_gate.extend(self, pin_gate)
        if protective_action_com is not None:
            Gate.protective_action_com.extend(self, protective_action_com)
        if stage_trigger_armed is not None:
            Gate.stage_trigger_armed.extend(self, stage_trigger_armed)
        if remedial_action_scheme is not None:
            Gate.remedial_action_scheme.extend(self, remedial_action_scheme)

    def add_gate_input_pin(self, gate_input_pin: GateInputPin) -> Self:
        return Gate.gate_input_pin.add(self, gate_input_pin)

    def remove_gate_input_pin(self, gate_input_pin: GateInputPin) -> Self:
        return Gate.gate_input_pin.remove(self, gate_input_pin)

    def clear_gate_input_pin(self) -> Self:
        return Gate.gate_input_pin.clear(self)

    def num_gate_input_pin(self) -> int:
        return Gate.gate_input_pin.count(self)

    def get_gate_input_pin_by_mrid(self, mrid: str) -> GateInputPin | None:
        return Gate.gate_input_pin.get_by_mrid(self, mrid)

    def add_protective_action_enabled(self, protective_action_enabled: ProtectiveAction) -> Self:
        return Gate.protective_action_enabled.add(self, protective_action_enabled)

    def remove_protective_action_enabled(self, protective_action_enabled: ProtectiveAction) -> Self:
        return Gate.protective_action_enabled.remove(self, protective_action_enabled)

    def clear_protective_action_enabled(self) -> Self:
        return Gate.protective_action_enabled.clear(self)

    def num_protective_action_enabled(self) -> int:
        return Gate.protective_action_enabled.count(self)

    def get_protective_action_enabled_by_mrid(self, mrid: str) -> ProtectiveAction | None:
        return Gate.protective_action_enabled.get_by_mrid(self, mrid)

    def add_trigger_condition(self, trigger_condition: TriggerCondition) -> Self:
        return Gate.trigger_condition.add(self, trigger_condition)

    def remove_trigger_condition(self, trigger_condition: TriggerCondition) -> Self:
        return Gate.trigger_condition.remove(self, trigger_condition)

    def clear_trigger_condition(self) -> Self:
        return Gate.trigger_condition.clear(self)

    def num_trigger_condition(self) -> int:
        return Gate.trigger_condition.count(self)

    def get_trigger_condition_by_mrid(self, mrid: str) -> TriggerCondition | None:
        return Gate.trigger_condition.get_by_mrid(self, mrid)

    def add_stage_trigger(self, stage_trigger: StageTrigger) -> Self:
        return Gate.stage_trigger.add(self, stage_trigger)

    def remove_stage_trigger(self, stage_trigger: StageTrigger) -> Self:
        return Gate.stage_trigger.remove(self, stage_trigger)

    def clear_stage_trigger(self) -> Self:
        return Gate.stage_trigger.clear(self)

    def num_stage_trigger(self) -> int:
        return Gate.stage_trigger.count(self)

    def get_stage_trigger_by_mrid(self, mrid: str) -> StageTrigger | None:
        return Gate.stage_trigger.get_by_mrid(self, mrid)

    def add_stage_trigger_com(self, stage_trigger_com: StageTrigger) -> Self:
        return Gate.stage_trigger_com.add(self, stage_trigger_com)

    def remove_stage_trigger_com(self, stage_trigger_com: StageTrigger) -> Self:
        return Gate.stage_trigger_com.remove(self, stage_trigger_com)

    def clear_stage_trigger_com(self) -> Self:
        return Gate.stage_trigger_com.clear(self)

    def num_stage_trigger_com(self) -> int:
        return Gate.stage_trigger_com.count(self)

    def get_stage_trigger_com_by_mrid(self, mrid: str) -> StageTrigger | None:
        return Gate.stage_trigger_com.get_by_mrid(self, mrid)

    def add_pin_gate(self, pin_gate: PinGate) -> Self:
        return Gate.pin_gate.add(self, pin_gate)

    def remove_pin_gate(self, pin_gate: PinGate) -> Self:
        return Gate.pin_gate.remove(self, pin_gate)

    def clear_pin_gate(self) -> Self:
        return Gate.pin_gate.clear(self)

    def num_pin_gate(self) -> int:
        return Gate.pin_gate.count(self)

    def get_pin_gate_by_mrid(self, mrid: str) -> PinGate | None:
        return Gate.pin_gate.get_by_mrid(self, mrid)

    def add_protective_action_com(self, protective_action_com: ProtectiveAction) -> Self:
        return Gate.protective_action_com.add(self, protective_action_com)

    def remove_protective_action_com(self, protective_action_com: ProtectiveAction) -> Self:
        return Gate.protective_action_com.remove(self, protective_action_com)

    def clear_protective_action_com(self) -> Self:
        return Gate.protective_action_com.clear(self)

    def num_protective_action_com(self) -> int:
        return Gate.protective_action_com.count(self)

    def get_protective_action_com_by_mrid(self, mrid: str) -> ProtectiveAction | None:
        return Gate.protective_action_com.get_by_mrid(self, mrid)

    def add_stage_trigger_armed(self, stage_trigger_armed: StageTrigger) -> Self:
        return Gate.stage_trigger_armed.add(self, stage_trigger_armed)

    def remove_stage_trigger_armed(self, stage_trigger_armed: StageTrigger) -> Self:
        return Gate.stage_trigger_armed.remove(self, stage_trigger_armed)

    def clear_stage_trigger_armed(self) -> Self:
        return Gate.stage_trigger_armed.clear(self)

    def num_stage_trigger_armed(self) -> int:
        return Gate.stage_trigger_armed.count(self)

    def get_stage_trigger_armed_by_mrid(self, mrid: str) -> StageTrigger | None:
        return Gate.stage_trigger_armed.get_by_mrid(self, mrid)

    def add_remedial_action_scheme(self, remedial_action_scheme: RemedialActionScheme) -> Self:
        return Gate.remedial_action_scheme.add(self, remedial_action_scheme)

    def remove_remedial_action_scheme(self, remedial_action_scheme: RemedialActionScheme) -> Self:
        return Gate.remedial_action_scheme.remove(self, remedial_action_scheme)

    def clear_remedial_action_scheme(self) -> Self:
        return Gate.remedial_action_scheme.clear(self)

    def num_remedial_action_scheme(self) -> int:
        return Gate.remedial_action_scheme.count(self)

    def get_remedial_action_scheme_by_mrid(self, mrid: str) -> RemedialActionScheme | None:
        return Gate.remedial_action_scheme.get_by_mrid(self, mrid)
