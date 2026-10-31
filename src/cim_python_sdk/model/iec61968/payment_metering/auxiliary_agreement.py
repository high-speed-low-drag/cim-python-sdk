"""CIM class AuxiliaryAgreement (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.agreement import Agreement

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.payment_metering.auxiliary_account import AuxiliaryAccount


class AuxiliaryAgreement(Agreement):
    """An ad-hoc auxiliary account agreement associated with a customer agreement, not part of
    the customer's account, but typically subject to formal agreement between customer and
    supplier (utility). Typically this is used to collect revenue owed by the customer for
    other services or arrears accrued with the utility for other services. It is typically
    linked to a prepaid token purchase transaction, thus forcing the customer to make a
    payment towards settlement of the auxiliary account balance whenever the customer needs
    to purchase a prepaid token for electricity.

    The present status of the auxiliary agreement can be defined in the context of the
    utility's business rules, for example: enabled, disabled, pending, over recovered, under
    recovered, written off, etc."""

    __slots__ = (
        "_auxiliary_accounts",
        "_customer_agreement",
        "arrears_interest",
        "aux_cycle",
        "aux_priority_code",
        "fixed_amount",
        "min_amount",
        "pay_cycle",
        "sub_type",
        "vend_portion",
        "vend_portion_arrear",
    )

    sub_type: str | None
    aux_cycle: str | None
    aux_priority_code: str | None
    arrears_interest: float | None  # PerCent
    pay_cycle: str | None
    min_amount: _decimal.Decimal | None  # Money
    vend_portion: float | None  # PerCent
    vend_portion_arrear: float | None  # PerCent
    fixed_amount: _decimal.Decimal | None  # Money

    auxiliary_accounts: Many[AuxiliaryAccount] = Many(
        EndMeta(
            name="auxiliary_accounts",
            cim_role="AuxiliaryAccounts",
            target="cim_python_sdk.model.iec61968.payment_metering.auxiliary_account:AuxiliaryAccount",
            many=True,
            lower=1,
            upper=None,
            inverse="auxiliary_agreement",
            aggregation="none",
        )
    )
    customer_agreement: One[CustomerAgreement] = One(
        EndMeta(
            name="customer_agreement",
            cim_role="CustomerAgreement",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=False,
            lower=0,
            upper=1,
            inverse="auxiliary_agreements",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AuxiliaryAgreement",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{6ED1E240-5AEA-4247-955F-B05AC035D644}",
        attributes=(
            AttrMeta("sub_type", "subType", "str", 0, 1, "primitive"),
            AttrMeta("aux_cycle", "auxCycle", "str", 0, 1, "primitive"),
            AttrMeta("aux_priority_code", "auxPriorityCode", "str", 0, 1, "primitive"),
            AttrMeta("arrears_interest", "arrearsInterest", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("pay_cycle", "payCycle", "str", 0, 1, "primitive"),
            AttrMeta("min_amount", "minAmount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("vend_portion", "vendPortion", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("vend_portion_arrear", "vendPortionArrear", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("fixed_amount", "fixedAmount", "Money", 0, 1, "cimdatatype"),
        ),
        ends=(
            auxiliary_accounts.meta,
            customer_agreement.meta,
        ),
    )

    def __init__(
        self,
        *,
        sub_type: str | None = None,
        aux_cycle: str | None = None,
        aux_priority_code: str | None = None,
        arrears_interest: float | None = None,
        pay_cycle: str | None = None,
        min_amount: _decimal.Decimal | None = None,
        vend_portion: float | None = None,
        vend_portion_arrear: float | None = None,
        fixed_amount: _decimal.Decimal | None = None,
        auxiliary_accounts: Iterable[AuxiliaryAccount] | None = None,
        customer_agreement: CustomerAgreement | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sub_type = sub_type
        self.aux_cycle = aux_cycle
        self.aux_priority_code = aux_priority_code
        self.arrears_interest = arrears_interest
        self.pay_cycle = pay_cycle
        self.min_amount = min_amount
        self.vend_portion = vend_portion
        self.vend_portion_arrear = vend_portion_arrear
        self.fixed_amount = fixed_amount
        if auxiliary_accounts is not None:
            AuxiliaryAgreement.auxiliary_accounts.extend(self, auxiliary_accounts)
        if customer_agreement is not None:
            self.customer_agreement = customer_agreement

    def add_auxiliary_account(self, auxiliary_account: AuxiliaryAccount) -> Self:
        return AuxiliaryAgreement.auxiliary_accounts.add(self, auxiliary_account)

    def remove_auxiliary_account(self, auxiliary_account: AuxiliaryAccount) -> Self:
        return AuxiliaryAgreement.auxiliary_accounts.remove(self, auxiliary_account)

    def clear_auxiliary_accounts(self) -> Self:
        return AuxiliaryAgreement.auxiliary_accounts.clear(self)

    def num_auxiliary_account(self) -> int:
        return AuxiliaryAgreement.auxiliary_accounts.count(self)

    def get_auxiliary_account_by_mrid(self, mrid: str) -> AuxiliaryAccount | None:
        return AuxiliaryAgreement.auxiliary_accounts.get_by_mrid(self, mrid)
