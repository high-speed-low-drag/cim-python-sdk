"""CIM class SteamSupply (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.steam_turbine import (
        SteamTurbine,
    )


class SteamSupply(PowerSystemResource):
    """Steam supply for steam turbine."""

    __slots__ = ("_steam_turbines", "steam_supply_rating")

    steam_supply_rating: float | None

    steam_turbines: Many[SteamTurbine] = Many(
        EndMeta(
            name="steam_turbines",
            cim_role="SteamTurbines",
            target="cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.steam_turbine:SteamTurbine",
            many=True,
            lower=0,
            upper=None,
            inverse="steam_supplys",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SteamSupply",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{EFFC79C3-293D-4a14-ADCA-E5F18F29951B}",
        attributes=(
            AttrMeta("steam_supply_rating", "steamSupplyRating", "float", 0, 1, "primitive"),
        ),
        ends=(steam_turbines.meta,),
    )

    def __init__(
        self,
        *,
        steam_supply_rating: float | None = None,
        steam_turbines: Iterable[SteamTurbine] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.steam_supply_rating = steam_supply_rating
        if steam_turbines is not None:
            SteamSupply.steam_turbines.extend(self, steam_turbines)

    def add_steam_turbine(self, steam_turbine: SteamTurbine) -> Self:
        return SteamSupply.steam_turbines.add(self, steam_turbine)

    def remove_steam_turbine(self, steam_turbine: SteamTurbine) -> Self:
        return SteamSupply.steam_turbines.remove(self, steam_turbine)

    def clear_steam_turbines(self) -> Self:
        return SteamSupply.steam_turbines.clear(self)

    def num_steam_turbine(self) -> int:
        return SteamSupply.steam_turbines.count(self)

    def get_steam_turbine_by_mrid(self, mrid: str) -> SteamTurbine | None:
        return SteamSupply.steam_turbines.get_by_mrid(self, mrid)
