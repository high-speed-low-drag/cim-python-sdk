"""CIM class ErpReceivable (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_line_item import (
        ErpRecLineItem,
    )


class ErpReceivable(ErpDocument):
    """Transaction representing an invoice, credit memo or debit memo to a customer. It is an
    open (unpaid) item in the Accounts Receivable ledger."""

    __slots__ = ("_erp_rec_line_items",)

    erp_rec_line_items: Many[ErpRecLineItem] = Many(
        EndMeta(
            name="erp_rec_line_items",
            cim_role="ErpRecLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_line_item:ErpRecLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_receivable",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpReceivable",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{8F2ED892-4481-40a4-9E78-9090AE9E10D0}",
        ends=(erp_rec_line_items.meta,),
    )

    def __init__(
        self,
        *,
        erp_rec_line_items: Iterable[ErpRecLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_rec_line_items is not None:
            ErpReceivable.erp_rec_line_items.extend(self, erp_rec_line_items)

    def add_erp_rec_line_item(self, erp_rec_line_item: ErpRecLineItem) -> Self:
        return ErpReceivable.erp_rec_line_items.add(self, erp_rec_line_item)

    def remove_erp_rec_line_item(self, erp_rec_line_item: ErpRecLineItem) -> Self:
        return ErpReceivable.erp_rec_line_items.remove(self, erp_rec_line_item)

    def clear_erp_rec_line_items(self) -> Self:
        return ErpReceivable.erp_rec_line_items.clear(self)

    def num_erp_rec_line_item(self) -> int:
        return ErpReceivable.erp_rec_line_items.count(self)

    def get_erp_rec_line_item_by_mrid(self, mrid: str) -> ErpRecLineItem | None:
        return ErpReceivable.erp_rec_line_items.get_by_mrid(self, mrid)
