"""CIM class ErpLedBudLineItem (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_budget import (
        ErpLedgerBudget,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_entry import (
        ErpLedgerEntry,
    )


class ErpLedBudLineItem(ErpIdentifiedObject):
    """Individual entry of a given Ledger Budget, typically containing information such as
    amount, accounting date, accounting period, and is associated with the applicable
    general ledger account."""

    __slots__ = ("_erp_led_bud_line_item", "_erp_ledger_budget", "status")

    status: Status | None

    erp_led_bud_line_item: One[ErpLedgerEntry] = One(
        EndMeta(
            name="erp_led_bud_line_item",
            cim_role="ErpLedBudLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_entry:ErpLedgerEntry",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_ledger_entry",
            aggregation="none",
        )
    )
    erp_ledger_budget: One[ErpLedgerBudget] = One(
        EndMeta(
            name="erp_ledger_budget",
            cim_role="ErpLedgerBudget",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_budget:ErpLedgerBudget",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_led_bud_line_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpLedBudLineItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{497D8708-FB86-4141-8C80-548011F5C0C3}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(
            erp_led_bud_line_item.meta,
            erp_ledger_budget.meta,
        ),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        erp_led_bud_line_item: ErpLedgerEntry | None = None,
        erp_ledger_budget: ErpLedgerBudget | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if erp_led_bud_line_item is not None:
            self.erp_led_bud_line_item = erp_led_bud_line_item
        if erp_ledger_budget is not None:
            self.erp_ledger_budget = erp_ledger_budget
