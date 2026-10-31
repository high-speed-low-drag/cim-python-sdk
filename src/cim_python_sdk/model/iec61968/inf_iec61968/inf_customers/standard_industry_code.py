"""CIM class StandardIndustryCode (TC57CIM/IEC61968/InfIEC61968/InfCustomers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement


class StandardIndustryCode(Document):
    """The Standard Industrial Classification (SIC) are the codes that identify the type of
    products/service an industry is involved in, and used for statutory reporting purposes.
    For example, in the USA these codes are located by the federal government, and then
    published in a book entitled "The Standard Industrial Classification Manual". The codes
    are arranged in a hierarchical structure.

    Note that Residential Service Agreements are not classified according to the SIC codes."""

    __slots__ = ("_customer_agreements", "code")

    code: str | None

    customer_agreements: Many[CustomerAgreement] = Many(
        EndMeta(
            name="customer_agreements",
            cim_role="CustomerAgreements",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="standard_industry_code",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StandardIndustryCode",
        package="TC57CIM/IEC61968/InfIEC61968/InfCustomers",
        guid="{4BD9C91C-E2EF-48fa-A6C2-A7E03669C29B}",
        attributes=(AttrMeta("code", "code", "str", 0, 1, "primitive"),),
        ends=(customer_agreements.meta,),
    )

    def __init__(
        self,
        *,
        code: str | None = None,
        customer_agreements: Iterable[CustomerAgreement] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.code = code
        if customer_agreements is not None:
            StandardIndustryCode.customer_agreements.extend(self, customer_agreements)

    def add_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return StandardIndustryCode.customer_agreements.add(self, customer_agreement)

    def remove_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return StandardIndustryCode.customer_agreements.remove(self, customer_agreement)

    def clear_customer_agreements(self) -> Self:
        return StandardIndustryCode.customer_agreements.clear(self)

    def num_customer_agreement(self) -> int:
        return StandardIndustryCode.customer_agreements.count(self)

    def get_customer_agreement_by_mrid(self, mrid: str) -> CustomerAgreement | None:
        return StandardIndustryCode.customer_agreements.get_by_mrid(self, mrid)
