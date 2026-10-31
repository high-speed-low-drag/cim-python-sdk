"""CIM class MarketStatementLineItem (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute import (
        MktUserAttribute,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement import (
        MarketStatement,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pass_through_bill import (
        PassThroughBill,
    )


class MarketStatementLineItem(IdentifiedObject):
    """An individual line item on an ISO settlement statement."""

    __slots__ = (
        "_component_market_statement_line_item",
        "_container_market_statement_line_item",
        "_market_statement",
        "_mkt_user_attribute",
        "_pass_through_bill",
        "current_amount",
        "current_iso_amount",
        "current_iso_quantity",
        "current_price",
        "current_quantity",
        "interval_date",
        "interval_number",
        "net_amount",
        "net_iso_amount",
        "net_iso_quantity",
        "net_price",
        "net_quantity",
        "previous_amount",
        "previous_iso_amount",
        "previous_iso_quantity",
        "previous_price",
        "previous_quantity",
        "quantity_uom",
    )

    current_amount: float | None
    current_iso_amount: float | None
    current_iso_quantity: float | None
    current_price: float | None
    current_quantity: float | None
    interval_date: _dt.datetime | None
    interval_number: str | None
    net_amount: float | None
    net_iso_amount: float | None
    net_iso_quantity: float | None
    net_price: float | None
    net_quantity: float | None
    previous_amount: float | None
    previous_iso_amount: float | None
    previous_iso_quantity: float | None
    previous_price: float | None
    previous_quantity: float | None
    quantity_uom: str | None

    container_market_statement_line_item: One[MarketStatementLineItem] = One(
        EndMeta(
            name="container_market_statement_line_item",
            cim_role="ContainerMarketStatementLineItem",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement_line_item:MarketStatementLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="component_market_statement_line_item",
            aggregation="none",
        )
    )
    component_market_statement_line_item: Many[MarketStatementLineItem] = Many(
        EndMeta(
            name="component_market_statement_line_item",
            cim_role="ComponentMarketStatementLineItem",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement_line_item:MarketStatementLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="container_market_statement_line_item",
            aggregation="none",
        )
    )
    pass_through_bill: One[PassThroughBill] = One(
        EndMeta(
            name="pass_through_bill",
            cim_role="PassThroughBill",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pass_through_bill:PassThroughBill",
            many=False,
            lower=0,
            upper=1,
            inverse="market_statement_line_item",
            aggregation="none",
        )
    )
    market_statement: One[MarketStatement] = One(
        EndMeta(
            name="market_statement",
            cim_role="MarketStatement",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement:MarketStatement",
            many=False,
            lower=1,
            upper=1,
            inverse="market_statement_line_item",
            aggregation="none",
        )
    )
    mkt_user_attribute: Many[MktUserAttribute] = Many(
        EndMeta(
            name="mkt_user_attribute",
            cim_role="MktUserAttribute",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute:MktUserAttribute",
            many=True,
            lower=0,
            upper=None,
            inverse="market_statement_line_item",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketStatementLineItem",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{8EEFD522-B659-4b02-AA47-9D57996FACCF}",
        attributes=(
            AttrMeta("current_amount", "currentAmount", "float", 0, 1, "primitive"),
            AttrMeta("current_iso_amount", "currentISOAmount", "float", 0, 1, "primitive"),
            AttrMeta("current_iso_quantity", "currentISOQuantity", "float", 0, 1, "primitive"),
            AttrMeta("current_price", "currentPrice", "float", 0, 1, "primitive"),
            AttrMeta("current_quantity", "currentQuantity", "float", 0, 1, "primitive"),
            AttrMeta("interval_date", "intervalDate", "datetime", 0, 1, "primitive"),
            AttrMeta("interval_number", "intervalNumber", "str", 0, 1, "primitive"),
            AttrMeta("net_amount", "netAmount", "float", 0, 1, "primitive"),
            AttrMeta("net_iso_amount", "netISOAmount", "float", 0, 1, "primitive"),
            AttrMeta("net_iso_quantity", "netISOQuantity", "float", 0, 1, "primitive"),
            AttrMeta("net_price", "netPrice", "float", 0, 1, "primitive"),
            AttrMeta("net_quantity", "netQuantity", "float", 0, 1, "primitive"),
            AttrMeta("previous_amount", "previousAmount", "float", 0, 1, "primitive"),
            AttrMeta("previous_iso_amount", "previousISOAmount", "float", 0, 1, "primitive"),
            AttrMeta("previous_iso_quantity", "previousISOQuantity", "float", 0, 1, "primitive"),
            AttrMeta("previous_price", "previousPrice", "float", 0, 1, "primitive"),
            AttrMeta("previous_quantity", "previousQuantity", "float", 0, 1, "primitive"),
            AttrMeta("quantity_uom", "quantityUOM", "str", 0, 1, "primitive"),
        ),
        ends=(
            container_market_statement_line_item.meta,
            component_market_statement_line_item.meta,
            pass_through_bill.meta,
            market_statement.meta,
            mkt_user_attribute.meta,
        ),
    )

    def __init__(
        self,
        *,
        current_amount: float | None = None,
        current_iso_amount: float | None = None,
        current_iso_quantity: float | None = None,
        current_price: float | None = None,
        current_quantity: float | None = None,
        interval_date: _dt.datetime | None = None,
        interval_number: str | None = None,
        net_amount: float | None = None,
        net_iso_amount: float | None = None,
        net_iso_quantity: float | None = None,
        net_price: float | None = None,
        net_quantity: float | None = None,
        previous_amount: float | None = None,
        previous_iso_amount: float | None = None,
        previous_iso_quantity: float | None = None,
        previous_price: float | None = None,
        previous_quantity: float | None = None,
        quantity_uom: str | None = None,
        container_market_statement_line_item: MarketStatementLineItem | None = None,
        component_market_statement_line_item: Iterable[MarketStatementLineItem] | None = None,
        pass_through_bill: PassThroughBill | None = None,
        market_statement: MarketStatement | None = None,
        mkt_user_attribute: Iterable[MktUserAttribute] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.current_amount = current_amount
        self.current_iso_amount = current_iso_amount
        self.current_iso_quantity = current_iso_quantity
        self.current_price = current_price
        self.current_quantity = current_quantity
        self.interval_date = interval_date
        self.interval_number = interval_number
        self.net_amount = net_amount
        self.net_iso_amount = net_iso_amount
        self.net_iso_quantity = net_iso_quantity
        self.net_price = net_price
        self.net_quantity = net_quantity
        self.previous_amount = previous_amount
        self.previous_iso_amount = previous_iso_amount
        self.previous_iso_quantity = previous_iso_quantity
        self.previous_price = previous_price
        self.previous_quantity = previous_quantity
        self.quantity_uom = quantity_uom
        if container_market_statement_line_item is not None:
            self.container_market_statement_line_item = container_market_statement_line_item
        if component_market_statement_line_item is not None:
            MarketStatementLineItem.component_market_statement_line_item.extend(
                self, component_market_statement_line_item
            )
        if pass_through_bill is not None:
            self.pass_through_bill = pass_through_bill
        if market_statement is not None:
            self.market_statement = market_statement
        if mkt_user_attribute is not None:
            MarketStatementLineItem.mkt_user_attribute.extend(self, mkt_user_attribute)

    def add_component_market_statement_line_item(
        self, component_market_statement_line_item: MarketStatementLineItem
    ) -> Self:
        return MarketStatementLineItem.component_market_statement_line_item.add(
            self, component_market_statement_line_item
        )

    def remove_component_market_statement_line_item(
        self, component_market_statement_line_item: MarketStatementLineItem
    ) -> Self:
        return MarketStatementLineItem.component_market_statement_line_item.remove(
            self, component_market_statement_line_item
        )

    def clear_component_market_statement_line_item(self) -> Self:
        return MarketStatementLineItem.component_market_statement_line_item.clear(self)

    def num_component_market_statement_line_item(self) -> int:
        return MarketStatementLineItem.component_market_statement_line_item.count(self)

    def get_component_market_statement_line_item_by_mrid(
        self, mrid: str
    ) -> MarketStatementLineItem | None:
        return MarketStatementLineItem.component_market_statement_line_item.get_by_mrid(self, mrid)

    def add_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return MarketStatementLineItem.mkt_user_attribute.add(self, mkt_user_attribute)

    def remove_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return MarketStatementLineItem.mkt_user_attribute.remove(self, mkt_user_attribute)

    def clear_mkt_user_attribute(self) -> Self:
        return MarketStatementLineItem.mkt_user_attribute.clear(self)

    def num_mkt_user_attribute(self) -> int:
        return MarketStatementLineItem.mkt_user_attribute.count(self)
