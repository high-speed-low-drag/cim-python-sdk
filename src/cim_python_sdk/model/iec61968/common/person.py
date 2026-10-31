"""CIM class Person (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.electronic_address import ElectronicAddress
    from cim_python_sdk.model.iec61968.common.person_role import PersonRole
    from cim_python_sdk.model.iec61968.common.telephone_number import TelephoneNumber
    from cim_python_sdk.model.iec61968.customers.customer import Customer


class Person(IdentifiedObject):
    """General purpose information for name and other information to contact people."""

    __slots__ = (
        "_customer",
        "_roles",
        "electronic_address",
        "first_name",
        "landline_phone",
        "last_name",
        "m_name",
        "mobile_phone",
        "prefix",
        "special_need",
        "suffix",
    )

    last_name: str | None
    first_name: str | None
    m_name: str | None
    landline_phone: TelephoneNumber | None
    mobile_phone: TelephoneNumber | None
    electronic_address: ElectronicAddress | None
    special_need: str | None
    prefix: str | None
    suffix: str | None

    roles: Many[PersonRole] = Many(
        EndMeta(
            name="roles",
            cim_role="Roles",
            target="cim_python_sdk.model.iec61968.common.person_role:PersonRole",
            many=True,
            lower=0,
            upper=None,
            inverse="person",
            aggregation="none",
        )
    )
    customer: Many[Customer] = Many(
        EndMeta(
            name="customer",
            cim_role="Customer",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=True,
            lower=0,
            upper=None,
            inverse="person",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Person",
        package="TC57CIM/IEC61968/Common",
        guid="{29202C3E-E050-443e-A5FA-F139D34A26F6}",
        attributes=(
            AttrMeta("last_name", "lastName", "str", 0, 1, "primitive"),
            AttrMeta("first_name", "firstName", "str", 0, 1, "primitive"),
            AttrMeta("m_name", "mName", "str", 0, 1, "primitive"),
            AttrMeta("landline_phone", "landlinePhone", "TelephoneNumber", 0, 1, "compound"),
            AttrMeta("mobile_phone", "mobilePhone", "TelephoneNumber", 0, 1, "compound"),
            AttrMeta(
                "electronic_address", "electronicAddress", "ElectronicAddress", 0, 1, "compound"
            ),
            AttrMeta("special_need", "specialNeed", "str", 0, 1, "primitive"),
            AttrMeta("prefix", "prefix", "str", 0, 1, "primitive"),
            AttrMeta("suffix", "suffix", "str", 0, 1, "primitive"),
        ),
        ends=(
            roles.meta,
            customer.meta,
        ),
    )

    def __init__(
        self,
        *,
        last_name: str | None = None,
        first_name: str | None = None,
        m_name: str | None = None,
        landline_phone: TelephoneNumber | None = None,
        mobile_phone: TelephoneNumber | None = None,
        electronic_address: ElectronicAddress | None = None,
        special_need: str | None = None,
        prefix: str | None = None,
        suffix: str | None = None,
        roles: Iterable[PersonRole] | None = None,
        customer: Iterable[Customer] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.last_name = last_name
        self.first_name = first_name
        self.m_name = m_name
        self.landline_phone = landline_phone
        self.mobile_phone = mobile_phone
        self.electronic_address = electronic_address
        self.special_need = special_need
        self.prefix = prefix
        self.suffix = suffix
        if roles is not None:
            Person.roles.extend(self, roles)
        if customer is not None:
            Person.customer.extend(self, customer)

    def add_role(self, role: PersonRole) -> Self:
        return Person.roles.add(self, role)

    def remove_role(self, role: PersonRole) -> Self:
        return Person.roles.remove(self, role)

    def clear_roles(self) -> Self:
        return Person.roles.clear(self)

    def num_role(self) -> int:
        return Person.roles.count(self)

    def get_role_by_mrid(self, mrid: str) -> PersonRole | None:
        return Person.roles.get_by_mrid(self, mrid)

    def add_customer(self, customer: Customer) -> Self:
        return Person.customer.add(self, customer)

    def remove_customer(self, customer: Customer) -> Self:
        return Person.customer.remove(self, customer)

    def clear_customer(self) -> Self:
        return Person.customer.clear(self)

    def num_customer(self) -> int:
        return Person.customer.count(self)

    def get_customer_by_mrid(self, mrid: str) -> Customer | None:
        return Person.customer.get_by_mrid(self, mrid)
