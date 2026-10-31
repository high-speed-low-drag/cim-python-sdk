"""CIM class ExcIEEEAC2A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEAC2A(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type AC2A model. The model represents a high initial response
    field-controlled alternator-rectifier excitation system. The alternator main exciter is
    used with non-controlled rectifiers. The type AC2A model is similar to that of type AC1A
    except for the inclusion of exciter time constant compensation and exciter field current
    limiting elements.

    Reference: IEEE 421.5-2005, 6.2."""

    __slots__ = (
        "ka",
        "kb",
        "kc",
        "kd",
        "ke",
        "kf",
        "kh",
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
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    te: float | None  # Seconds
    vfemax: float | None  # PU
    kh: float | None  # PU
    kf: float | None  # PU
    tf: float | None  # Seconds
    kc: float | None  # PU
    kd: float | None  # PU
    ke: float | None  # PU
    ve1: float | None  # PU
    seve1: float | None
    ve2: float | None  # PU
    seve2: float | None

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEAC2A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{872A1C8E-D47A-438c-9AE6-CC6471983F4A}",
        attributes=(
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kb", "kb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vfemax", "vfemax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kh", "kh", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve1", "ve1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve1", "seve1", "float", 0, 1, "primitive"),
            AttrMeta("ve2", "ve2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve2", "seve2", "float", 0, 1, "primitive"),
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
        vrmax: float | None = None,
        vrmin: float | None = None,
        te: float | None = None,
        vfemax: float | None = None,
        kh: float | None = None,
        kf: float | None = None,
        tf: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        ke: float | None = None,
        ve1: float | None = None,
        seve1: float | None = None,
        ve2: float | None = None,
        seve2: float | None = None,
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
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.te = te
        self.vfemax = vfemax
        self.kh = kh
        self.kf = kf
        self.tf = tf
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2
