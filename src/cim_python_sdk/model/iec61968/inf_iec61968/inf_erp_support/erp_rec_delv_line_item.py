"""CIM class ErpRecDelvLineItem (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item import (
        ErpInvoiceLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_po_line_item import (
        ErpPOLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_receive_delivery import (
        ErpReceiveDelivery,
    )


class ErpRecDelvLineItem(ErpIdentifiedObject):
    """Of an ErpReceiveDelivery, this is an individually received good or service by the
    Organisation receiving goods or services. It may be used to indicate receipt of goods in
    conjunction with a purchase order line item."""

    __slots__ = (
        "_assets",
        "_erp_invoice_line_item",
        "_erp_po_line_item",
        "_erp_receive_delivery",
        "status",
    )

    status: Status | None

    erp_receive_delivery: One[ErpReceiveDelivery] = One(
        EndMeta(
            name="erp_receive_delivery",
            cim_role="ErpReceiveDelivery",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_receive_delivery:ErpReceiveDelivery",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_rec_delv_line_items",
            aggregation="none",
        )
    )
    erp_po_line_item: One[ErpPOLineItem] = One(
        EndMeta(
            name="erp_po_line_item",
            cim_role="ErpPOLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_po_line_item:ErpPOLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_rec_del_line_item",
            aggregation="none",
        )
    )
    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_rec_delivery_items",
            aggregation="none",
        )
    )
    erp_invoice_line_item: One[ErpInvoiceLineItem] = One(
        EndMeta(
            name="erp_invoice_line_item",
            cim_role="ErpInvoiceLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_rec_delv_line_item",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpRecDelvLineItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{B4E2F4F0-78A8-4dd7-BC64-7A5E37411161}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(
            erp_receive_delivery.meta,
            erp_po_line_item.meta,
            assets.meta,
            erp_invoice_line_item.meta,
        ),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        erp_receive_delivery: ErpReceiveDelivery | None = None,
        erp_po_line_item: ErpPOLineItem | None = None,
        assets: Iterable[Asset] | None = None,
        erp_invoice_line_item: ErpInvoiceLineItem | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if erp_receive_delivery is not None:
            self.erp_receive_delivery = erp_receive_delivery
        if erp_po_line_item is not None:
            self.erp_po_line_item = erp_po_line_item
        if assets is not None:
            ErpRecDelvLineItem.assets.extend(self, assets)
        if erp_invoice_line_item is not None:
            self.erp_invoice_line_item = erp_invoice_line_item

    def add_asset(self, asset: Asset) -> Self:
        return ErpRecDelvLineItem.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return ErpRecDelvLineItem.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return ErpRecDelvLineItem.assets.clear(self)

    def num_asset(self) -> int:
        return ErpRecDelvLineItem.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return ErpRecDelvLineItem.assets.get_by_mrid(self, mrid)
