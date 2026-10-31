"""CIM class Project (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_project_accounting import (
        ErpProjectAccounting,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.business_case import BusinessCase
    from cim_python_sdk.model.iec61968.work.work import Work


class Project(WorkDocument):
    """A collection of related work. For construction projects and maintenance projects,
    multiple phases may be performed."""

    __slots__ = (
        "_business_case",
        "_erp_project_accounting",
        "_parent_project",
        "_sub_projects",
        "_works",
        "budget",
    )

    budget: _decimal.Decimal | None  # Money

    sub_projects: Many[Project] = Many(
        EndMeta(
            name="sub_projects",
            cim_role="SubProjects",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.project:Project",
            many=True,
            lower=0,
            upper=None,
            inverse="parent_project",
            aggregation="none",
        )
    )
    parent_project: One[Project] = One(
        EndMeta(
            name="parent_project",
            cim_role="ParentProject",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.project:Project",
            many=False,
            lower=0,
            upper=1,
            inverse="sub_projects",
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
            inverse="projects",
            aggregation="none",
        )
    )
    erp_project_accounting: One[ErpProjectAccounting] = One(
        EndMeta(
            name="erp_project_accounting",
            cim_role="ErpProjectAccounting",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_project_accounting:ErpProjectAccounting",
            many=False,
            lower=1,
            upper=1,
            inverse="projects",
            aggregation="none",
        )
    )
    works: Many[Work] = Many(
        EndMeta(
            name="works",
            cim_role="Works",
            target="cim_python_sdk.model.iec61968.work.work:Work",
            many=True,
            lower=0,
            upper=None,
            inverse="project",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Project",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{A2FA7B7B-8141-4486-AE1E-5CDE98AFCB36}",
        attributes=(AttrMeta("budget", "budget", "Money", 0, 1, "cimdatatype"),),
        ends=(
            sub_projects.meta,
            parent_project.meta,
            business_case.meta,
            erp_project_accounting.meta,
            works.meta,
        ),
    )

    def __init__(
        self,
        *,
        budget: _decimal.Decimal | None = None,
        sub_projects: Iterable[Project] | None = None,
        parent_project: Project | None = None,
        business_case: BusinessCase | None = None,
        erp_project_accounting: ErpProjectAccounting | None = None,
        works: Iterable[Work] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.budget = budget
        if sub_projects is not None:
            Project.sub_projects.extend(self, sub_projects)
        if parent_project is not None:
            self.parent_project = parent_project
        if business_case is not None:
            self.business_case = business_case
        if erp_project_accounting is not None:
            self.erp_project_accounting = erp_project_accounting
        if works is not None:
            Project.works.extend(self, works)

    def add_sub_project(self, sub_project: Project) -> Self:
        return Project.sub_projects.add(self, sub_project)

    def remove_sub_project(self, sub_project: Project) -> Self:
        return Project.sub_projects.remove(self, sub_project)

    def clear_sub_projects(self) -> Self:
        return Project.sub_projects.clear(self)

    def num_sub_project(self) -> int:
        return Project.sub_projects.count(self)

    def get_sub_project_by_mrid(self, mrid: str) -> Project | None:
        return Project.sub_projects.get_by_mrid(self, mrid)

    def add_work(self, work: Work) -> Self:
        return Project.works.add(self, work)

    def remove_work(self, work: Work) -> Self:
        return Project.works.remove(self, work)

    def clear_works(self) -> Self:
        return Project.works.clear(self)

    def num_work(self) -> int:
        return Project.works.count(self)

    def get_work_by_mrid(self, mrid: str) -> Work | None:
        return Project.works.get_by_mrid(self, mrid)
