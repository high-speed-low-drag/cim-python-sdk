"""CIM class StageTrigger (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate import Gate
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_collection import (
        ProtectiveActionCollection,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage import Stage


class StageTrigger(IdentifiedObject):
    """Condition that is triggered either by TriggerCondition of by gate condition within a
    stage and has remedial action-s."""

    __slots__ = (
        "_gate_armed",
        "_gate_com_condition",
        "_gate_trigger",
        "_protective_action_collection",
        "_stage",
        "armed",
        "normal_armed",
        "priority",
    )

    armed: bool | None
    normal_armed: bool | None
    priority: int | None

    gate_trigger: One[Gate] = One(
        EndMeta(
            name="gate_trigger",
            cim_role="GateTrigger",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate:Gate",
            many=False,
            lower=0,
            upper=1,
            inverse="stage_trigger",
            aggregation="none",
        )
    )
    gate_com_condition: One[Gate] = One(
        EndMeta(
            name="gate_com_condition",
            cim_role="GateComCondition",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate:Gate",
            many=False,
            lower=0,
            upper=1,
            inverse="stage_trigger_com",
            aggregation="none",
        )
    )
    stage: One[Stage] = One(
        EndMeta(
            name="stage",
            cim_role="Stage",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage:Stage",
            many=False,
            lower=1,
            upper=1,
            inverse="stage_trigger",
            aggregation="none",
        )
    )
    protective_action_collection: One[ProtectiveActionCollection] = One(
        EndMeta(
            name="protective_action_collection",
            cim_role="ProtectiveActionCollection",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_collection:ProtectiveActionCollection",
            many=False,
            lower=1,
            upper=1,
            inverse="stage_trigger",
            aggregation="none",
        )
    )
    gate_armed: One[Gate] = One(
        EndMeta(
            name="gate_armed",
            cim_role="GateArmed",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate:Gate",
            many=False,
            lower=0,
            upper=1,
            inverse="stage_trigger_armed",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StageTrigger",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{88383979-C8C0-46c1-9E3B-2E720872694F}",
        attributes=(
            AttrMeta("armed", "armed", "bool", 0, 1, "primitive"),
            AttrMeta("normal_armed", "normalArmed", "bool", 0, 1, "primitive"),
            AttrMeta("priority", "priority", "int", 0, 1, "primitive"),
        ),
        ends=(
            gate_trigger.meta,
            gate_com_condition.meta,
            stage.meta,
            protective_action_collection.meta,
            gate_armed.meta,
        ),
    )

    def __init__(
        self,
        *,
        armed: bool | None = None,
        normal_armed: bool | None = None,
        priority: int | None = None,
        gate_trigger: Gate | None = None,
        gate_com_condition: Gate | None = None,
        stage: Stage | None = None,
        protective_action_collection: ProtectiveActionCollection | None = None,
        gate_armed: Gate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.armed = armed
        self.normal_armed = normal_armed
        self.priority = priority
        if gate_trigger is not None:
            self.gate_trigger = gate_trigger
        if gate_com_condition is not None:
            self.gate_com_condition = gate_com_condition
        if stage is not None:
            self.stage = stage
        if protective_action_collection is not None:
            self.protective_action_collection = protective_action_collection
        if gate_armed is not None:
            self.gate_armed = gate_armed
