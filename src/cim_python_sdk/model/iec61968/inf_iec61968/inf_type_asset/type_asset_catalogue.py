"""CIM class TypeAssetCatalogue (TC57CIM/IEC61968/InfIEC61968/InfTypeAsset). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.catalog_asset_type import CatalogAssetType
    from cim_python_sdk.model.iec61968.common.status import Status


class TypeAssetCatalogue(IdentifiedObject):
    """Catalogue of generic types of assets (TypeAsset) that may be used for design purposes.
    It is not associated with a particular manufacturer."""

    __slots__ = ("_type_assets", "status")

    status: Status | None

    type_assets: Many[CatalogAssetType] = Many(
        EndMeta(
            name="type_assets",
            cim_role="TypeAssets",
            target="cim_python_sdk.model.iec61968.assets.catalog_asset_type:CatalogAssetType",
            many=True,
            lower=0,
            upper=None,
            inverse="type_asset_catalogue",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TypeAssetCatalogue",
        package="TC57CIM/IEC61968/InfIEC61968/InfTypeAsset",
        guid="{1740D770-E84A-42e6-AD51-CA7779A78944}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(type_assets.meta,),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        type_assets: Iterable[CatalogAssetType] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if type_assets is not None:
            TypeAssetCatalogue.type_assets.extend(self, type_assets)

    def add_type_asset(self, type_asset: CatalogAssetType) -> Self:
        return TypeAssetCatalogue.type_assets.add(self, type_asset)

    def remove_type_asset(self, type_asset: CatalogAssetType) -> Self:
        return TypeAssetCatalogue.type_assets.remove(self, type_asset)

    def clear_type_assets(self) -> Self:
        return TypeAssetCatalogue.type_assets.clear(self)

    def num_type_asset(self) -> int:
        return TypeAssetCatalogue.type_assets.count(self)

    def get_type_asset_by_mrid(self, mrid: str) -> CatalogAssetType | None:
        return TypeAssetCatalogue.type_assets.get_by_mrid(self, mrid)
