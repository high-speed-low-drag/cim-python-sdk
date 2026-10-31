"""CIM class SwitchingStepGroup (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.switching_plan import SwitchingPlan
    from cim_python_sdk.model.iec61968.operations.switching_step import SwitchingStep


class SwitchingStepGroup(CimObject):
    """A logical step, grouping atomic switching steps that are important to distinguish when
    they may change topology (e.g. placing a jumper between two cuts)."""

    __slots__ = (
        "_switching_plan",
        "_switching_step",
        "description",
        "is_free_sequence",
        "purpose",
        "sequence_number",
    )

    sequence_number: int | None
    description: str | None
    is_free_sequence: bool | None
    purpose: str | None

    switching_plan: One[SwitchingPlan] = One(
        EndMeta(
            name="switching_plan",
            cim_role="SwitchingPlan",
            target="cim_python_sdk.model.iec61968.operations.switching_plan:SwitchingPlan",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_step_groups",
            aggregation="none",
        )
    )
    switching_step: Many[SwitchingStep] = Many(
        EndMeta(
            name="switching_step",
            cim_role="SwitchingStep",
            target="cim_python_sdk.model.iec61968.operations.switching_step:SwitchingStep",
            many=True,
            lower=0,
            upper=None,
            inverse="switching_step_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchingStepGroup",
        package="TC57CIM/IEC61968/Operations",
        guid="{A45191CC-01B4-4f9d-BD30-806616AC04C8}",
        attributes=(
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("description", "description", "str", 0, 1, "primitive"),
            AttrMeta("is_free_sequence", "isFreeSequence", "bool", 0, 1, "primitive"),
            AttrMeta("purpose", "purpose", "str", 0, 1, "primitive"),
        ),
        ends=(
            switching_plan.meta,
            switching_step.meta,
        ),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        description: str | None = None,
        is_free_sequence: bool | None = None,
        purpose: str | None = None,
        switching_plan: SwitchingPlan | None = None,
        switching_step: Iterable[SwitchingStep] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        self.description = description
        self.is_free_sequence = is_free_sequence
        self.purpose = purpose
        if switching_plan is not None:
            self.switching_plan = switching_plan
        if switching_step is not None:
            SwitchingStepGroup.switching_step.extend(self, switching_step)

    def add_switching_step(self, switching_step: SwitchingStep) -> Self:
        return SwitchingStepGroup.switching_step.add(self, switching_step)

    def remove_switching_step(self, switching_step: SwitchingStep) -> Self:
        return SwitchingStepGroup.switching_step.remove(self, switching_step)

    def clear_switching_step(self) -> Self:
        return SwitchingStepGroup.switching_step.clear(self)

    def num_switching_step(self) -> int:
        return SwitchingStepGroup.switching_step.count(self)
