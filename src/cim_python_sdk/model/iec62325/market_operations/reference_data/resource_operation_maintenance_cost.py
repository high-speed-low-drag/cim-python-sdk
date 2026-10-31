"""CIM class ResourceOperationMaintenanceCost (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.resource_verifiable_costs import (
        ResourceVerifiableCosts,
    )


class ResourceOperationMaintenanceCost(Curve):
    """To model the Operation and Maintenance (O and M) costs of a generation resource."""

    __slots__ = (
        "_resource_verifiable_costs",
        "gas_percent_above_low_sustained_limit",
        "oil_percent_above_low_sustained_limit",
        "om_cost_cold_startup",
        "om_cost_hot_startup",
        "om_cost_intermediate_startup",
        "om_cost_low_sustained_limit",
        "solidfuel_percent_above_low_sustained_limit",
    )

    gas_percent_above_low_sustained_limit: float | None  # PerCent
    oil_percent_above_low_sustained_limit: float | None  # PerCent
    om_cost_cold_startup: float | None
    om_cost_hot_startup: float | None
    om_cost_intermediate_startup: float | None
    om_cost_low_sustained_limit: float | None
    solidfuel_percent_above_low_sustained_limit: float | None  # PerCent

    resource_verifiable_costs: One[ResourceVerifiableCosts] = One(
        EndMeta(
            name="resource_verifiable_costs",
            cim_role="ResourceVerifiableCosts",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.resource_verifiable_costs:ResourceVerifiableCosts",
            many=False,
            lower=0,
            upper=1,
            inverse="resource_operation_maintenance_cost",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceOperationMaintenanceCost",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{80204EE8-3326-45cd-A41B-385DFC54F5D3}",
        attributes=(
            AttrMeta(
                "gas_percent_above_low_sustained_limit",
                "gasPercentAboveLowSustainedLimit",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "oil_percent_above_low_sustained_limit",
                "oilPercentAboveLowSustainedLimit",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("om_cost_cold_startup", "omCostColdStartup", "float", 0, 1, "primitive"),
            AttrMeta("om_cost_hot_startup", "omCostHotStartup", "float", 0, 1, "primitive"),
            AttrMeta(
                "om_cost_intermediate_startup",
                "omCostIntermediateStartup",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "om_cost_low_sustained_limit", "omCostLowSustainedLimit", "float", 0, 1, "primitive"
            ),
            AttrMeta(
                "solidfuel_percent_above_low_sustained_limit",
                "solidfuelPercentAboveLowSustainedLimit",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
        ),
        ends=(resource_verifiable_costs.meta,),
    )

    def __init__(
        self,
        *,
        gas_percent_above_low_sustained_limit: float | None = None,
        oil_percent_above_low_sustained_limit: float | None = None,
        om_cost_cold_startup: float | None = None,
        om_cost_hot_startup: float | None = None,
        om_cost_intermediate_startup: float | None = None,
        om_cost_low_sustained_limit: float | None = None,
        solidfuel_percent_above_low_sustained_limit: float | None = None,
        resource_verifiable_costs: ResourceVerifiableCosts | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.gas_percent_above_low_sustained_limit = gas_percent_above_low_sustained_limit
        self.oil_percent_above_low_sustained_limit = oil_percent_above_low_sustained_limit
        self.om_cost_cold_startup = om_cost_cold_startup
        self.om_cost_hot_startup = om_cost_hot_startup
        self.om_cost_intermediate_startup = om_cost_intermediate_startup
        self.om_cost_low_sustained_limit = om_cost_low_sustained_limit
        self.solidfuel_percent_above_low_sustained_limit = (
            solidfuel_percent_above_low_sustained_limit
        )
        if resource_verifiable_costs is not None:
            self.resource_verifiable_costs = resource_verifiable_costs
