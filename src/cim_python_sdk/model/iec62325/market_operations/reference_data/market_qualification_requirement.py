"""CIM class MarketQualificationRequirement (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.market_skill import (
        MarketSkill,
    )


class MarketQualificationRequirement(IdentifiedObject):
    """Certain skills are required and shall be certified in order for a person (typically a
    member of a crew) to be qualified to work on types of equipment."""

    __slots__ = (
        "_market_skills",
        "effective_date",
        "expiration_date",
        "qualification_id",
        "status",
        "status_type",
    )

    effective_date: _dt.datetime | None
    expiration_date: _dt.datetime | None
    qualification_id: str | None
    status: int | None
    status_type: str | None

    market_skills: Many[MarketSkill] = Many(
        EndMeta(
            name="market_skills",
            cim_role="MarketSkills",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.market_skill:MarketSkill",
            many=True,
            lower=0,
            upper=None,
            inverse="market_qualification_requirements",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketQualificationRequirement",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{F30DEF68-DD5F-40e5-8646-0997994399AE}",
        attributes=(
            AttrMeta("effective_date", "effectiveDate", "datetime", 0, 1, "primitive"),
            AttrMeta("expiration_date", "expirationDate", "datetime", 0, 1, "primitive"),
            AttrMeta("qualification_id", "qualificationID", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "int", 0, 1, "primitive"),
            AttrMeta("status_type", "statusType", "str", 0, 1, "primitive"),
        ),
        ends=(market_skills.meta,),
    )

    def __init__(
        self,
        *,
        effective_date: _dt.datetime | None = None,
        expiration_date: _dt.datetime | None = None,
        qualification_id: str | None = None,
        status: int | None = None,
        status_type: str | None = None,
        market_skills: Iterable[MarketSkill] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.effective_date = effective_date
        self.expiration_date = expiration_date
        self.qualification_id = qualification_id
        self.status = status
        self.status_type = status_type
        if market_skills is not None:
            MarketQualificationRequirement.market_skills.extend(self, market_skills)

    def add_market_skill(self, market_skill: MarketSkill) -> Self:
        return MarketQualificationRequirement.market_skills.add(self, market_skill)

    def remove_market_skill(self, market_skill: MarketSkill) -> Self:
        return MarketQualificationRequirement.market_skills.remove(self, market_skill)

    def clear_market_skills(self) -> Self:
        return MarketQualificationRequirement.market_skills.clear(self)

    def num_market_skill(self) -> int:
        return MarketQualificationRequirement.market_skills.count(self)

    def get_market_skill_by_mrid(self, mrid: str) -> MarketSkill | None:
        return MarketQualificationRequirement.market_skills.get_by_mrid(self, mrid)
