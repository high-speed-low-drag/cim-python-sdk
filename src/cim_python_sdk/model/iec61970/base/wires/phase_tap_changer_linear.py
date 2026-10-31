"""CIM class PhaseTapChangerLinear (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer import PhaseTapChanger

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PhaseTapChangerLinear(PhaseTapChanger):
    """Describes a tap changer with a linear relation between the tap step and the phase angle
    difference across the transformer. This is a mathematical model that is an approximation
    of a real phase tap changer.

    The phase angle is computed as stepPhaseShiftIncrement times the tap position.

    The voltage magnitude of both sides is the same."""

    __slots__ = ("step_phase_shift_increment", "x_max", "x_min")

    step_phase_shift_increment: float | None  # AngleDegrees
    x_max: float | None  # Reactance
    x_min: float | None  # Reactance

    _cim_meta = ClassMeta(
        cim_name="PhaseTapChangerLinear",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{BFC68185-DEEC-4665-B2E9-64EC73F18241}",
        attributes=(
            AttrMeta(
                "step_phase_shift_increment",
                "stepPhaseShiftIncrement",
                "AngleDegrees",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("x_max", "xMax", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_min", "xMin", "Reactance", 0, 1, "cimdatatype", deprecated=True),
        ),
    )

    def __init__(
        self,
        *,
        step_phase_shift_increment: float | None = None,
        x_max: float | None = None,
        x_min: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.step_phase_shift_increment = step_phase_shift_increment
        self.x_max = x_max
        self.x_min = x_min
