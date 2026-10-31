"""CIM class Craft (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person import OldPerson
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.skill import Skill
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.capability import Capability


class Craft(IdentifiedObject):
    """Craft of a person or a crew. Examples include overhead electric, underground electric,
    high pressure gas, etc. This ensures necessary knowledge and skills before being allowed
    to perform certain types of work."""

    __slots__ = ("_capabilities", "_erp_persons", "_skills", "status", "type")

    type: str | None
    status: Status | None

    erp_persons: Many[OldPerson] = Many(
        EndMeta(
            name="erp_persons",
            cim_role="ErpPersons",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person:OldPerson",
            many=True,
            lower=0,
            upper=None,
            inverse="crafts",
            aggregation="none",
        )
    )
    capabilities: Many[Capability] = Many(
        EndMeta(
            name="capabilities",
            cim_role="Capabilities",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.capability:Capability",
            many=True,
            lower=0,
            upper=None,
            inverse="crafts",
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
            inverse="crafts",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Craft",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{8C0BFCC8-2AFC-46d1-A9AB-7922B3447265}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            erp_persons.meta,
            capabilities.meta,
            skills.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        status: Status | None = None,
        erp_persons: Iterable[OldPerson] | None = None,
        capabilities: Iterable[Capability] | None = None,
        skills: Iterable[Skill] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.status = status
        if erp_persons is not None:
            Craft.erp_persons.extend(self, erp_persons)
        if capabilities is not None:
            Craft.capabilities.extend(self, capabilities)
        if skills is not None:
            Craft.skills.extend(self, skills)

    def add_erp_person(self, erp_person: OldPerson) -> Self:
        return Craft.erp_persons.add(self, erp_person)

    def remove_erp_person(self, erp_person: OldPerson) -> Self:
        return Craft.erp_persons.remove(self, erp_person)

    def clear_erp_persons(self) -> Self:
        return Craft.erp_persons.clear(self)

    def num_erp_person(self) -> int:
        return Craft.erp_persons.count(self)

    def get_erp_person_by_mrid(self, mrid: str) -> OldPerson | None:
        return Craft.erp_persons.get_by_mrid(self, mrid)

    def add_capability(self, capability: Capability) -> Self:
        return Craft.capabilities.add(self, capability)

    def remove_capability(self, capability: Capability) -> Self:
        return Craft.capabilities.remove(self, capability)

    def clear_capabilities(self) -> Self:
        return Craft.capabilities.clear(self)

    def num_capability(self) -> int:
        return Craft.capabilities.count(self)

    def get_capability_by_mrid(self, mrid: str) -> Capability | None:
        return Craft.capabilities.get_by_mrid(self, mrid)

    def add_skill(self, skill: Skill) -> Self:
        return Craft.skills.add(self, skill)

    def remove_skill(self, skill: Skill) -> Self:
        return Craft.skills.remove(self, skill)

    def clear_skills(self) -> Self:
        return Craft.skills.clear(self)

    def num_skill(self) -> int:
        return Craft.skills.count(self)

    def get_skill_by_mrid(self, mrid: str) -> Skill | None:
        return Craft.skills.get_by_mrid(self, mrid)
