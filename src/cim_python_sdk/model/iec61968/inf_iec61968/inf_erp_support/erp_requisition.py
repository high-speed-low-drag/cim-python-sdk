"""CIM class ErpRequisition (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_req_line_item import (
        ErpReqLineItem,
    )


class ErpRequisition(ErpDocument):
    """General information that applies to a utility requisition that is a request for the
    purchase of goods or services. Typically, a requisition leads to the creation of a
    purchase order to a specific supplier."""

    __slots__ = ("_erp_req_line_items",)

    erp_req_line_items: Many[ErpReqLineItem] = Many(
        EndMeta(
            name="erp_req_line_items",
            cim_role="ErpReqLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_req_line_item:ErpReqLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_requisition",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpRequisition",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{1D8F6379-AE58-4c91-B287-CA3BEF7851BD}",
        ends=(erp_req_line_items.meta,),
    )

    def __init__(
        self,
        *,
        erp_req_line_items: Iterable[ErpReqLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_req_line_items is not None:
            ErpRequisition.erp_req_line_items.extend(self, erp_req_line_items)

    def add_erp_req_line_item(self, erp_req_line_item: ErpReqLineItem) -> Self:
        return ErpRequisition.erp_req_line_items.add(self, erp_req_line_item)

    def remove_erp_req_line_item(self, erp_req_line_item: ErpReqLineItem) -> Self:
        return ErpRequisition.erp_req_line_items.remove(self, erp_req_line_item)

    def clear_erp_req_line_items(self) -> Self:
        return ErpRequisition.erp_req_line_items.clear(self)

    def num_erp_req_line_item(self) -> int:
        return ErpRequisition.erp_req_line_items.count(self)

    def get_erp_req_line_item_by_mrid(self, mrid: str) -> ErpReqLineItem | None:
        return ErpRequisition.erp_req_line_items.get_by_mrid(self, mrid)
