"""CIM class Stage (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.remedial_action_scheme import (
        RemedialActionScheme,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage_trigger import StageTrigger


class Stage(IdentifiedObject):
    """Stage of a remedial action scheme."""

    __slots__ = ("_remedial_action_scheme", "_stage_trigger", "priority")

    priority: int | None

    remedial_action_scheme: One[RemedialActionScheme] = One(
        EndMeta(
            name="remedial_action_scheme",
            cim_role="RemedialActionScheme",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.remedial_action_scheme:RemedialActionScheme",
            many=False,
            lower=1,
            upper=1,
            inverse="stage",
            aggregation="none",
        )
    )
    stage_trigger: Many[StageTrigger] = Many(
        EndMeta(
            name="stage_trigger",
            cim_role="StageTrigger",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage_trigger:StageTrigger",
            many=True,
            lower=1,
            upper=None,
            inverse="stage",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Stage",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{F18F00A6-9C7B-483b-A568-BFD9B14DCB0E}",
        attributes=(AttrMeta("priority", "priority", "int", 0, 1, "primitive"),),
        ends=(
            remedial_action_scheme.meta,
            stage_trigger.meta,
        ),
    )

    def __init__(
        self,
        *,
        priority: int | None = None,
        remedial_action_scheme: RemedialActionScheme | None = None,
        stage_trigger: Iterable[StageTrigger] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.priority = priority
        if remedial_action_scheme is not None:
            self.remedial_action_scheme = remedial_action_scheme
        if stage_trigger is not None:
            Stage.stage_trigger.extend(self, stage_trigger)

    def add_stage_trigger(self, stage_trigger: StageTrigger) -> Self:
        return Stage.stage_trigger.add(self, stage_trigger)

    def remove_stage_trigger(self, stage_trigger: StageTrigger) -> Self:
        return Stage.stage_trigger.remove(self, stage_trigger)

    def clear_stage_trigger(self) -> Self:
        return Stage.stage_trigger.clear(self)

    def num_stage_trigger(self) -> int:
        return Stage.stage_trigger.count(self)

    def get_stage_trigger_by_mrid(self, mrid: str) -> StageTrigger | None:
        return Stage.stage_trigger.get_by_mrid(self, mrid)
