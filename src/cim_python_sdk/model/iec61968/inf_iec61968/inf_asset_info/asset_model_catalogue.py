"""CIM class AssetModelCatalogue (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.asset_model_catalogue_item import (
        AssetModelCatalogueItem,
    )


class AssetModelCatalogue(IdentifiedObject):
    """Catalogue of available types of products and materials that are used to build or
    install, maintain or operate an Asset. Each catalogue item is for a specific product
    (AssetModel) available from a specific supplier."""

    __slots__ = ("_asset_model_catalogue_items", "status")

    status: Status | None

    asset_model_catalogue_items: Many[AssetModelCatalogueItem] = Many(
        EndMeta(
            name="asset_model_catalogue_items",
            cim_role="AssetModelCatalogueItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.asset_model_catalogue_item:AssetModelCatalogueItem",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_model_catalogue",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetModelCatalogue",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{6453AF51-F9D2-49b8-8FDA-BE5F7D2E96E0}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(asset_model_catalogue_items.meta,),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        asset_model_catalogue_items: Iterable[AssetModelCatalogueItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if asset_model_catalogue_items is not None:
            AssetModelCatalogue.asset_model_catalogue_items.extend(
                self, asset_model_catalogue_items
            )

    def add_asset_model_catalogue_item(
        self, asset_model_catalogue_item: AssetModelCatalogueItem
    ) -> Self:
        return AssetModelCatalogue.asset_model_catalogue_items.add(self, asset_model_catalogue_item)

    def remove_asset_model_catalogue_item(
        self, asset_model_catalogue_item: AssetModelCatalogueItem
    ) -> Self:
        return AssetModelCatalogue.asset_model_catalogue_items.remove(
            self, asset_model_catalogue_item
        )

    def clear_asset_model_catalogue_items(self) -> Self:
        return AssetModelCatalogue.asset_model_catalogue_items.clear(self)

    def num_asset_model_catalogue_item(self) -> int:
        return AssetModelCatalogue.asset_model_catalogue_items.count(self)

    def get_asset_model_catalogue_item_by_mrid(self, mrid: str) -> AssetModelCatalogueItem | None:
        return AssetModelCatalogue.asset_model_catalogue_items.get_by_mrid(self, mrid)
