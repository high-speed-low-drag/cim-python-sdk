"""CIM class OrgPnodeAllocation (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode


class OrgPnodeAllocation(IdentifiedObject):
    """This class models the allocation between asset owners and pricing nodes."""

    __slots__ = ("_pnode", "max_mw_allocation")

    max_mw_allocation: float | None  # ActivePower

    pnode: One[Pnode] = One(
        EndMeta(
            name="pnode",
            cim_role="Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=False,
            lower=1,
            upper=1,
            inverse="org_pnode_allocation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OrgPnodeAllocation",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{AE1F59C4-5574-486b-A3B6-51C18D0FBDA1}",
        attributes=(
            AttrMeta("max_mw_allocation", "maxMWAllocation", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(pnode.meta,),
    )

    def __init__(
        self,
        *,
        max_mw_allocation: float | None = None,
        pnode: Pnode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_mw_allocation = max_mw_allocation
        if pnode is not None:
            self.pnode = pnode
