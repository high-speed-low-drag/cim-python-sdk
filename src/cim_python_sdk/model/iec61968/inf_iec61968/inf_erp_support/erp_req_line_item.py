"""CIM class ErpReqLineItem (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.catalog_asset_type import CatalogAssetType
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_po_line_item import (
        ErpPOLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item import (
        ErpQuoteLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_requisition import (
        ErpRequisition,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.type_material import TypeMaterial


class ErpReqLineItem(ErpIdentifiedObject):
    """Information that describes a requested item and its attributes."""

    __slots__ = (
        "_erp_po_line_item",
        "_erp_quote_line_item",
        "_erp_requisition",
        "_type_asset",
        "_type_material",
        "code",
        "cost",
        "delivery_date",
        "quantity",
        "status",
    )

    code: str | None
    quantity: int | None
    delivery_date: _dt.date | None
    cost: _decimal.Decimal | None  # Money
    status: Status | None

    erp_requisition: One[ErpRequisition] = One(
        EndMeta(
            name="erp_requisition",
            cim_role="ErpRequisition",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_requisition:ErpRequisition",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_req_line_items",
            aggregation="none",
        )
    )
    type_material: One[TypeMaterial] = One(
        EndMeta(
            name="type_material",
            cim_role="TypeMaterial",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.type_material:TypeMaterial",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_req_line_items",
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
            inverse="erp_req_line_item",
            aggregation="none",
        )
    )
    type_asset: One[CatalogAssetType] = One(
        EndMeta(
            name="type_asset",
            cim_role="TypeAsset",
            target="cim_python_sdk.model.iec61968.assets.catalog_asset_type:CatalogAssetType",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_req_line_items",
            aggregation="none",
        )
    )
    erp_quote_line_item: One[ErpQuoteLineItem] = One(
        EndMeta(
            name="erp_quote_line_item",
            cim_role="ErpQuoteLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item:ErpQuoteLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_req_line_item",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpReqLineItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{704B113A-CD61-4877-97DA-A23E4F7F77C8}",
        attributes=(
            AttrMeta("code", "code", "str", 0, 1, "primitive"),
            AttrMeta("quantity", "quantity", "int", 0, 1, "primitive"),
            AttrMeta("delivery_date", "deliveryDate", "date", 0, 1, "primitive"),
            AttrMeta("cost", "cost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            erp_requisition.meta,
            type_material.meta,
            erp_po_line_item.meta,
            type_asset.meta,
            erp_quote_line_item.meta,
        ),
    )

    def __init__(
        self,
        *,
        code: str | None = None,
        quantity: int | None = None,
        delivery_date: _dt.date | None = None,
        cost: _decimal.Decimal | None = None,
        status: Status | None = None,
        erp_requisition: ErpRequisition | None = None,
        type_material: TypeMaterial | None = None,
        erp_po_line_item: ErpPOLineItem | None = None,
        type_asset: CatalogAssetType | None = None,
        erp_quote_line_item: ErpQuoteLineItem | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.code = code
        self.quantity = quantity
        self.delivery_date = delivery_date
        self.cost = cost
        self.status = status
        if erp_requisition is not None:
            self.erp_requisition = erp_requisition
        if type_material is not None:
            self.type_material = type_material
        if erp_po_line_item is not None:
            self.erp_po_line_item = erp_po_line_item
        if type_asset is not None:
            self.type_asset = type_asset
        if erp_quote_line_item is not None:
            self.erp_quote_line_item = erp_quote_line_item
