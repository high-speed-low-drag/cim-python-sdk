"""CIM class MarketSkill (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec62325.market_operations.reference_data.market_person import (
        MarketPerson,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.market_qualification_requirement import (
        MarketQualificationRequirement,
    )


class MarketSkill(Document):
    """Proficiency level of a craft, which is required to operate or maintain a particular type
    of asset and/or perform certain types of work."""

    __slots__ = (
        "_market_person",
        "_market_qualification_requirements",
        "certification_period",
        "effective_date_time",
        "level",
    )

    certification_period: DateTimeInterval | None
    effective_date_time: _dt.datetime | None
    level: str | None

    market_person: One[MarketPerson] = One(
        EndMeta(
            name="market_person",
            cim_role="MarketPerson",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.market_person:MarketPerson",
            many=False,
            lower=0,
            upper=1,
            inverse="market_skills",
            aggregation="none",
        )
    )
    market_qualification_requirements: Many[MarketQualificationRequirement] = Many(
        EndMeta(
            name="market_qualification_requirements",
            cim_role="MarketQualificationRequirements",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.market_qualification_requirement:MarketQualificationRequirement",
            many=True,
            lower=0,
            upper=None,
            inverse="market_skills",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketSkill",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{4EACB8B2-0E30-4b17-9A2D-844B414A1B6B}",
        attributes=(
            AttrMeta(
                "certification_period", "certificationPeriod", "DateTimeInterval", 0, 1, "compound"
            ),
            AttrMeta("effective_date_time", "effectiveDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("level", "level", "str", 0, 1, "primitive"),
        ),
        ends=(
            market_person.meta,
            market_qualification_requirements.meta,
        ),
    )

    def __init__(
        self,
        *,
        certification_period: DateTimeInterval | None = None,
        effective_date_time: _dt.datetime | None = None,
        level: str | None = None,
        market_person: MarketPerson | None = None,
        market_qualification_requirements: Iterable[MarketQualificationRequirement] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.certification_period = certification_period
        self.effective_date_time = effective_date_time
        self.level = level
        if market_person is not None:
            self.market_person = market_person
        if market_qualification_requirements is not None:
            MarketSkill.market_qualification_requirements.extend(
                self, market_qualification_requirements
            )

    def add_market_qualification_requirement(
        self, market_qualification_requirement: MarketQualificationRequirement
    ) -> Self:
        return MarketSkill.market_qualification_requirements.add(
            self, market_qualification_requirement
        )

    def remove_market_qualification_requirement(
        self, market_qualification_requirement: MarketQualificationRequirement
    ) -> Self:
        return MarketSkill.market_qualification_requirements.remove(
            self, market_qualification_requirement
        )

    def clear_market_qualification_requirements(self) -> Self:
        return MarketSkill.market_qualification_requirements.clear(self)

    def num_market_qualification_requirement(self) -> int:
        return MarketSkill.market_qualification_requirements.count(self)

    def get_market_qualification_requirement_by_mrid(
        self, mrid: str
    ) -> MarketQualificationRequirement | None:
        return MarketSkill.market_qualification_requirements.get_by_mrid(self, mrid)
