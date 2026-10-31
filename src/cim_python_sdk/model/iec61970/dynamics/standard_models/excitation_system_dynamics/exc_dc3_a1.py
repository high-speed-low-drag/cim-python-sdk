"""CIM class ExcDC3A1 (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcDC3A1(ExcitationSystemDynamics):
    """Modified old IEEE type 3 excitation system."""

    __slots__ = (
        "exclim",
        "ka",
        "ke",
        "kf",
        "ki",
        "kp",
        "ta",
        "te",
        "tf",
        "vb1max",
        "vblim",
        "vbmax",
        "vrmax",
        "vrmin",
    )

    ka: float | None  # PU
    ta: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    te: float | None  # Seconds
    kf: float | None  # PU
    tf: float | None  # Seconds
    kp: float | None  # PU
    ki: float | None  # PU
    vbmax: float | None  # PU
    exclim: bool | None
    ke: float | None  # PU
    vb1max: float | None  # PU
    vblim: bool | None

    _cim_meta = ClassMeta(
        cim_name="ExcDC3A1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{61150142-5A5C-4950-8737-CCCA34D9C146}",
        attributes=(
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vbmax", "vbmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("exclim", "exclim", "bool", 0, 1, "primitive"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vb1max", "vb1max", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vblim", "vblim", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        ka: float | None = None,
        ta: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        te: float | None = None,
        kf: float | None = None,
        tf: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        vbmax: float | None = None,
        exclim: bool | None = None,
        ke: float | None = None,
        vb1max: float | None = None,
        vblim: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ka = ka
        self.ta = ta
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.te = te
        self.kf = kf
        self.tf = tf
        self.kp = kp
        self.ki = ki
        self.vbmax = vbmax
        self.exclim = exclim
        self.ke = ke
        self.vb1max = vb1max
        self.vblim = vblim
