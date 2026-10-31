"""CIM class PFVArType2IEEEPFController (TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType2Dynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type2_dynamics.pfv_ar_controller_type2_dynamics import (
    PFVArControllerType2Dynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PFVArType2IEEEPFController(PFVArControllerType2Dynamics):
    """IEEE PF controller type 2 which is a summing point type controller making up the outside
    loop of a two-loop system. This controller is implemented as a slow PI type controller.
    The voltage regulator forms the inner loop and is implemented as a fast controller.

    Reference: IEEE 421.5-2005, 11.4."""

    __slots__ = ("exlon", "ki", "kp", "pfref", "vclmt", "vref", "vs")

    pfref: float | None  # PU
    vref: float | None  # PU
    vclmt: float | None  # PU
    kp: float | None  # PU
    ki: float | None  # PU
    vs: float | None
    exlon: bool | None

    _cim_meta = ClassMeta(
        cim_name="PFVArType2IEEEPFController",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType2Dynamics",
        guid="{5211ED6D-3BA7-4b1f-8E0B-C32886FB1B11}",
        attributes=(
            AttrMeta("pfref", "pfref", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vref", "vref", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vclmt", "vclmt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vs", "vs", "float", 0, 1, "primitive"),
            AttrMeta("exlon", "exlon", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        pfref: float | None = None,
        vref: float | None = None,
        vclmt: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        vs: float | None = None,
        exlon: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.pfref = pfref
        self.vref = vref
        self.vclmt = vclmt
        self.kp = kp
        self.ki = ki
        self.vs = vs
        self.exlon = exlon
