"""CIM class RemedialActionScheme (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate import Gate
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.remedial_action_scheme_kind import (
        RemedialActionSchemeKind,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage import Stage
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.trigger_condition import (
        TriggerCondition,
    )


class RemedialActionScheme(PowerSystemResource):
    """Remedial Action Scheme (RAS), Special Protection Schemes (SPS), System Protection
    Schemes (SPS) or System Integrity Protection Schemes (SIPS)."""

    __slots__ = ("_gate_armed", "_stage", "_trigger_condition", "armed", "kind", "normal_armed")

    armed: bool | None
    kind: RemedialActionSchemeKind | None
    normal_armed: bool | None

    trigger_condition: Many[TriggerCondition] = Many(
        EndMeta(
            name="trigger_condition",
            cim_role="TriggerCondition",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.trigger_condition:TriggerCondition",
            many=True,
            lower=0,
            upper=None,
            inverse="remedial_action_scheme",
            aggregation="none",
        )
    )
    stage: Many[Stage] = Many(
        EndMeta(
            name="stage",
            cim_role="Stage",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage:Stage",
            many=True,
            lower=1,
            upper=None,
            inverse="remedial_action_scheme",
            aggregation="shared",
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
            inverse="remedial_action_scheme",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RemedialActionScheme",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{DA505846-8BFC-4185-8F6E-20C3A5761B0C}",
        attributes=(
            AttrMeta("armed", "armed", "bool", 0, 1, "primitive"),
            AttrMeta("kind", "kind", "RemedialActionSchemeKind", 0, 1, "enumeration"),
            AttrMeta("normal_armed", "normalArmed", "bool", 0, 1, "primitive"),
        ),
        ends=(
            trigger_condition.meta,
            stage.meta,
            gate_armed.meta,
        ),
    )

    def __init__(
        self,
        *,
        armed: bool | None = None,
        kind: RemedialActionSchemeKind | None = None,
        normal_armed: bool | None = None,
        trigger_condition: Iterable[TriggerCondition] | None = None,
        stage: Iterable[Stage] | None = None,
        gate_armed: Gate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.armed = armed
        self.kind = kind
        self.normal_armed = normal_armed
        if trigger_condition is not None:
            RemedialActionScheme.trigger_condition.extend(self, trigger_condition)
        if stage is not None:
            RemedialActionScheme.stage.extend(self, stage)
        if gate_armed is not None:
            self.gate_armed = gate_armed

    def add_trigger_condition(self, trigger_condition: TriggerCondition) -> Self:
        return RemedialActionScheme.trigger_condition.add(self, trigger_condition)

    def remove_trigger_condition(self, trigger_condition: TriggerCondition) -> Self:
        return RemedialActionScheme.trigger_condition.remove(self, trigger_condition)

    def clear_trigger_condition(self) -> Self:
        return RemedialActionScheme.trigger_condition.clear(self)

    def num_trigger_condition(self) -> int:
        return RemedialActionScheme.trigger_condition.count(self)

    def get_trigger_condition_by_mrid(self, mrid: str) -> TriggerCondition | None:
        return RemedialActionScheme.trigger_condition.get_by_mrid(self, mrid)

    def add_stage(self, stage: Stage) -> Self:
        return RemedialActionScheme.stage.add(self, stage)

    def remove_stage(self, stage: Stage) -> Self:
        return RemedialActionScheme.stage.remove(self, stage)

    def clear_stage(self) -> Self:
        return RemedialActionScheme.stage.clear(self)

    def num_stage(self) -> int:
        return RemedialActionScheme.stage.count(self)

    def get_stage_by_mrid(self, mrid: str) -> Stage | None:
        return RemedialActionScheme.stage.get_by_mrid(self, mrid)
