"""CIM class ExcAC1A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAC1A(ExcitationSystemDynamics):
    """Modified IEEE AC1A alternator-supplied rectifier excitation system with different rate
    feedback source."""

    __slots__ = (
        "hvlvgates",
        "ka",
        "kc",
        "kd",
        "ke",
        "kf",
        "kf1",
        "kf2",
        "ks",
        "seve1",
        "seve2",
        "ta",
        "tb",
        "tc",
        "te",
        "tf",
        "vamax",
        "vamin",
        "ve1",
        "ve2",
        "vrmax",
        "vrmin",
    )

    tb: float | None  # Seconds
    tc: float | None  # Seconds
    ka: float | None  # PU
    ta: float | None  # Seconds
    vamax: float | None  # PU
    vamin: float | None  # PU
    te: float | None  # Seconds
    kf: float | None  # PU
    kf1: float | None  # PU
    kf2: float | None  # PU
    ks: float | None  # PU
    tf: float | None  # Seconds
    kc: float | None  # PU
    kd: float | None  # PU
    ke: float | None  # PU
    ve1: float | None  # PU
    seve1: float | None
    ve2: float | None  # PU
    seve2: float | None
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    hvlvgates: bool | None

    _cim_meta = ClassMeta(
        cim_name="ExcAC1A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{7C5087C8-2137-40b6-89FE-5426A5A880A7}",
        attributes=(
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf1", "kf1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf2", "kf2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve1", "ve1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve1", "seve1", "float", 0, 1, "primitive"),
            AttrMeta("ve2", "ve2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve2", "seve2", "float", 0, 1, "primitive"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("hvlvgates", "hvlvgates", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        tb: float | None = None,
        tc: float | None = None,
        ka: float | None = None,
        ta: float | None = None,
        vamax: float | None = None,
        vamin: float | None = None,
        te: float | None = None,
        kf: float | None = None,
        kf1: float | None = None,
        kf2: float | None = None,
        ks: float | None = None,
        tf: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        ke: float | None = None,
        ve1: float | None = None,
        seve1: float | None = None,
        ve2: float | None = None,
        seve2: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        hvlvgates: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tb = tb
        self.tc = tc
        self.ka = ka
        self.ta = ta
        self.vamax = vamax
        self.vamin = vamin
        self.te = te
        self.kf = kf
        self.kf1 = kf1
        self.kf2 = kf2
        self.ks = ks
        self.tf = tf
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.hvlvgates = hvlvgates
