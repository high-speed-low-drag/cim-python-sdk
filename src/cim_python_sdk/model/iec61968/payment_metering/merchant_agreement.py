"""CIM class MerchantAgreement (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.agreement import Agreement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.merchant_account import MerchantAccount


class MerchantAgreement(Agreement):
    """A formal controlling contractual agreement between supplier and merchant, in terms of
    which the merchant is authorised to vend tokens and receipt payments on behalf of the
    supplier. The merchant is accountable to the supplier for revenue collected at point of
    sale."""

    __slots__ = ("_merchant_accounts",)

    merchant_accounts: Many[MerchantAccount] = Many(
        EndMeta(
            name="merchant_accounts",
            cim_role="MerchantAccounts",
            target="cim_python_sdk.model.iec61968.payment_metering.merchant_account:MerchantAccount",
            many=True,
            lower=0,
            upper=None,
            inverse="merchant_agreement",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MerchantAgreement",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{264A71E5-64A3-4977-BEE2-F571D4576C97}",
        ends=(merchant_accounts.meta,),
    )

    def __init__(
        self,
        *,
        merchant_accounts: Iterable[MerchantAccount] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if merchant_accounts is not None:
            MerchantAgreement.merchant_accounts.extend(self, merchant_accounts)

    def add_merchant_account(self, merchant_account: MerchantAccount) -> Self:
        return MerchantAgreement.merchant_accounts.add(self, merchant_account)

    def remove_merchant_account(self, merchant_account: MerchantAccount) -> Self:
        return MerchantAgreement.merchant_accounts.remove(self, merchant_account)

    def clear_merchant_accounts(self) -> Self:
        return MerchantAgreement.merchant_accounts.clear(self)

    def num_merchant_account(self) -> int:
        return MerchantAgreement.merchant_accounts.count(self)

    def get_merchant_account_by_mrid(self, mrid: str) -> MerchantAccount | None:
        return MerchantAgreement.merchant_accounts.get_by_mrid(self, mrid)
