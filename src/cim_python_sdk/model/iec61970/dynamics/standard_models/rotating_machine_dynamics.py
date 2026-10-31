"""CIM class RotatingMachineDynamics (TC57CIM/IEC61970/Dynamics/StandardModels). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class RotatingMachineDynamics(DynamicsFunctionBlock):
    """Abstract parent class for all synchronous and asynchronous machine standard models."""

    __slots__ = (
        "damping",
        "inertia",
        "saturation_factor",
        "saturation_factor120",
        "stator_leakage_reactance",
        "stator_resistance",
    )

    damping: float | None
    inertia: float | None  # Seconds
    saturation_factor: float | None
    saturation_factor120: float | None
    stator_leakage_reactance: float | None  # PU
    stator_resistance: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="RotatingMachineDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels",
        guid="{AE986CE7-783B-4310-8D50-95FEB16A0A76}",
        attributes=(
            AttrMeta("damping", "damping", "float", 0, 1, "primitive"),
            AttrMeta("inertia", "inertia", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("saturation_factor", "saturationFactor", "float", 0, 1, "primitive"),
            AttrMeta("saturation_factor120", "saturationFactor120", "float", 0, 1, "primitive"),
            AttrMeta(
                "stator_leakage_reactance", "statorLeakageReactance", "PU", 0, 1, "cimdatatype"
            ),
            AttrMeta("stator_resistance", "statorResistance", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        damping: float | None = None,
        inertia: float | None = None,
        saturation_factor: float | None = None,
        saturation_factor120: float | None = None,
        stator_leakage_reactance: float | None = None,
        stator_resistance: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.damping = damping
        self.inertia = inertia
        self.saturation_factor = saturation_factor
        self.saturation_factor120 = saturation_factor120
        self.stator_leakage_reactance = stator_leakage_reactance
        self.stator_resistance = stator_resistance
