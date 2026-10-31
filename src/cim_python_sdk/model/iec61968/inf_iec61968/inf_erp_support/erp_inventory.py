"""CIM class ErpInventory (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.common.status import Status


class ErpInventory(ErpIdentifiedObject):
    """Utility inventory-related information about an item or part (and not for description of
    the item and its attributes). It is used by ERP applications to enable the
    synchronization of Inventory data that exists on separate Item Master databases. This
    data is not the master data that describes the attributes of the item such as
    dimensions, weight, or unit of measure - it describes the item as it exists at a
    specific location."""

    __slots__ = ("_asset", "status")

    status: Status | None

    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_inventory",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpInventory",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{CAE157A1-AB4E-4403-8A06-5386CA3118F0}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(asset.meta,),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        asset: Asset | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if asset is not None:
            self.asset = asset
