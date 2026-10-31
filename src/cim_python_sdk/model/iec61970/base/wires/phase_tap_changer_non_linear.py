"""CIM class PhaseTapChangerNonLinear (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer import PhaseTapChanger

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PhaseTapChangerNonLinear(PhaseTapChanger):
    """The non-linear phase tap changer describes the non-linear behaviour of a phase tap
    changer. This is a base class for the symmetrical and asymmetrical phase tap changer
    models. The details of these models can be found in IEC 61970-301."""

    __slots__ = ("voltage_step_increment", "x_max", "x_min")

    voltage_step_increment: float | None  # PerCent
    x_max: float | None  # Reactance
    x_min: float | None  # Reactance

    _cim_meta = ClassMeta(
        cim_name="PhaseTapChangerNonLinear",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{5B26C38F-A09B-439c-B5E2-A9F4ED801883}",
        attributes=(
            AttrMeta(
                "voltage_step_increment", "voltageStepIncrement", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta("x_max", "xMax", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_min", "xMin", "Reactance", 0, 1, "cimdatatype", deprecated=True),
        ),
    )

    def __init__(
        self,
        *,
        voltage_step_increment: float | None = None,
        x_max: float | None = None,
        x_min: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.voltage_step_increment = voltage_step_increment
        self.x_max = x_max
        self.x_min = x_min
