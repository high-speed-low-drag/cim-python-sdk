"""CIM class Organisation (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.electronic_address import ElectronicAddress
    from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole
    from cim_python_sdk.model.iec61968.common.parent_organization import ParentOrganization
    from cim_python_sdk.model.iec61968.common.street_address import StreetAddress
    from cim_python_sdk.model.iec61968.common.telephone_number import TelephoneNumber
    from cim_python_sdk.model.iec61968.operations.switching_plan_request import SwitchingPlanRequest


class Organisation(IdentifiedObject):
    """Organisation that might have roles as utility, contractor, supplier, manufacturer,
    customer, etc."""

    __slots__ = (
        "_parent_organisation",
        "_roles",
        "_switching_plan_request",
        "electronic_address",
        "phone1",
        "phone2",
        "postal_address",
        "street_address",
    )

    street_address: StreetAddress | None
    postal_address: StreetAddress | None
    phone1: TelephoneNumber | None
    phone2: TelephoneNumber | None
    electronic_address: ElectronicAddress | None

    roles: Many[OrganisationRole] = Many(
        EndMeta(
            name="roles",
            cim_role="Roles",
            target="cim_python_sdk.model.iec61968.common.organisation_role:OrganisationRole",
            many=True,
            lower=0,
            upper=None,
            inverse="organisation",
            aggregation="none",
        )
    )
    parent_organisation: One[ParentOrganization] = One(
        EndMeta(
            name="parent_organisation",
            cim_role="ParentOrganisation",
            target="cim_python_sdk.model.iec61968.common.parent_organization:ParentOrganization",
            many=False,
            lower=0,
            upper=1,
            inverse="organisation",
            aggregation="none",
        )
    )
    switching_plan_request: Many[SwitchingPlanRequest] = Many(
        EndMeta(
            name="switching_plan_request",
            cim_role="SwitchingPlanRequest",
            target="cim_python_sdk.model.iec61968.operations.switching_plan_request:SwitchingPlanRequest",
            many=True,
            lower=0,
            upper=None,
            inverse="requesting_organization",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Organisation",
        package="TC57CIM/IEC61968/Common",
        guid="{F8CDB36C-C67A-437e-B836-79674718904E}",
        attributes=(
            AttrMeta("street_address", "streetAddress", "StreetAddress", 0, 1, "compound"),
            AttrMeta("postal_address", "postalAddress", "StreetAddress", 0, 1, "compound"),
            AttrMeta("phone1", "phone1", "TelephoneNumber", 0, 1, "compound"),
            AttrMeta("phone2", "phone2", "TelephoneNumber", 0, 1, "compound"),
            AttrMeta(
                "electronic_address", "electronicAddress", "ElectronicAddress", 0, 1, "compound"
            ),
        ),
        ends=(
            roles.meta,
            parent_organisation.meta,
            switching_plan_request.meta,
        ),
    )

    def __init__(
        self,
        *,
        street_address: StreetAddress | None = None,
        postal_address: StreetAddress | None = None,
        phone1: TelephoneNumber | None = None,
        phone2: TelephoneNumber | None = None,
        electronic_address: ElectronicAddress | None = None,
        roles: Iterable[OrganisationRole] | None = None,
        parent_organisation: ParentOrganization | None = None,
        switching_plan_request: Iterable[SwitchingPlanRequest] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.street_address = street_address
        self.postal_address = postal_address
        self.phone1 = phone1
        self.phone2 = phone2
        self.electronic_address = electronic_address
        if roles is not None:
            Organisation.roles.extend(self, roles)
        if parent_organisation is not None:
            self.parent_organisation = parent_organisation
        if switching_plan_request is not None:
            Organisation.switching_plan_request.extend(self, switching_plan_request)

    def add_role(self, role: OrganisationRole) -> Self:
        return Organisation.roles.add(self, role)

    def remove_role(self, role: OrganisationRole) -> Self:
        return Organisation.roles.remove(self, role)

    def clear_roles(self) -> Self:
        return Organisation.roles.clear(self)

    def num_role(self) -> int:
        return Organisation.roles.count(self)

    def get_role_by_mrid(self, mrid: str) -> OrganisationRole | None:
        return Organisation.roles.get_by_mrid(self, mrid)

    def add_switching_plan_request(self, switching_plan_request: SwitchingPlanRequest) -> Self:
        return Organisation.switching_plan_request.add(self, switching_plan_request)

    def remove_switching_plan_request(self, switching_plan_request: SwitchingPlanRequest) -> Self:
        return Organisation.switching_plan_request.remove(self, switching_plan_request)

    def clear_switching_plan_request(self) -> Self:
        return Organisation.switching_plan_request.clear(self)

    def num_switching_plan_request(self) -> int:
        return Organisation.switching_plan_request.count(self)

    def get_switching_plan_request_by_mrid(self, mrid: str) -> SwitchingPlanRequest | None:
        return Organisation.switching_plan_request.get_by_mrid(self, mrid)
