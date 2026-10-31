"""CIM class SwitchingStep (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.revision_history import RevisionHistory
    from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction
    from cim_python_sdk.model.iec61968.operations.switching_step_group import SwitchingStepGroup


class SwitchingStep(CimObject):
    """Atomic switching step; can be part of a switching step group, or part of a switching
    plan."""

    __slots__ = (
        "_revision_history",
        "_switching_action",
        "_switching_step_group",
        "is_free_sequence",
        "sequence_number",
        "sub_step_sequence_number",
    )

    sequence_number: int | None
    is_free_sequence: bool | None
    sub_step_sequence_number: int | None

    revision_history: One[RevisionHistory] = One(
        EndMeta(
            name="revision_history",
            cim_role="RevisionHistory",
            target="cim_python_sdk.model.iec61968.operations.revision_history:RevisionHistory",
            many=False,
            lower=1,
            upper=1,
            inverse="switching_step",
            aggregation="none",
        )
    )
    switching_step_group: One[SwitchingStepGroup] = One(
        EndMeta(
            name="switching_step_group",
            cim_role="SwitchingStepGroup",
            target="cim_python_sdk.model.iec61968.operations.switching_step_group:SwitchingStepGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_step",
            aggregation="none",
        )
    )
    switching_action: One[SwitchingAction] = One(
        EndMeta(
            name="switching_action",
            cim_role="SwitchingAction",
            target="cim_python_sdk.model.iec61968.operations.switching_action:SwitchingAction",
            many=False,
            lower=1,
            upper=1,
            inverse="switching_step",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchingStep",
        package="TC57CIM/IEC61968/Operations",
        guid="{EE8680C2-ED07-4a60-9EF9-7A23C54F7FD0}",
        attributes=(
            AttrMeta("sequence_number", "sequenceNumber", "int", 1, 1, "primitive"),
            AttrMeta("is_free_sequence", "isFreeSequence", "bool", 1, 1, "primitive"),
            AttrMeta("sub_step_sequence_number", "subStepSequenceNumber", "int", 1, 1, "primitive"),
        ),
        ends=(
            revision_history.meta,
            switching_step_group.meta,
            switching_action.meta,
        ),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        is_free_sequence: bool | None = None,
        sub_step_sequence_number: int | None = None,
        revision_history: RevisionHistory | None = None,
        switching_step_group: SwitchingStepGroup | None = None,
        switching_action: SwitchingAction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        self.is_free_sequence = is_free_sequence
        self.sub_step_sequence_number = sub_step_sequence_number
        if revision_history is not None:
            self.revision_history = revision_history
        if switching_step_group is not None:
            self.switching_step_group = switching_step_group
        if switching_action is not None:
            self.switching_action = switching_action
