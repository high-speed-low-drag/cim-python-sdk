"""CIM class ErpPurchaseOrder (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_po_line_item import (
        ErpPOLineItem,
    )


class ErpPurchaseOrder(ErpDocument):
    """A document that communicates an order to purchase goods from a buyer to a supplier. The
    PurchaseOrder carries information to and from the buyer and supplier. It is a legally
    binding document once both Parties agree to the contents and the specified terms and
    conditions of the order."""

    __slots__ = ("_erp_po_line_items",)

    erp_po_line_items: Many[ErpPOLineItem] = Many(
        EndMeta(
            name="erp_po_line_items",
            cim_role="ErpPOLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_po_line_item:ErpPOLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_purchase_order",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpPurchaseOrder",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{B59BE666-E41E-4f68-A564-2A6E32C8DA78}",
        ends=(erp_po_line_items.meta,),
    )

    def __init__(
        self,
        *,
        erp_po_line_items: Iterable[ErpPOLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_po_line_items is not None:
            ErpPurchaseOrder.erp_po_line_items.extend(self, erp_po_line_items)

    def add_erp_po_line_item(self, erp_po_line_item: ErpPOLineItem) -> Self:
        return ErpPurchaseOrder.erp_po_line_items.add(self, erp_po_line_item)

    def remove_erp_po_line_item(self, erp_po_line_item: ErpPOLineItem) -> Self:
        return ErpPurchaseOrder.erp_po_line_items.remove(self, erp_po_line_item)

    def clear_erp_po_line_items(self) -> Self:
        return ErpPurchaseOrder.erp_po_line_items.clear(self)

    def num_erp_po_line_item(self) -> int:
        return ErpPurchaseOrder.erp_po_line_items.count(self)

    def get_erp_po_line_item_by_mrid(self, mrid: str) -> ErpPOLineItem | None:
        return ErpPurchaseOrder.erp_po_line_items.get_by_mrid(self, mrid)
