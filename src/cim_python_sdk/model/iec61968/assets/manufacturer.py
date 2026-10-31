"""CIM class Manufacturer (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.product_asset_model import ProductAssetModel


class Manufacturer(OrganisationRole):
    """Organisation that manufactures asset products."""

    __slots__ = ("_product_asset_models",)

    product_asset_models: Many[ProductAssetModel] = Many(
        EndMeta(
            name="product_asset_models",
            cim_role="ProductAssetModels",
            target="cim_python_sdk.model.iec61968.assets.product_asset_model:ProductAssetModel",
            many=True,
            lower=0,
            upper=None,
            inverse="manufacturer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Manufacturer",
        package="TC57CIM/IEC61968/Assets",
        guid="{7A73B277-AD64-4e35-BCB0-C6495F8E63CA}",
        ends=(product_asset_models.meta,),
    )

    def __init__(
        self,
        *,
        product_asset_models: Iterable[ProductAssetModel] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if product_asset_models is not None:
            Manufacturer.product_asset_models.extend(self, product_asset_models)

    def add_product_asset_model(self, product_asset_model: ProductAssetModel) -> Self:
        return Manufacturer.product_asset_models.add(self, product_asset_model)

    def remove_product_asset_model(self, product_asset_model: ProductAssetModel) -> Self:
        return Manufacturer.product_asset_models.remove(self, product_asset_model)

    def clear_product_asset_models(self) -> Self:
        return Manufacturer.product_asset_models.clear(self)

    def num_product_asset_model(self) -> int:
        return Manufacturer.product_asset_models.count(self)

    def get_product_asset_model_by_mrid(self, mrid: str) -> ProductAssetModel | None:
        return Manufacturer.product_asset_models.get_by_mrid(self, mrid)
