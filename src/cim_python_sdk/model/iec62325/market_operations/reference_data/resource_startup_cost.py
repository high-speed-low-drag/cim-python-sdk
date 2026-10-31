"""CIM class ResourceStartupCost (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.resource_verifiable_costs import (
        ResourceVerifiableCosts,
    )


class ResourceStartupCost(CimObject):
    """To model the startup costs of a generation resource."""

    __slots__ = (
        "_resource_verifiable_costs",
        "fuel_cold_startup",
        "fuel_hot_startup",
        "fuel_intermediate_startup",
        "fuel_low_sustained_limit",
        "gas_percent_cold_startup",
        "gas_percent_hot_startup",
        "gas_percent_intermediate_startup",
        "gas_percent_low_sustained_limit",
        "oil_percent_cold_startup",
        "oil_percent_hot_startup",
        "oil_percent_intermediate_startup",
        "oil_percent_low_sustained_limit",
        "solidfuel_percent_cold_startup",
        "solidfuel_percent_hot_startup",
        "solidfuel_percent_intermediate_startup",
        "solidfuel_percent_low_sustained_limit",
    )

    fuel_cold_startup: float | None
    fuel_hot_startup: float | None
    fuel_intermediate_startup: float | None
    fuel_low_sustained_limit: float | None
    gas_percent_cold_startup: float | None  # PerCent
    gas_percent_hot_startup: float | None  # PerCent
    gas_percent_intermediate_startup: float | None  # PerCent
    gas_percent_low_sustained_limit: float | None  # PerCent
    oil_percent_cold_startup: float | None  # PerCent
    oil_percent_hot_startup: float | None  # PerCent
    oil_percent_intermediate_startup: float | None  # PerCent
    oil_percent_low_sustained_limit: float | None  # PerCent
    solidfuel_percent_cold_startup: float | None  # PerCent
    solidfuel_percent_hot_startup: float | None  # PerCent
    solidfuel_percent_intermediate_startup: float | None  # PerCent
    solidfuel_percent_low_sustained_limit: float | None  # PerCent

    resource_verifiable_costs: One[ResourceVerifiableCosts] = One(
        EndMeta(
            name="resource_verifiable_costs",
            cim_role="ResourceVerifiableCosts",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.resource_verifiable_costs:ResourceVerifiableCosts",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_startup_cost",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceStartupCost",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{1969CDE2-401C-4490-88C2-5E16365B5B54}",
        attributes=(
            AttrMeta("fuel_cold_startup", "fuelColdStartup", "float", 0, 1, "primitive"),
            AttrMeta("fuel_hot_startup", "fuelHotStartup", "float", 0, 1, "primitive"),
            AttrMeta(
                "fuel_intermediate_startup", "fuelIntermediateStartup", "float", 0, 1, "primitive"
            ),
            AttrMeta(
                "fuel_low_sustained_limit", "fuelLowSustainedLimit", "float", 0, 1, "primitive"
            ),
            AttrMeta(
                "gas_percent_cold_startup", "gasPercentColdStartup", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "gas_percent_hot_startup", "gasPercentHotStartup", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "gas_percent_intermediate_startup",
                "gasPercentIntermediateStartup",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "gas_percent_low_sustained_limit",
                "gasPercentLowSustainedLimit",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "oil_percent_cold_startup", "oilPercentColdStartup", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "oil_percent_hot_startup", "oilPercentHotStartup", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "oil_percent_intermediate_startup",
                "oilPercentIntermediateStartup",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "oil_percent_low_sustained_limit",
                "oilPercentLowSustainedLimit",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "solidfuel_percent_cold_startup",
                "solidfuelPercentColdStartup",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "solidfuel_percent_hot_startup",
                "solidfuelPercentHotStartup",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "solidfuel_percent_intermediate_startup",
                "solidfuelPercentIntermediateStartup",
                "PerCent",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "solidfuel_percent_low_sustained_limit",
                "solidfuelPercentLowSustainedLimit",
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
        fuel_cold_startup: float | None = None,
        fuel_hot_startup: float | None = None,
        fuel_intermediate_startup: float | None = None,
        fuel_low_sustained_limit: float | None = None,
        gas_percent_cold_startup: float | None = None,
        gas_percent_hot_startup: float | None = None,
        gas_percent_intermediate_startup: float | None = None,
        gas_percent_low_sustained_limit: float | None = None,
        oil_percent_cold_startup: float | None = None,
        oil_percent_hot_startup: float | None = None,
        oil_percent_intermediate_startup: float | None = None,
        oil_percent_low_sustained_limit: float | None = None,
        solidfuel_percent_cold_startup: float | None = None,
        solidfuel_percent_hot_startup: float | None = None,
        solidfuel_percent_intermediate_startup: float | None = None,
        solidfuel_percent_low_sustained_limit: float | None = None,
        resource_verifiable_costs: ResourceVerifiableCosts | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.fuel_cold_startup = fuel_cold_startup
        self.fuel_hot_startup = fuel_hot_startup
        self.fuel_intermediate_startup = fuel_intermediate_startup
        self.fuel_low_sustained_limit = fuel_low_sustained_limit
        self.gas_percent_cold_startup = gas_percent_cold_startup
        self.gas_percent_hot_startup = gas_percent_hot_startup
        self.gas_percent_intermediate_startup = gas_percent_intermediate_startup
        self.gas_percent_low_sustained_limit = gas_percent_low_sustained_limit
        self.oil_percent_cold_startup = oil_percent_cold_startup
        self.oil_percent_hot_startup = oil_percent_hot_startup
        self.oil_percent_intermediate_startup = oil_percent_intermediate_startup
        self.oil_percent_low_sustained_limit = oil_percent_low_sustained_limit
        self.solidfuel_percent_cold_startup = solidfuel_percent_cold_startup
        self.solidfuel_percent_hot_startup = solidfuel_percent_hot_startup
        self.solidfuel_percent_intermediate_startup = solidfuel_percent_intermediate_startup
        self.solidfuel_percent_low_sustained_limit = solidfuel_percent_low_sustained_limit
        if resource_verifiable_costs is not None:
            self.resource_verifiable_costs = resource_verifiable_costs
