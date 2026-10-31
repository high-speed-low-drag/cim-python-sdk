"""CIM class ErpBomItemData (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.catalog_asset_type import CatalogAssetType
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom import ErpBOM
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location import DesignLocation


class ErpBomItemData(ErpIdentifiedObject):
    """An individual item on a bill of materials."""

    __slots__ = ("_design_location", "_erp_bom", "_type_asset")

    type_asset: One[CatalogAssetType] = One(
        EndMeta(
            name="type_asset",
            cim_role="TypeAsset",
            target="cim_python_sdk.model.iec61968.assets.catalog_asset_type:CatalogAssetType",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_bom_item_datas",
            aggregation="none",
        )
    )
    design_location: One[DesignLocation] = One(
        EndMeta(
            name="design_location",
            cim_role="DesignLocation",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location:DesignLocation",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_bom_item_datas",
            aggregation="none",
        )
    )
    erp_bom: One[ErpBOM] = One(
        EndMeta(
            name="erp_bom",
            cim_role="ErpBOM",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom:ErpBOM",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_bom_item_datas",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpBomItemData",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{198400B5-F041-4acd-B0AB-7C06E1EAE80F}",
        ends=(
            type_asset.meta,
            design_location.meta,
            erp_bom.meta,
        ),
    )

    def __init__(
        self,
        *,
        type_asset: CatalogAssetType | None = None,
        design_location: DesignLocation | None = None,
        erp_bom: ErpBOM | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if type_asset is not None:
            self.type_asset = type_asset
        if design_location is not None:
            self.design_location = design_location
        if erp_bom is not None:
            self.erp_bom = erp_bom
