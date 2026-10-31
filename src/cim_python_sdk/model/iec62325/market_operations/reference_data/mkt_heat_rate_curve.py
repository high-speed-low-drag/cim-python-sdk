"""CIM class MktHeatRateCurve (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.generation.production.heat_rate_curve import HeatRateCurve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.resource_verifiable_costs import (
        ResourceVerifiableCosts,
    )


class MktHeatRateCurve(HeatRateCurve):
    """Subclass of IEC 61970: Generation: Production:HeatRateCurve."""

    __slots__ = ("_registered_generator", "_resource_verifiable_costs")

    resource_verifiable_costs: One[ResourceVerifiableCosts] = One(
        EndMeta(
            name="resource_verifiable_costs",
            cim_role="ResourceVerifiableCosts",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.resource_verifiable_costs:ResourceVerifiableCosts",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_heat_rate_curve",
            aggregation="none",
        )
    )
    registered_generator: One[RegisteredGenerator] = One(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_heat_rate_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktHeatRateCurve",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{142CE3B4-C829-4f94-8571-7009E5FEB0C7}",
        ends=(
            resource_verifiable_costs.meta,
            registered_generator.meta,
        ),
    )

    def __init__(
        self,
        *,
        resource_verifiable_costs: ResourceVerifiableCosts | None = None,
        registered_generator: RegisteredGenerator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if resource_verifiable_costs is not None:
            self.resource_verifiable_costs = resource_verifiable_costs
        if registered_generator is not None:
            self.registered_generator = registered_generator
