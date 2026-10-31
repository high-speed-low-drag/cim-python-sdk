"""CIM class BusinessCase (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.project import Project
    from cim_python_sdk.model.iec61968.work.work import Work


class BusinessCase(WorkDocument):
    """Business justification for capital expenditures, usually addressing operations and
    maintenance costs as well."""

    __slots__ = ("_projects", "_works", "corporate_code")

    corporate_code: str | None

    projects: Many[Project] = Many(
        EndMeta(
            name="projects",
            cim_role="Projects",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.project:Project",
            many=True,
            lower=0,
            upper=None,
            inverse="business_case",
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
            inverse="business_case",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BusinessCase",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{7D1894DE-529E-4574-80FA-AA8B38E9B88D}",
        attributes=(AttrMeta("corporate_code", "corporateCode", "str", 0, 1, "primitive"),),
        ends=(
            projects.meta,
            works.meta,
        ),
    )

    def __init__(
        self,
        *,
        corporate_code: str | None = None,
        projects: Iterable[Project] | None = None,
        works: Iterable[Work] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.corporate_code = corporate_code
        if projects is not None:
            BusinessCase.projects.extend(self, projects)
        if works is not None:
            BusinessCase.works.extend(self, works)

    def add_project(self, project: Project) -> Self:
        return BusinessCase.projects.add(self, project)

    def remove_project(self, project: Project) -> Self:
        return BusinessCase.projects.remove(self, project)

    def clear_projects(self) -> Self:
        return BusinessCase.projects.clear(self)

    def num_project(self) -> int:
        return BusinessCase.projects.count(self)

    def get_project_by_mrid(self, mrid: str) -> Project | None:
        return BusinessCase.projects.get_by_mrid(self, mrid)

    def add_work(self, work: Work) -> Self:
        return BusinessCase.works.add(self, work)

    def remove_work(self, work: Work) -> Self:
        return BusinessCase.works.remove(self, work)

    def clear_works(self) -> Self:
        return BusinessCase.works.clear(self)

    def num_work(self) -> int:
        return BusinessCase.works.count(self)

    def get_work_by_mrid(self, mrid: str) -> Work | None:
        return BusinessCase.works.get_by_mrid(self, mrid)
