"""CIM class ResponseMethod (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_distributed_resource import (
        RegisteredDistributedResource,
    )


class ResponseMethod(IdentifiedObject):
    """Specifies a category of energy usage that the demand response applies for; e.g. energy
    from lighting, HVAC, other."""

    __slots__ = (
        "_registered_resource",
        "active_power",
        "active_power_uom",
        "method",
        "site_multiplier",
    )

    active_power: float | None
    active_power_uom: str | None
    method: str | None
    site_multiplier: int | None

    registered_resource: One[RegisteredDistributedResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_distributed_resource:RegisteredDistributedResource",
            many=False,
            lower=1,
            upper=1,
            inverse="response_methods",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResponseMethod",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{9878550E-874A-44d5-8003-59ED85F2A8CE}",
        attributes=(
            AttrMeta("active_power", "activePower", "float", 0, 1, "primitive"),
            AttrMeta("active_power_uom", "activePowerUOM", "str", 0, 1, "primitive"),
            AttrMeta("method", "method", "str", 0, 1, "primitive"),
            AttrMeta("site_multiplier", "siteMultiplier", "int", 0, 1, "primitive"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        active_power: float | None = None,
        active_power_uom: str | None = None,
        method: str | None = None,
        site_multiplier: int | None = None,
        registered_resource: RegisteredDistributedResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.active_power = active_power
        self.active_power_uom = active_power_uom
        self.method = method
        self.site_multiplier = site_multiplier
        if registered_resource is not None:
            self.registered_resource = registered_resource
