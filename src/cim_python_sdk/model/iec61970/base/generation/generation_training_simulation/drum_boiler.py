"""CIM class DrumBoiler (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.fossil_steam_supply import (
    FossilSteamSupply,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class DrumBoiler(FossilSteamSupply):
    """Drum boiler."""

    __slots__ = ("drum_boiler_rating",)

    drum_boiler_rating: float | None

    _cim_meta = ClassMeta(
        cim_name="DrumBoiler",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{3B3A9E99-55A6-49c1-A8E8-3D7881624BCE}",
        attributes=(
            AttrMeta("drum_boiler_rating", "drumBoilerRating", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        drum_boiler_rating: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.drum_boiler_rating = drum_boiler_rating
