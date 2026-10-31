"""CIM class FuelAllocationSchedule (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.fossil_fuel import FossilFuel
    from cim_python_sdk.model.iec61970.base.generation.production.fuel_type import FuelType
    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class FuelAllocationSchedule(Curve):
    """The amount of fuel of a given type which is allocated for consumption over a specified
    period of time."""

    __slots__ = (
        "_fossil_fuel",
        "_thermal_generating_unit",
        "fuel_allocation_end_date",
        "fuel_allocation_start_date",
        "fuel_type",
        "max_fuel_allocation",
        "min_fuel_allocation",
    )

    fuel_allocation_end_date: _dt.datetime | None
    fuel_allocation_start_date: _dt.datetime | None
    fuel_type: FuelType | None
    max_fuel_allocation: float | None
    min_fuel_allocation: float | None

    thermal_generating_unit: One[ThermalGeneratingUnit] = One(
        EndMeta(
            name="thermal_generating_unit",
            cim_role="ThermalGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="fuel_allocation_schedules",
            aggregation="none",
        )
    )
    fossil_fuel: One[FossilFuel] = One(
        EndMeta(
            name="fossil_fuel",
            cim_role="FossilFuel",
            target="cim_python_sdk.model.iec61970.base.generation.production.fossil_fuel:FossilFuel",
            many=False,
            lower=1,
            upper=1,
            inverse="fuel_allocation_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FuelAllocationSchedule",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{B21C6F0E-95AD-4069-A317-588C262B1EF0}",
        attributes=(
            AttrMeta(
                "fuel_allocation_end_date", "fuelAllocationEndDate", "datetime", 0, 1, "primitive"
            ),
            AttrMeta(
                "fuel_allocation_start_date",
                "fuelAllocationStartDate",
                "datetime",
                0,
                1,
                "primitive",
            ),
            AttrMeta("fuel_type", "fuelType", "FuelType", 0, 1, "enumeration"),
            AttrMeta("max_fuel_allocation", "maxFuelAllocation", "float", 0, 1, "primitive"),
            AttrMeta("min_fuel_allocation", "minFuelAllocation", "float", 0, 1, "primitive"),
        ),
        ends=(
            thermal_generating_unit.meta,
            fossil_fuel.meta,
        ),
    )

    def __init__(
        self,
        *,
        fuel_allocation_end_date: _dt.datetime | None = None,
        fuel_allocation_start_date: _dt.datetime | None = None,
        fuel_type: FuelType | None = None,
        max_fuel_allocation: float | None = None,
        min_fuel_allocation: float | None = None,
        thermal_generating_unit: ThermalGeneratingUnit | None = None,
        fossil_fuel: FossilFuel | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.fuel_allocation_end_date = fuel_allocation_end_date
        self.fuel_allocation_start_date = fuel_allocation_start_date
        self.fuel_type = fuel_type
        self.max_fuel_allocation = max_fuel_allocation
        self.min_fuel_allocation = min_fuel_allocation
        if thermal_generating_unit is not None:
            self.thermal_generating_unit = thermal_generating_unit
        if fossil_fuel is not None:
            self.fossil_fuel = fossil_fuel
