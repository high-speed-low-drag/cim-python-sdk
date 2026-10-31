"""CIM class SwitchingPlan (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.outage import Outage
    from cim_python_sdk.model.iec61968.operations.outage_plan import OutagePlan
    from cim_python_sdk.model.iec61968.operations.planned_outage_notification import (
        PlannedOutageNotification,
    )
    from cim_python_sdk.model.iec61968.operations.safety_document import SafetyDocument
    from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction
    from cim_python_sdk.model.iec61968.operations.switching_order import SwitchingOrder
    from cim_python_sdk.model.iec61968.operations.switching_plan_request import SwitchingPlanRequest
    from cim_python_sdk.model.iec61968.operations.switching_step_group import SwitchingStepGroup
    from cim_python_sdk.model.iec61968.work.work_task import WorkTask
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class SwitchingPlan(Document):
    """A sequence of grouped or atomic steps intended to:

    - de-energise equipment or part of the network for safe work, and/or

    - bring back in service previously de-energised equipment or part of the network."""

    __slots__ = (
        "_outage",
        "_outage_plan",
        "_planned_outage_notification",
        "_safety_documents",
        "_switching_action",
        "_switching_order",
        "_switching_plan_request",
        "_switching_step_groups",
        "_work_tasks",
        "approved_date_time",
        "cancelled_date_time",
        "planned_period",
        "purpose",
        "rank",
    )

    rank: int | None
    purpose: str | None
    approved_date_time: _dt.datetime | None
    cancelled_date_time: _dt.datetime | None
    planned_period: DateTimeInterval | None

    work_tasks: Many[WorkTask] = Many(
        EndMeta(
            name="work_tasks",
            cim_role="WorkTasks",
            target="cim_python_sdk.model.iec61968.work.work_task:WorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="switching_plan",
            aggregation="none",
        )
    )
    outage_plan: One[OutagePlan] = One(
        EndMeta(
            name="outage_plan",
            cim_role="OutagePlan",
            target="cim_python_sdk.model.iec61968.operations.outage_plan:OutagePlan",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_plan",
            aggregation="none",
        )
    )
    safety_documents: Many[SafetyDocument] = Many(
        EndMeta(
            name="safety_documents",
            cim_role="SafetyDocuments",
            target="cim_python_sdk.model.iec61968.operations.safety_document:SafetyDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="switching_plan",
            aggregation="none",
        )
    )
    switching_action: Many[SwitchingAction] = Many(
        EndMeta(
            name="switching_action",
            cim_role="SwitchingAction",
            target="cim_python_sdk.model.iec61968.operations.switching_action:SwitchingAction",
            many=True,
            lower=0,
            upper=None,
            inverse="switching_plan",
            aggregation="none",
        )
    )
    switching_step_groups: Many[SwitchingStepGroup] = Many(
        EndMeta(
            name="switching_step_groups",
            cim_role="SwitchingStepGroups",
            target="cim_python_sdk.model.iec61968.operations.switching_step_group:SwitchingStepGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="switching_plan",
            aggregation="none",
        )
    )
    switching_plan_request: One[SwitchingPlanRequest] = One(
        EndMeta(
            name="switching_plan_request",
            cim_role="SwitchingPlanRequest",
            target="cim_python_sdk.model.iec61968.operations.switching_plan_request:SwitchingPlanRequest",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_plan",
            aggregation="none",
        )
    )
    switching_order: One[SwitchingOrder] = One(
        EndMeta(
            name="switching_order",
            cim_role="SwitchingOrder",
            target="cim_python_sdk.model.iec61968.operations.switching_order:SwitchingOrder",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_plan",
            aggregation="none",
        )
    )
    outage: One[Outage] = One(
        EndMeta(
            name="outage",
            cim_role="Outage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_plans",
            aggregation="none",
        )
    )
    planned_outage_notification: One[PlannedOutageNotification] = One(
        EndMeta(
            name="planned_outage_notification",
            cim_role="PlannedOutageNotification",
            target="cim_python_sdk.model.iec61968.operations.planned_outage_notification:PlannedOutageNotification",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_plan",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchingPlan",
        package="TC57CIM/IEC61968/Operations",
        guid="{94D8F29A-7F14-475a-A47C-4A7A44FDC831}",
        attributes=(
            AttrMeta("rank", "rank", "int", 0, 1, "primitive"),
            AttrMeta("purpose", "purpose", "str", 0, 1, "primitive"),
            AttrMeta("approved_date_time", "approvedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("cancelled_date_time", "cancelledDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("planned_period", "plannedPeriod", "DateTimeInterval", 0, 1, "compound"),
        ),
        ends=(
            work_tasks.meta,
            outage_plan.meta,
            safety_documents.meta,
            switching_action.meta,
            switching_step_groups.meta,
            switching_plan_request.meta,
            switching_order.meta,
            outage.meta,
            planned_outage_notification.meta,
        ),
    )

    def __init__(
        self,
        *,
        rank: int | None = None,
        purpose: str | None = None,
        approved_date_time: _dt.datetime | None = None,
        cancelled_date_time: _dt.datetime | None = None,
        planned_period: DateTimeInterval | None = None,
        work_tasks: Iterable[WorkTask] | None = None,
        outage_plan: OutagePlan | None = None,
        safety_documents: Iterable[SafetyDocument] | None = None,
        switching_action: Iterable[SwitchingAction] | None = None,
        switching_step_groups: Iterable[SwitchingStepGroup] | None = None,
        switching_plan_request: SwitchingPlanRequest | None = None,
        switching_order: SwitchingOrder | None = None,
        outage: Outage | None = None,
        planned_outage_notification: PlannedOutageNotification | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rank = rank
        self.purpose = purpose
        self.approved_date_time = approved_date_time
        self.cancelled_date_time = cancelled_date_time
        self.planned_period = planned_period
        if work_tasks is not None:
            SwitchingPlan.work_tasks.extend(self, work_tasks)
        if outage_plan is not None:
            self.outage_plan = outage_plan
        if safety_documents is not None:
            SwitchingPlan.safety_documents.extend(self, safety_documents)
        if switching_action is not None:
            SwitchingPlan.switching_action.extend(self, switching_action)
        if switching_step_groups is not None:
            SwitchingPlan.switching_step_groups.extend(self, switching_step_groups)
        if switching_plan_request is not None:
            self.switching_plan_request = switching_plan_request
        if switching_order is not None:
            self.switching_order = switching_order
        if outage is not None:
            self.outage = outage
        if planned_outage_notification is not None:
            self.planned_outage_notification = planned_outage_notification

    def add_work_task(self, work_task: WorkTask) -> Self:
        return SwitchingPlan.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: WorkTask) -> Self:
        return SwitchingPlan.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return SwitchingPlan.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return SwitchingPlan.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> WorkTask | None:
        return SwitchingPlan.work_tasks.get_by_mrid(self, mrid)

    def add_safety_document(self, safety_document: SafetyDocument) -> Self:
        return SwitchingPlan.safety_documents.add(self, safety_document)

    def remove_safety_document(self, safety_document: SafetyDocument) -> Self:
        return SwitchingPlan.safety_documents.remove(self, safety_document)

    def clear_safety_documents(self) -> Self:
        return SwitchingPlan.safety_documents.clear(self)

    def num_safety_document(self) -> int:
        return SwitchingPlan.safety_documents.count(self)

    def get_safety_document_by_mrid(self, mrid: str) -> SafetyDocument | None:
        return SwitchingPlan.safety_documents.get_by_mrid(self, mrid)

    def add_switching_action(self, switching_action: SwitchingAction) -> Self:
        return SwitchingPlan.switching_action.add(self, switching_action)

    def remove_switching_action(self, switching_action: SwitchingAction) -> Self:
        return SwitchingPlan.switching_action.remove(self, switching_action)

    def clear_switching_action(self) -> Self:
        return SwitchingPlan.switching_action.clear(self)

    def num_switching_action(self) -> int:
        return SwitchingPlan.switching_action.count(self)

    def get_switching_action_by_mrid(self, mrid: str) -> SwitchingAction | None:
        return SwitchingPlan.switching_action.get_by_mrid(self, mrid)

    def add_switching_step_group(self, switching_step_group: SwitchingStepGroup) -> Self:
        return SwitchingPlan.switching_step_groups.add(self, switching_step_group)

    def remove_switching_step_group(self, switching_step_group: SwitchingStepGroup) -> Self:
        return SwitchingPlan.switching_step_groups.remove(self, switching_step_group)

    def clear_switching_step_groups(self) -> Self:
        return SwitchingPlan.switching_step_groups.clear(self)

    def num_switching_step_group(self) -> int:
        return SwitchingPlan.switching_step_groups.count(self)
