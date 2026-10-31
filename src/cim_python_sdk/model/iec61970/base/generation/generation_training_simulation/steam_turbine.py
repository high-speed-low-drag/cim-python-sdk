"""CIM class SteamTurbine (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.prime_mover import (
    PrimeMover,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.steam_supply import (
        SteamSupply,
    )


class SteamTurbine(PrimeMover):
    """Steam turbine."""

    __slots__ = (
        "_steam_supplys",
        "crossover_tc",
        "reheater1_tc",
        "reheater2_tc",
        "shaft1_power_hp",
        "shaft1_power_ip",
        "shaft1_power_lp1",
        "shaft1_power_lp2",
        "shaft2_power_hp",
        "shaft2_power_ip",
        "shaft2_power_lp1",
        "shaft2_power_lp2",
        "steam_chest_tc",
    )

    crossover_tc: float | None  # Seconds
    reheater1_tc: float | None  # Seconds
    reheater2_tc: float | None  # Seconds
    shaft1_power_hp: float | None
    shaft1_power_ip: float | None
    shaft1_power_lp1: float | None
    shaft1_power_lp2: float | None
    shaft2_power_hp: float | None
    shaft2_power_ip: float | None
    shaft2_power_lp1: float | None
    shaft2_power_lp2: float | None
    steam_chest_tc: float | None  # Seconds

    steam_supplys: Many[SteamSupply] = Many(
        EndMeta(
            name="steam_supplys",
            cim_role="SteamSupplys",
            target="cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.steam_supply:SteamSupply",
            many=True,
            lower=0,
            upper=None,
            inverse="steam_turbines",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SteamTurbine",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{6195DBA1-8A7F-491e-BD36-AFF11AD6D563}",
        attributes=(
            AttrMeta("crossover_tc", "crossoverTC", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("reheater1_tc", "reheater1TC", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("reheater2_tc", "reheater2TC", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("shaft1_power_hp", "shaft1PowerHP", "float", 0, 1, "primitive"),
            AttrMeta("shaft1_power_ip", "shaft1PowerIP", "float", 0, 1, "primitive"),
            AttrMeta("shaft1_power_lp1", "shaft1PowerLP1", "float", 0, 1, "primitive"),
            AttrMeta("shaft1_power_lp2", "shaft1PowerLP2", "float", 0, 1, "primitive"),
            AttrMeta("shaft2_power_hp", "shaft2PowerHP", "float", 0, 1, "primitive"),
            AttrMeta("shaft2_power_ip", "shaft2PowerIP", "float", 0, 1, "primitive"),
            AttrMeta("shaft2_power_lp1", "shaft2PowerLP1", "float", 0, 1, "primitive"),
            AttrMeta("shaft2_power_lp2", "shaft2PowerLP2", "float", 0, 1, "primitive"),
            AttrMeta("steam_chest_tc", "steamChestTC", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(steam_supplys.meta,),
    )

    def __init__(
        self,
        *,
        crossover_tc: float | None = None,
        reheater1_tc: float | None = None,
        reheater2_tc: float | None = None,
        shaft1_power_hp: float | None = None,
        shaft1_power_ip: float | None = None,
        shaft1_power_lp1: float | None = None,
        shaft1_power_lp2: float | None = None,
        shaft2_power_hp: float | None = None,
        shaft2_power_ip: float | None = None,
        shaft2_power_lp1: float | None = None,
        shaft2_power_lp2: float | None = None,
        steam_chest_tc: float | None = None,
        steam_supplys: Iterable[SteamSupply] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.crossover_tc = crossover_tc
        self.reheater1_tc = reheater1_tc
        self.reheater2_tc = reheater2_tc
        self.shaft1_power_hp = shaft1_power_hp
        self.shaft1_power_ip = shaft1_power_ip
        self.shaft1_power_lp1 = shaft1_power_lp1
        self.shaft1_power_lp2 = shaft1_power_lp2
        self.shaft2_power_hp = shaft2_power_hp
        self.shaft2_power_ip = shaft2_power_ip
        self.shaft2_power_lp1 = shaft2_power_lp1
        self.shaft2_power_lp2 = shaft2_power_lp2
        self.steam_chest_tc = steam_chest_tc
        if steam_supplys is not None:
            SteamTurbine.steam_supplys.extend(self, steam_supplys)

    def add_steam_supply(self, steam_supply: SteamSupply) -> Self:
        return SteamTurbine.steam_supplys.add(self, steam_supply)

    def remove_steam_supply(self, steam_supply: SteamSupply) -> Self:
        return SteamTurbine.steam_supplys.remove(self, steam_supply)

    def clear_steam_supplys(self) -> Self:
        return SteamTurbine.steam_supplys.clear(self)

    def num_steam_supply(self) -> int:
        return SteamTurbine.steam_supplys.count(self)

    def get_steam_supply_by_mrid(self, mrid: str) -> SteamSupply | None:
        return SteamTurbine.steam_supplys.get_by_mrid(self, mrid)
