"""CIM class Earthquake (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.geospheric_phenomenon import GeosphericPhenomenon

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.relative_displacement import (
        RelativeDisplacement,
    )


class Earthquake(GeosphericPhenomenon):
    """An earthquake."""

    __slots__ = ("focal_depth", "intensity", "magnitude")

    focal_depth: RelativeDisplacement | None
    intensity: int | None
    magnitude: float | None

    _cim_meta = ClassMeta(
        cim_name="Earthquake",
        package="TC57CIM/IEC62325/Environmental",
        guid="{373062A9-7596-4730-8087-BC3A476D7017}",
        attributes=(
            AttrMeta("focal_depth", "focalDepth", "RelativeDisplacement", 0, 1, "compound"),
            AttrMeta("intensity", "intensity", "int", 0, 1, "primitive"),
            AttrMeta("magnitude", "magnitude", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        focal_depth: RelativeDisplacement | None = None,
        intensity: int | None = None,
        magnitude: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.focal_depth = focal_depth
        self.intensity = intensity
        self.magnitude = magnitude
