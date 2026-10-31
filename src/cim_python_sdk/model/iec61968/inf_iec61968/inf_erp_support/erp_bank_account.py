"""CIM class ErpBankAccount (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.bank_account import BankAccount

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ErpBankAccount(BankAccount):
    """Relationship under a particular name, usually evidenced by a deposit against which
    withdrawals can be made. Types of bank accounts include: demand, time, custodial, joint,
    trustee, corporate, special, and regular accounts.

    A statement of transactions during a fiscal period and the resulting balance is
    maintained on each account.

    For Payment metering, the account is associated with Bank and Supplier, reflecting
    details of the bank account used for depositing revenue collected by TokenVendor. The
    name of the account holder should be specified in 'name' attribute."""

    __slots__ = ("bank_aba",)

    bank_aba: str | None

    _cim_meta = ClassMeta(
        cim_name="ErpBankAccount",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{EFB4BC24-92B4-4912-B051-F7727578FA81}",
        attributes=(AttrMeta("bank_aba", "bankABA", "str", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        bank_aba: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bank_aba = bank_aba
