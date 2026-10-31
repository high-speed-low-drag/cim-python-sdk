"""CIM class Settlement (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice_line_item import (
        MarketInvoiceLineItem,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.market_ledger_entry import (
        MarketLedgerEntry,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_plan.energy_market import (
        EnergyMarket,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.major_charge_group import (
        MajorChargeGroup,
    )


class Settlement(Document):
    """Specifies a settlement run."""

    __slots__ = (
        "_energy_market",
        "_major_charge_group",
        "_market_invoice_line_item",
        "_market_ledger_entry",
        "trade_date",
    )

    trade_date: _dt.datetime | None

    energy_market: One[EnergyMarket] = One(
        EndMeta(
            name="energy_market",
            cim_role="EnergyMarket",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.energy_market:EnergyMarket",
            many=False,
            lower=0,
            upper=1,
            inverse="settlements",
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
            inverse="settlement",
            aggregation="none",
        )
    )
    market_invoice_line_item: Many[MarketInvoiceLineItem] = Many(
        EndMeta(
            name="market_invoice_line_item",
            cim_role="MarketInvoiceLineItem",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice_line_item:MarketInvoiceLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="settlement",
            aggregation="none",
        )
    )
    market_ledger_entry: Many[MarketLedgerEntry] = Many(
        EndMeta(
            name="market_ledger_entry",
            cim_role="MarketLedgerEntry",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.market_ledger_entry:MarketLedgerEntry",
            many=True,
            lower=0,
            upper=None,
            inverse="settlement",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Settlement",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{C50E18F4-0D25-4f2c-AF5A-70E1851041B2}",
        attributes=(AttrMeta("trade_date", "tradeDate", "datetime", 0, 1, "primitive"),),
        ends=(
            energy_market.meta,
            major_charge_group.meta,
            market_invoice_line_item.meta,
            market_ledger_entry.meta,
        ),
    )

    def __init__(
        self,
        *,
        trade_date: _dt.datetime | None = None,
        energy_market: EnergyMarket | None = None,
        major_charge_group: Iterable[MajorChargeGroup] | None = None,
        market_invoice_line_item: Iterable[MarketInvoiceLineItem] | None = None,
        market_ledger_entry: Iterable[MarketLedgerEntry] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.trade_date = trade_date
        if energy_market is not None:
            self.energy_market = energy_market
        if major_charge_group is not None:
            Settlement.major_charge_group.extend(self, major_charge_group)
        if market_invoice_line_item is not None:
            Settlement.market_invoice_line_item.extend(self, market_invoice_line_item)
        if market_ledger_entry is not None:
            Settlement.market_ledger_entry.extend(self, market_ledger_entry)

    def add_major_charge_group(self, major_charge_group: MajorChargeGroup) -> Self:
        return Settlement.major_charge_group.add(self, major_charge_group)

    def remove_major_charge_group(self, major_charge_group: MajorChargeGroup) -> Self:
        return Settlement.major_charge_group.remove(self, major_charge_group)

    def clear_major_charge_group(self) -> Self:
        return Settlement.major_charge_group.clear(self)

    def num_major_charge_group(self) -> int:
        return Settlement.major_charge_group.count(self)

    def get_major_charge_group_by_mrid(self, mrid: str) -> MajorChargeGroup | None:
        return Settlement.major_charge_group.get_by_mrid(self, mrid)

    def add_market_invoice_line_item(self, market_invoice_line_item: MarketInvoiceLineItem) -> Self:
        return Settlement.market_invoice_line_item.add(self, market_invoice_line_item)

    def remove_market_invoice_line_item(
        self, market_invoice_line_item: MarketInvoiceLineItem
    ) -> Self:
        return Settlement.market_invoice_line_item.remove(self, market_invoice_line_item)

    def clear_market_invoice_line_item(self) -> Self:
        return Settlement.market_invoice_line_item.clear(self)

    def num_market_invoice_line_item(self) -> int:
        return Settlement.market_invoice_line_item.count(self)

    def add_market_ledger_entry(self, market_ledger_entry: MarketLedgerEntry) -> Self:
        return Settlement.market_ledger_entry.add(self, market_ledger_entry)

    def remove_market_ledger_entry(self, market_ledger_entry: MarketLedgerEntry) -> Self:
        return Settlement.market_ledger_entry.remove(self, market_ledger_entry)

    def clear_market_ledger_entry(self) -> Self:
        return Settlement.market_ledger_entry.clear(self)

    def num_market_ledger_entry(self) -> int:
        return Settlement.market_ledger_entry.count(self)
