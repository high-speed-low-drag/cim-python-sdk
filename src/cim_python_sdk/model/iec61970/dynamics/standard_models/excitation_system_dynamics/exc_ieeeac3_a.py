"""CIM class ExcIEEEAC3A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEAC3A(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type AC3A model. The model represents the field-controlled
    alternator-rectifier excitation systems designated type AC3A. These excitation systems
    include an alternator main exciter with non-controlled rectifiers. The exciter employs
    self-excitation, and the voltage regulator power is derived from the exciter output
    voltage. Therefore, this system has an additional nonlinearity, simulated by the use of
    a multiplier whose inputs are the voltage regulator command signal, Va, and the exciter
    output voltage, Efd, times KR. This model is applicable to excitation systems employing
    static voltage regulators.

    Reference: IEEE 421.5-2005, 6.3."""

    __slots__ = (
        "efdn",
        "ka",
        "kc",
        "kd",
        "ke",
        "kf",
        "kn",
        "kr",
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
    )

    efdn: float | None  # PU
    ka: float | None  # PU
    kc: float | None  # PU
    kd: float | None  # PU
    ke: float | None  # PU
    kf: float | None  # PU
    kn: float | None  # PU
    kr: float | None  # PU
    seve1: float | None
    seve2: float | None
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    te: float | None  # Seconds
    tf: float | None  # Seconds
    vamax: float | None  # PU
    vamin: float | None  # PU
    ve1: float | None  # PU
    ve2: float | None  # PU
    vemin: float | None  # PU
    vfemax: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEAC3A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{F4168622-5B5F-4acf-A248-E670C038660A}",
        attributes=(
            AttrMeta("efdn", "efdn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kn", "kn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kr", "kr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve1", "seve1", "float", 0, 1, "primitive"),
            AttrMeta("seve2", "seve2", "float", 0, 1, "primitive"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve1", "ve1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve2", "ve2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vemin", "vemin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vfemax", "vfemax", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        efdn: float | None = None,
        ka: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        ke: float | None = None,
        kf: float | None = None,
        kn: float | None = None,
        kr: float | None = None,
        seve1: float | None = None,
        seve2: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        te: float | None = None,
        tf: float | None = None,
        vamax: float | None = None,
        vamin: float | None = None,
        ve1: float | None = None,
        ve2: float | None = None,
        vemin: float | None = None,
        vfemax: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.efdn = efdn
        self.ka = ka
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.kf = kf
        self.kn = kn
        self.kr = kr
        self.seve1 = seve1
        self.seve2 = seve2
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.te = te
        self.tf = tf
        self.vamax = vamax
        self.vamin = vamin
        self.ve1 = ve1
        self.ve2 = ve2
        self.vemin = vemin
        self.vfemax = vfemax
