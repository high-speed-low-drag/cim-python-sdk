"""CIM class VendorShift (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.payment_metering.shift import Shift

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.merchant_account import MerchantAccount
    from cim_python_sdk.model.iec61968.payment_metering.receipt import Receipt
    from cim_python_sdk.model.iec61968.payment_metering.transaction import Transaction
    from cim_python_sdk.model.iec61968.payment_metering.vendor import Vendor


class VendorShift(Shift):
    """The operating shift for a vendor during which the vendor may transact against the
    merchant's account. It aggregates transactions and receipts during the shift and
    periodically debits a merchant account. The totals in vendor shift should always be the
    sum of totals aggregated in all cashier shifts that were open under the particular
    vendor shift."""

    __slots__ = (
        "_merchant_account",
        "_receipts",
        "_transactions",
        "_vendor",
        "merchant_debit_amount",
        "posted",
    )

    merchant_debit_amount: _decimal.Decimal | None  # Money
    posted: bool | None

    merchant_account: One[MerchantAccount] = One(
        EndMeta(
            name="merchant_account",
            cim_role="MerchantAccount",
            target="cim_python_sdk.model.iec61968.payment_metering.merchant_account:MerchantAccount",
            many=False,
            lower=0,
            upper=1,
            inverse="vendor_shifts",
            aggregation="none",
        )
    )
    receipts: Many[Receipt] = Many(
        EndMeta(
            name="receipts",
            cim_role="Receipts",
            target="cim_python_sdk.model.iec61968.payment_metering.receipt:Receipt",
            many=True,
            lower=0,
            upper=None,
            inverse="vendor_shift",
            aggregation="none",
        )
    )
    vendor: One[Vendor] = One(
        EndMeta(
            name="vendor",
            cim_role="Vendor",
            target="cim_python_sdk.model.iec61968.payment_metering.vendor:Vendor",
            many=False,
            lower=0,
            upper=1,
            inverse="vendor_shifts",
            aggregation="none",
        )
    )
    transactions: Many[Transaction] = Many(
        EndMeta(
            name="transactions",
            cim_role="Transactions",
            target="cim_python_sdk.model.iec61968.payment_metering.transaction:Transaction",
            many=True,
            lower=0,
            upper=None,
            inverse="vendor_shift",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VendorShift",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{7B733E0A-EB0F-4e94-B638-9B140A883587}",
        attributes=(
            AttrMeta("merchant_debit_amount", "merchantDebitAmount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("posted", "posted", "bool", 0, 1, "primitive"),
        ),
        ends=(
            merchant_account.meta,
            receipts.meta,
            vendor.meta,
            transactions.meta,
        ),
    )

    def __init__(
        self,
        *,
        merchant_debit_amount: _decimal.Decimal | None = None,
        posted: bool | None = None,
        merchant_account: MerchantAccount | None = None,
        receipts: Iterable[Receipt] | None = None,
        vendor: Vendor | None = None,
        transactions: Iterable[Transaction] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.merchant_debit_amount = merchant_debit_amount
        self.posted = posted
        if merchant_account is not None:
            self.merchant_account = merchant_account
        if receipts is not None:
            VendorShift.receipts.extend(self, receipts)
        if vendor is not None:
            self.vendor = vendor
        if transactions is not None:
            VendorShift.transactions.extend(self, transactions)

    def add_receipt(self, receipt: Receipt) -> Self:
        return VendorShift.receipts.add(self, receipt)

    def remove_receipt(self, receipt: Receipt) -> Self:
        return VendorShift.receipts.remove(self, receipt)

    def clear_receipts(self) -> Self:
        return VendorShift.receipts.clear(self)

    def num_receipt(self) -> int:
        return VendorShift.receipts.count(self)

    def get_receipt_by_mrid(self, mrid: str) -> Receipt | None:
        return VendorShift.receipts.get_by_mrid(self, mrid)

    def add_transaction(self, transaction: Transaction) -> Self:
        return VendorShift.transactions.add(self, transaction)

    def remove_transaction(self, transaction: Transaction) -> Self:
        return VendorShift.transactions.remove(self, transaction)

    def clear_transactions(self) -> Self:
        return VendorShift.transactions.clear(self)

    def num_transaction(self) -> int:
        return VendorShift.transactions.count(self)

    def get_transaction_by_mrid(self, mrid: str) -> Transaction | None:
        return VendorShift.transactions.get_by_mrid(self, mrid)
