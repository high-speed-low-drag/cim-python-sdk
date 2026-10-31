"""CIM class ErpPOLineItem (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.asset_model_catalogue_item import (
        AssetModelCatalogueItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_purchase_order import (
        ErpPurchaseOrder,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_delv_line_item import (
        ErpRecDelvLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_req_line_item import (
        ErpReqLineItem,
    )


class ErpPOLineItem(ErpDocument):
    """Of an ErpPurchaseOrder, this is an individually ordered item or product along with the
    quantity, price and other descriptive information."""

    __slots__ = (
        "_asset_model_catalogue_item",
        "_erp_purchase_order",
        "_erp_rec_del_line_item",
        "_erp_req_line_item",
    )

    erp_rec_del_line_item: One[ErpRecDelvLineItem] = One(
        EndMeta(
            name="erp_rec_del_line_item",
            cim_role="ErpRecDelLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_delv_line_item:ErpRecDelvLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_po_line_item",
            aggregation="none",
        )
    )
    erp_req_line_item: One[ErpReqLineItem] = One(
        EndMeta(
            name="erp_req_line_item",
            cim_role="ErpReqLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_req_line_item:ErpReqLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_po_line_item",
            aggregation="none",
        )
    )
    asset_model_catalogue_item: One[AssetModelCatalogueItem] = One(
        EndMeta(
            name="asset_model_catalogue_item",
            cim_role="AssetModelCatalogueItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.asset_model_catalogue_item:AssetModelCatalogueItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_po_line_items",
            aggregation="none",
        )
    )
    erp_purchase_order: One[ErpPurchaseOrder] = One(
        EndMeta(
            name="erp_purchase_order",
            cim_role="ErpPurchaseOrder",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_purchase_order:ErpPurchaseOrder",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_po_line_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpPOLineItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{5F91E07F-F701-4b38-8CB8-1CA87251C0D5}",
        ends=(
            erp_rec_del_line_item.meta,
            erp_req_line_item.meta,
            asset_model_catalogue_item.meta,
            erp_purchase_order.meta,
        ),
    )

    def __init__(
        self,
        *,
        erp_rec_del_line_item: ErpRecDelvLineItem | None = None,
        erp_req_line_item: ErpReqLineItem | None = None,
        asset_model_catalogue_item: AssetModelCatalogueItem | None = None,
        erp_purchase_order: ErpPurchaseOrder | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_rec_del_line_item is not None:
            self.erp_rec_del_line_item = erp_rec_del_line_item
        if erp_req_line_item is not None:
            self.erp_req_line_item = erp_req_line_item
        if asset_model_catalogue_item is not None:
            self.asset_model_catalogue_item = asset_model_catalogue_item
        if erp_purchase_order is not None:
            self.erp_purchase_order = erp_purchase_order
