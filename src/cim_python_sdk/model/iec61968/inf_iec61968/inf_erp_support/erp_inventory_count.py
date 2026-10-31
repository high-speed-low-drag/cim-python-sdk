"""CIM class ErpInventoryCount (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status


class ErpInventoryCount(ErpIdentifiedObject):
    """This is related to Inventory physical counts organized by AssetModel. Note that a count
    of a type of asset can be accomplished by the association inherited by AssetModel (from
    Document) to Asset.

    It enables ERP applications to transfer an inventory count between ERP and the actual
    physical inventory location. This count may be a cycle count or a physical count."""

    __slots__ = ("status",)

    status: Status | None

    _cim_meta = ClassMeta(
        cim_name="ErpInventoryCount",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{FED13292-1658-4732-82E1-6DD3D974F8EB}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
