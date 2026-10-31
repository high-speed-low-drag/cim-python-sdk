"""CIM class ErpQuote (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item import (
        ErpQuoteLineItem,
    )


class ErpQuote(ErpDocument):
    """Document describing the prices of goods or services provided by a supplier. It includes
    the terms of the purchase, delivery proposals, identification of goods or services
    ordered, as well as their quantities."""

    __slots__ = ("_erp_quote_line_items",)

    erp_quote_line_items: Many[ErpQuoteLineItem] = Many(
        EndMeta(
            name="erp_quote_line_items",
            cim_role="ErpQuoteLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item:ErpQuoteLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_quote",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpQuote",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{0908A794-42AB-4d96-915B-CD52EA913AFD}",
        ends=(erp_quote_line_items.meta,),
    )

    def __init__(
        self,
        *,
        erp_quote_line_items: Iterable[ErpQuoteLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_quote_line_items is not None:
            ErpQuote.erp_quote_line_items.extend(self, erp_quote_line_items)

    def add_erp_quote_line_item(self, erp_quote_line_item: ErpQuoteLineItem) -> Self:
        return ErpQuote.erp_quote_line_items.add(self, erp_quote_line_item)

    def remove_erp_quote_line_item(self, erp_quote_line_item: ErpQuoteLineItem) -> Self:
        return ErpQuote.erp_quote_line_items.remove(self, erp_quote_line_item)

    def clear_erp_quote_line_items(self) -> Self:
        return ErpQuote.erp_quote_line_items.clear(self)

    def num_erp_quote_line_item(self) -> int:
        return ErpQuote.erp_quote_line_items.count(self)

    def get_erp_quote_line_item_by_mrid(self, mrid: str) -> ErpQuoteLineItem | None:
        return ErpQuote.erp_quote_line_items.get_by_mrid(self, mrid)
