"""CIM class ExcAC8B (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAC8B(ExcitationSystemDynamics):
    """Modified IEEE AC8B alternator-supplied rectifier excitation system with speed input and
    input limiter."""

    __slots__ = (
        "inlim",
        "ka",
        "kc",
        "kd",
        "kdr",
        "ke",
        "kir",
        "kpr",
        "ks",
        "pidlim",
        "seve1",
        "seve2",
        "ta",
        "tdr",
        "te",
        "telim",
        "ve1",
        "ve2",
        "vemin",
        "vfemax",
        "vimax",
        "vimin",
        "vpidmax",
        "vpidmin",
        "vrmax",
        "vrmin",
        "vtmult",
    )

    inlim: bool | None
    ka: float | None  # PU
    kc: float | None  # PU
    kd: float | None  # PU
    kdr: float | None  # PU
    ke: float | None  # PU
    kir: float | None  # PU
    kpr: float | None  # PU
    ks: float | None  # PU
    pidlim: bool | None
    seve1: float | None
    seve2: float | None
    ta: float | None  # Seconds
    tdr: float | None  # Seconds
    te: float | None  # Seconds
    telim: bool | None
    ve1: float | None  # PU
    ve2: float | None  # PU
    vemin: float | None  # PU
    vfemax: float | None  # PU
    vimax: float | None  # PU
    vimin: float | None  # PU
    vpidmax: float | None  # PU
    vpidmin: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    vtmult: bool | None

    _cim_meta = ClassMeta(
        cim_name="ExcAC8B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{F71F0FCB-91F7-4d93-9B69-B7BCE2B9B605}",
        attributes=(
            AttrMeta("inlim", "inlim", "bool", 0, 1, "primitive"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kdr", "kdr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kir", "kir", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpr", "kpr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pidlim", "pidlim", "bool", 0, 1, "primitive"),
            AttrMeta("seve1", "seve1", "float", 0, 1, "primitive"),
            AttrMeta("seve2", "seve2", "float", 0, 1, "primitive"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tdr", "tdr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("telim", "telim", "bool", 0, 1, "primitive"),
            AttrMeta("ve1", "ve1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve2", "ve2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vemin", "vemin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vfemax", "vfemax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimax", "vimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimin", "vimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vpidmax", "vpidmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vpidmin", "vpidmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vtmult", "vtmult", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        inlim: bool | None = None,
        ka: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        kdr: float | None = None,
        ke: float | None = None,
        kir: float | None = None,
        kpr: float | None = None,
        ks: float | None = None,
        pidlim: bool | None = None,
        seve1: float | None = None,
        seve2: float | None = None,
        ta: float | None = None,
        tdr: float | None = None,
        te: float | None = None,
        telim: bool | None = None,
        ve1: float | None = None,
        ve2: float | None = None,
        vemin: float | None = None,
        vfemax: float | None = None,
        vimax: float | None = None,
        vimin: float | None = None,
        vpidmax: float | None = None,
        vpidmin: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        vtmult: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.inlim = inlim
        self.ka = ka
        self.kc = kc
        self.kd = kd
        self.kdr = kdr
        self.ke = ke
        self.kir = kir
        self.kpr = kpr
        self.ks = ks
        self.pidlim = pidlim
        self.seve1 = seve1
        self.seve2 = seve2
        self.ta = ta
        self.tdr = tdr
        self.te = te
        self.telim = telim
        self.ve1 = ve1
        self.ve2 = ve2
        self.vemin = vemin
        self.vfemax = vfemax
        self.vimax = vimax
        self.vimin = vimin
        self.vpidmax = vpidmax
        self.vpidmin = vpidmin
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.vtmult = vtmult
