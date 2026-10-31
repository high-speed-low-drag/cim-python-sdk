"""CIM class AuxiliaryAccount (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.account_movement import AccountMovement
    from cim_python_sdk.model.iec61968.payment_metering.auxiliary_agreement import (
        AuxiliaryAgreement,
    )
    from cim_python_sdk.model.iec61968.payment_metering.charge import Charge
    from cim_python_sdk.model.iec61968.payment_metering.due import Due
    from cim_python_sdk.model.iec61968.payment_metering.transaction import Transaction


class AuxiliaryAccount(Document):
    """Variable and dynamic part of auxiliary agreement, generally representing the current
    state of the account related to the outstanding balance defined in auxiliary agreement."""

    __slots__ = (
        "_auxiliary_agreement",
        "_charges",
        "_payment_transactions",
        "balance",
        "due",
        "last_credit",
        "last_debit",
        "principle_amount",
    )

    principle_amount: _decimal.Decimal | None  # Money
    balance: _decimal.Decimal | None  # Money
    due: Due | None
    last_credit: AccountMovement | None
    last_debit: AccountMovement | None

    auxiliary_agreement: One[AuxiliaryAgreement] = One(
        EndMeta(
            name="auxiliary_agreement",
            cim_role="AuxiliaryAgreement",
            target="cim_python_sdk.model.iec61968.payment_metering.auxiliary_agreement:AuxiliaryAgreement",
            many=False,
            lower=0,
            upper=1,
            inverse="auxiliary_accounts",
            aggregation="none",
        )
    )
    charges: Many[Charge] = Many(
        EndMeta(
            name="charges",
            cim_role="Charges",
            target="cim_python_sdk.model.iec61968.payment_metering.charge:Charge",
            many=True,
            lower=0,
            upper=None,
            inverse="auxiliary_accounts",
            aggregation="none",
        )
    )
    payment_transactions: Many[Transaction] = Many(
        EndMeta(
            name="payment_transactions",
            cim_role="PaymentTransactions",
            target="cim_python_sdk.model.iec61968.payment_metering.transaction:Transaction",
            many=True,
            lower=0,
            upper=None,
            inverse="auxiliary_account",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AuxiliaryAccount",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{F1D6FA24-D6CF-42de-A657-421C3EA19A6F}",
        attributes=(
            AttrMeta("principle_amount", "principleAmount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("balance", "balance", "Money", 0, 1, "cimdatatype"),
            AttrMeta("due", "due", "Due", 0, 1, "compound"),
            AttrMeta("last_credit", "lastCredit", "AccountMovement", 0, 1, "compound"),
            AttrMeta("last_debit", "lastDebit", "AccountMovement", 0, 1, "compound"),
        ),
        ends=(
            auxiliary_agreement.meta,
            charges.meta,
            payment_transactions.meta,
        ),
    )

    def __init__(
        self,
        *,
        principle_amount: _decimal.Decimal | None = None,
        balance: _decimal.Decimal | None = None,
        due: Due | None = None,
        last_credit: AccountMovement | None = None,
        last_debit: AccountMovement | None = None,
        auxiliary_agreement: AuxiliaryAgreement | None = None,
        charges: Iterable[Charge] | None = None,
        payment_transactions: Iterable[Transaction] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.principle_amount = principle_amount
        self.balance = balance
        self.due = due
        self.last_credit = last_credit
        self.last_debit = last_debit
        if auxiliary_agreement is not None:
            self.auxiliary_agreement = auxiliary_agreement
        if charges is not None:
            AuxiliaryAccount.charges.extend(self, charges)
        if payment_transactions is not None:
            AuxiliaryAccount.payment_transactions.extend(self, payment_transactions)

    def add_charge(self, charge: Charge) -> Self:
        return AuxiliaryAccount.charges.add(self, charge)

    def remove_charge(self, charge: Charge) -> Self:
        return AuxiliaryAccount.charges.remove(self, charge)

    def clear_charges(self) -> Self:
        return AuxiliaryAccount.charges.clear(self)

    def num_charge(self) -> int:
        return AuxiliaryAccount.charges.count(self)

    def get_charge_by_mrid(self, mrid: str) -> Charge | None:
        return AuxiliaryAccount.charges.get_by_mrid(self, mrid)

    def add_payment_transaction(self, payment_transaction: Transaction) -> Self:
        return AuxiliaryAccount.payment_transactions.add(self, payment_transaction)

    def remove_payment_transaction(self, payment_transaction: Transaction) -> Self:
        return AuxiliaryAccount.payment_transactions.remove(self, payment_transaction)

    def clear_payment_transactions(self) -> Self:
        return AuxiliaryAccount.payment_transactions.clear(self)

    def num_payment_transaction(self) -> int:
        return AuxiliaryAccount.payment_transactions.count(self)

    def get_payment_transaction_by_mrid(self, mrid: str) -> Transaction | None:
        return AuxiliaryAccount.payment_transactions.get_by_mrid(self, mrid)
