"""CIM class VolcanicAshCloud (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.atmospheric_phenomenon import AtmosphericPhenomenon

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class VolcanicAshCloud(AtmosphericPhenomenon):
    """An ash cloud formed as a result of a volcanic eruption."""

    __slots__ = ("density", "particle_size")

    density: float | None  # ParticulateDensity
    particle_size: float | None  # Length

    _cim_meta = ClassMeta(
        cim_name="VolcanicAshCloud",
        package="TC57CIM/IEC62325/Environmental",
        guid="{162DBE7F-3666-4598-AB70-05EA04A35213}",
        attributes=(
            AttrMeta("density", "density", "ParticulateDensity", 0, 1, "cimdatatype"),
            AttrMeta("particle_size", "particleSize", "Length", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        density: float | None = None,
        particle_size: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.density = density
        self.particle_size = particle_size
