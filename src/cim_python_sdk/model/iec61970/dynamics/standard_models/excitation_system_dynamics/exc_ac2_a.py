"""CIM class ExcAC2A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAC2A(ExcitationSystemDynamics):
    """Modified IEEE AC2A alternator-supplied rectifier excitation system with different field
    current limit."""

    __slots__ = (
        "hvgate",
        "ka",
        "kb",
        "kb1",
        "kc",
        "kd",
        "ke",
        "kf",
        "kh",
        "kl",
        "kl1",
        "ks",
        "lvgate",
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
        "vfemax",
        "vlr",
        "vrmax",
        "vrmin",
    )

    tb: float | None  # Seconds
    tc: float | None  # Seconds
    ka: float | None  # PU
    ta: float | None  # Seconds
    vamax: float | None  # PU
    vamin: float | None  # PU
    kb: float | None  # PU
    kb1: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    te: float | None  # Seconds
    vfemax: float | None  # PU
    kh: float | None  # PU
    kf: float | None  # PU
    kl: float | None  # PU
    vlr: float | None  # PU
    kl1: float | None  # PU
    ks: float | None  # PU
    tf: float | None  # Seconds
    kc: float | None  # PU
    kd: float | None  # PU
    ke: float | None  # PU
    ve1: float | None  # PU
    seve1: float | None
    ve2: float | None  # PU
    seve2: float | None
    hvgate: bool | None
    lvgate: bool | None

    _cim_meta = ClassMeta(
        cim_name="ExcAC2A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{427E622F-63B0-453f-B645-111E8D44788E}",
        attributes=(
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kb", "kb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kb1", "kb1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vfemax", "vfemax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kh", "kh", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kl", "kl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vlr", "vlr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kl1", "kl1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve1", "ve1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve1", "seve1", "float", 0, 1, "primitive"),
            AttrMeta("ve2", "ve2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve2", "seve2", "float", 0, 1, "primitive"),
            AttrMeta("hvgate", "hvgate", "bool", 0, 1, "primitive"),
            AttrMeta("lvgate", "lvgate", "bool", 0, 1, "primitive"),
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
        kb: float | None = None,
        kb1: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        te: float | None = None,
        vfemax: float | None = None,
        kh: float | None = None,
        kf: float | None = None,
        kl: float | None = None,
        vlr: float | None = None,
        kl1: float | None = None,
        ks: float | None = None,
        tf: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        ke: float | None = None,
        ve1: float | None = None,
        seve1: float | None = None,
        ve2: float | None = None,
        seve2: float | None = None,
        hvgate: bool | None = None,
        lvgate: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tb = tb
        self.tc = tc
        self.ka = ka
        self.ta = ta
        self.vamax = vamax
        self.vamin = vamin
        self.kb = kb
        self.kb1 = kb1
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.te = te
        self.vfemax = vfemax
        self.kh = kh
        self.kf = kf
        self.kl = kl
        self.vlr = vlr
        self.kl1 = kl1
        self.ks = ks
        self.tf = tf
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2
        self.hvgate = hvgate
        self.lvgate = lvgate
