"""CIM class OverheadCost (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail


class OverheadCost(WorkIdentifiedObject):
    """Overhead cost applied to work order."""

    __slots__ = ("_work_cost_details", "_work_tasks", "code", "cost", "status")

    code: str | None
    cost: _decimal.Decimal | None  # Money
    status: Status | None

    work_tasks: Many[OldWorkTask] = Many(
        EndMeta(
            name="work_tasks",
            cim_role="WorkTasks",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task:OldWorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="overhead_cost",
            aggregation="none",
        )
    )
    work_cost_details: Many[WorkCostDetail] = Many(
        EndMeta(
            name="work_cost_details",
            cim_role="WorkCostDetails",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail:WorkCostDetail",
            many=True,
            lower=0,
            upper=None,
            inverse="overhead_cost",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OverheadCost",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{3A2959A1-9448-41e5-AAA9-E762F32458BA}",
        attributes=(
            AttrMeta("code", "code", "str", 0, 1, "primitive"),
            AttrMeta("cost", "cost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            work_tasks.meta,
            work_cost_details.meta,
        ),
    )

    def __init__(
        self,
        *,
        code: str | None = None,
        cost: _decimal.Decimal | None = None,
        status: Status | None = None,
        work_tasks: Iterable[OldWorkTask] | None = None,
        work_cost_details: Iterable[WorkCostDetail] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.code = code
        self.cost = cost
        self.status = status
        if work_tasks is not None:
            OverheadCost.work_tasks.extend(self, work_tasks)
        if work_cost_details is not None:
            OverheadCost.work_cost_details.extend(self, work_cost_details)

    def add_work_task(self, work_task: OldWorkTask) -> Self:
        return OverheadCost.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: OldWorkTask) -> Self:
        return OverheadCost.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return OverheadCost.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return OverheadCost.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> OldWorkTask | None:
        return OverheadCost.work_tasks.get_by_mrid(self, mrid)

    def add_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return OverheadCost.work_cost_details.add(self, work_cost_detail)

    def remove_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return OverheadCost.work_cost_details.remove(self, work_cost_detail)

    def clear_work_cost_details(self) -> Self:
        return OverheadCost.work_cost_details.clear(self)

    def num_work_cost_detail(self) -> int:
        return OverheadCost.work_cost_details.count(self)

    def get_work_cost_detail_by_mrid(self, mrid: str) -> WorkCostDetail | None:
        return OverheadCost.work_cost_details.get_by_mrid(self, mrid)
