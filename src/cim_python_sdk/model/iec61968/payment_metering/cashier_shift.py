"""CIM class CashierShift (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.payment_metering.shift import Shift

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.cashier import Cashier
    from cim_python_sdk.model.iec61968.payment_metering.point_of_sale import PointOfSale
    from cim_python_sdk.model.iec61968.payment_metering.receipt import Receipt
    from cim_python_sdk.model.iec61968.payment_metering.transaction import Transaction


class CashierShift(Shift):
    """The operating shift for a cashier, during which the cashier may transact against the
    cashier shift, subject to vendor shift being open."""

    __slots__ = ("_cashier", "_point_of_sale", "_receipts", "_transactions", "cash_float")

    cash_float: _decimal.Decimal | None  # Money

    transactions: Many[Transaction] = Many(
        EndMeta(
            name="transactions",
            cim_role="Transactions",
            target="cim_python_sdk.model.iec61968.payment_metering.transaction:Transaction",
            many=True,
            lower=0,
            upper=None,
            inverse="cashier_shift",
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
            inverse="cashier_shift",
            aggregation="none",
        )
    )
    point_of_sale: One[PointOfSale] = One(
        EndMeta(
            name="point_of_sale",
            cim_role="PointOfSale",
            target="cim_python_sdk.model.iec61968.payment_metering.point_of_sale:PointOfSale",
            many=False,
            lower=0,
            upper=1,
            inverse="cashier_shifts",
            aggregation="none",
        )
    )
    cashier: One[Cashier] = One(
        EndMeta(
            name="cashier",
            cim_role="Cashier",
            target="cim_python_sdk.model.iec61968.payment_metering.cashier:Cashier",
            many=False,
            lower=0,
            upper=1,
            inverse="cashier_shifts",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CashierShift",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{ED290EE7-433C-4457-977B-DF074546CBD3}",
        attributes=(AttrMeta("cash_float", "cashFloat", "Money", 0, 1, "cimdatatype"),),
        ends=(
            transactions.meta,
            receipts.meta,
            point_of_sale.meta,
            cashier.meta,
        ),
    )

    def __init__(
        self,
        *,
        cash_float: _decimal.Decimal | None = None,
        transactions: Iterable[Transaction] | None = None,
        receipts: Iterable[Receipt] | None = None,
        point_of_sale: PointOfSale | None = None,
        cashier: Cashier | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cash_float = cash_float
        if transactions is not None:
            CashierShift.transactions.extend(self, transactions)
        if receipts is not None:
            CashierShift.receipts.extend(self, receipts)
        if point_of_sale is not None:
            self.point_of_sale = point_of_sale
        if cashier is not None:
            self.cashier = cashier

    def add_transaction(self, transaction: Transaction) -> Self:
        return CashierShift.transactions.add(self, transaction)

    def remove_transaction(self, transaction: Transaction) -> Self:
        return CashierShift.transactions.remove(self, transaction)

    def clear_transactions(self) -> Self:
        return CashierShift.transactions.clear(self)

    def num_transaction(self) -> int:
        return CashierShift.transactions.count(self)

    def get_transaction_by_mrid(self, mrid: str) -> Transaction | None:
        return CashierShift.transactions.get_by_mrid(self, mrid)

    def add_receipt(self, receipt: Receipt) -> Self:
        return CashierShift.receipts.add(self, receipt)

    def remove_receipt(self, receipt: Receipt) -> Self:
        return CashierShift.receipts.remove(self, receipt)

    def clear_receipts(self) -> Self:
        return CashierShift.receipts.clear(self)

    def num_receipt(self) -> int:
        return CashierShift.receipts.count(self)

    def get_receipt_by_mrid(self, mrid: str) -> Receipt | None:
        return CashierShift.receipts.get_by_mrid(self, mrid)
