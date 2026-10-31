"""CIM class ErpLedgerBudget (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_led_bud_line_item import (
        ErpLedBudLineItem,
    )


class ErpLedgerBudget(ErpDocument):
    """Information for utility Ledger Budgets. They support the transfer budget amounts between
    all possible source applications throughout an enterprise and a general ledger or budget
    application."""

    __slots__ = ("_erp_led_bud_line_items",)

    erp_led_bud_line_items: Many[ErpLedBudLineItem] = Many(
        EndMeta(
            name="erp_led_bud_line_items",
            cim_role="ErpLedBudLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_led_bud_line_item:ErpLedBudLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_ledger_budget",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpLedgerBudget",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{648B9268-D9CD-468c-9BFE-B2329ED60032}",
        ends=(erp_led_bud_line_items.meta,),
    )

    def __init__(
        self,
        *,
        erp_led_bud_line_items: Iterable[ErpLedBudLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_led_bud_line_items is not None:
            ErpLedgerBudget.erp_led_bud_line_items.extend(self, erp_led_bud_line_items)

    def add_erp_led_bud_line_item(self, erp_led_bud_line_item: ErpLedBudLineItem) -> Self:
        return ErpLedgerBudget.erp_led_bud_line_items.add(self, erp_led_bud_line_item)

    def remove_erp_led_bud_line_item(self, erp_led_bud_line_item: ErpLedBudLineItem) -> Self:
        return ErpLedgerBudget.erp_led_bud_line_items.remove(self, erp_led_bud_line_item)

    def clear_erp_led_bud_line_items(self) -> Self:
        return ErpLedgerBudget.erp_led_bud_line_items.clear(self)

    def num_erp_led_bud_line_item(self) -> int:
        return ErpLedgerBudget.erp_led_bud_line_items.count(self)

    def get_erp_led_bud_line_item_by_mrid(self, mrid: str) -> ErpLedBudLineItem | None:
        return ErpLedgerBudget.erp_led_bud_line_items.get_by_mrid(self, mrid)
