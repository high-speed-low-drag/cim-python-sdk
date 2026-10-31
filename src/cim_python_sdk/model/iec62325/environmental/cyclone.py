"""CIM class Cyclone (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.atmospheric_phenomenon import AtmosphericPhenomenon

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Cyclone(AtmosphericPhenomenon):
    """A cyclone (or tropical cyclone), a rapidly-rotating storm system characterized by a
    low-pressure center, strong winds, and a spiral arrangement of thunderstorms that
    produce heavy rain."""

    __slots__ = ("central_pressure", "max_surface_wind_speed", "wind_force")

    central_pressure: float | None  # Pressure
    max_surface_wind_speed: float | None  # Speed
    wind_force: int | None

    _cim_meta = ClassMeta(
        cim_name="Cyclone",
        package="TC57CIM/IEC62325/Environmental",
        guid="{F10D06E9-4C74-4c6d-8FAD-8099ECC3F04C}",
        attributes=(
            AttrMeta("central_pressure", "centralPressure", "Pressure", 0, 1, "cimdatatype"),
            AttrMeta("max_surface_wind_speed", "maxSurfaceWindSpeed", "Speed", 0, 1, "cimdatatype"),
            AttrMeta("wind_force", "windForce", "int", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        central_pressure: float | None = None,
        max_surface_wind_speed: float | None = None,
        wind_force: int | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.central_pressure = central_pressure
        self.max_surface_wind_speed = max_surface_wind_speed
        self.wind_force = wind_force
