"""CIM class ProtectiveActionCollection (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action import (
        ProtectiveAction,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.stage_trigger import StageTrigger


class ProtectiveActionCollection(IdentifiedObject):
    """A collection of protective actions to protect the integrity of the power system."""

    __slots__ = ("_protective_action", "_stage_trigger")

    protective_action: Many[ProtectiveAction] = Many(
        EndMeta(
            name="protective_action",
            cim_role="ProtectiveAction",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action:ProtectiveAction",
            many=True,
            lower=1,
            upper=None,
            inverse="protective_action_collection",
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
            inverse="protective_action_collection",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProtectiveActionCollection",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{122E89AF-E8F4-4003-8375-EC133E9069AA}",
        ends=(
            protective_action.meta,
            stage_trigger.meta,
        ),
    )

    def __init__(
        self,
        *,
        protective_action: Iterable[ProtectiveAction] | None = None,
        stage_trigger: Iterable[StageTrigger] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if protective_action is not None:
            ProtectiveActionCollection.protective_action.extend(self, protective_action)
        if stage_trigger is not None:
            ProtectiveActionCollection.stage_trigger.extend(self, stage_trigger)

    def add_protective_action(self, protective_action: ProtectiveAction) -> Self:
        return ProtectiveActionCollection.protective_action.add(self, protective_action)

    def remove_protective_action(self, protective_action: ProtectiveAction) -> Self:
        return ProtectiveActionCollection.protective_action.remove(self, protective_action)

    def clear_protective_action(self) -> Self:
        return ProtectiveActionCollection.protective_action.clear(self)

    def num_protective_action(self) -> int:
        return ProtectiveActionCollection.protective_action.count(self)

    def get_protective_action_by_mrid(self, mrid: str) -> ProtectiveAction | None:
        return ProtectiveActionCollection.protective_action.get_by_mrid(self, mrid)

    def add_stage_trigger(self, stage_trigger: StageTrigger) -> Self:
        return ProtectiveActionCollection.stage_trigger.add(self, stage_trigger)

    def remove_stage_trigger(self, stage_trigger: StageTrigger) -> Self:
        return ProtectiveActionCollection.stage_trigger.remove(self, stage_trigger)

    def clear_stage_trigger(self) -> Self:
        return ProtectiveActionCollection.stage_trigger.clear(self)

    def num_stage_trigger(self) -> int:
        return ProtectiveActionCollection.stage_trigger.count(self)

    def get_stage_trigger_by_mrid(self, mrid: str) -> StageTrigger | None:
        return ProtectiveActionCollection.stage_trigger.get_by_mrid(self, mrid)
