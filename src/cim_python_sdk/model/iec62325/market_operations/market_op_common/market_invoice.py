"""CIM class MarketInvoice (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice_line_item import (
        MarketInvoiceLineItem,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mkt_account_kind import (
        MktAccountKind,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mkt_bill_media_kind import (
        MktBillMediaKind,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.major_charge_group import (
        MajorChargeGroup,
    )


class MarketInvoice(CimObject):
    """A roll up of invoice line items. The whole invoice has a due date and amount to be paid,
    with information such as customer, banks etc. being obtained through associations. The
    invoice roll up is based on individual line items that each contain amounts and
    descriptions for specific services or products."""

    __slots__ = (
        "_major_charge_group",
        "_market_invoice_line_items",
        "amount",
        "bill_media_kind",
        "due_date",
        "kind",
        "mailed_date",
        "pro_forma",
        "reference_number",
        "transaction_date_time",
        "transfer_type",
    )

    amount: _decimal.Decimal | None  # Money
    bill_media_kind: MktBillMediaKind | None
    due_date: _dt.date | None
    kind: MktAccountKind | None
    mailed_date: _dt.date | None
    pro_forma: bool | None
    reference_number: str | None
    transaction_date_time: _dt.datetime | None
    transfer_type: str | None

    market_invoice_line_items: Many[MarketInvoiceLineItem] = Many(
        EndMeta(
            name="market_invoice_line_items",
            cim_role="MarketInvoiceLineItems",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice_line_item:MarketInvoiceLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="market_invoice",
            aggregation="none",
        )
    )
    major_charge_group: Many[MajorChargeGroup] = Many(
        EndMeta(
            name="major_charge_group",
            cim_role="MajorChargeGroup",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.major_charge_group:MajorChargeGroup",
            many=True,
            lower=1,
            upper=None,
            inverse="market_invoice",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketInvoice",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{C70AF7F3-A8E2-4c10-A262-E5EC8388A555}",
        attributes=(
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("bill_media_kind", "billMediaKind", "MktBillMediaKind", 0, 1, "enumeration"),
            AttrMeta("due_date", "dueDate", "date", 0, 1, "primitive"),
            AttrMeta("kind", "kind", "MktAccountKind", 0, 1, "enumeration"),
            AttrMeta("mailed_date", "mailedDate", "date", 0, 1, "primitive"),
            AttrMeta("pro_forma", "proForma", "bool", 0, 1, "primitive"),
            AttrMeta("reference_number", "referenceNumber", "str", 0, 1, "primitive"),
            AttrMeta("transaction_date_time", "transactionDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("transfer_type", "transferType", "str", 0, 1, "primitive"),
        ),
        ends=(
            market_invoice_line_items.meta,
            major_charge_group.meta,
        ),
    )

    def __init__(
        self,
        *,
        amount: _decimal.Decimal | None = None,
        bill_media_kind: MktBillMediaKind | None = None,
        due_date: _dt.date | None = None,
        kind: MktAccountKind | None = None,
        mailed_date: _dt.date | None = None,
        pro_forma: bool | None = None,
        reference_number: str | None = None,
        transaction_date_time: _dt.datetime | None = None,
        transfer_type: str | None = None,
        market_invoice_line_items: Iterable[MarketInvoiceLineItem] | None = None,
        major_charge_group: Iterable[MajorChargeGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.amount = amount
        self.bill_media_kind = bill_media_kind
        self.due_date = due_date
        self.kind = kind
        self.mailed_date = mailed_date
        self.pro_forma = pro_forma
        self.reference_number = reference_number
        self.transaction_date_time = transaction_date_time
        self.transfer_type = transfer_type
        if market_invoice_line_items is not None:
            MarketInvoice.market_invoice_line_items.extend(self, market_invoice_line_items)
        if major_charge_group is not None:
            MarketInvoice.major_charge_group.extend(self, major_charge_group)

    def add_market_invoice_line_item(self, market_invoice_line_item: MarketInvoiceLineItem) -> Self:
        return MarketInvoice.market_invoice_line_items.add(self, market_invoice_line_item)

    def remove_market_invoice_line_item(
        self, market_invoice_line_item: MarketInvoiceLineItem
    ) -> Self:
        return MarketInvoice.market_invoice_line_items.remove(self, market_invoice_line_item)

    def clear_market_invoice_line_items(self) -> Self:
        return MarketInvoice.market_invoice_line_items.clear(self)

    def num_market_invoice_line_item(self) -> int:
        return MarketInvoice.market_invoice_line_items.count(self)

    def add_major_charge_group(self, major_charge_group: MajorChargeGroup) -> Self:
        return MarketInvoice.major_charge_group.add(self, major_charge_group)

    def remove_major_charge_group(self, major_charge_group: MajorChargeGroup) -> Self:
        return MarketInvoice.major_charge_group.remove(self, major_charge_group)

    def clear_major_charge_group(self) -> Self:
        return MarketInvoice.major_charge_group.clear(self)

    def num_major_charge_group(self) -> int:
        return MarketInvoice.major_charge_group.count(self)

    def get_major_charge_group_by_mrid(self, mrid: str) -> MajorChargeGroup | None:
        return MarketInvoice.major_charge_group.get_by_mrid(self, mrid)
