"""CIM class ExcREXS (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.exc_rexs_feedback_signal_kind import (
        ExcREXSFeedbackSignalKind,
    )


class ExcREXS(ExcitationSystemDynamics):
    """General purpose rotating excitation system. This model can be used to represent a wide
    range of excitation systems whose DC power source is an AC or DC generator. It
    encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system models."""

    __slots__ = (
        "e1",
        "e2",
        "fbf",
        "flimf",
        "kc",
        "kd",
        "ke",
        "kefd",
        "kf",
        "kh",
        "kii",
        "kip",
        "ks",
        "kvi",
        "kvp",
        "kvphz",
        "nvphz",
        "se1",
        "se2",
        "ta",
        "tb1",
        "tb2",
        "tc1",
        "tc2",
        "te",
        "tf",
        "tf1",
        "tf2",
        "tp",
        "vcmax",
        "vfmax",
        "vfmin",
        "vimax",
        "vrmax",
        "vrmin",
        "xc",
    )

    e1: float | None  # PU
    e2: float | None  # PU
    fbf: ExcREXSFeedbackSignalKind | None
    flimf: float | None  # PU
    kc: float | None  # PU
    kd: float | None  # PU
    ke: float | None  # PU
    kefd: float | None  # PU
    kf: float | None  # Seconds
    kh: float | None  # PU
    kii: float | None  # PU
    kip: float | None  # PU
    ks: float | None  # PU
    kvi: float | None  # PU
    kvp: float | None  # PU
    kvphz: float | None  # PU
    nvphz: float | None  # PU
    se1: float | None  # PU
    se2: float | None  # PU
    ta: float | None  # Seconds
    tb1: float | None  # Seconds
    tb2: float | None  # Seconds
    tc1: float | None  # Seconds
    tc2: float | None  # Seconds
    te: float | None  # Seconds
    tf: float | None  # Seconds
    tf1: float | None  # Seconds
    tf2: float | None  # Seconds
    tp: float | None  # Seconds
    vcmax: float | None  # PU
    vfmax: float | None  # PU
    vfmin: float | None  # PU
    vimax: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    xc: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcREXS",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{F3E4EB5B-1DEA-418b-945D-2F82E47C8600}",
        attributes=(
            AttrMeta("e1", "e1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("e2", "e2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fbf", "fbf", "ExcREXSFeedbackSignalKind", 0, 1, "enumeration"),
            AttrMeta("flimf", "flimf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kefd", "kefd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kh", "kh", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kii", "kii", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kip", "kip", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kvi", "kvi", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kvp", "kvp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kvphz", "kvphz", "PU", 0, 1, "cimdatatype"),
            AttrMeta("nvphz", "nvphz", "PU", 0, 1, "cimdatatype"),
            AttrMeta("se1", "se1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("se2", "se2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb1", "tb1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb2", "tb2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc1", "tc1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc2", "tc2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf1", "tf1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf2", "tf2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vcmax", "vcmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vfmax", "vfmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vfmin", "vfmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimax", "vimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xc", "xc", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        e1: float | None = None,
        e2: float | None = None,
        fbf: ExcREXSFeedbackSignalKind | None = None,
        flimf: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        ke: float | None = None,
        kefd: float | None = None,
        kf: float | None = None,
        kh: float | None = None,
        kii: float | None = None,
        kip: float | None = None,
        ks: float | None = None,
        kvi: float | None = None,
        kvp: float | None = None,
        kvphz: float | None = None,
        nvphz: float | None = None,
        se1: float | None = None,
        se2: float | None = None,
        ta: float | None = None,
        tb1: float | None = None,
        tb2: float | None = None,
        tc1: float | None = None,
        tc2: float | None = None,
        te: float | None = None,
        tf: float | None = None,
        tf1: float | None = None,
        tf2: float | None = None,
        tp: float | None = None,
        vcmax: float | None = None,
        vfmax: float | None = None,
        vfmin: float | None = None,
        vimax: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        xc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.e1 = e1
        self.e2 = e2
        self.fbf = fbf
        self.flimf = flimf
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.kefd = kefd
        self.kf = kf
        self.kh = kh
        self.kii = kii
        self.kip = kip
        self.ks = ks
        self.kvi = kvi
        self.kvp = kvp
        self.kvphz = kvphz
        self.nvphz = nvphz
        self.se1 = se1
        self.se2 = se2
        self.ta = ta
        self.tb1 = tb1
        self.tb2 = tb2
        self.tc1 = tc1
        self.tc2 = tc2
        self.te = te
        self.tf = tf
        self.tf1 = tf1
        self.tf2 = tf2
        self.tp = tp
        self.vcmax = vcmax
        self.vfmax = vfmax
        self.vfmin = vfmin
        self.vimax = vimax
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.xc = xc
