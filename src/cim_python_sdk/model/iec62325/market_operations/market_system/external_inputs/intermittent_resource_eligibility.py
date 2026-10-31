"""CIM class IntermittentResourceEligibility (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource


class IntermittentResourceEligibility(MarketFactors):
    """Indicates whether unit is eligible for treatment as a intermittent variable renewable
    resource."""

    __slots__ = ("_registered_resource", "eligibility_status")

    eligibility_status: str | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="intermittent_resource_eligibility",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IntermittentResourceEligibility",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{F58AC39F-91BD-4366-88BD-EB2967288474}",
        attributes=(AttrMeta("eligibility_status", "eligibilityStatus", "str", 0, 1, "primitive"),),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        eligibility_status: str | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.eligibility_status = eligibility_status
        if registered_resource is not None:
            self.registered_resource = registered_resource
