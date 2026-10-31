"""CIM class Tsunami (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.hydrospheric_phenomenon import (
    HydrosphericPhenomenon,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Tsunami(HydrosphericPhenomenon):
    """A tsunami (tidal wave), a long high sea wave caused by an earthquake, submarine
    landslide, or other disturbance."""

    __slots__ = ("intensity", "magnitude")

    intensity: int | None
    magnitude: float | None

    _cim_meta = ClassMeta(
        cim_name="Tsunami",
        package="TC57CIM/IEC62325/Environmental",
        guid="{47F4C552-1F1C-4a7a-8ACB-40E292598249}",
        attributes=(
            AttrMeta("intensity", "intensity", "int", 0, 1, "primitive"),
            AttrMeta("magnitude", "magnitude", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        intensity: int | None = None,
        magnitude: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.intensity = intensity
        self.magnitude = magnitude
