"""CIM class PassThroughBill (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.domain.float_quantity import FloatQuantity
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute import (
        MktUserAttribute,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile import (
        ChargeProfile,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement_line_item import (
        MarketStatementLineItem,
    )


class PassThroughBill(Document):
    """Pass Through Bill is used for:

    1)Two sided charge transactions with or without ISO involvement

    2) Specific direct charges or payments that are calculated outside or provided directly
    to settlements

    3) Specific charge bill determinants that are externally supplied and used in charge
    calculations"""

    __slots__ = (
        "_charge_profiles",
        "_market_statement_line_item",
        "_mkt_user_attribute",
        "adjusted_amount",
        "amount",
        "bill_end",
        "bill_run_type",
        "bill_start",
        "billed_to",
        "effective_date",
        "is_disputed",
        "is_profiled",
        "paid_to",
        "previous_end",
        "previous_start",
        "price",
        "product_code",
        "provided_by",
        "quantity",
        "service_end",
        "service_start",
        "sold_to",
        "tax_amount",
        "time_zone",
        "trade_date",
        "transaction_date",
        "transaction_type",
    )

    adjusted_amount: _decimal.Decimal | None  # Money
    amount: _decimal.Decimal | None  # Money
    billed_to: str | None
    bill_end: _dt.datetime | None
    bill_run_type: str | None
    bill_start: _dt.datetime | None
    effective_date: _dt.datetime | None
    is_disputed: bool | None
    is_profiled: bool | None
    paid_to: str | None
    previous_end: _dt.datetime | None
    previous_start: _dt.datetime | None
    price: _decimal.Decimal | None  # Money
    product_code: str | None
    provided_by: str | None
    quantity: FloatQuantity | None
    service_end: _dt.datetime | None
    service_start: _dt.datetime | None
    sold_to: str | None
    tax_amount: _decimal.Decimal | None  # Money
    time_zone: str | None
    trade_date: _dt.datetime | None
    transaction_date: _dt.datetime | None
    transaction_type: str | None

    charge_profiles: Many[ChargeProfile] = Many(
        EndMeta(
            name="charge_profiles",
            cim_role="ChargeProfiles",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile:ChargeProfile",
            many=True,
            lower=0,
            upper=None,
            inverse="pass_trough_bill",
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
            inverse="pass_through_bill",
            aggregation="none",
        )
    )
    market_statement_line_item: One[MarketStatementLineItem] = One(
        EndMeta(
            name="market_statement_line_item",
            cim_role="MarketStatementLineItem",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement_line_item:MarketStatementLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="pass_through_bill",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PassThroughBill",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{06D05CC2-7BD1-4561-8C77-80ED631F22EC}",
        attributes=(
            AttrMeta("adjusted_amount", "adjustedAmount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("billed_to", "billedTo", "str", 0, 1, "primitive"),
            AttrMeta("bill_end", "billEnd", "datetime", 0, 1, "primitive"),
            AttrMeta("bill_run_type", "billRunType", "str", 0, 1, "primitive"),
            AttrMeta("bill_start", "billStart", "datetime", 0, 1, "primitive"),
            AttrMeta("effective_date", "effectiveDate", "datetime", 0, 1, "primitive"),
            AttrMeta("is_disputed", "isDisputed", "bool", 0, 1, "primitive"),
            AttrMeta("is_profiled", "isProfiled", "bool", 0, 1, "primitive"),
            AttrMeta("paid_to", "paidTo", "str", 0, 1, "primitive"),
            AttrMeta("previous_end", "previousEnd", "datetime", 0, 1, "primitive"),
            AttrMeta("previous_start", "previousStart", "datetime", 0, 1, "primitive"),
            AttrMeta("price", "price", "Money", 0, 1, "cimdatatype"),
            AttrMeta("product_code", "productCode", "str", 0, 1, "primitive"),
            AttrMeta("provided_by", "providedBy", "str", 0, 1, "primitive"),
            AttrMeta("quantity", "quantity", "FloatQuantity", 0, 1, "compound"),
            AttrMeta("service_end", "serviceEnd", "datetime", 0, 1, "primitive"),
            AttrMeta("service_start", "serviceStart", "datetime", 0, 1, "primitive"),
            AttrMeta("sold_to", "soldTo", "str", 0, 1, "primitive"),
            AttrMeta("tax_amount", "taxAmount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("time_zone", "timeZone", "str", 0, 1, "primitive"),
            AttrMeta("trade_date", "tradeDate", "datetime", 0, 1, "primitive"),
            AttrMeta("transaction_date", "transactionDate", "datetime", 0, 1, "primitive"),
            AttrMeta("transaction_type", "transactionType", "str", 0, 1, "primitive"),
        ),
        ends=(
            charge_profiles.meta,
            mkt_user_attribute.meta,
            market_statement_line_item.meta,
        ),
    )

    def __init__(
        self,
        *,
        adjusted_amount: _decimal.Decimal | None = None,
        amount: _decimal.Decimal | None = None,
        billed_to: str | None = None,
        bill_end: _dt.datetime | None = None,
        bill_run_type: str | None = None,
        bill_start: _dt.datetime | None = None,
        effective_date: _dt.datetime | None = None,
        is_disputed: bool | None = None,
        is_profiled: bool | None = None,
        paid_to: str | None = None,
        previous_end: _dt.datetime | None = None,
        previous_start: _dt.datetime | None = None,
        price: _decimal.Decimal | None = None,
        product_code: str | None = None,
        provided_by: str | None = None,
        quantity: FloatQuantity | None = None,
        service_end: _dt.datetime | None = None,
        service_start: _dt.datetime | None = None,
        sold_to: str | None = None,
        tax_amount: _decimal.Decimal | None = None,
        time_zone: str | None = None,
        trade_date: _dt.datetime | None = None,
        transaction_date: _dt.datetime | None = None,
        transaction_type: str | None = None,
        charge_profiles: Iterable[ChargeProfile] | None = None,
        mkt_user_attribute: Iterable[MktUserAttribute] | None = None,
        market_statement_line_item: MarketStatementLineItem | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.adjusted_amount = adjusted_amount
        self.amount = amount
        self.billed_to = billed_to
        self.bill_end = bill_end
        self.bill_run_type = bill_run_type
        self.bill_start = bill_start
        self.effective_date = effective_date
        self.is_disputed = is_disputed
        self.is_profiled = is_profiled
        self.paid_to = paid_to
        self.previous_end = previous_end
        self.previous_start = previous_start
        self.price = price
        self.product_code = product_code
        self.provided_by = provided_by
        self.quantity = quantity
        self.service_end = service_end
        self.service_start = service_start
        self.sold_to = sold_to
        self.tax_amount = tax_amount
        self.time_zone = time_zone
        self.trade_date = trade_date
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        if charge_profiles is not None:
            PassThroughBill.charge_profiles.extend(self, charge_profiles)
        if mkt_user_attribute is not None:
            PassThroughBill.mkt_user_attribute.extend(self, mkt_user_attribute)
        if market_statement_line_item is not None:
            self.market_statement_line_item = market_statement_line_item

    def add_charge_profile(self, charge_profile: ChargeProfile) -> Self:
        return PassThroughBill.charge_profiles.add(self, charge_profile)

    def remove_charge_profile(self, charge_profile: ChargeProfile) -> Self:
        return PassThroughBill.charge_profiles.remove(self, charge_profile)

    def clear_charge_profiles(self) -> Self:
        return PassThroughBill.charge_profiles.clear(self)

    def num_charge_profile(self) -> int:
        return PassThroughBill.charge_profiles.count(self)

    def get_charge_profile_by_mrid(self, mrid: str) -> ChargeProfile | None:
        return PassThroughBill.charge_profiles.get_by_mrid(self, mrid)

    def add_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return PassThroughBill.mkt_user_attribute.add(self, mkt_user_attribute)

    def remove_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return PassThroughBill.mkt_user_attribute.remove(self, mkt_user_attribute)

    def clear_mkt_user_attribute(self) -> Self:
        return PassThroughBill.mkt_user_attribute.clear(self)

    def num_mkt_user_attribute(self) -> int:
        return PassThroughBill.mkt_user_attribute.count(self)
