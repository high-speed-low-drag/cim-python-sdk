"""CIM class Reservoir (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.production.hydro_power_plant import (
        HydroPowerPlant,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.inflow_forecast import (
        InflowForecast,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.level_vs_volume_curve import (
        LevelVsVolumeCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.target_level_schedule import (
        TargetLevelSchedule,
    )


class Reservoir(PowerSystemResource):
    """A water storage facility within a hydro system, including: ponds, lakes, lagoons, and
    rivers. The storage is usually behind some type of dam."""

    __slots__ = (
        "_hydro_power_plants",
        "_inflow_forecasts",
        "_level_vs_volume_curves",
        "_spills_from_reservoir",
        "_spills_into_reservoirs",
        "_target_level_schedule",
        "_upstream_from_hydro_power_plants",
        "active_storage_capacity",
        "energy_storage_rating",
        "full_supply_level",
        "gross_capacity",
        "normal_min_operate_level",
        "river_outlet_works",
        "spill_travel_delay",
        "spill_way_gate_type",
        "spillway_capacity",
        "spillway_crest_length",
        "spillway_crest_level",
    )

    active_storage_capacity: float | None  # Volume
    energy_storage_rating: float | None
    full_supply_level: float | None  # WaterLevel
    gross_capacity: float | None  # Volume
    normal_min_operate_level: float | None  # WaterLevel
    river_outlet_works: str | None
    spill_travel_delay: float | None  # Seconds
    spillway_capacity: float | None
    spillway_crest_length: float | None  # Length
    spillway_crest_level: float | None  # WaterLevel
    spill_way_gate_type: str | None

    upstream_from_hydro_power_plants: Many[HydroPowerPlant] = Many(
        EndMeta(
            name="upstream_from_hydro_power_plants",
            cim_role="UpstreamFromHydroPowerPlants",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_power_plant:HydroPowerPlant",
            many=True,
            lower=0,
            upper=None,
            inverse="gen_source_pump_discharge_reservoir",
            aggregation="none",
        )
    )
    level_vs_volume_curves: Many[LevelVsVolumeCurve] = Many(
        EndMeta(
            name="level_vs_volume_curves",
            cim_role="LevelVsVolumeCurves",
            target="cim_python_sdk.model.iec61970.base.generation.production.level_vs_volume_curve:LevelVsVolumeCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="reservoir",
            aggregation="shared",
        )
    )
    hydro_power_plants: Many[HydroPowerPlant] = Many(
        EndMeta(
            name="hydro_power_plants",
            cim_role="HydroPowerPlants",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_power_plant:HydroPowerPlant",
            many=True,
            lower=0,
            upper=None,
            inverse="reservoir",
            aggregation="none",
        )
    )
    inflow_forecasts: Many[InflowForecast] = Many(
        EndMeta(
            name="inflow_forecasts",
            cim_role="InflowForecasts",
            target="cim_python_sdk.model.iec61970.base.generation.production.inflow_forecast:InflowForecast",
            many=True,
            lower=0,
            upper=None,
            inverse="reservoir",
            aggregation="shared",
        )
    )
    target_level_schedule: One[TargetLevelSchedule] = One(
        EndMeta(
            name="target_level_schedule",
            cim_role="TargetLevelSchedule",
            target="cim_python_sdk.model.iec61970.base.generation.production.target_level_schedule:TargetLevelSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="reservoir",
            aggregation="shared",
        )
    )
    spills_into_reservoirs: Many[Reservoir] = Many(
        EndMeta(
            name="spills_into_reservoirs",
            cim_role="SpillsIntoReservoirs",
            target="cim_python_sdk.model.iec61970.base.generation.production.reservoir:Reservoir",
            many=True,
            lower=0,
            upper=None,
            inverse="spills_from_reservoir",
            aggregation="none",
        )
    )
    spills_from_reservoir: One[Reservoir] = One(
        EndMeta(
            name="spills_from_reservoir",
            cim_role="SpillsFromReservoir",
            target="cim_python_sdk.model.iec61970.base.generation.production.reservoir:Reservoir",
            many=False,
            lower=0,
            upper=1,
            inverse="spills_into_reservoirs",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Reservoir",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{7702412B-7FEB-4af0-9785-C4FDBEB525F0}",
        attributes=(
            AttrMeta(
                "active_storage_capacity", "activeStorageCapacity", "Volume", 0, 1, "cimdatatype"
            ),
            AttrMeta("energy_storage_rating", "energyStorageRating", "float", 0, 1, "primitive"),
            AttrMeta("full_supply_level", "fullSupplyLevel", "WaterLevel", 0, 1, "cimdatatype"),
            AttrMeta("gross_capacity", "grossCapacity", "Volume", 0, 1, "cimdatatype"),
            AttrMeta(
                "normal_min_operate_level",
                "normalMinOperateLevel",
                "WaterLevel",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("river_outlet_works", "riverOutletWorks", "str", 0, 1, "primitive"),
            AttrMeta("spill_travel_delay", "spillTravelDelay", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("spillway_capacity", "spillwayCapacity", "float", 0, 1, "primitive"),
            AttrMeta("spillway_crest_length", "spillwayCrestLength", "Length", 0, 1, "cimdatatype"),
            AttrMeta(
                "spillway_crest_level", "spillwayCrestLevel", "WaterLevel", 0, 1, "cimdatatype"
            ),
            AttrMeta("spill_way_gate_type", "spillWayGateType", "str", 0, 1, "primitive"),
        ),
        ends=(
            upstream_from_hydro_power_plants.meta,
            level_vs_volume_curves.meta,
            hydro_power_plants.meta,
            inflow_forecasts.meta,
            target_level_schedule.meta,
            spills_into_reservoirs.meta,
            spills_from_reservoir.meta,
        ),
    )

    def __init__(
        self,
        *,
        active_storage_capacity: float | None = None,
        energy_storage_rating: float | None = None,
        full_supply_level: float | None = None,
        gross_capacity: float | None = None,
        normal_min_operate_level: float | None = None,
        river_outlet_works: str | None = None,
        spill_travel_delay: float | None = None,
        spillway_capacity: float | None = None,
        spillway_crest_length: float | None = None,
        spillway_crest_level: float | None = None,
        spill_way_gate_type: str | None = None,
        upstream_from_hydro_power_plants: Iterable[HydroPowerPlant] | None = None,
        level_vs_volume_curves: Iterable[LevelVsVolumeCurve] | None = None,
        hydro_power_plants: Iterable[HydroPowerPlant] | None = None,
        inflow_forecasts: Iterable[InflowForecast] | None = None,
        target_level_schedule: TargetLevelSchedule | None = None,
        spills_into_reservoirs: Iterable[Reservoir] | None = None,
        spills_from_reservoir: Reservoir | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.active_storage_capacity = active_storage_capacity
        self.energy_storage_rating = energy_storage_rating
        self.full_supply_level = full_supply_level
        self.gross_capacity = gross_capacity
        self.normal_min_operate_level = normal_min_operate_level
        self.river_outlet_works = river_outlet_works
        self.spill_travel_delay = spill_travel_delay
        self.spillway_capacity = spillway_capacity
        self.spillway_crest_length = spillway_crest_length
        self.spillway_crest_level = spillway_crest_level
        self.spill_way_gate_type = spill_way_gate_type
        if upstream_from_hydro_power_plants is not None:
            Reservoir.upstream_from_hydro_power_plants.extend(
                self, upstream_from_hydro_power_plants
            )
        if level_vs_volume_curves is not None:
            Reservoir.level_vs_volume_curves.extend(self, level_vs_volume_curves)
        if hydro_power_plants is not None:
            Reservoir.hydro_power_plants.extend(self, hydro_power_plants)
        if inflow_forecasts is not None:
            Reservoir.inflow_forecasts.extend(self, inflow_forecasts)
        if target_level_schedule is not None:
            self.target_level_schedule = target_level_schedule
        if spills_into_reservoirs is not None:
            Reservoir.spills_into_reservoirs.extend(self, spills_into_reservoirs)
        if spills_from_reservoir is not None:
            self.spills_from_reservoir = spills_from_reservoir

    def add_upstream_from_hydro_power_plant(
        self, upstream_from_hydro_power_plant: HydroPowerPlant
    ) -> Self:
        return Reservoir.upstream_from_hydro_power_plants.add(self, upstream_from_hydro_power_plant)

    def remove_upstream_from_hydro_power_plant(
        self, upstream_from_hydro_power_plant: HydroPowerPlant
    ) -> Self:
        return Reservoir.upstream_from_hydro_power_plants.remove(
            self, upstream_from_hydro_power_plant
        )

    def clear_upstream_from_hydro_power_plants(self) -> Self:
        return Reservoir.upstream_from_hydro_power_plants.clear(self)

    def num_upstream_from_hydro_power_plant(self) -> int:
        return Reservoir.upstream_from_hydro_power_plants.count(self)

    def get_upstream_from_hydro_power_plant_by_mrid(self, mrid: str) -> HydroPowerPlant | None:
        return Reservoir.upstream_from_hydro_power_plants.get_by_mrid(self, mrid)

    def add_level_vs_volume_curve(self, level_vs_volume_curve: LevelVsVolumeCurve) -> Self:
        return Reservoir.level_vs_volume_curves.add(self, level_vs_volume_curve)

    def remove_level_vs_volume_curve(self, level_vs_volume_curve: LevelVsVolumeCurve) -> Self:
        return Reservoir.level_vs_volume_curves.remove(self, level_vs_volume_curve)

    def clear_level_vs_volume_curves(self) -> Self:
        return Reservoir.level_vs_volume_curves.clear(self)

    def num_level_vs_volume_curve(self) -> int:
        return Reservoir.level_vs_volume_curves.count(self)

    def get_level_vs_volume_curve_by_mrid(self, mrid: str) -> LevelVsVolumeCurve | None:
        return Reservoir.level_vs_volume_curves.get_by_mrid(self, mrid)

    def add_hydro_power_plant(self, hydro_power_plant: HydroPowerPlant) -> Self:
        return Reservoir.hydro_power_plants.add(self, hydro_power_plant)

    def remove_hydro_power_plant(self, hydro_power_plant: HydroPowerPlant) -> Self:
        return Reservoir.hydro_power_plants.remove(self, hydro_power_plant)

    def clear_hydro_power_plants(self) -> Self:
        return Reservoir.hydro_power_plants.clear(self)

    def num_hydro_power_plant(self) -> int:
        return Reservoir.hydro_power_plants.count(self)

    def get_hydro_power_plant_by_mrid(self, mrid: str) -> HydroPowerPlant | None:
        return Reservoir.hydro_power_plants.get_by_mrid(self, mrid)

    def add_inflow_forecast(self, inflow_forecast: InflowForecast) -> Self:
        return Reservoir.inflow_forecasts.add(self, inflow_forecast)

    def remove_inflow_forecast(self, inflow_forecast: InflowForecast) -> Self:
        return Reservoir.inflow_forecasts.remove(self, inflow_forecast)

    def clear_inflow_forecasts(self) -> Self:
        return Reservoir.inflow_forecasts.clear(self)

    def num_inflow_forecast(self) -> int:
        return Reservoir.inflow_forecasts.count(self)

    def get_inflow_forecast_by_mrid(self, mrid: str) -> InflowForecast | None:
        return Reservoir.inflow_forecasts.get_by_mrid(self, mrid)

    def add_spills_into_reservoir(self, spills_into_reservoir: Reservoir) -> Self:
        return Reservoir.spills_into_reservoirs.add(self, spills_into_reservoir)

    def remove_spills_into_reservoir(self, spills_into_reservoir: Reservoir) -> Self:
        return Reservoir.spills_into_reservoirs.remove(self, spills_into_reservoir)

    def clear_spills_into_reservoirs(self) -> Self:
        return Reservoir.spills_into_reservoirs.clear(self)

    def num_spills_into_reservoir(self) -> int:
        return Reservoir.spills_into_reservoirs.count(self)

    def get_spills_into_reservoir_by_mrid(self, mrid: str) -> Reservoir | None:
        return Reservoir.spills_into_reservoirs.get_by_mrid(self, mrid)
