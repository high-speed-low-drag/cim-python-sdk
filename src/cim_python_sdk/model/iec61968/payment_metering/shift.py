"""CIM class Shift (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from typing import Any

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class Shift(IdentifiedObject):
    """Generally referring to a period of operation or work performed. Whether the shift is
    open/closed can be derived from attributes 'activityInterval.start' and
    'activityInterval.end'.

    The grand total for receipts (i.e., cumulative total of all actual receipted amounts
    during this shift; bankable + non-bankable; excludes rounding error totals) can be
    derived from receipt:

    =sum('Receipt.receiptAmount'); includes bankable and non-bankable receipts.

    It also has to be reconciled against:

    =sum('receiptsGrandTotalBankable' + 'receiptsGrandTotalNonBankable')

    and against receipt summary:

    =sum('ReceiptSummary.receiptsTotal').

    The attributes with "GrandTotal" defined in this class may need to be used when the
    source data is periodically flushed from the system and then these cannot be derived."""

    __slots__ = (
        "activity_interval",
        "receipts_grand_total_bankable",
        "receipts_grand_total_non_bankable",
        "receipts_grand_total_rounding",
        "transactions_grand_total",
        "transactions_grand_total_rounding",
    )

    activity_interval: DateTimeInterval | None
    receipts_grand_total_bankable: _decimal.Decimal | None  # Money
    receipts_grand_total_non_bankable: _decimal.Decimal | None  # Money
    receipts_grand_total_rounding: _decimal.Decimal | None  # Money
    transactions_grand_total: _decimal.Decimal | None  # Money
    transactions_grand_total_rounding: _decimal.Decimal | None  # Money

    _cim_meta = ClassMeta(
        cim_name="Shift",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{12465F6E-EA5E-4a9e-AEA0-FDD1E2F30E49}",
        attributes=(
            AttrMeta("activity_interval", "activityInterval", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta(
                "receipts_grand_total_bankable",
                "receiptsGrandTotalBankable",
                "Money",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "receipts_grand_total_non_bankable",
                "receiptsGrandTotalNonBankable",
                "Money",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "receipts_grand_total_rounding",
                "receiptsGrandTotalRounding",
                "Money",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "transactions_grand_total", "transactionsGrandTotal", "Money", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "transactions_grand_total_rounding",
                "transactionsGrandTotalRounding",
                "Money",
                0,
                1,
                "cimdatatype",
            ),
        ),
    )

    def __init__(
        self,
        *,
        activity_interval: DateTimeInterval | None = None,
        receipts_grand_total_bankable: _decimal.Decimal | None = None,
        receipts_grand_total_non_bankable: _decimal.Decimal | None = None,
        receipts_grand_total_rounding: _decimal.Decimal | None = None,
        transactions_grand_total: _decimal.Decimal | None = None,
        transactions_grand_total_rounding: _decimal.Decimal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.activity_interval = activity_interval
        self.receipts_grand_total_bankable = receipts_grand_total_bankable
        self.receipts_grand_total_non_bankable = receipts_grand_total_non_bankable
        self.receipts_grand_total_rounding = receipts_grand_total_rounding
        self.transactions_grand_total = transactions_grand_total
        self.transactions_grand_total_rounding = transactions_grand_total_rounding
