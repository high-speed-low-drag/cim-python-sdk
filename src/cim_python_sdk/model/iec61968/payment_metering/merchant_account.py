"""CIM class MerchantAccount (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.merchant_agreement import MerchantAgreement
    from cim_python_sdk.model.iec61968.payment_metering.transactor import Transactor
    from cim_python_sdk.model.iec61968.payment_metering.vendor_shift import VendorShift


class MerchantAccount(Document):
    """The operating account controlled by merchant agreement, against which the vendor may
    vend tokens or receipt payments. Transactions via vendor shift debit the account and
    bank deposits via bank statement credit the account."""

    __slots__ = (
        "_merchant_agreement",
        "_transactors",
        "_vendor_shifts",
        "current_balance",
        "provisional_balance",
    )

    current_balance: _decimal.Decimal | None  # Money
    provisional_balance: _decimal.Decimal | None  # Money

    vendor_shifts: Many[VendorShift] = Many(
        EndMeta(
            name="vendor_shifts",
            cim_role="VendorShifts",
            target="cim_python_sdk.model.iec61968.payment_metering.vendor_shift:VendorShift",
            many=True,
            lower=0,
            upper=None,
            inverse="merchant_account",
            aggregation="none",
        )
    )
    transactors: Many[Transactor] = Many(
        EndMeta(
            name="transactors",
            cim_role="Transactors",
            target="cim_python_sdk.model.iec61968.payment_metering.transactor:Transactor",
            many=True,
            lower=0,
            upper=None,
            inverse="merchant_accounts",
            aggregation="none",
        )
    )
    merchant_agreement: One[MerchantAgreement] = One(
        EndMeta(
            name="merchant_agreement",
            cim_role="MerchantAgreement",
            target="cim_python_sdk.model.iec61968.payment_metering.merchant_agreement:MerchantAgreement",
            many=False,
            lower=0,
            upper=1,
            inverse="merchant_accounts",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MerchantAccount",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{9872E766-CD0F-47dc-A36A-0BA0E1A3DBBE}",
        attributes=(
            AttrMeta("current_balance", "currentBalance", "Money", 0, 1, "cimdatatype"),
            AttrMeta("provisional_balance", "provisionalBalance", "Money", 0, 1, "cimdatatype"),
        ),
        ends=(
            vendor_shifts.meta,
            transactors.meta,
            merchant_agreement.meta,
        ),
    )

    def __init__(
        self,
        *,
        current_balance: _decimal.Decimal | None = None,
        provisional_balance: _decimal.Decimal | None = None,
        vendor_shifts: Iterable[VendorShift] | None = None,
        transactors: Iterable[Transactor] | None = None,
        merchant_agreement: MerchantAgreement | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.current_balance = current_balance
        self.provisional_balance = provisional_balance
        if vendor_shifts is not None:
            MerchantAccount.vendor_shifts.extend(self, vendor_shifts)
        if transactors is not None:
            MerchantAccount.transactors.extend(self, transactors)
        if merchant_agreement is not None:
            self.merchant_agreement = merchant_agreement

    def add_vendor_shift(self, vendor_shift: VendorShift) -> Self:
        return MerchantAccount.vendor_shifts.add(self, vendor_shift)

    def remove_vendor_shift(self, vendor_shift: VendorShift) -> Self:
        return MerchantAccount.vendor_shifts.remove(self, vendor_shift)

    def clear_vendor_shifts(self) -> Self:
        return MerchantAccount.vendor_shifts.clear(self)

    def num_vendor_shift(self) -> int:
        return MerchantAccount.vendor_shifts.count(self)

    def get_vendor_shift_by_mrid(self, mrid: str) -> VendorShift | None:
        return MerchantAccount.vendor_shifts.get_by_mrid(self, mrid)

    def add_transactor(self, transactor: Transactor) -> Self:
        return MerchantAccount.transactors.add(self, transactor)

    def remove_transactor(self, transactor: Transactor) -> Self:
        return MerchantAccount.transactors.remove(self, transactor)

    def clear_transactors(self) -> Self:
        return MerchantAccount.transactors.clear(self)

    def num_transactor(self) -> int:
        return MerchantAccount.transactors.count(self)

    def get_transactor_by_mrid(self, mrid: str) -> Transactor | None:
        return MerchantAccount.transactors.get_by_mrid(self, mrid)
