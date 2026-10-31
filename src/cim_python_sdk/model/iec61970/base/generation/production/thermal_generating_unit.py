"""CIM class ThermalGeneratingUnit (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import GeneratingUnit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.production.caes_plant import CAESPlant
    from cim_python_sdk.model.iec61970.base.generation.production.cogeneration_plant import (
        CogenerationPlant,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.combined_cycle_plant import (
        CombinedCyclePlant,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.emission_account import (
        EmissionAccount,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.emission_curve import (
        EmissionCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.fossil_fuel import FossilFuel
    from cim_python_sdk.model.iec61970.base.generation.production.fuel_allocation_schedule import (
        FuelAllocationSchedule,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.heat_input_curve import (
        HeatInputCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.heat_rate_curve import (
        HeatRateCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.incremental_heat_rate_curve import (
        IncrementalHeatRateCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.shutdown_curve import (
        ShutdownCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.startup_model import StartupModel


class ThermalGeneratingUnit(GeneratingUnit):
    """A generating unit whose prime mover could be a steam turbine, combustion turbine, or
    diesel engine."""

    __slots__ = (
        "_caes_plant",
        "_cogeneration_plant",
        "_combined_cycle_plant",
        "_emission_curves",
        "_emmission_accounts",
        "_fossil_fuels",
        "_fuel_allocation_schedules",
        "_heat_input_curve",
        "_heat_rate_curve",
        "_incremental_heat_rate_curve",
        "_shutdown_curve",
        "_startup_model",
        "o_m_cost",
    )

    o_m_cost: float | None  # CostPerHeatUnit

    emmission_accounts: Many[EmissionAccount] = Many(
        EndMeta(
            name="emmission_accounts",
            cim_role="EmmissionAccounts",
            target="cim_python_sdk.model.iec61970.base.generation.production.emission_account:EmissionAccount",
            many=True,
            lower=0,
            upper=None,
            inverse="thermal_generating_unit",
            aggregation="shared",
        )
    )
    heat_input_curve: One[HeatInputCurve] = One(
        EndMeta(
            name="heat_input_curve",
            cim_role="HeatInputCurve",
            target="cim_python_sdk.model.iec61970.base.generation.production.heat_input_curve:HeatInputCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="thermal_generating_unit",
            aggregation="shared",
        )
    )
    combined_cycle_plant: One[CombinedCyclePlant] = One(
        EndMeta(
            name="combined_cycle_plant",
            cim_role="CombinedCyclePlant",
            target="cim_python_sdk.model.iec61970.base.generation.production.combined_cycle_plant:CombinedCyclePlant",
            many=False,
            lower=0,
            upper=1,
            inverse="thermal_generating_units",
            aggregation="none",
        )
    )
    caes_plant: One[CAESPlant] = One(
        EndMeta(
            name="caes_plant",
            cim_role="CAESPlant",
            target="cim_python_sdk.model.iec61970.base.generation.production.caes_plant:CAESPlant",
            many=False,
            lower=0,
            upper=1,
            inverse="thermal_generating_unit",
            aggregation="none",
        )
    )
    fossil_fuels: Many[FossilFuel] = Many(
        EndMeta(
            name="fossil_fuels",
            cim_role="FossilFuels",
            target="cim_python_sdk.model.iec61970.base.generation.production.fossil_fuel:FossilFuel",
            many=True,
            lower=0,
            upper=None,
            inverse="thermal_generating_unit",
            aggregation="none",
        )
    )
    incremental_heat_rate_curve: One[IncrementalHeatRateCurve] = One(
        EndMeta(
            name="incremental_heat_rate_curve",
            cim_role="IncrementalHeatRateCurve",
            target="cim_python_sdk.model.iec61970.base.generation.production.incremental_heat_rate_curve:IncrementalHeatRateCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="thermal_generating_unit",
            aggregation="shared",
        )
    )
    shutdown_curve: One[ShutdownCurve] = One(
        EndMeta(
            name="shutdown_curve",
            cim_role="ShutdownCurve",
            target="cim_python_sdk.model.iec61970.base.generation.production.shutdown_curve:ShutdownCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="thermal_generating_unit",
            aggregation="shared",
        )
    )
    emission_curves: Many[EmissionCurve] = Many(
        EndMeta(
            name="emission_curves",
            cim_role="EmissionCurves",
            target="cim_python_sdk.model.iec61970.base.generation.production.emission_curve:EmissionCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="thermal_generating_unit",
            aggregation="shared",
        )
    )
    startup_model: One[StartupModel] = One(
        EndMeta(
            name="startup_model",
            cim_role="StartupModel",
            target="cim_python_sdk.model.iec61970.base.generation.production.startup_model:StartupModel",
            many=False,
            lower=0,
            upper=1,
            inverse="thermal_generating_unit",
            aggregation="shared",
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
            inverse="thermal_generating_unit",
            aggregation="shared",
        )
    )
    cogeneration_plant: One[CogenerationPlant] = One(
        EndMeta(
            name="cogeneration_plant",
            cim_role="CogenerationPlant",
            target="cim_python_sdk.model.iec61970.base.generation.production.cogeneration_plant:CogenerationPlant",
            many=False,
            lower=0,
            upper=1,
            inverse="thermal_generating_units",
            aggregation="none",
        )
    )
    heat_rate_curve: One[HeatRateCurve] = One(
        EndMeta(
            name="heat_rate_curve",
            cim_role="HeatRateCurve",
            target="cim_python_sdk.model.iec61970.base.generation.production.heat_rate_curve:HeatRateCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="thermal_generating_unit",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ThermalGeneratingUnit",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{74F16962-C880-450f-8B4F-0CFBD6BEF79A}",
        attributes=(AttrMeta("o_m_cost", "oMCost", "CostPerHeatUnit", 0, 1, "cimdatatype"),),
        ends=(
            emmission_accounts.meta,
            heat_input_curve.meta,
            combined_cycle_plant.meta,
            caes_plant.meta,
            fossil_fuels.meta,
            incremental_heat_rate_curve.meta,
            shutdown_curve.meta,
            emission_curves.meta,
            startup_model.meta,
            fuel_allocation_schedules.meta,
            cogeneration_plant.meta,
            heat_rate_curve.meta,
        ),
    )

    def __init__(
        self,
        *,
        o_m_cost: float | None = None,
        emmission_accounts: Iterable[EmissionAccount] | None = None,
        heat_input_curve: HeatInputCurve | None = None,
        combined_cycle_plant: CombinedCyclePlant | None = None,
        caes_plant: CAESPlant | None = None,
        fossil_fuels: Iterable[FossilFuel] | None = None,
        incremental_heat_rate_curve: IncrementalHeatRateCurve | None = None,
        shutdown_curve: ShutdownCurve | None = None,
        emission_curves: Iterable[EmissionCurve] | None = None,
        startup_model: StartupModel | None = None,
        fuel_allocation_schedules: Iterable[FuelAllocationSchedule] | None = None,
        cogeneration_plant: CogenerationPlant | None = None,
        heat_rate_curve: HeatRateCurve | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.o_m_cost = o_m_cost
        if emmission_accounts is not None:
            ThermalGeneratingUnit.emmission_accounts.extend(self, emmission_accounts)
        if heat_input_curve is not None:
            self.heat_input_curve = heat_input_curve
        if combined_cycle_plant is not None:
            self.combined_cycle_plant = combined_cycle_plant
        if caes_plant is not None:
            self.caes_plant = caes_plant
        if fossil_fuels is not None:
            ThermalGeneratingUnit.fossil_fuels.extend(self, fossil_fuels)
        if incremental_heat_rate_curve is not None:
            self.incremental_heat_rate_curve = incremental_heat_rate_curve
        if shutdown_curve is not None:
            self.shutdown_curve = shutdown_curve
        if emission_curves is not None:
            ThermalGeneratingUnit.emission_curves.extend(self, emission_curves)
        if startup_model is not None:
            self.startup_model = startup_model
        if fuel_allocation_schedules is not None:
            ThermalGeneratingUnit.fuel_allocation_schedules.extend(self, fuel_allocation_schedules)
        if cogeneration_plant is not None:
            self.cogeneration_plant = cogeneration_plant
        if heat_rate_curve is not None:
            self.heat_rate_curve = heat_rate_curve

    def add_emmission_account(self, emmission_account: EmissionAccount) -> Self:
        return ThermalGeneratingUnit.emmission_accounts.add(self, emmission_account)

    def remove_emmission_account(self, emmission_account: EmissionAccount) -> Self:
        return ThermalGeneratingUnit.emmission_accounts.remove(self, emmission_account)

    def clear_emmission_accounts(self) -> Self:
        return ThermalGeneratingUnit.emmission_accounts.clear(self)

    def num_emmission_account(self) -> int:
        return ThermalGeneratingUnit.emmission_accounts.count(self)

    def get_emmission_account_by_mrid(self, mrid: str) -> EmissionAccount | None:
        return ThermalGeneratingUnit.emmission_accounts.get_by_mrid(self, mrid)

    def add_fossil_fuel(self, fossil_fuel: FossilFuel) -> Self:
        return ThermalGeneratingUnit.fossil_fuels.add(self, fossil_fuel)

    def remove_fossil_fuel(self, fossil_fuel: FossilFuel) -> Self:
        return ThermalGeneratingUnit.fossil_fuels.remove(self, fossil_fuel)

    def clear_fossil_fuels(self) -> Self:
        return ThermalGeneratingUnit.fossil_fuels.clear(self)

    def num_fossil_fuel(self) -> int:
        return ThermalGeneratingUnit.fossil_fuels.count(self)

    def get_fossil_fuel_by_mrid(self, mrid: str) -> FossilFuel | None:
        return ThermalGeneratingUnit.fossil_fuels.get_by_mrid(self, mrid)

    def add_emission_curve(self, emission_curve: EmissionCurve) -> Self:
        return ThermalGeneratingUnit.emission_curves.add(self, emission_curve)

    def remove_emission_curve(self, emission_curve: EmissionCurve) -> Self:
        return ThermalGeneratingUnit.emission_curves.remove(self, emission_curve)

    def clear_emission_curves(self) -> Self:
        return ThermalGeneratingUnit.emission_curves.clear(self)

    def num_emission_curve(self) -> int:
        return ThermalGeneratingUnit.emission_curves.count(self)

    def get_emission_curve_by_mrid(self, mrid: str) -> EmissionCurve | None:
        return ThermalGeneratingUnit.emission_curves.get_by_mrid(self, mrid)

    def add_fuel_allocation_schedule(
        self, fuel_allocation_schedule: FuelAllocationSchedule
    ) -> Self:
        return ThermalGeneratingUnit.fuel_allocation_schedules.add(self, fuel_allocation_schedule)

    def remove_fuel_allocation_schedule(
        self, fuel_allocation_schedule: FuelAllocationSchedule
    ) -> Self:
        return ThermalGeneratingUnit.fuel_allocation_schedules.remove(
            self, fuel_allocation_schedule
        )

    def clear_fuel_allocation_schedules(self) -> Self:
        return ThermalGeneratingUnit.fuel_allocation_schedules.clear(self)

    def num_fuel_allocation_schedule(self) -> int:
        return ThermalGeneratingUnit.fuel_allocation_schedules.count(self)

    def get_fuel_allocation_schedule_by_mrid(self, mrid: str) -> FuelAllocationSchedule | None:
        return ThermalGeneratingUnit.fuel_allocation_schedules.get_by_mrid(self, mrid)
