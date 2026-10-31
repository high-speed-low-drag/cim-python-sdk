"""CIM class Bank (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.bank_account import BankAccount


class Bank(OrganisationRole):
    """Organisation that is a commercial bank, agency, or other institution that offers a
    similar service."""

    __slots__ = ("_bank_accounts", "bic", "iban")

    iban: str | None
    bic: str | None

    bank_accounts: Many[BankAccount] = Many(
        EndMeta(
            name="bank_accounts",
            cim_role="BankAccounts",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.bank_account:BankAccount",
            many=True,
            lower=0,
            upper=None,
            inverse="bank",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Bank",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{AA268BA3-B7CC-4f9b-9DFF-D1213564F804}",
        attributes=(
            AttrMeta("iban", "iban", "str", 0, 1, "primitive"),
            AttrMeta("bic", "bic", "str", 0, 1, "primitive"),
        ),
        ends=(bank_accounts.meta,),
    )

    def __init__(
        self,
        *,
        iban: str | None = None,
        bic: str | None = None,
        bank_accounts: Iterable[BankAccount] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.iban = iban
        self.bic = bic
        if bank_accounts is not None:
            Bank.bank_accounts.extend(self, bank_accounts)

    def add_bank_account(self, bank_account: BankAccount) -> Self:
        return Bank.bank_accounts.add(self, bank_account)

    def remove_bank_account(self, bank_account: BankAccount) -> Self:
        return Bank.bank_accounts.remove(self, bank_account)

    def clear_bank_accounts(self) -> Self:
        return Bank.bank_accounts.clear(self)

    def num_bank_account(self) -> int:
        return Bank.bank_accounts.count(self)

    def get_bank_account_by_mrid(self, mrid: str) -> BankAccount | None:
        return Bank.bank_accounts.get_by_mrid(self, mrid)
