"""CIM class ProductAssetModel (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo
    from cim_python_sdk.model.iec61968.assets.asset_model_usage_kind import AssetModelUsageKind
    from cim_python_sdk.model.iec61968.assets.catalog_asset_type import CatalogAssetType
    from cim_python_sdk.model.iec61968.assets.corporate_standard_kind import CorporateStandardKind
    from cim_python_sdk.model.iec61968.assets.manufacturer import Manufacturer
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.asset_model_catalogue_item import (
        AssetModelCatalogueItem,
    )
    from cim_python_sdk.model.iec61968.operations.operational_restriction import (
        OperationalRestriction,
    )


class ProductAssetModel(IdentifiedObject):
    """Asset model by a specific manufacturer."""

    __slots__ = (
        "_asset",
        "_asset_info",
        "_asset_model_catalogue_items",
        "_catalog_asset_type",
        "_manufacturer",
        "_operational_restrictions",
        "catalogue_number",
        "corporate_standard_kind",
        "drawing_number",
        "instruction_manual",
        "model_number",
        "model_version",
        "overall_length",
        "style_number",
        "usage_kind",
        "weight_total",
    )

    model_number: str | None
    model_version: str | None
    style_number: str | None
    corporate_standard_kind: CorporateStandardKind | None
    usage_kind: AssetModelUsageKind | None
    catalogue_number: str | None
    drawing_number: str | None
    instruction_manual: str | None
    overall_length: float | None  # Length
    weight_total: float | None  # Mass

    asset: Many[Asset] = Many(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="product_asset_model",
            aggregation="none",
        )
    )
    catalog_asset_type: One[CatalogAssetType] = One(
        EndMeta(
            name="catalog_asset_type",
            cim_role="CatalogAssetType",
            target="cim_python_sdk.model.iec61968.assets.catalog_asset_type:CatalogAssetType",
            many=False,
            lower=0,
            upper=1,
            inverse="product_asset_model",
            aggregation="none",
        )
    )
    asset_model_catalogue_items: Many[AssetModelCatalogueItem] = Many(
        EndMeta(
            name="asset_model_catalogue_items",
            cim_role="AssetModelCatalogueItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.asset_model_catalogue_item:AssetModelCatalogueItem",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_model",
            aggregation="none",
        )
    )
    manufacturer: One[Manufacturer] = One(
        EndMeta(
            name="manufacturer",
            cim_role="Manufacturer",
            target="cim_python_sdk.model.iec61968.assets.manufacturer:Manufacturer",
            many=False,
            lower=0,
            upper=1,
            inverse="product_asset_models",
            aggregation="none",
        )
    )
    operational_restrictions: Many[OperationalRestriction] = Many(
        EndMeta(
            name="operational_restrictions",
            cim_role="OperationalRestrictions",
            target="cim_python_sdk.model.iec61968.operations.operational_restriction:OperationalRestriction",
            many=True,
            lower=0,
            upper=None,
            inverse="product_asset_model",
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
            inverse="product_asset_model",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProductAssetModel",
        package="TC57CIM/IEC61968/Assets",
        guid="{3355C111-67F6-40b0-97D2-660FF76A1F1E}",
        attributes=(
            AttrMeta("model_number", "modelNumber", "str", 0, 1, "primitive"),
            AttrMeta("model_version", "modelVersion", "str", 0, 1, "primitive"),
            AttrMeta("style_number", "styleNumber", "str", 0, 1, "primitive"),
            AttrMeta(
                "corporate_standard_kind",
                "corporateStandardKind",
                "CorporateStandardKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("usage_kind", "usageKind", "AssetModelUsageKind", 0, 1, "enumeration"),
            AttrMeta("catalogue_number", "catalogueNumber", "str", 0, 1, "primitive"),
            AttrMeta("drawing_number", "drawingNumber", "str", 0, 1, "primitive"),
            AttrMeta("instruction_manual", "instructionManual", "str", 0, 1, "primitive"),
            AttrMeta("overall_length", "overallLength", "Length", 0, 1, "cimdatatype"),
            AttrMeta("weight_total", "weightTotal", "Mass", 0, 1, "cimdatatype"),
        ),
        ends=(
            asset.meta,
            catalog_asset_type.meta,
            asset_model_catalogue_items.meta,
            manufacturer.meta,
            operational_restrictions.meta,
            asset_info.meta,
        ),
    )

    def __init__(
        self,
        *,
        model_number: str | None = None,
        model_version: str | None = None,
        style_number: str | None = None,
        corporate_standard_kind: CorporateStandardKind | None = None,
        usage_kind: AssetModelUsageKind | None = None,
        catalogue_number: str | None = None,
        drawing_number: str | None = None,
        instruction_manual: str | None = None,
        overall_length: float | None = None,
        weight_total: float | None = None,
        asset: Iterable[Asset] | None = None,
        catalog_asset_type: CatalogAssetType | None = None,
        asset_model_catalogue_items: Iterable[AssetModelCatalogueItem] | None = None,
        manufacturer: Manufacturer | None = None,
        operational_restrictions: Iterable[OperationalRestriction] | None = None,
        asset_info: AssetInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.model_number = model_number
        self.model_version = model_version
        self.style_number = style_number
        self.corporate_standard_kind = corporate_standard_kind
        self.usage_kind = usage_kind
        self.catalogue_number = catalogue_number
        self.drawing_number = drawing_number
        self.instruction_manual = instruction_manual
        self.overall_length = overall_length
        self.weight_total = weight_total
        if asset is not None:
            ProductAssetModel.asset.extend(self, asset)
        if catalog_asset_type is not None:
            self.catalog_asset_type = catalog_asset_type
        if asset_model_catalogue_items is not None:
            ProductAssetModel.asset_model_catalogue_items.extend(self, asset_model_catalogue_items)
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if operational_restrictions is not None:
            ProductAssetModel.operational_restrictions.extend(self, operational_restrictions)
        if asset_info is not None:
            self.asset_info = asset_info

    def add_asset(self, asset: Asset) -> Self:
        return ProductAssetModel.asset.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return ProductAssetModel.asset.remove(self, asset)

    def clear_asset(self) -> Self:
        return ProductAssetModel.asset.clear(self)

    def num_asset(self) -> int:
        return ProductAssetModel.asset.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return ProductAssetModel.asset.get_by_mrid(self, mrid)

    def add_asset_model_catalogue_item(
        self, asset_model_catalogue_item: AssetModelCatalogueItem
    ) -> Self:
        return ProductAssetModel.asset_model_catalogue_items.add(self, asset_model_catalogue_item)

    def remove_asset_model_catalogue_item(
        self, asset_model_catalogue_item: AssetModelCatalogueItem
    ) -> Self:
        return ProductAssetModel.asset_model_catalogue_items.remove(
            self, asset_model_catalogue_item
        )

    def clear_asset_model_catalogue_items(self) -> Self:
        return ProductAssetModel.asset_model_catalogue_items.clear(self)

    def num_asset_model_catalogue_item(self) -> int:
        return ProductAssetModel.asset_model_catalogue_items.count(self)

    def get_asset_model_catalogue_item_by_mrid(self, mrid: str) -> AssetModelCatalogueItem | None:
        return ProductAssetModel.asset_model_catalogue_items.get_by_mrid(self, mrid)

    def add_operational_restriction(self, operational_restriction: OperationalRestriction) -> Self:
        return ProductAssetModel.operational_restrictions.add(self, operational_restriction)

    def remove_operational_restriction(
        self, operational_restriction: OperationalRestriction
    ) -> Self:
        return ProductAssetModel.operational_restrictions.remove(self, operational_restriction)

    def clear_operational_restrictions(self) -> Self:
        return ProductAssetModel.operational_restrictions.clear(self)

    def num_operational_restriction(self) -> int:
        return ProductAssetModel.operational_restrictions.count(self)

    def get_operational_restriction_by_mrid(self, mrid: str) -> OperationalRestriction | None:
        return ProductAssetModel.operational_restrictions.get_by_mrid(self, mrid)
