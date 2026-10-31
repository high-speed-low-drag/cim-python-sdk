"""CIM class ServiceSupplier (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.bank_account import BankAccount
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61968.payment_metering.supplier_kind import SupplierKind


class ServiceSupplier(OrganisationRole):
    """Organisation that provides services to customers."""

    __slots__ = (
        "_bank_accounts",
        "_customer_agreements",
        "_usage_points",
        "issuer_identification_number",
        "kind",
    )

    kind: SupplierKind | None
    issuer_identification_number: str | None

    customer_agreements: Many[CustomerAgreement] = Many(
        EndMeta(
            name="customer_agreements",
            cim_role="CustomerAgreements",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="service_supplier",
            aggregation="none",
        )
    )
    usage_points: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_points",
            cim_role="UsagePoints",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="service_supplier",
            aggregation="none",
        )
    )
    bank_accounts: Many[BankAccount] = Many(
        EndMeta(
            name="bank_accounts",
            cim_role="BankAccounts",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.bank_account:BankAccount",
            many=True,
            lower=0,
            upper=None,
            inverse="service_supplier",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ServiceSupplier",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{D521178C-D4CD-4701-9633-E658D9D812EC}",
        attributes=(
            AttrMeta("kind", "kind", "SupplierKind", 0, 1, "enumeration"),
            AttrMeta(
                "issuer_identification_number",
                "issuerIdentificationNumber",
                "str",
                0,
                1,
                "primitive",
            ),
        ),
        ends=(
            customer_agreements.meta,
            usage_points.meta,
            bank_accounts.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: SupplierKind | None = None,
        issuer_identification_number: str | None = None,
        customer_agreements: Iterable[CustomerAgreement] | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        bank_accounts: Iterable[BankAccount] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.issuer_identification_number = issuer_identification_number
        if customer_agreements is not None:
            ServiceSupplier.customer_agreements.extend(self, customer_agreements)
        if usage_points is not None:
            ServiceSupplier.usage_points.extend(self, usage_points)
        if bank_accounts is not None:
            ServiceSupplier.bank_accounts.extend(self, bank_accounts)

    def add_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return ServiceSupplier.customer_agreements.add(self, customer_agreement)

    def remove_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return ServiceSupplier.customer_agreements.remove(self, customer_agreement)

    def clear_customer_agreements(self) -> Self:
        return ServiceSupplier.customer_agreements.clear(self)

    def num_customer_agreement(self) -> int:
        return ServiceSupplier.customer_agreements.count(self)

    def get_customer_agreement_by_mrid(self, mrid: str) -> CustomerAgreement | None:
        return ServiceSupplier.customer_agreements.get_by_mrid(self, mrid)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return ServiceSupplier.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return ServiceSupplier.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return ServiceSupplier.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return ServiceSupplier.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return ServiceSupplier.usage_points.get_by_mrid(self, mrid)

    def add_bank_account(self, bank_account: BankAccount) -> Self:
        return ServiceSupplier.bank_accounts.add(self, bank_account)

    def remove_bank_account(self, bank_account: BankAccount) -> Self:
        return ServiceSupplier.bank_accounts.remove(self, bank_account)

    def clear_bank_accounts(self) -> Self:
        return ServiceSupplier.bank_accounts.clear(self)

    def num_bank_account(self) -> int:
        return ServiceSupplier.bank_accounts.count(self)

    def get_bank_account_by_mrid(self, mrid: str) -> BankAccount | None:
        return ServiceSupplier.bank_accounts.get_by_mrid(self, mrid)
