"""CIM class ErpProjectAccounting (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_time_entry import (
        ErpTimeEntry,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.project import Project
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail
    from cim_python_sdk.model.iec61968.work.work import Work


class ErpProjectAccounting(ErpDocument):
    """Utility Project Accounting information, used by ERP applications to enable all relevant
    sub-systems that submit single sided transactions to transfer information with a Project
    Accounting Application. This would include, but not necessarily be limited to: Accounts
    Payable, Accounts Receivable, Budget, Order Management, Purchasing, Time and Labor,
    Travel and Expense."""

    __slots__ = ("_erp_time_entries", "_projects", "_work_cost_details", "_works")

    works: Many[Work] = Many(
        EndMeta(
            name="works",
            cim_role="Works",
            target="cim_python_sdk.model.iec61968.work.work:Work",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_project_accounting",
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
            inverse="erp_project_accounting",
            aggregation="none",
        )
    )
    projects: Many[Project] = Many(
        EndMeta(
            name="projects",
            cim_role="Projects",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.project:Project",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_project_accounting",
            aggregation="none",
        )
    )
    erp_time_entries: Many[ErpTimeEntry] = Many(
        EndMeta(
            name="erp_time_entries",
            cim_role="ErpTimeEntries",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_time_entry:ErpTimeEntry",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_project_accounting",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpProjectAccounting",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{93D527C0-CE28-4069-A6FB-D862754B4420}",
        ends=(
            works.meta,
            work_cost_details.meta,
            projects.meta,
            erp_time_entries.meta,
        ),
    )

    def __init__(
        self,
        *,
        works: Iterable[Work] | None = None,
        work_cost_details: Iterable[WorkCostDetail] | None = None,
        projects: Iterable[Project] | None = None,
        erp_time_entries: Iterable[ErpTimeEntry] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if works is not None:
            ErpProjectAccounting.works.extend(self, works)
        if work_cost_details is not None:
            ErpProjectAccounting.work_cost_details.extend(self, work_cost_details)
        if projects is not None:
            ErpProjectAccounting.projects.extend(self, projects)
        if erp_time_entries is not None:
            ErpProjectAccounting.erp_time_entries.extend(self, erp_time_entries)

    def add_work(self, work: Work) -> Self:
        return ErpProjectAccounting.works.add(self, work)

    def remove_work(self, work: Work) -> Self:
        return ErpProjectAccounting.works.remove(self, work)

    def clear_works(self) -> Self:
        return ErpProjectAccounting.works.clear(self)

    def num_work(self) -> int:
        return ErpProjectAccounting.works.count(self)

    def get_work_by_mrid(self, mrid: str) -> Work | None:
        return ErpProjectAccounting.works.get_by_mrid(self, mrid)

    def add_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return ErpProjectAccounting.work_cost_details.add(self, work_cost_detail)

    def remove_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return ErpProjectAccounting.work_cost_details.remove(self, work_cost_detail)

    def clear_work_cost_details(self) -> Self:
        return ErpProjectAccounting.work_cost_details.clear(self)

    def num_work_cost_detail(self) -> int:
        return ErpProjectAccounting.work_cost_details.count(self)

    def get_work_cost_detail_by_mrid(self, mrid: str) -> WorkCostDetail | None:
        return ErpProjectAccounting.work_cost_details.get_by_mrid(self, mrid)

    def add_project(self, project: Project) -> Self:
        return ErpProjectAccounting.projects.add(self, project)

    def remove_project(self, project: Project) -> Self:
        return ErpProjectAccounting.projects.remove(self, project)

    def clear_projects(self) -> Self:
        return ErpProjectAccounting.projects.clear(self)

    def num_project(self) -> int:
        return ErpProjectAccounting.projects.count(self)

    def get_project_by_mrid(self, mrid: str) -> Project | None:
        return ErpProjectAccounting.projects.get_by_mrid(self, mrid)

    def add_erp_time_entry(self, erp_time_entry: ErpTimeEntry) -> Self:
        return ErpProjectAccounting.erp_time_entries.add(self, erp_time_entry)

    def remove_erp_time_entry(self, erp_time_entry: ErpTimeEntry) -> Self:
        return ErpProjectAccounting.erp_time_entries.remove(self, erp_time_entry)

    def clear_erp_time_entries(self) -> Self:
        return ErpProjectAccounting.erp_time_entries.clear(self)

    def num_erp_time_entry(self) -> int:
        return ErpProjectAccounting.erp_time_entries.count(self)

    def get_erp_time_entry_by_mrid(self, mrid: str) -> ErpTimeEntry | None:
        return ErpProjectAccounting.erp_time_entries.get_by_mrid(self, mrid)
