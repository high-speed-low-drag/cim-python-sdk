"""CIM class CogenerationPlant (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.production.steam_sendout_schedule import (
        SteamSendoutSchedule,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class CogenerationPlant(PowerSystemResource):
    """A set of thermal generating units for the production of electrical energy and process
    steam (usually from the output of the steam turbines). The steam sendout is typically
    used for industrial purposes or for municipal heating and cooling."""

    __slots__ = (
        "_steam_sendout_schedule",
        "_thermal_generating_units",
        "cogen_hp_sendout_rating",
        "cogen_hp_steam_rating",
        "cogen_lp_sendout_rating",
        "cogen_lp_steam_rating",
        "rated_p",
    )

    cogen_hp_sendout_rating: float | None
    cogen_hp_steam_rating: float | None
    cogen_lp_sendout_rating: float | None
    cogen_lp_steam_rating: float | None
    rated_p: float | None  # ActivePower

    steam_sendout_schedule: One[SteamSendoutSchedule] = One(
        EndMeta(
            name="steam_sendout_schedule",
            cim_role="SteamSendoutSchedule",
            target="cim_python_sdk.model.iec61970.base.generation.production.steam_sendout_schedule:SteamSendoutSchedule",
            many=False,
            lower=1,
            upper=1,
            inverse="cogeneration_plant",
            aggregation="shared",
        )
    )
    thermal_generating_units: Many[ThermalGeneratingUnit] = Many(
        EndMeta(
            name="thermal_generating_units",
            cim_role="ThermalGeneratingUnits",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="cogeneration_plant",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CogenerationPlant",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{E9D71516-7D2D-44d5-944E-C1E43E8D365E}",
        attributes=(
            AttrMeta("cogen_hp_sendout_rating", "cogenHPSendoutRating", "float", 0, 1, "primitive"),
            AttrMeta("cogen_hp_steam_rating", "cogenHPSteamRating", "float", 0, 1, "primitive"),
            AttrMeta("cogen_lp_sendout_rating", "cogenLPSendoutRating", "float", 0, 1, "primitive"),
            AttrMeta("cogen_lp_steam_rating", "cogenLPSteamRating", "float", 0, 1, "primitive"),
            AttrMeta("rated_p", "ratedP", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            steam_sendout_schedule.meta,
            thermal_generating_units.meta,
        ),
    )

    def __init__(
        self,
        *,
        cogen_hp_sendout_rating: float | None = None,
        cogen_hp_steam_rating: float | None = None,
        cogen_lp_sendout_rating: float | None = None,
        cogen_lp_steam_rating: float | None = None,
        rated_p: float | None = None,
        steam_sendout_schedule: SteamSendoutSchedule | None = None,
        thermal_generating_units: Iterable[ThermalGeneratingUnit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cogen_hp_sendout_rating = cogen_hp_sendout_rating
        self.cogen_hp_steam_rating = cogen_hp_steam_rating
        self.cogen_lp_sendout_rating = cogen_lp_sendout_rating
        self.cogen_lp_steam_rating = cogen_lp_steam_rating
        self.rated_p = rated_p
        if steam_sendout_schedule is not None:
            self.steam_sendout_schedule = steam_sendout_schedule
        if thermal_generating_units is not None:
            CogenerationPlant.thermal_generating_units.extend(self, thermal_generating_units)

    def add_thermal_generating_unit(self, thermal_generating_unit: ThermalGeneratingUnit) -> Self:
        return CogenerationPlant.thermal_generating_units.add(self, thermal_generating_unit)

    def remove_thermal_generating_unit(
        self, thermal_generating_unit: ThermalGeneratingUnit
    ) -> Self:
        return CogenerationPlant.thermal_generating_units.remove(self, thermal_generating_unit)

    def clear_thermal_generating_units(self) -> Self:
        return CogenerationPlant.thermal_generating_units.clear(self)

    def num_thermal_generating_unit(self) -> int:
        return CogenerationPlant.thermal_generating_units.count(self)

    def get_thermal_generating_unit_by_mrid(self, mrid: str) -> ThermalGeneratingUnit | None:
        return CogenerationPlant.thermal_generating_units.get_by_mrid(self, mrid)
