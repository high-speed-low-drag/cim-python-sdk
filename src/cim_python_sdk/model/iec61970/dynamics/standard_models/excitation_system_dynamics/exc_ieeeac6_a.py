"""CIM class ExcIEEEAC6A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEAC6A(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type AC6A model. The model represents field-controlled
    alternator-rectifier excitation systems with system-supplied electronic voltage
    regulators. The maximum output of the regulator, VR, is a function of terminal voltage,
    VT. The field current limiter included in the original model AC6A remains in the 2005
    update.

    Reference: IEEE 421.5-2005, 6.6."""

    __slots__ = (
        "ka",
        "kc",
        "kd",
        "ke",
        "kh",
        "seve1",
        "seve2",
        "ta",
        "tb",
        "tc",
        "te",
        "th",
        "tj",
        "tk",
        "vamax",
        "vamin",
        "ve1",
        "ve2",
        "vfelim",
        "vhmax",
        "vrmax",
        "vrmin",
    )

    ka: float | None  # PU
    ta: float | None  # Seconds
    tk: float | None  # Seconds
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    vamax: float | None  # PU
    vamin: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    te: float | None  # Seconds
    kh: float | None  # PU
    tj: float | None  # Seconds
    th: float | None  # Seconds
    vfelim: float | None  # PU
    vhmax: float | None  # PU
    kc: float | None  # PU
    kd: float | None  # PU
    ke: float | None  # PU
    ve1: float | None  # PU
    seve1: float | None
    ve2: float | None  # PU
    seve2: float | None

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEAC6A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{52AB8022-3DF9-4f56-8342-FBBD1650B319}",
        attributes=(
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tk", "tk", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kh", "kh", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tj", "tj", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("th", "th", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vfelim", "vfelim", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vhmax", "vhmax", "PU", 0, 1, "cimdatatype"),
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
        ka: float | None = None,
        ta: float | None = None,
        tk: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        vamax: float | None = None,
        vamin: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        te: float | None = None,
        kh: float | None = None,
        tj: float | None = None,
        th: float | None = None,
        vfelim: float | None = None,
        vhmax: float | None = None,
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
        self.ka = ka
        self.ta = ta
        self.tk = tk
        self.tb = tb
        self.tc = tc
        self.vamax = vamax
        self.vamin = vamin
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.te = te
        self.kh = kh
        self.tj = tj
        self.th = th
        self.vfelim = vfelim
        self.vhmax = vhmax
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2
