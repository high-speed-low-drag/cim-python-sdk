"""CIM class Receipt (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.cashier_shift import CashierShift
    from cim_python_sdk.model.iec61968.payment_metering.line_detail import LineDetail
    from cim_python_sdk.model.iec61968.payment_metering.tender import Tender
    from cim_python_sdk.model.iec61968.payment_metering.transaction import Transaction
    from cim_python_sdk.model.iec61968.payment_metering.vendor_shift import VendorShift


class Receipt(IdentifiedObject):
    """Record of total receipted payment from customer."""

    __slots__ = (
        "_cashier_shift",
        "_tenders",
        "_transactions",
        "_vendor_shift",
        "is_bankable",
        "line",
    )

    is_bankable: bool | None
    line: LineDetail | None

    cashier_shift: One[CashierShift] = One(
        EndMeta(
            name="cashier_shift",
            cim_role="CashierShift",
            target="cim_python_sdk.model.iec61968.payment_metering.cashier_shift:CashierShift",
            many=False,
            lower=0,
            upper=1,
            inverse="receipts",
            aggregation="none",
        )
    )
    transactions: Many[Transaction] = Many(
        EndMeta(
            name="transactions",
            cim_role="Transactions",
            target="cim_python_sdk.model.iec61968.payment_metering.transaction:Transaction",
            many=True,
            lower=1,
            upper=None,
            inverse="receipt",
            aggregation="none",
        )
    )
    tenders: Many[Tender] = Many(
        EndMeta(
            name="tenders",
            cim_role="Tenders",
            target="cim_python_sdk.model.iec61968.payment_metering.tender:Tender",
            many=True,
            lower=1,
            upper=None,
            inverse="receipt",
            aggregation="none",
        )
    )
    vendor_shift: One[VendorShift] = One(
        EndMeta(
            name="vendor_shift",
            cim_role="VendorShift",
            target="cim_python_sdk.model.iec61968.payment_metering.vendor_shift:VendorShift",
            many=False,
            lower=0,
            upper=1,
            inverse="receipts",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Receipt",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{8C5F5500-4850-4997-A7C7-5C3B363E7049}",
        attributes=(
            AttrMeta("is_bankable", "isBankable", "bool", 0, 1, "primitive"),
            AttrMeta("line", "line", "LineDetail", 0, 1, "compound"),
        ),
        ends=(
            cashier_shift.meta,
            transactions.meta,
            tenders.meta,
            vendor_shift.meta,
        ),
    )

    def __init__(
        self,
        *,
        is_bankable: bool | None = None,
        line: LineDetail | None = None,
        cashier_shift: CashierShift | None = None,
        transactions: Iterable[Transaction] | None = None,
        tenders: Iterable[Tender] | None = None,
        vendor_shift: VendorShift | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_bankable = is_bankable
        self.line = line
        if cashier_shift is not None:
            self.cashier_shift = cashier_shift
        if transactions is not None:
            Receipt.transactions.extend(self, transactions)
        if tenders is not None:
            Receipt.tenders.extend(self, tenders)
        if vendor_shift is not None:
            self.vendor_shift = vendor_shift

    def add_transaction(self, transaction: Transaction) -> Self:
        return Receipt.transactions.add(self, transaction)

    def remove_transaction(self, transaction: Transaction) -> Self:
        return Receipt.transactions.remove(self, transaction)

    def clear_transactions(self) -> Self:
        return Receipt.transactions.clear(self)

    def num_transaction(self) -> int:
        return Receipt.transactions.count(self)

    def get_transaction_by_mrid(self, mrid: str) -> Transaction | None:
        return Receipt.transactions.get_by_mrid(self, mrid)

    def add_tender(self, tender: Tender) -> Self:
        return Receipt.tenders.add(self, tender)

    def remove_tender(self, tender: Tender) -> Self:
        return Receipt.tenders.remove(self, tender)

    def clear_tenders(self) -> Self:
        return Receipt.tenders.clear(self)

    def num_tender(self) -> int:
        return Receipt.tenders.count(self)

    def get_tender_by_mrid(self, mrid: str) -> Tender | None:
        return Receipt.tenders.get_by_mrid(self, mrid)
