"""CIM class ErpIssueInventory (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.catalog_asset_type import CatalogAssetType
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.type_material import TypeMaterial


class ErpIssueInventory(ErpIdentifiedObject):
    """Can be used to request an application to process an issue or request information about
    an issue."""

    __slots__ = ("_type_asset", "_type_material", "status")

    status: Status | None

    type_material: One[TypeMaterial] = One(
        EndMeta(
            name="type_material",
            cim_role="TypeMaterial",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.type_material:TypeMaterial",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_issue_inventories",
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
            inverse="erp_inventory_issues",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpIssueInventory",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{D127CF41-0C3B-439f-A453-5071ED143BD2}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(
            type_material.meta,
            type_asset.meta,
        ),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        type_material: TypeMaterial | None = None,
        type_asset: CatalogAssetType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if type_material is not None:
            self.type_material = type_material
        if type_asset is not None:
            self.type_asset = type_asset
