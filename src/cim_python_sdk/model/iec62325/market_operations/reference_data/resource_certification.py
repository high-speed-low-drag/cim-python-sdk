"""CIM class ResourceCertification (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.resource_certification_kind import (
        ResourceCertificationKind,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class ResourceCertification(CimObject):
    """Specifies certification for a resource to participate in a specific markets."""

    __slots__ = ("_registered_resource", "market", "qualification_flag", "type")

    market: MarketType | None
    qualification_flag: YesNo | None
    type: ResourceCertificationKind | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_ancillary_service_qualification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceCertification",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{C27E4ACF-F11A-4912-9628-29357405DB51}",
        attributes=(
            AttrMeta("market", "market", "MarketType", 0, 1, "enumeration"),
            AttrMeta("qualification_flag", "qualificationFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("type", "type", "ResourceCertificationKind", 0, 1, "enumeration"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        market: MarketType | None = None,
        qualification_flag: YesNo | None = None,
        type: ResourceCertificationKind | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.market = market
        self.qualification_flag = qualification_flag
        self.type = type
        if registered_resource is not None:
            self.registered_resource = registered_resource
