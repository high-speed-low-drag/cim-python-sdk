"""CIM class MarketInvoiceLineItem (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice import (
        MarketInvoice,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.settlement import (
        Settlement,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mkt_invoice_line_item_kind import (
        MktInvoiceLineItemKind,
    )


class MarketInvoiceLineItem(CimObject):
    """An individual line item on an invoice."""

    __slots__ = (
        "_component_market_invoice_line_items",
        "_container_market_invoice_line_item",
        "_market_invoice",
        "_settlement",
        "bill_period",
        "gl_account",
        "gl_date_time",
        "kind",
        "line_amount",
        "line_number",
        "line_version",
        "net_amount",
        "previous_amount",
    )

    bill_period: DateTimeInterval | None
    gl_account: str | None
    gl_date_time: _dt.datetime | None
    kind: MktInvoiceLineItemKind | None
    line_amount: float | None
    line_number: str | None
    line_version: str | None
    net_amount: float | None
    previous_amount: float | None

    market_invoice: One[MarketInvoice] = One(
        EndMeta(
            name="market_invoice",
            cim_role="MarketInvoice",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice:MarketInvoice",
            many=False,
            lower=1,
            upper=1,
            inverse="market_invoice_line_items",
            aggregation="none",
        )
    )
    container_market_invoice_line_item: One[MarketInvoiceLineItem] = One(
        EndMeta(
            name="container_market_invoice_line_item",
            cim_role="ContainerMarketInvoiceLineItem",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice_line_item:MarketInvoiceLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="component_market_invoice_line_items",
            aggregation="none",
        )
    )
    component_market_invoice_line_items: Many[MarketInvoiceLineItem] = Many(
        EndMeta(
            name="component_market_invoice_line_items",
            cim_role="ComponentMarketInvoiceLineItems",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice_line_item:MarketInvoiceLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="container_market_invoice_line_item",
            aggregation="none",
        )
    )
    settlement: Many[Settlement] = Many(
        EndMeta(
            name="settlement",
            cim_role="Settlement",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.settlement:Settlement",
            many=True,
            lower=0,
            upper=None,
            inverse="market_invoice_line_item",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketInvoiceLineItem",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{E89C82DB-FA7B-4c33-88A7-065081AC01DF}",
        attributes=(
            AttrMeta("bill_period", "billPeriod", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("gl_account", "glAccount", "str", 0, 1, "primitive"),
            AttrMeta("gl_date_time", "glDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("kind", "kind", "MktInvoiceLineItemKind", 0, 1, "enumeration"),
            AttrMeta("line_amount", "lineAmount", "float", 0, 1, "primitive"),
            AttrMeta("line_number", "lineNumber", "str", 0, 1, "primitive"),
            AttrMeta("line_version", "lineVersion", "str", 0, 1, "primitive"),
            AttrMeta("net_amount", "netAmount", "float", 0, 1, "primitive"),
            AttrMeta("previous_amount", "previousAmount", "float", 0, 1, "primitive"),
        ),
        ends=(
            market_invoice.meta,
            container_market_invoice_line_item.meta,
            component_market_invoice_line_items.meta,
            settlement.meta,
        ),
    )

    def __init__(
        self,
        *,
        bill_period: DateTimeInterval | None = None,
        gl_account: str | None = None,
        gl_date_time: _dt.datetime | None = None,
        kind: MktInvoiceLineItemKind | None = None,
        line_amount: float | None = None,
        line_number: str | None = None,
        line_version: str | None = None,
        net_amount: float | None = None,
        previous_amount: float | None = None,
        market_invoice: MarketInvoice | None = None,
        container_market_invoice_line_item: MarketInvoiceLineItem | None = None,
        component_market_invoice_line_items: Iterable[MarketInvoiceLineItem] | None = None,
        settlement: Iterable[Settlement] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bill_period = bill_period
        self.gl_account = gl_account
        self.gl_date_time = gl_date_time
        self.kind = kind
        self.line_amount = line_amount
        self.line_number = line_number
        self.line_version = line_version
        self.net_amount = net_amount
        self.previous_amount = previous_amount
        if market_invoice is not None:
            self.market_invoice = market_invoice
        if container_market_invoice_line_item is not None:
            self.container_market_invoice_line_item = container_market_invoice_line_item
        if component_market_invoice_line_items is not None:
            MarketInvoiceLineItem.component_market_invoice_line_items.extend(
                self, component_market_invoice_line_items
            )
        if settlement is not None:
            MarketInvoiceLineItem.settlement.extend(self, settlement)

    def add_component_market_invoice_line_item(
        self, component_market_invoice_line_item: MarketInvoiceLineItem
    ) -> Self:
        return MarketInvoiceLineItem.component_market_invoice_line_items.add(
            self, component_market_invoice_line_item
        )

    def remove_component_market_invoice_line_item(
        self, component_market_invoice_line_item: MarketInvoiceLineItem
    ) -> Self:
        return MarketInvoiceLineItem.component_market_invoice_line_items.remove(
            self, component_market_invoice_line_item
        )

    def clear_component_market_invoice_line_items(self) -> Self:
        return MarketInvoiceLineItem.component_market_invoice_line_items.clear(self)

    def num_component_market_invoice_line_item(self) -> int:
        return MarketInvoiceLineItem.component_market_invoice_line_items.count(self)

    def add_settlement(self, settlement: Settlement) -> Self:
        return MarketInvoiceLineItem.settlement.add(self, settlement)

    def remove_settlement(self, settlement: Settlement) -> Self:
        return MarketInvoiceLineItem.settlement.remove(self, settlement)

    def clear_settlement(self) -> Self:
        return MarketInvoiceLineItem.settlement.clear(self)

    def num_settlement(self) -> int:
        return MarketInvoiceLineItem.settlement.count(self)

    def get_settlement_by_mrid(self, mrid: str) -> Settlement | None:
        return MarketInvoiceLineItem.settlement.get_by_mrid(self, mrid)
