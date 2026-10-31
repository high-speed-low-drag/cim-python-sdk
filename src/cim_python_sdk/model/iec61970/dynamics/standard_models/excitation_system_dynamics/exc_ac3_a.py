"""CIM class ExcAC3A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAC3A(ExcitationSystemDynamics):
    """Modified IEEE AC3A alternator-supplied rectifier excitation system with different field
    current limit."""

    __slots__ = (
        "efdn",
        "ka",
        "kc",
        "kd",
        "ke",
        "kf",
        "kf1",
        "kf2",
        "klv",
        "kn",
        "kr",
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
        "vemin",
        "vfemax",
        "vlv",
    )

    tb: float | None  # Seconds
    tc: float | None  # Seconds
    ka: float | None  # Seconds
    ta: float | None  # PU
    vamax: float | None  # PU
    vamin: float | None  # PU
    te: float | None  # Seconds
    vemin: float | None  # PU
    kr: float | None  # PU
    kf: float | None  # PU
    tf: float | None  # Seconds
    kn: float | None  # PU
    efdn: float | None  # PU
    kc: float | None  # PU
    kd: float | None  # PU
    ke: float | None  # PU
    klv: float | None  # PU
    kf1: float | None  # PU
    kf2: float | None  # PU
    ks: float | None  # PU
    vfemax: float | None  # PU
    ve1: float | None  # PU
    seve1: float | None
    ve2: float | None  # PU
    seve2: float | None
    vlv: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcAC3A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{442B06CD-43E7-4cc5-9E46-87B65F5E90A8}",
        attributes=(
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vemin", "vemin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kr", "kr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kn", "kn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdn", "efdn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("klv", "klv", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf1", "kf1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf2", "kf2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vfemax", "vfemax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve1", "ve1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve1", "seve1", "float", 0, 1, "primitive"),
            AttrMeta("ve2", "ve2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve2", "seve2", "float", 0, 1, "primitive"),
            AttrMeta("vlv", "vlv", "PU", 0, 1, "cimdatatype"),
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
        vemin: float | None = None,
        kr: float | None = None,
        kf: float | None = None,
        tf: float | None = None,
        kn: float | None = None,
        efdn: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        ke: float | None = None,
        klv: float | None = None,
        kf1: float | None = None,
        kf2: float | None = None,
        ks: float | None = None,
        vfemax: float | None = None,
        ve1: float | None = None,
        seve1: float | None = None,
        ve2: float | None = None,
        seve2: float | None = None,
        vlv: float | None = None,
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
        self.vemin = vemin
        self.kr = kr
        self.kf = kf
        self.tf = tf
        self.kn = kn
        self.efdn = efdn
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.klv = klv
        self.kf1 = kf1
        self.kf2 = kf2
        self.ks = ks
        self.vfemax = vfemax
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2
        self.vlv = vlv
