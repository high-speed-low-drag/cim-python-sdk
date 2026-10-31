"""CIM class MarketPerson (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.electronic_address import ElectronicAddress
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.common.telephone_number import TelephoneNumber
    from cim_python_sdk.model.iec62325.market_common.market_participant import MarketParticipant
    from cim_python_sdk.model.iec62325.market_operations.reference_data.market_skill import (
        MarketSkill,
    )


class MarketPerson(IdentifiedObject):
    """General purpose information for name and other information to contact people."""

    __slots__ = (
        "_market_participant",
        "_market_skills",
        "category",
        "electronic_address_alternate",
        "electronic_address_primary",
        "first_name",
        "government_id",
        "landline_phone",
        "last_name",
        "m_name",
        "mobile_phone",
        "prefix",
        "special_need",
        "status",
        "suffix",
        "user_id",
    )

    category: str | None
    electronic_address_alternate: ElectronicAddress | None
    electronic_address_primary: ElectronicAddress | None
    first_name: str | None
    government_id: str | None
    landline_phone: TelephoneNumber | None
    last_name: str | None
    m_name: str | None
    mobile_phone: TelephoneNumber | None
    prefix: str | None
    special_need: str | None
    status: Status | None
    suffix: str | None
    user_id: str | None

    market_skills: Many[MarketSkill] = Many(
        EndMeta(
            name="market_skills",
            cim_role="MarketSkills",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.market_skill:MarketSkill",
            many=True,
            lower=0,
            upper=None,
            inverse="market_person",
            aggregation="none",
        )
    )
    market_participant: Many[MarketParticipant] = Many(
        EndMeta(
            name="market_participant",
            cim_role="MarketParticipant",
            target="cim_python_sdk.model.iec62325.market_common.market_participant:MarketParticipant",
            many=True,
            lower=0,
            upper=None,
            inverse="market_person",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketPerson",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{920B428C-558A-4196-AC2B-DFD8CB2F83C1}",
        attributes=(
            AttrMeta("category", "category", "str", 0, 1, "primitive"),
            AttrMeta(
                "electronic_address_alternate",
                "electronicAddressAlternate",
                "ElectronicAddress",
                0,
                1,
                "compound",
            ),
            AttrMeta(
                "electronic_address_primary",
                "electronicAddressPrimary",
                "ElectronicAddress",
                0,
                1,
                "compound",
            ),
            AttrMeta("first_name", "firstName", "str", 0, 1, "primitive"),
            AttrMeta("government_id", "governmentID", "str", 0, 1, "primitive"),
            AttrMeta("landline_phone", "landlinePhone", "TelephoneNumber", 0, 1, "compound"),
            AttrMeta("last_name", "lastName", "str", 0, 1, "primitive"),
            AttrMeta("m_name", "mName", "str", 0, 1, "primitive"),
            AttrMeta("mobile_phone", "mobilePhone", "TelephoneNumber", 0, 1, "compound"),
            AttrMeta("prefix", "prefix", "str", 0, 1, "primitive"),
            AttrMeta("special_need", "specialNeed", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
            AttrMeta("suffix", "suffix", "str", 0, 1, "primitive"),
            AttrMeta("user_id", "userID", "str", 0, 1, "primitive"),
        ),
        ends=(
            market_skills.meta,
            market_participant.meta,
        ),
    )

    def __init__(
        self,
        *,
        category: str | None = None,
        electronic_address_alternate: ElectronicAddress | None = None,
        electronic_address_primary: ElectronicAddress | None = None,
        first_name: str | None = None,
        government_id: str | None = None,
        landline_phone: TelephoneNumber | None = None,
        last_name: str | None = None,
        m_name: str | None = None,
        mobile_phone: TelephoneNumber | None = None,
        prefix: str | None = None,
        special_need: str | None = None,
        status: Status | None = None,
        suffix: str | None = None,
        user_id: str | None = None,
        market_skills: Iterable[MarketSkill] | None = None,
        market_participant: Iterable[MarketParticipant] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.category = category
        self.electronic_address_alternate = electronic_address_alternate
        self.electronic_address_primary = electronic_address_primary
        self.first_name = first_name
        self.government_id = government_id
        self.landline_phone = landline_phone
        self.last_name = last_name
        self.m_name = m_name
        self.mobile_phone = mobile_phone
        self.prefix = prefix
        self.special_need = special_need
        self.status = status
        self.suffix = suffix
        self.user_id = user_id
        if market_skills is not None:
            MarketPerson.market_skills.extend(self, market_skills)
        if market_participant is not None:
            MarketPerson.market_participant.extend(self, market_participant)

    def add_market_skill(self, market_skill: MarketSkill) -> Self:
        return MarketPerson.market_skills.add(self, market_skill)

    def remove_market_skill(self, market_skill: MarketSkill) -> Self:
        return MarketPerson.market_skills.remove(self, market_skill)

    def clear_market_skills(self) -> Self:
        return MarketPerson.market_skills.clear(self)

    def num_market_skill(self) -> int:
        return MarketPerson.market_skills.count(self)

    def get_market_skill_by_mrid(self, mrid: str) -> MarketSkill | None:
        return MarketPerson.market_skills.get_by_mrid(self, mrid)

    def add_market_participant(self, market_participant: MarketParticipant) -> Self:
        return MarketPerson.market_participant.add(self, market_participant)

    def remove_market_participant(self, market_participant: MarketParticipant) -> Self:
        return MarketPerson.market_participant.remove(self, market_participant)

    def clear_market_participant(self) -> Self:
        return MarketPerson.market_participant.clear(self)

    def num_market_participant(self) -> int:
        return MarketPerson.market_participant.count(self)

    def get_market_participant_by_mrid(self, mrid: str) -> MarketParticipant | None:
        return MarketPerson.market_participant.get_by_mrid(self, mrid)
