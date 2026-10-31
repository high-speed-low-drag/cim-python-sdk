"""CIM class Work (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.work.base_work import BaseWork

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.appointment import Appointment
    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.work_billing_info import (
        WorkBillingInfo,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_project_accounting import (
        ErpProjectAccounting,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.business_case import BusinessCase
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design import Design
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.project import Project
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_flow_step import WorkFlowStep
    from cim_python_sdk.model.iec61968.operations.incident import Incident
    from cim_python_sdk.model.iec61968.work.work_task import WorkTask


class Work(BaseWork):
    """Document used to request, initiate, track and record work."""

    __slots__ = (
        "_appointments",
        "_business_case",
        "_customers",
        "_designs",
        "_erp_project_accounting",
        "_incidents",
        "_project",
        "_work_billing_info",
        "_work_cost_details",
        "_work_flow_steps",
        "_work_tasks",
        "request_date_time",
        "work_order_number",
    )

    work_order_number: str | None
    request_date_time: _dt.datetime | None

    customers: Many[Customer] = Many(
        EndMeta(
            name="customers",
            cim_role="Customers",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=True,
            lower=0,
            upper=None,
            inverse="works",
            aggregation="none",
        )
    )
    erp_project_accounting: One[ErpProjectAccounting] = One(
        EndMeta(
            name="erp_project_accounting",
            cim_role="ErpProjectAccounting",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_project_accounting:ErpProjectAccounting",
            many=False,
            lower=0,
            upper=1,
            inverse="works",
            aggregation="none",
        )
    )
    incidents: Many[Incident] = Many(
        EndMeta(
            name="incidents",
            cim_role="Incidents",
            target="cim_python_sdk.model.iec61968.operations.incident:Incident",
            many=True,
            lower=0,
            upper=None,
            inverse="works",
            aggregation="none",
        )
    )
    work_flow_steps: Many[WorkFlowStep] = Many(
        EndMeta(
            name="work_flow_steps",
            cim_role="WorkFlowSteps",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_flow_step:WorkFlowStep",
            many=True,
            lower=0,
            upper=None,
            inverse="work",
            aggregation="none",
        )
    )
    business_case: One[BusinessCase] = One(
        EndMeta(
            name="business_case",
            cim_role="BusinessCase",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.business_case:BusinessCase",
            many=False,
            lower=0,
            upper=1,
            inverse="works",
            aggregation="none",
        )
    )
    appointments: Many[Appointment] = Many(
        EndMeta(
            name="appointments",
            cim_role="Appointments",
            target="cim_python_sdk.model.iec61968.common.appointment:Appointment",
            many=True,
            lower=0,
            upper=None,
            inverse="works",
            aggregation="none",
        )
    )
    designs: Many[Design] = Many(
        EndMeta(
            name="designs",
            cim_role="Designs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design:Design",
            many=True,
            lower=0,
            upper=None,
            inverse="work",
            aggregation="none",
        )
    )
    work_billing_info: One[WorkBillingInfo] = One(
        EndMeta(
            name="work_billing_info",
            cim_role="WorkBillingInfo",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.work_billing_info:WorkBillingInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="works",
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
            inverse="works",
            aggregation="none",
        )
    )
    work_tasks: Many[WorkTask] = Many(
        EndMeta(
            name="work_tasks",
            cim_role="WorkTasks",
            target="cim_python_sdk.model.iec61968.work.work_task:WorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="work",
            aggregation="none",
        )
    )
    project: One[Project] = One(
        EndMeta(
            name="project",
            cim_role="Project",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.project:Project",
            many=False,
            lower=0,
            upper=1,
            inverse="works",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Work",
        package="TC57CIM/IEC61968/Work",
        guid="{BBD91857-52A1-4304-AC16-27142B5B76FB}",
        attributes=(
            AttrMeta("work_order_number", "workOrderNumber", "str", 0, 1, "primitive"),
            AttrMeta("request_date_time", "requestDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            customers.meta,
            erp_project_accounting.meta,
            incidents.meta,
            work_flow_steps.meta,
            business_case.meta,
            appointments.meta,
            designs.meta,
            work_billing_info.meta,
            work_cost_details.meta,
            work_tasks.meta,
            project.meta,
        ),
    )

    def __init__(
        self,
        *,
        work_order_number: str | None = None,
        request_date_time: _dt.datetime | None = None,
        customers: Iterable[Customer] | None = None,
        erp_project_accounting: ErpProjectAccounting | None = None,
        incidents: Iterable[Incident] | None = None,
        work_flow_steps: Iterable[WorkFlowStep] | None = None,
        business_case: BusinessCase | None = None,
        appointments: Iterable[Appointment] | None = None,
        designs: Iterable[Design] | None = None,
        work_billing_info: WorkBillingInfo | None = None,
        work_cost_details: Iterable[WorkCostDetail] | None = None,
        work_tasks: Iterable[WorkTask] | None = None,
        project: Project | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.work_order_number = work_order_number
        self.request_date_time = request_date_time
        if customers is not None:
            Work.customers.extend(self, customers)
        if erp_project_accounting is not None:
            self.erp_project_accounting = erp_project_accounting
        if incidents is not None:
            Work.incidents.extend(self, incidents)
        if work_flow_steps is not None:
            Work.work_flow_steps.extend(self, work_flow_steps)
        if business_case is not None:
            self.business_case = business_case
        if appointments is not None:
            Work.appointments.extend(self, appointments)
        if designs is not None:
            Work.designs.extend(self, designs)
        if work_billing_info is not None:
            self.work_billing_info = work_billing_info
        if work_cost_details is not None:
            Work.work_cost_details.extend(self, work_cost_details)
        if work_tasks is not None:
            Work.work_tasks.extend(self, work_tasks)
        if project is not None:
            self.project = project

    def add_customer(self, customer: Customer) -> Self:
        return Work.customers.add(self, customer)

    def remove_customer(self, customer: Customer) -> Self:
        return Work.customers.remove(self, customer)

    def clear_customers(self) -> Self:
        return Work.customers.clear(self)

    def num_customer(self) -> int:
        return Work.customers.count(self)

    def get_customer_by_mrid(self, mrid: str) -> Customer | None:
        return Work.customers.get_by_mrid(self, mrid)

    def add_incident(self, incident: Incident) -> Self:
        return Work.incidents.add(self, incident)

    def remove_incident(self, incident: Incident) -> Self:
        return Work.incidents.remove(self, incident)

    def clear_incidents(self) -> Self:
        return Work.incidents.clear(self)

    def num_incident(self) -> int:
        return Work.incidents.count(self)

    def get_incident_by_mrid(self, mrid: str) -> Incident | None:
        return Work.incidents.get_by_mrid(self, mrid)

    def add_work_flow_step(self, work_flow_step: WorkFlowStep) -> Self:
        return Work.work_flow_steps.add(self, work_flow_step)

    def remove_work_flow_step(self, work_flow_step: WorkFlowStep) -> Self:
        return Work.work_flow_steps.remove(self, work_flow_step)

    def clear_work_flow_steps(self) -> Self:
        return Work.work_flow_steps.clear(self)

    def num_work_flow_step(self) -> int:
        return Work.work_flow_steps.count(self)

    def get_work_flow_step_by_mrid(self, mrid: str) -> WorkFlowStep | None:
        return Work.work_flow_steps.get_by_mrid(self, mrid)

    def add_appointment(self, appointment: Appointment) -> Self:
        return Work.appointments.add(self, appointment)

    def remove_appointment(self, appointment: Appointment) -> Self:
        return Work.appointments.remove(self, appointment)

    def clear_appointments(self) -> Self:
        return Work.appointments.clear(self)

    def num_appointment(self) -> int:
        return Work.appointments.count(self)

    def get_appointment_by_mrid(self, mrid: str) -> Appointment | None:
        return Work.appointments.get_by_mrid(self, mrid)

    def add_design(self, design: Design) -> Self:
        return Work.designs.add(self, design)

    def remove_design(self, design: Design) -> Self:
        return Work.designs.remove(self, design)

    def clear_designs(self) -> Self:
        return Work.designs.clear(self)

    def num_design(self) -> int:
        return Work.designs.count(self)

    def get_design_by_mrid(self, mrid: str) -> Design | None:
        return Work.designs.get_by_mrid(self, mrid)

    def add_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return Work.work_cost_details.add(self, work_cost_detail)

    def remove_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return Work.work_cost_details.remove(self, work_cost_detail)

    def clear_work_cost_details(self) -> Self:
        return Work.work_cost_details.clear(self)

    def num_work_cost_detail(self) -> int:
        return Work.work_cost_details.count(self)

    def get_work_cost_detail_by_mrid(self, mrid: str) -> WorkCostDetail | None:
        return Work.work_cost_details.get_by_mrid(self, mrid)

    def add_work_task(self, work_task: WorkTask) -> Self:
        return Work.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: WorkTask) -> Self:
        return Work.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return Work.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return Work.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> WorkTask | None:
        return Work.work_tasks.get_by_mrid(self, mrid)
