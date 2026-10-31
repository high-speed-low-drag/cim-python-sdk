"""CIM class PFVArType1IEEEVArController (TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType1Dynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type1_dynamics.pfv_ar_controller_type1_dynamics import (
    PFVArControllerType1Dynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PFVArType1IEEEVArController(PFVArControllerType1Dynamics):
    """IEEE VAR controller type 1 which operates by moving the voltage reference directly.

    Reference: IEEE 421.5-2005, 11.3."""

    __slots__ = ("tvarc", "vvar", "vvarcbw", "vvarref", "vvtmax", "vvtmin")

    tvarc: float | None  # Seconds
    vvar: float | None  # PU
    vvarcbw: float | None
    vvarref: float | None  # PU
    vvtmax: float | None  # PU
    vvtmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PFVArType1IEEEVArController",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType1Dynamics",
        guid="{052E3899-735D-414d-B54E-56CB584B0BEA}",
        attributes=(
            AttrMeta("tvarc", "tvarc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vvar", "vvar", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vvarcbw", "vvarcbw", "float", 0, 1, "primitive"),
            AttrMeta("vvarref", "vvarref", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vvtmax", "vvtmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vvtmin", "vvtmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        tvarc: float | None = None,
        vvar: float | None = None,
        vvarcbw: float | None = None,
        vvarref: float | None = None,
        vvtmax: float | None = None,
        vvtmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tvarc = tvarc
        self.vvar = vvar
        self.vvarcbw = vvarcbw
        self.vvarref = vvarref
        self.vvtmax = vvtmax
        self.vvtmin = vvtmin
