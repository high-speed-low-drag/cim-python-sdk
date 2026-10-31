"""CIM class FossilFuel (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.production.fuel_allocation_schedule import (
        FuelAllocationSchedule,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.fuel_type import FuelType
    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class FossilFuel(IdentifiedObject):
    """The fossil fuel consumed by the non-nuclear thermal generating unit. For example, coal,
    oil, gas, etc. These are the specific fuels that the generating unit can consume."""

    __slots__ = (
        "_fuel_allocation_schedules",
        "_thermal_generating_unit",
        "fossil_fuel_type",
        "fuel_cost",
        "fuel_dispatch_cost",
        "fuel_eff_factor",
        "fuel_handling_cost",
        "fuel_heat_content",
        "fuel_mixture",
        "fuel_sulfur",
        "high_breakpoint_p",
        "low_breakpoint_p",
    )

    fossil_fuel_type: FuelType | None
    fuel_cost: float | None  # CostPerHeatUnit
    fuel_dispatch_cost: float | None  # CostPerHeatUnit
    fuel_eff_factor: float | None  # PU
    fuel_handling_cost: float | None  # CostPerHeatUnit
    fuel_heat_content: float | None
    fuel_mixture: float | None  # PerCent
    fuel_sulfur: float | None  # PU
    high_breakpoint_p: float | None  # ActivePower
    low_breakpoint_p: float | None  # ActivePower

    thermal_generating_unit: One[ThermalGeneratingUnit] = One(
        EndMeta(
            name="thermal_generating_unit",
            cim_role="ThermalGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="fossil_fuels",
            aggregation="none",
        )
    )
    fuel_allocation_schedules: Many[FuelAllocationSchedule] = Many(
        EndMeta(
            name="fuel_allocation_schedules",
            cim_role="FuelAllocationSchedules",
            target="cim_python_sdk.model.iec61970.base.generation.production.fuel_allocation_schedule:FuelAllocationSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="fossil_fuel",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FossilFuel",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{CEB38297-AEE1-4b55-8ECC-272DE5EDA874}",
        attributes=(
            AttrMeta("fossil_fuel_type", "fossilFuelType", "FuelType", 0, 1, "enumeration"),
            AttrMeta("fuel_cost", "fuelCost", "CostPerHeatUnit", 0, 1, "cimdatatype"),
            AttrMeta(
                "fuel_dispatch_cost", "fuelDispatchCost", "CostPerHeatUnit", 0, 1, "cimdatatype"
            ),
            AttrMeta("fuel_eff_factor", "fuelEffFactor", "PU", 0, 1, "cimdatatype"),
            AttrMeta(
                "fuel_handling_cost", "fuelHandlingCost", "CostPerHeatUnit", 0, 1, "cimdatatype"
            ),
            AttrMeta("fuel_heat_content", "fuelHeatContent", "float", 0, 1, "primitive"),
            AttrMeta("fuel_mixture", "fuelMixture", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("fuel_sulfur", "fuelSulfur", "PU", 0, 1, "cimdatatype"),
            AttrMeta("high_breakpoint_p", "highBreakpointP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("low_breakpoint_p", "lowBreakpointP", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            thermal_generating_unit.meta,
            fuel_allocation_schedules.meta,
        ),
    )

    def __init__(
        self,
        *,
        fossil_fuel_type: FuelType | None = None,
        fuel_cost: float | None = None,
        fuel_dispatch_cost: float | None = None,
        fuel_eff_factor: float | None = None,
        fuel_handling_cost: float | None = None,
        fuel_heat_content: float | None = None,
        fuel_mixture: float | None = None,
        fuel_sulfur: float | None = None,
        high_breakpoint_p: float | None = None,
        low_breakpoint_p: float | None = None,
        thermal_generating_unit: ThermalGeneratingUnit | None = None,
        fuel_allocation_schedules: Iterable[FuelAllocationSchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.fossil_fuel_type = fossil_fuel_type
        self.fuel_cost = fuel_cost
        self.fuel_dispatch_cost = fuel_dispatch_cost
        self.fuel_eff_factor = fuel_eff_factor
        self.fuel_handling_cost = fuel_handling_cost
        self.fuel_heat_content = fuel_heat_content
        self.fuel_mixture = fuel_mixture
        self.fuel_sulfur = fuel_sulfur
        self.high_breakpoint_p = high_breakpoint_p
        self.low_breakpoint_p = low_breakpoint_p
        if thermal_generating_unit is not None:
            self.thermal_generating_unit = thermal_generating_unit
        if fuel_allocation_schedules is not None:
            FossilFuel.fuel_allocation_schedules.extend(self, fuel_allocation_schedules)

    def add_fuel_allocation_schedule(
        self, fuel_allocation_schedule: FuelAllocationSchedule
    ) -> Self:
        return FossilFuel.fuel_allocation_schedules.add(self, fuel_allocation_schedule)

    def remove_fuel_allocation_schedule(
        self, fuel_allocation_schedule: FuelAllocationSchedule
    ) -> Self:
        return FossilFuel.fuel_allocation_schedules.remove(self, fuel_allocation_schedule)

    def clear_fuel_allocation_schedules(self) -> Self:
        return FossilFuel.fuel_allocation_schedules.clear(self)

    def num_fuel_allocation_schedule(self) -> int:
        return FossilFuel.fuel_allocation_schedules.count(self)

    def get_fuel_allocation_schedule_by_mrid(self, mrid: str) -> FuelAllocationSchedule | None:
        return FossilFuel.fuel_allocation_schedules.get_by_mrid(self, mrid)
