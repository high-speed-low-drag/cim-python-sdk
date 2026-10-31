"""CIM class Skill (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.craft import Craft
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person import OldPerson
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.skill_level_kind import (
        SkillLevelKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.qualification_requirement import (
        QualificationRequirement,
    )
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class Skill(Document):
    """Proficiency level of a craft, which is required to operate or maintain a particular type
    of asset and/or perform certain types of work."""

    __slots__ = (
        "_crafts",
        "_erp_person",
        "_qualification_requirements",
        "certification_period",
        "effective_date_time",
        "level",
    )

    level: SkillLevelKind | None
    certification_period: DateTimeInterval | None
    effective_date_time: _dt.datetime | None

    erp_person: One[OldPerson] = One(
        EndMeta(
            name="erp_person",
            cim_role="ErpPerson",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person:OldPerson",
            many=False,
            lower=0,
            upper=1,
            inverse="skills",
            aggregation="none",
        )
    )
    qualification_requirements: Many[QualificationRequirement] = Many(
        EndMeta(
            name="qualification_requirements",
            cim_role="QualificationRequirements",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.qualification_requirement:QualificationRequirement",
            many=True,
            lower=0,
            upper=None,
            inverse="skills",
            aggregation="none",
        )
    )
    crafts: Many[Craft] = Many(
        EndMeta(
            name="crafts",
            cim_role="Crafts",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.craft:Craft",
            many=True,
            lower=0,
            upper=None,
            inverse="skills",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Skill",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{13EF0D6F-830A-4054-B0A2-D02F94EF4C74}",
        attributes=(
            AttrMeta("level", "level", "SkillLevelKind", 0, 1, "enumeration"),
            AttrMeta(
                "certification_period", "certificationPeriod", "DateTimeInterval", 0, 1, "compound"
            ),
            AttrMeta("effective_date_time", "effectiveDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            erp_person.meta,
            qualification_requirements.meta,
            crafts.meta,
        ),
    )

    def __init__(
        self,
        *,
        level: SkillLevelKind | None = None,
        certification_period: DateTimeInterval | None = None,
        effective_date_time: _dt.datetime | None = None,
        erp_person: OldPerson | None = None,
        qualification_requirements: Iterable[QualificationRequirement] | None = None,
        crafts: Iterable[Craft] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.level = level
        self.certification_period = certification_period
        self.effective_date_time = effective_date_time
        if erp_person is not None:
            self.erp_person = erp_person
        if qualification_requirements is not None:
            Skill.qualification_requirements.extend(self, qualification_requirements)
        if crafts is not None:
            Skill.crafts.extend(self, crafts)

    def add_qualification_requirement(
        self, qualification_requirement: QualificationRequirement
    ) -> Self:
        return Skill.qualification_requirements.add(self, qualification_requirement)

    def remove_qualification_requirement(
        self, qualification_requirement: QualificationRequirement
    ) -> Self:
        return Skill.qualification_requirements.remove(self, qualification_requirement)

    def clear_qualification_requirements(self) -> Self:
        return Skill.qualification_requirements.clear(self)

    def num_qualification_requirement(self) -> int:
        return Skill.qualification_requirements.count(self)

    def get_qualification_requirement_by_mrid(self, mrid: str) -> QualificationRequirement | None:
        return Skill.qualification_requirements.get_by_mrid(self, mrid)

    def add_craft(self, craft: Craft) -> Self:
        return Skill.crafts.add(self, craft)

    def remove_craft(self, craft: Craft) -> Self:
        return Skill.crafts.remove(self, craft)

    def clear_crafts(self) -> Self:
        return Skill.crafts.clear(self)

    def num_craft(self) -> int:
        return Skill.crafts.count(self)

    def get_craft_by_mrid(self, mrid: str) -> Craft | None:
        return Skill.crafts.get_by_mrid(self, mrid)
