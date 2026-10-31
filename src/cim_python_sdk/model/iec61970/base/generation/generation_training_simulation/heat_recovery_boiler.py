"""CIM class HeatRecoveryBoiler (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.fossil_steam_supply import (
    FossilSteamSupply,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.combustion_turbine import (
        CombustionTurbine,
    )


class HeatRecoveryBoiler(FossilSteamSupply):
    """The heat recovery system associated with combustion turbines in order to produce steam
    for combined cycle plants."""

    __slots__ = ("_combustion_turbines", "steam_supply_rating2")

    steam_supply_rating2: float | None

    combustion_turbines: Many[CombustionTurbine] = Many(
        EndMeta(
            name="combustion_turbines",
            cim_role="CombustionTurbines",
            target="cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.combustion_turbine:CombustionTurbine",
            many=True,
            lower=0,
            upper=None,
            inverse="heat_recovery_boiler",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HeatRecoveryBoiler",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{CC23120F-6FA7-48b4-8366-F5C6A57FF2FF}",
        attributes=(
            AttrMeta("steam_supply_rating2", "steamSupplyRating2", "float", 0, 1, "primitive"),
        ),
        ends=(combustion_turbines.meta,),
    )

    def __init__(
        self,
        *,
        steam_supply_rating2: float | None = None,
        combustion_turbines: Iterable[CombustionTurbine] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.steam_supply_rating2 = steam_supply_rating2
        if combustion_turbines is not None:
            HeatRecoveryBoiler.combustion_turbines.extend(self, combustion_turbines)

    def add_combustion_turbine(self, combustion_turbine: CombustionTurbine) -> Self:
        return HeatRecoveryBoiler.combustion_turbines.add(self, combustion_turbine)

    def remove_combustion_turbine(self, combustion_turbine: CombustionTurbine) -> Self:
        return HeatRecoveryBoiler.combustion_turbines.remove(self, combustion_turbine)

    def clear_combustion_turbines(self) -> Self:
        return HeatRecoveryBoiler.combustion_turbines.clear(self)

    def num_combustion_turbine(self) -> int:
        return HeatRecoveryBoiler.combustion_turbines.count(self)

    def get_combustion_turbine_by_mrid(self, mrid: str) -> CombustionTurbine | None:
        return HeatRecoveryBoiler.combustion_turbines.get_by_mrid(self, mrid)
