"""CIM class AssetModelCatalogueItem (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.product_asset_model import ProductAssetModel
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.asset_model_catalogue import (
        AssetModelCatalogue,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_po_line_item import (
        ErpPOLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item import (
        ErpQuoteLineItem,
    )


class AssetModelCatalogueItem(Document):
    """Provides pricing and other relevant information about a specific manufacturer's product
    (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be
    availble from multiple suppliers. Note that manufacturer and supplier are both types of
    organisation, which the association is inherited from Document."""

    __slots__ = (
        "_asset_model",
        "_asset_model_catalogue",
        "_erp_po_line_items",
        "_erp_quote_line_items",
        "unit_cost",
    )

    unit_cost: _decimal.Decimal | None  # Money

    asset_model_catalogue: One[AssetModelCatalogue] = One(
        EndMeta(
            name="asset_model_catalogue",
            cim_role="AssetModelCatalogue",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.asset_model_catalogue:AssetModelCatalogue",
            many=False,
            lower=1,
            upper=1,
            inverse="asset_model_catalogue_items",
            aggregation="none",
        )
    )
    asset_model: One[ProductAssetModel] = One(
        EndMeta(
            name="asset_model",
            cim_role="AssetModel",
            target="cim_python_sdk.model.iec61968.assets.product_asset_model:ProductAssetModel",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_model_catalogue_items",
            aggregation="none",
        )
    )
    erp_po_line_items: Many[ErpPOLineItem] = Many(
        EndMeta(
            name="erp_po_line_items",
            cim_role="ErpPOLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_po_line_item:ErpPOLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_model_catalogue_item",
            aggregation="none",
        )
    )
    erp_quote_line_items: Many[ErpQuoteLineItem] = Many(
        EndMeta(
            name="erp_quote_line_items",
            cim_role="ErpQuoteLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item:ErpQuoteLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_model_catalogue_item",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetModelCatalogueItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{0BC94DBD-0BA4-4298-8439-48D9C8EF9CC5}",
        attributes=(AttrMeta("unit_cost", "unitCost", "Money", 0, 1, "cimdatatype"),),
        ends=(
            asset_model_catalogue.meta,
            asset_model.meta,
            erp_po_line_items.meta,
            erp_quote_line_items.meta,
        ),
    )

    def __init__(
        self,
        *,
        unit_cost: _decimal.Decimal | None = None,
        asset_model_catalogue: AssetModelCatalogue | None = None,
        asset_model: ProductAssetModel | None = None,
        erp_po_line_items: Iterable[ErpPOLineItem] | None = None,
        erp_quote_line_items: Iterable[ErpQuoteLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.unit_cost = unit_cost
        if asset_model_catalogue is not None:
            self.asset_model_catalogue = asset_model_catalogue
        if asset_model is not None:
            self.asset_model = asset_model
        if erp_po_line_items is not None:
            AssetModelCatalogueItem.erp_po_line_items.extend(self, erp_po_line_items)
        if erp_quote_line_items is not None:
            AssetModelCatalogueItem.erp_quote_line_items.extend(self, erp_quote_line_items)

    def add_erp_po_line_item(self, erp_po_line_item: ErpPOLineItem) -> Self:
        return AssetModelCatalogueItem.erp_po_line_items.add(self, erp_po_line_item)

    def remove_erp_po_line_item(self, erp_po_line_item: ErpPOLineItem) -> Self:
        return AssetModelCatalogueItem.erp_po_line_items.remove(self, erp_po_line_item)

    def clear_erp_po_line_items(self) -> Self:
        return AssetModelCatalogueItem.erp_po_line_items.clear(self)

    def num_erp_po_line_item(self) -> int:
        return AssetModelCatalogueItem.erp_po_line_items.count(self)

    def get_erp_po_line_item_by_mrid(self, mrid: str) -> ErpPOLineItem | None:
        return AssetModelCatalogueItem.erp_po_line_items.get_by_mrid(self, mrid)

    def add_erp_quote_line_item(self, erp_quote_line_item: ErpQuoteLineItem) -> Self:
        return AssetModelCatalogueItem.erp_quote_line_items.add(self, erp_quote_line_item)

    def remove_erp_quote_line_item(self, erp_quote_line_item: ErpQuoteLineItem) -> Self:
        return AssetModelCatalogueItem.erp_quote_line_items.remove(self, erp_quote_line_item)

    def clear_erp_quote_line_items(self) -> Self:
        return AssetModelCatalogueItem.erp_quote_line_items.clear(self)

    def num_erp_quote_line_item(self) -> int:
        return AssetModelCatalogueItem.erp_quote_line_items.count(self)

    def get_erp_quote_line_item_by_mrid(self, mrid: str) -> ErpQuoteLineItem | None:
        return AssetModelCatalogueItem.erp_quote_line_items.get_by_mrid(self, mrid)
