"""CIM class CatalogAssetType (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo
    from cim_python_sdk.model.iec61968.assets.asset_kind import AssetKind
    from cim_python_sdk.model.iec61968.assets.product_asset_model import ProductAssetModel
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom_item_data import (
        ErpBomItemData,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_issue_inventory import (
        ErpIssueInventory,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_req_line_item import (
        ErpReqLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_type_asset.type_asset_catalogue import (
        TypeAssetCatalogue,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit import CompatibleUnit
    from cim_python_sdk.model.iec61970.base.domain.string_quantity import StringQuantity


class CatalogAssetType(IdentifiedObject):
    """a Assets that may be used for planning, work or design purposes."""

    __slots__ = (
        "_asset_info",
        "_compatible_units",
        "_erp_bom_item_datas",
        "_erp_inventory_issues",
        "_erp_req_line_items",
        "_product_asset_model",
        "_type_asset_catalogue",
        "estimated_unit_cost",
        "kind",
        "quantity",
        "stock_item",
        "type",
    )

    estimated_unit_cost: _decimal.Decimal | None  # Money
    quantity: StringQuantity | None
    kind: AssetKind | None
    stock_item: bool | None
    type: str | None

    product_asset_model: Many[ProductAssetModel] = Many(
        EndMeta(
            name="product_asset_model",
            cim_role="ProductAssetModel",
            target="cim_python_sdk.model.iec61968.assets.product_asset_model:ProductAssetModel",
            many=True,
            lower=0,
            upper=None,
            inverse="catalog_asset_type",
            aggregation="none",
        )
    )
    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="generic_asset_model",
            aggregation="none",
        )
    )
    erp_bom_item_datas: Many[ErpBomItemData] = Many(
        EndMeta(
            name="erp_bom_item_datas",
            cim_role="ErpBomItemDatas",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom_item_data:ErpBomItemData",
            many=True,
            lower=0,
            upper=None,
            inverse="type_asset",
            aggregation="none",
        )
    )
    erp_req_line_items: Many[ErpReqLineItem] = Many(
        EndMeta(
            name="erp_req_line_items",
            cim_role="ErpReqLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_req_line_item:ErpReqLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="type_asset",
            aggregation="none",
        )
    )
    asset_info: One[AssetInfo] = One(
        EndMeta(
            name="asset_info",
            cim_role="AssetInfo",
            target="cim_python_sdk.model.iec61968.assets.asset_info:AssetInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="catalog_asset_type",
            aggregation="none",
        )
    )
    erp_inventory_issues: Many[ErpIssueInventory] = Many(
        EndMeta(
            name="erp_inventory_issues",
            cim_role="ErpInventoryIssues",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_issue_inventory:ErpIssueInventory",
            many=True,
            lower=0,
            upper=None,
            inverse="type_asset",
            aggregation="none",
        )
    )
    type_asset_catalogue: One[TypeAssetCatalogue] = One(
        EndMeta(
            name="type_asset_catalogue",
            cim_role="TypeAssetCatalogue",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_type_asset.type_asset_catalogue:TypeAssetCatalogue",
            many=False,
            lower=0,
            upper=1,
            inverse="type_assets",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CatalogAssetType",
        package="TC57CIM/IEC61968/Assets",
        guid="{67717FD4-C9CF-40b6-B178-138A244718EA}",
        attributes=(
            AttrMeta("estimated_unit_cost", "estimatedUnitCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("quantity", "quantity", "StringQuantity", 0, 1, "compound"),
            AttrMeta("kind", "kind", "AssetKind", 0, 1, "enumeration"),
            AttrMeta("stock_item", "stockItem", "bool", 0, 1, "primitive"),
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
        ),
        ends=(
            product_asset_model.meta,
            compatible_units.meta,
            erp_bom_item_datas.meta,
            erp_req_line_items.meta,
            asset_info.meta,
            erp_inventory_issues.meta,
            type_asset_catalogue.meta,
        ),
    )

    def __init__(
        self,
        *,
        estimated_unit_cost: _decimal.Decimal | None = None,
        quantity: StringQuantity | None = None,
        kind: AssetKind | None = None,
        stock_item: bool | None = None,
        type: str | None = None,
        product_asset_model: Iterable[ProductAssetModel] | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        erp_bom_item_datas: Iterable[ErpBomItemData] | None = None,
        erp_req_line_items: Iterable[ErpReqLineItem] | None = None,
        asset_info: AssetInfo | None = None,
        erp_inventory_issues: Iterable[ErpIssueInventory] | None = None,
        type_asset_catalogue: TypeAssetCatalogue | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.estimated_unit_cost = estimated_unit_cost
        self.quantity = quantity
        self.kind = kind
        self.stock_item = stock_item
        self.type = type
        if product_asset_model is not None:
            CatalogAssetType.product_asset_model.extend(self, product_asset_model)
        if compatible_units is not None:
            CatalogAssetType.compatible_units.extend(self, compatible_units)
        if erp_bom_item_datas is not None:
            CatalogAssetType.erp_bom_item_datas.extend(self, erp_bom_item_datas)
        if erp_req_line_items is not None:
            CatalogAssetType.erp_req_line_items.extend(self, erp_req_line_items)
        if asset_info is not None:
            self.asset_info = asset_info
        if erp_inventory_issues is not None:
            CatalogAssetType.erp_inventory_issues.extend(self, erp_inventory_issues)
        if type_asset_catalogue is not None:
            self.type_asset_catalogue = type_asset_catalogue

    def add_product_asset_model(self, product_asset_model: ProductAssetModel) -> Self:
        return CatalogAssetType.product_asset_model.add(self, product_asset_model)

    def remove_product_asset_model(self, product_asset_model: ProductAssetModel) -> Self:
        return CatalogAssetType.product_asset_model.remove(self, product_asset_model)

    def clear_product_asset_model(self) -> Self:
        return CatalogAssetType.product_asset_model.clear(self)

    def num_product_asset_model(self) -> int:
        return CatalogAssetType.product_asset_model.count(self)

    def get_product_asset_model_by_mrid(self, mrid: str) -> ProductAssetModel | None:
        return CatalogAssetType.product_asset_model.get_by_mrid(self, mrid)

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CatalogAssetType.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CatalogAssetType.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return CatalogAssetType.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return CatalogAssetType.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return CatalogAssetType.compatible_units.get_by_mrid(self, mrid)

    def add_erp_bom_item_data(self, erp_bom_item_data: ErpBomItemData) -> Self:
        return CatalogAssetType.erp_bom_item_datas.add(self, erp_bom_item_data)

    def remove_erp_bom_item_data(self, erp_bom_item_data: ErpBomItemData) -> Self:
        return CatalogAssetType.erp_bom_item_datas.remove(self, erp_bom_item_data)

    def clear_erp_bom_item_datas(self) -> Self:
        return CatalogAssetType.erp_bom_item_datas.clear(self)

    def num_erp_bom_item_data(self) -> int:
        return CatalogAssetType.erp_bom_item_datas.count(self)

    def get_erp_bom_item_data_by_mrid(self, mrid: str) -> ErpBomItemData | None:
        return CatalogAssetType.erp_bom_item_datas.get_by_mrid(self, mrid)

    def add_erp_req_line_item(self, erp_req_line_item: ErpReqLineItem) -> Self:
        return CatalogAssetType.erp_req_line_items.add(self, erp_req_line_item)

    def remove_erp_req_line_item(self, erp_req_line_item: ErpReqLineItem) -> Self:
        return CatalogAssetType.erp_req_line_items.remove(self, erp_req_line_item)

    def clear_erp_req_line_items(self) -> Self:
        return CatalogAssetType.erp_req_line_items.clear(self)

    def num_erp_req_line_item(self) -> int:
        return CatalogAssetType.erp_req_line_items.count(self)

    def get_erp_req_line_item_by_mrid(self, mrid: str) -> ErpReqLineItem | None:
        return CatalogAssetType.erp_req_line_items.get_by_mrid(self, mrid)

    def add_erp_inventory_issue(self, erp_inventory_issue: ErpIssueInventory) -> Self:
        return CatalogAssetType.erp_inventory_issues.add(self, erp_inventory_issue)

    def remove_erp_inventory_issue(self, erp_inventory_issue: ErpIssueInventory) -> Self:
        return CatalogAssetType.erp_inventory_issues.remove(self, erp_inventory_issue)

    def clear_erp_inventory_issues(self) -> Self:
        return CatalogAssetType.erp_inventory_issues.clear(self)

    def num_erp_inventory_issue(self) -> int:
        return CatalogAssetType.erp_inventory_issues.count(self)

    def get_erp_inventory_issue_by_mrid(self, mrid: str) -> ErpIssueInventory | None:
        return CatalogAssetType.erp_inventory_issues.get_by_mrid(self, mrid)
