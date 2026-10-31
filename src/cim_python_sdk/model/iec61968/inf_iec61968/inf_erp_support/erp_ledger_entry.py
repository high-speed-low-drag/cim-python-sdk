"""CIM class ErpLedgerEntry (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.common.user_attribute import UserAttribute
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_account_kind import (
        ErpAccountKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal_entry import (
        ErpJournalEntry,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_led_bud_line_item import (
        ErpLedBudLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger import ErpLedger


class ErpLedgerEntry(ErpIdentifiedObject):
    """Details of an individual entry in a ledger, which was posted from a journal on the
    posted date."""

    __slots__ = (
        "_erp_jounal_entry",
        "_erp_ledger",
        "_erp_ledger_entry",
        "_user_attributes",
        "account_id",
        "account_kind",
        "amount",
        "posted_date_time",
        "status",
        "transaction_date_time",
    )

    account_id: str | None
    account_kind: ErpAccountKind | None
    amount: _decimal.Decimal | None  # Money
    posted_date_time: _dt.datetime | None
    transaction_date_time: _dt.datetime | None
    status: Status | None

    erp_jounal_entry: One[ErpJournalEntry] = One(
        EndMeta(
            name="erp_jounal_entry",
            cim_role="ErpJounalEntry",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal_entry:ErpJournalEntry",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_ledger_entry",
            aggregation="none",
        )
    )
    user_attributes: Many[UserAttribute] = Many(
        EndMeta(
            name="user_attributes",
            cim_role="UserAttributes",
            target="cim_python_sdk.model.iec61968.common.user_attribute:UserAttribute",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_ledger_entries",
            aggregation="none",
        )
    )
    erp_ledger: One[ErpLedger] = One(
        EndMeta(
            name="erp_ledger",
            cim_role="ErpLedger",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger:ErpLedger",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_ledger_entries",
            aggregation="none",
        )
    )
    erp_ledger_entry: One[ErpLedBudLineItem] = One(
        EndMeta(
            name="erp_ledger_entry",
            cim_role="ErpLedgerEntry",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_led_bud_line_item:ErpLedBudLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_led_bud_line_item",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpLedgerEntry",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{8CFB51A0-6C9E-48a0-A8CC-AA2E97B62DAE}",
        attributes=(
            AttrMeta("account_id", "accountID", "str", 0, 1, "primitive"),
            AttrMeta("account_kind", "accountKind", "ErpAccountKind", 0, 1, "enumeration"),
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("posted_date_time", "postedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("transaction_date_time", "transactionDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            erp_jounal_entry.meta,
            user_attributes.meta,
            erp_ledger.meta,
            erp_ledger_entry.meta,
        ),
    )

    def __init__(
        self,
        *,
        account_id: str | None = None,
        account_kind: ErpAccountKind | None = None,
        amount: _decimal.Decimal | None = None,
        posted_date_time: _dt.datetime | None = None,
        transaction_date_time: _dt.datetime | None = None,
        status: Status | None = None,
        erp_jounal_entry: ErpJournalEntry | None = None,
        user_attributes: Iterable[UserAttribute] | None = None,
        erp_ledger: ErpLedger | None = None,
        erp_ledger_entry: ErpLedBudLineItem | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.account_id = account_id
        self.account_kind = account_kind
        self.amount = amount
        self.posted_date_time = posted_date_time
        self.transaction_date_time = transaction_date_time
        self.status = status
        if erp_jounal_entry is not None:
            self.erp_jounal_entry = erp_jounal_entry
        if user_attributes is not None:
            ErpLedgerEntry.user_attributes.extend(self, user_attributes)
        if erp_ledger is not None:
            self.erp_ledger = erp_ledger
        if erp_ledger_entry is not None:
            self.erp_ledger_entry = erp_ledger_entry

    def add_user_attribute(self, user_attribute: UserAttribute) -> Self:
        return ErpLedgerEntry.user_attributes.add(self, user_attribute)

    def remove_user_attribute(self, user_attribute: UserAttribute) -> Self:
        return ErpLedgerEntry.user_attributes.remove(self, user_attribute)

    def clear_user_attributes(self) -> Self:
        return ErpLedgerEntry.user_attributes.clear(self)

    def num_user_attribute(self) -> int:
        return ErpLedgerEntry.user_attributes.count(self)
