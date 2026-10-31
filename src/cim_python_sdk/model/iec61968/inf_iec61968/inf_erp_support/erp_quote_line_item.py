"""CIM class ErpQuoteLineItem (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.asset_model_catalogue_item import (
        AssetModelCatalogueItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item import (
        ErpInvoiceLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote import ErpQuote
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_req_line_item import (
        ErpReqLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design import Design


class ErpQuoteLineItem(ErpIdentifiedObject):
    """Of an ErpQuote, the item or product quoted along with quantity, price and other
    descriptive information."""

    __slots__ = (
        "_asset_model_catalogue_item",
        "_design",
        "_erp_invoice_line_item",
        "_erp_quote",
        "_erp_req_line_item",
        "status",
    )

    status: Status | None

    erp_quote: One[ErpQuote] = One(
        EndMeta(
            name="erp_quote",
            cim_role="ErpQuote",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote:ErpQuote",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_quote_line_items",
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
            inverse="erp_quote_line_item",
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
            inverse="erp_quote_line_item",
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
            inverse="erp_quote_line_items",
            aggregation="none",
        )
    )
    design: One[Design] = One(
        EndMeta(
            name="design",
            cim_role="Design",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design:Design",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_quote_line_item",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpQuoteLineItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{41C0DEAC-191E-4b9c-85DA-917554C0FDF7}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(
            erp_quote.meta,
            erp_invoice_line_item.meta,
            erp_req_line_item.meta,
            asset_model_catalogue_item.meta,
            design.meta,
        ),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        erp_quote: ErpQuote | None = None,
        erp_invoice_line_item: ErpInvoiceLineItem | None = None,
        erp_req_line_item: ErpReqLineItem | None = None,
        asset_model_catalogue_item: AssetModelCatalogueItem | None = None,
        design: Design | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if erp_quote is not None:
            self.erp_quote = erp_quote
        if erp_invoice_line_item is not None:
            self.erp_invoice_line_item = erp_invoice_line_item
        if erp_req_line_item is not None:
            self.erp_req_line_item = erp_req_line_item
        if asset_model_catalogue_item is not None:
            self.asset_model_catalogue_item = asset_model_catalogue_item
        if design is not None:
            self.design = design
