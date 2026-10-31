"""CIM class HydroTurbine (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.prime_mover import (
    PrimeMover,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.hydro_turbine_kind import (
        HydroTurbineKind,
    )


class HydroTurbine(PrimeMover):
    """A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton."""

    __slots__ = (
        "gate_rate_limit",
        "gate_upper_limit",
        "max_head_max_p",
        "min_head_max_p",
        "speed_rating",
        "speed_regulation",
        "transient_droop_time",
        "transient_regulation",
        "turbine_rating",
        "turbine_type",
        "water_starting_time",
    )

    gate_rate_limit: float | None
    gate_upper_limit: float | None  # PU
    max_head_max_p: float | None  # ActivePower
    min_head_max_p: float | None  # ActivePower
    speed_rating: float | None  # RotationSpeed
    speed_regulation: float | None  # PU
    transient_droop_time: float | None  # Seconds
    transient_regulation: float | None  # PU
    turbine_rating: float | None  # ActivePower
    turbine_type: HydroTurbineKind | None
    water_starting_time: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="HydroTurbine",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{F8920620-0A8D-4878-818B-67AB6813D9AC}",
        attributes=(
            AttrMeta("gate_rate_limit", "gateRateLimit", "float", 0, 1, "primitive"),
            AttrMeta("gate_upper_limit", "gateUpperLimit", "PU", 0, 1, "cimdatatype"),
            AttrMeta("max_head_max_p", "maxHeadMaxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_head_max_p", "minHeadMaxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("speed_rating", "speedRating", "RotationSpeed", 0, 1, "cimdatatype"),
            AttrMeta("speed_regulation", "speedRegulation", "PU", 0, 1, "cimdatatype"),
            AttrMeta("transient_droop_time", "transientDroopTime", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("transient_regulation", "transientRegulation", "PU", 0, 1, "cimdatatype"),
            AttrMeta("turbine_rating", "turbineRating", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("turbine_type", "turbineType", "HydroTurbineKind", 0, 1, "enumeration"),
            AttrMeta("water_starting_time", "waterStartingTime", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        gate_rate_limit: float | None = None,
        gate_upper_limit: float | None = None,
        max_head_max_p: float | None = None,
        min_head_max_p: float | None = None,
        speed_rating: float | None = None,
        speed_regulation: float | None = None,
        transient_droop_time: float | None = None,
        transient_regulation: float | None = None,
        turbine_rating: float | None = None,
        turbine_type: HydroTurbineKind | None = None,
        water_starting_time: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.gate_rate_limit = gate_rate_limit
        self.gate_upper_limit = gate_upper_limit
        self.max_head_max_p = max_head_max_p
        self.min_head_max_p = min_head_max_p
        self.speed_rating = speed_rating
        self.speed_regulation = speed_regulation
        self.transient_droop_time = transient_droop_time
        self.transient_regulation = transient_regulation
        self.turbine_rating = turbine_rating
        self.turbine_type = turbine_type
        self.water_starting_time = water_starting_time
