"""CIM class Transactor (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.merchant_account import MerchantAccount


class Transactor(IdentifiedObject):
    """The entity that ultimately executes the transaction and which is in control of the
    process; typically this is embodied in secure software running on a server that may
    employ secure hardware encryption devices for secure transaction processing."""

    __slots__ = ("_merchant_accounts",)

    merchant_accounts: Many[MerchantAccount] = Many(
        EndMeta(
            name="merchant_accounts",
            cim_role="MerchantAccounts",
            target="cim_python_sdk.model.iec61968.payment_metering.merchant_account:MerchantAccount",
            many=True,
            lower=0,
            upper=None,
            inverse="transactors",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Transactor",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{D0927466-4532-44e7-803B-1F7FE1D7CC44}",
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
            Transactor.merchant_accounts.extend(self, merchant_accounts)

    def add_merchant_account(self, merchant_account: MerchantAccount) -> Self:
        return Transactor.merchant_accounts.add(self, merchant_account)

    def remove_merchant_account(self, merchant_account: MerchantAccount) -> Self:
        return Transactor.merchant_accounts.remove(self, merchant_account)

    def clear_merchant_accounts(self) -> Self:
        return Transactor.merchant_accounts.clear(self)

    def num_merchant_account(self) -> int:
        return Transactor.merchant_accounts.count(self)

    def get_merchant_account_by_mrid(self, mrid: str) -> MerchantAccount | None:
        return Transactor.merchant_accounts.get_by_mrid(self, mrid)
