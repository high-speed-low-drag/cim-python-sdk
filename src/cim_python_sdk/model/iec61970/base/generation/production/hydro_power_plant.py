"""CIM class HydroPowerPlant (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_unit import (
        HydroGeneratingUnit,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.hydro_plant_storage_kind import (
        HydroPlantStorageKind,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.hydro_pump import HydroPump
    from cim_python_sdk.model.iec61970.base.generation.production.reservoir import Reservoir


class HydroPowerPlant(PowerSystemResource):
    """A hydro power station which can generate or pump. When generating, the generator
    turbines receive water from an upper reservoir. When pumping, the pumps receive their
    water from a lower reservoir."""

    __slots__ = (
        "_gen_source_pump_discharge_reservoir",
        "_hydro_generating_units",
        "_hydro_pumps",
        "_reservoir",
        "discharge_travel_delay",
        "gen_rated_p",
        "hydro_plant_storage_type",
        "penstock_type",
        "plant_discharge_capacity",
        "plant_rated_head",
        "pump_rated_p",
        "surge_tank_code",
        "surge_tank_crest_level",
    )

    discharge_travel_delay: float | None  # Seconds
    gen_rated_p: float | None  # ActivePower
    hydro_plant_storage_type: HydroPlantStorageKind | None
    penstock_type: str | None
    plant_discharge_capacity: float | None  # VolumeFlowRate
    plant_rated_head: float | None  # Length
    pump_rated_p: float | None  # ActivePower
    surge_tank_code: str | None
    surge_tank_crest_level: float | None  # WaterLevel

    gen_source_pump_discharge_reservoir: One[Reservoir] = One(
        EndMeta(
            name="gen_source_pump_discharge_reservoir",
            cim_role="GenSourcePumpDischargeReservoir",
            target="cim_python_sdk.model.iec61970.base.generation.production.reservoir:Reservoir",
            many=False,
            lower=1,
            upper=1,
            inverse="upstream_from_hydro_power_plants",
            aggregation="none",
        )
    )
    reservoir: One[Reservoir] = One(
        EndMeta(
            name="reservoir",
            cim_role="Reservoir",
            target="cim_python_sdk.model.iec61970.base.generation.production.reservoir:Reservoir",
            many=False,
            lower=0,
            upper=1,
            inverse="hydro_power_plants",
            aggregation="none",
        )
    )
    hydro_pumps: Many[HydroPump] = Many(
        EndMeta(
            name="hydro_pumps",
            cim_role="HydroPumps",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_pump:HydroPump",
            many=True,
            lower=0,
            upper=None,
            inverse="hydro_power_plant",
            aggregation="shared",
        )
    )
    hydro_generating_units: Many[HydroGeneratingUnit] = Many(
        EndMeta(
            name="hydro_generating_units",
            cim_role="HydroGeneratingUnits",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_unit:HydroGeneratingUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="hydro_power_plant",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HydroPowerPlant",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{363A5090-1D0E-40fc-91F1-7540EE479345}",
        attributes=(
            AttrMeta(
                "discharge_travel_delay", "dischargeTravelDelay", "Seconds", 0, 1, "cimdatatype"
            ),
            AttrMeta("gen_rated_p", "genRatedP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "hydro_plant_storage_type",
                "hydroPlantStorageType",
                "HydroPlantStorageKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("penstock_type", "penstockType", "str", 0, 1, "primitive"),
            AttrMeta(
                "plant_discharge_capacity",
                "plantDischargeCapacity",
                "VolumeFlowRate",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("plant_rated_head", "plantRatedHead", "Length", 0, 1, "cimdatatype"),
            AttrMeta("pump_rated_p", "pumpRatedP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("surge_tank_code", "surgeTankCode", "str", 0, 1, "primitive"),
            AttrMeta(
                "surge_tank_crest_level", "surgeTankCrestLevel", "WaterLevel", 0, 1, "cimdatatype"
            ),
        ),
        ends=(
            gen_source_pump_discharge_reservoir.meta,
            reservoir.meta,
            hydro_pumps.meta,
            hydro_generating_units.meta,
        ),
    )

    def __init__(
        self,
        *,
        discharge_travel_delay: float | None = None,
        gen_rated_p: float | None = None,
        hydro_plant_storage_type: HydroPlantStorageKind | None = None,
        penstock_type: str | None = None,
        plant_discharge_capacity: float | None = None,
        plant_rated_head: float | None = None,
        pump_rated_p: float | None = None,
        surge_tank_code: str | None = None,
        surge_tank_crest_level: float | None = None,
        gen_source_pump_discharge_reservoir: Reservoir | None = None,
        reservoir: Reservoir | None = None,
        hydro_pumps: Iterable[HydroPump] | None = None,
        hydro_generating_units: Iterable[HydroGeneratingUnit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.discharge_travel_delay = discharge_travel_delay
        self.gen_rated_p = gen_rated_p
        self.hydro_plant_storage_type = hydro_plant_storage_type
        self.penstock_type = penstock_type
        self.plant_discharge_capacity = plant_discharge_capacity
        self.plant_rated_head = plant_rated_head
        self.pump_rated_p = pump_rated_p
        self.surge_tank_code = surge_tank_code
        self.surge_tank_crest_level = surge_tank_crest_level
        if gen_source_pump_discharge_reservoir is not None:
            self.gen_source_pump_discharge_reservoir = gen_source_pump_discharge_reservoir
        if reservoir is not None:
            self.reservoir = reservoir
        if hydro_pumps is not None:
            HydroPowerPlant.hydro_pumps.extend(self, hydro_pumps)
        if hydro_generating_units is not None:
            HydroPowerPlant.hydro_generating_units.extend(self, hydro_generating_units)

    def add_hydro_pump(self, hydro_pump: HydroPump) -> Self:
        return HydroPowerPlant.hydro_pumps.add(self, hydro_pump)

    def remove_hydro_pump(self, hydro_pump: HydroPump) -> Self:
        return HydroPowerPlant.hydro_pumps.remove(self, hydro_pump)

    def clear_hydro_pumps(self) -> Self:
        return HydroPowerPlant.hydro_pumps.clear(self)

    def num_hydro_pump(self) -> int:
        return HydroPowerPlant.hydro_pumps.count(self)

    def get_hydro_pump_by_mrid(self, mrid: str) -> HydroPump | None:
        return HydroPowerPlant.hydro_pumps.get_by_mrid(self, mrid)

    def add_hydro_generating_unit(self, hydro_generating_unit: HydroGeneratingUnit) -> Self:
        return HydroPowerPlant.hydro_generating_units.add(self, hydro_generating_unit)

    def remove_hydro_generating_unit(self, hydro_generating_unit: HydroGeneratingUnit) -> Self:
        return HydroPowerPlant.hydro_generating_units.remove(self, hydro_generating_unit)

    def clear_hydro_generating_units(self) -> Self:
        return HydroPowerPlant.hydro_generating_units.clear(self)

    def num_hydro_generating_unit(self) -> int:
        return HydroPowerPlant.hydro_generating_units.count(self)

    def get_hydro_generating_unit_by_mrid(self, mrid: str) -> HydroGeneratingUnit | None:
        return HydroPowerPlant.hydro_generating_units.get_by_mrid(self, mrid)
