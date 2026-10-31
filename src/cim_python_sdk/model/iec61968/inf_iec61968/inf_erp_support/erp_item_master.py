"""CIM class ErpItemMaster (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

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


class ErpItemMaster(ErpIdentifiedObject):
    """Any unique purchased part for manufactured product tracked by ERP systems for a utility.

    Item, as used by the OAG, refers to the basic information about an item, including its
    attributes, cost, and locations. It does not include item quantities. Compare to the
    Inventory, which includes all quantities and other location-specific information."""

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
            inverse="erp_item_master",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpItemMaster",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{26D010CF-1FA8-43da-9EC5-A05965183BD0}",
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
