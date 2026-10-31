"""CIM class WorkFlowStep (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask
    from cim_python_sdk.model.iec61968.work.work import Work


class WorkFlowStep(WorkIdentifiedObject):
    """A pre-defined set of work steps for a given type of work."""

    __slots__ = ("_work", "_work_tasks", "sequence_number", "status")

    sequence_number: int | None
    status: Status | None

    work: One[Work] = One(
        EndMeta(
            name="work",
            cim_role="Work",
            target="cim_python_sdk.model.iec61968.work.work:Work",
            many=False,
            lower=0,
            upper=1,
            inverse="work_flow_steps",
            aggregation="none",
        )
    )
    work_tasks: Many[OldWorkTask] = Many(
        EndMeta(
            name="work_tasks",
            cim_role="WorkTasks",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task:OldWorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="work_flow_step",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WorkFlowStep",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{41A4996B-E85F-48bb-9849-706FA0E7BDB7}",
        attributes=(
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            work.meta,
            work_tasks.meta,
        ),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        status: Status | None = None,
        work: Work | None = None,
        work_tasks: Iterable[OldWorkTask] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        self.status = status
        if work is not None:
            self.work = work
        if work_tasks is not None:
            WorkFlowStep.work_tasks.extend(self, work_tasks)

    def add_work_task(self, work_task: OldWorkTask) -> Self:
        return WorkFlowStep.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: OldWorkTask) -> Self:
        return WorkFlowStep.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return WorkFlowStep.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return WorkFlowStep.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> OldWorkTask | None:
        return WorkFlowStep.work_tasks.get_by_mrid(self, mrid)
