"""CIM class OrgResOwnership (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.resource_assn_type import (
        ResourceAssnType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class OrgResOwnership(IdentifiedObject):
    """This class model the ownership percent and type of ownership between resource and
    organisation."""

    __slots__ = (
        "_registered_resource",
        "assc_type",
        "master_scheduling_coordinator_flag",
        "ownership_percent",
    )

    assc_type: ResourceAssnType | None
    master_scheduling_coordinator_flag: YesNo | None
    ownership_percent: float | None  # PerCent

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="org_res_ownership",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OrgResOwnership",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{146E3842-CF1A-43dd-A1CB-8512CB1101A5}",
        attributes=(
            AttrMeta("assc_type", "asscType", "ResourceAssnType", 0, 1, "enumeration"),
            AttrMeta(
                "master_scheduling_coordinator_flag",
                "masterSchedulingCoordinatorFlag",
                "YesNo",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("ownership_percent", "ownershipPercent", "PerCent", 0, 1, "cimdatatype"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        assc_type: ResourceAssnType | None = None,
        master_scheduling_coordinator_flag: YesNo | None = None,
        ownership_percent: float | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.assc_type = assc_type
        self.master_scheduling_coordinator_flag = master_scheduling_coordinator_flag
        self.ownership_percent = ownership_percent
        if registered_resource is not None:
            self.registered_resource = registered_resource
