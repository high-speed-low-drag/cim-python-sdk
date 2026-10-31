"""CIM class AllocationResultValues (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.allocation_result import (
        AllocationResult,
    )


class AllocationResultValues(CimObject):
    """Models Market clearing results in terms of price and MW values."""

    __slots__ = (
        "_allocation_result",
        "_registered_resource",
        "aggregate_type",
        "allocation_mw_hour",
        "allocation_price",
        "energy_type_code",
        "market_service_type",
    )

    aggregate_type: str | None
    allocation_mw_hour: float | None
    allocation_price: float | None
    energy_type_code: str | None
    market_service_type: str | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="allocation_result_values",
            aggregation="none",
        )
    )
    allocation_result: One[AllocationResult] = One(
        EndMeta(
            name="allocation_result",
            cim_role="AllocationResult",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.allocation_result:AllocationResult",
            many=False,
            lower=1,
            upper=1,
            inverse="allocation_result_values",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AllocationResultValues",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{664E0009-1ADD-4795-A1C4-4C8DE37DCAB8}",
        attributes=(
            AttrMeta("aggregate_type", "aggregateType", "str", 0, 1, "primitive"),
            AttrMeta("allocation_mw_hour", "allocationMwHour", "float", 0, 1, "primitive"),
            AttrMeta("allocation_price", "allocationPrice", "float", 0, 1, "primitive"),
            AttrMeta("energy_type_code", "energyTypeCode", "str", 0, 1, "primitive"),
            AttrMeta("market_service_type", "marketServiceType", "str", 0, 1, "primitive"),
        ),
        ends=(
            registered_resource.meta,
            allocation_result.meta,
        ),
    )

    def __init__(
        self,
        *,
        aggregate_type: str | None = None,
        allocation_mw_hour: float | None = None,
        allocation_price: float | None = None,
        energy_type_code: str | None = None,
        market_service_type: str | None = None,
        registered_resource: RegisteredResource | None = None,
        allocation_result: AllocationResult | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.aggregate_type = aggregate_type
        self.allocation_mw_hour = allocation_mw_hour
        self.allocation_price = allocation_price
        self.energy_type_code = energy_type_code
        self.market_service_type = market_service_type
        if registered_resource is not None:
            self.registered_resource = registered_resource
        if allocation_result is not None:
            self.allocation_result = allocation_result
