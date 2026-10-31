"""CIM class AtmosphericPhenomenon (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.environmental_phenomenon import (
    EnvironmentalPhenomenon,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.relative_displacement import (
        RelativeDisplacement,
    )


class AtmosphericPhenomenon(EnvironmentalPhenomenon):
    """An atmospheric phenomenon with a base and altitude providing the vertical coverage
    (combined with the Location to provide three dimensional space)."""

    __slots__ = ("altitude", "base", "direction", "max_coverage", "min_coverage", "speed")

    altitude: RelativeDisplacement | None
    base: RelativeDisplacement | None
    direction: float | None  # Bearing
    max_coverage: float | None  # PerCent
    min_coverage: float | None  # PerCent
    speed: float | None  # Speed

    _cim_meta = ClassMeta(
        cim_name="AtmosphericPhenomenon",
        package="TC57CIM/IEC62325/Environmental",
        guid="{F1AD8D7C-AA6E-4851-A962-BA2C2AD117E8}",
        attributes=(
            AttrMeta("altitude", "altitude", "RelativeDisplacement", 0, 1, "compound"),
            AttrMeta("base", "base", "RelativeDisplacement", 0, 1, "compound"),
            AttrMeta("direction", "direction", "Bearing", 0, 1, "cimdatatype"),
            AttrMeta("max_coverage", "maxCoverage", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("min_coverage", "minCoverage", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("speed", "speed", "Speed", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        altitude: RelativeDisplacement | None = None,
        base: RelativeDisplacement | None = None,
        direction: float | None = None,
        max_coverage: float | None = None,
        min_coverage: float | None = None,
        speed: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.altitude = altitude
        self.base = base
        self.direction = direction
        self.max_coverage = max_coverage
        self.min_coverage = min_coverage
        self.speed = speed
