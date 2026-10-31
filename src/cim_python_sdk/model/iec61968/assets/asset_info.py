"""CIM class AssetInfo (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.catalog_asset_type import CatalogAssetType
    from cim_python_sdk.model.iec61968.assets.product_asset_model import ProductAssetModel
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource


class AssetInfo(IdentifiedObject):
    """Set of attributes of an asset, representing typical datasheet information of a physical
    device that can be instantiated and shared in different data exchange contexts:

    - as attributes of an asset instance (installed or in stock)

    - as attributes of an asset model (product by a manufacturer)

    - as attributes of a type asset (generic type of an asset as used in designs/extension
    planning)."""

    __slots__ = (
        "_assets",
        "_catalog_asset_type",
        "_power_system_resources",
        "_product_asset_model",
    )

    power_system_resources: Many[PowerSystemResource] = Many(
        EndMeta(
            name="power_system_resources",
            cim_role="PowerSystemResources",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_datasheet",
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
            inverse="asset_info",
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
            inverse="asset_info",
            aggregation="none",
        )
    )
    product_asset_model: One[ProductAssetModel] = One(
        EndMeta(
            name="product_asset_model",
            cim_role="ProductAssetModel",
            target="cim_python_sdk.model.iec61968.assets.product_asset_model:ProductAssetModel",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetInfo",
        package="TC57CIM/IEC61968/Assets",
        guid="{6D78A817-1BB4-4cb1-8478-11A40AF8F62F}",
        ends=(
            power_system_resources.meta,
            assets.meta,
            catalog_asset_type.meta,
            product_asset_model.meta,
        ),
    )

    def __init__(
        self,
        *,
        power_system_resources: Iterable[PowerSystemResource] | None = None,
        assets: Iterable[Asset] | None = None,
        catalog_asset_type: CatalogAssetType | None = None,
        product_asset_model: ProductAssetModel | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if power_system_resources is not None:
            AssetInfo.power_system_resources.extend(self, power_system_resources)
        if assets is not None:
            AssetInfo.assets.extend(self, assets)
        if catalog_asset_type is not None:
            self.catalog_asset_type = catalog_asset_type
        if product_asset_model is not None:
            self.product_asset_model = product_asset_model

    def add_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return AssetInfo.power_system_resources.add(self, power_system_resource)

    def remove_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return AssetInfo.power_system_resources.remove(self, power_system_resource)

    def clear_power_system_resources(self) -> Self:
        return AssetInfo.power_system_resources.clear(self)

    def num_power_system_resource(self) -> int:
        return AssetInfo.power_system_resources.count(self)

    def get_power_system_resource_by_mrid(self, mrid: str) -> PowerSystemResource | None:
        return AssetInfo.power_system_resources.get_by_mrid(self, mrid)

    def add_asset(self, asset: Asset) -> Self:
        return AssetInfo.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return AssetInfo.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return AssetInfo.assets.clear(self)

    def num_asset(self) -> int:
        return AssetInfo.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return AssetInfo.assets.get_by_mrid(self, mrid)
