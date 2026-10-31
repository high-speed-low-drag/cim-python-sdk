"""CIM class ErpReceiveDelivery (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_delv_line_item import (
        ErpRecDelvLineItem,
    )


class ErpReceiveDelivery(ErpDocument):
    """Transaction for an Organisation receiving goods or services that may be used to indicate
    receipt of goods in conjunction with a purchase order. A receivable is an open (unpaid)
    item in the Accounts Receivable ledger."""

    __slots__ = ("_erp_rec_delv_line_items",)

    erp_rec_delv_line_items: Many[ErpRecDelvLineItem] = Many(
        EndMeta(
            name="erp_rec_delv_line_items",
            cim_role="ErpRecDelvLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_delv_line_item:ErpRecDelvLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_receive_delivery",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpReceiveDelivery",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{9A73381D-9D2E-45ba-9D63-6B31C8EE2F68}",
        ends=(erp_rec_delv_line_items.meta,),
    )

    def __init__(
        self,
        *,
        erp_rec_delv_line_items: Iterable[ErpRecDelvLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_rec_delv_line_items is not None:
            ErpReceiveDelivery.erp_rec_delv_line_items.extend(self, erp_rec_delv_line_items)

    def add_erp_rec_delv_line_item(self, erp_rec_delv_line_item: ErpRecDelvLineItem) -> Self:
        return ErpReceiveDelivery.erp_rec_delv_line_items.add(self, erp_rec_delv_line_item)

    def remove_erp_rec_delv_line_item(self, erp_rec_delv_line_item: ErpRecDelvLineItem) -> Self:
        return ErpReceiveDelivery.erp_rec_delv_line_items.remove(self, erp_rec_delv_line_item)

    def clear_erp_rec_delv_line_items(self) -> Self:
        return ErpReceiveDelivery.erp_rec_delv_line_items.clear(self)

    def num_erp_rec_delv_line_item(self) -> int:
        return ErpReceiveDelivery.erp_rec_delv_line_items.count(self)

    def get_erp_rec_delv_line_item_by_mrid(self, mrid: str) -> ErpRecDelvLineItem | None:
        return ErpReceiveDelivery.erp_rec_delv_line_items.get_by_mrid(self, mrid)
