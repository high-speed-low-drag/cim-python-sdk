"""CIM class QualificationRequirement (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification import Specification
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.skill import Skill
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_labor_item import CULaborItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask


class QualificationRequirement(WorkIdentifiedObject):
    """Certain skills are required and must be certified in order for a person (typically a
    member of a crew) to be qualified to work on types of equipment."""

    __slots__ = ("_cu_labor_items", "_skills", "_specifications", "_work_tasks", "qualification_id")

    qualification_id: str | None

    specifications: Many[Specification] = Many(
        EndMeta(
            name="specifications",
            cim_role="Specifications",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification:Specification",
            many=True,
            lower=0,
            upper=None,
            inverse="qualification_requirements",
            aggregation="none",
        )
    )
    cu_labor_items: Many[CULaborItem] = Many(
        EndMeta(
            name="cu_labor_items",
            cim_role="CULaborItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_labor_item:CULaborItem",
            many=True,
            lower=0,
            upper=None,
            inverse="qualification_requirements",
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
            inverse="qualification_requirements",
            aggregation="none",
        )
    )
    skills: Many[Skill] = Many(
        EndMeta(
            name="skills",
            cim_role="Skills",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.skill:Skill",
            many=True,
            lower=0,
            upper=None,
            inverse="qualification_requirements",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="QualificationRequirement",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{540D4F43-4F53-4ea4-8DEB-07918430C8AE}",
        attributes=(AttrMeta("qualification_id", "qualificationID", "str", 0, 1, "primitive"),),
        ends=(
            specifications.meta,
            cu_labor_items.meta,
            work_tasks.meta,
            skills.meta,
        ),
    )

    def __init__(
        self,
        *,
        qualification_id: str | None = None,
        specifications: Iterable[Specification] | None = None,
        cu_labor_items: Iterable[CULaborItem] | None = None,
        work_tasks: Iterable[OldWorkTask] | None = None,
        skills: Iterable[Skill] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.qualification_id = qualification_id
        if specifications is not None:
            QualificationRequirement.specifications.extend(self, specifications)
        if cu_labor_items is not None:
            QualificationRequirement.cu_labor_items.extend(self, cu_labor_items)
        if work_tasks is not None:
            QualificationRequirement.work_tasks.extend(self, work_tasks)
        if skills is not None:
            QualificationRequirement.skills.extend(self, skills)

    def add_specification(self, specification: Specification) -> Self:
        return QualificationRequirement.specifications.add(self, specification)

    def remove_specification(self, specification: Specification) -> Self:
        return QualificationRequirement.specifications.remove(self, specification)

    def clear_specifications(self) -> Self:
        return QualificationRequirement.specifications.clear(self)

    def num_specification(self) -> int:
        return QualificationRequirement.specifications.count(self)

    def get_specification_by_mrid(self, mrid: str) -> Specification | None:
        return QualificationRequirement.specifications.get_by_mrid(self, mrid)

    def add_cu_labor_item(self, cu_labor_item: CULaborItem) -> Self:
        return QualificationRequirement.cu_labor_items.add(self, cu_labor_item)

    def remove_cu_labor_item(self, cu_labor_item: CULaborItem) -> Self:
        return QualificationRequirement.cu_labor_items.remove(self, cu_labor_item)

    def clear_cu_labor_items(self) -> Self:
        return QualificationRequirement.cu_labor_items.clear(self)

    def num_cu_labor_item(self) -> int:
        return QualificationRequirement.cu_labor_items.count(self)

    def get_cu_labor_item_by_mrid(self, mrid: str) -> CULaborItem | None:
        return QualificationRequirement.cu_labor_items.get_by_mrid(self, mrid)

    def add_work_task(self, work_task: OldWorkTask) -> Self:
        return QualificationRequirement.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: OldWorkTask) -> Self:
        return QualificationRequirement.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return QualificationRequirement.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return QualificationRequirement.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> OldWorkTask | None:
        return QualificationRequirement.work_tasks.get_by_mrid(self, mrid)

    def add_skill(self, skill: Skill) -> Self:
        return QualificationRequirement.skills.add(self, skill)

    def remove_skill(self, skill: Skill) -> Self:
        return QualificationRequirement.skills.remove(self, skill)

    def clear_skills(self) -> Self:
        return QualificationRequirement.skills.clear(self)

    def num_skill(self) -> int:
        return QualificationRequirement.skills.count(self)

    def get_skill_by_mrid(self, mrid: str) -> Skill | None:
        return QualificationRequirement.skills.get_by_mrid(self, mrid)
