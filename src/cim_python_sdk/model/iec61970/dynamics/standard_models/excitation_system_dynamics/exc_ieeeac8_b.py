"""CIM class ExcIEEEAC8B (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEAC8B(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type AC8B model. This model represents a PID voltage regulator with
    either a brushless exciter or DC exciter. The AVR in this model consists of PID control,
    with separate constants for the proportional (KPR), integral (KIR), and derivative (KDR)
    gains. The representation of the brushless exciter (TE, KE, SE, KC, KD) is similar to
    the model type AC2A. The type AC8B model can be used to represent static voltage
    regulators applied to brushless excitation systems. Digitally based voltage regulators
    feeding DC rotating main exciters can be represented with the AC type AC8B model with
    the parameters KC and KD set to 0. For thyristor power stages fed from the generator
    terminals, the limits VRMAX and VRMIN should be a function of terminal voltage: VT x
    VRMAX and VT x VRMIN.

    Reference: IEEE 421.5-2005, 6.8."""

    __slots__ = (
        "ka",
        "kc",
        "kd",
        "kdr",
        "ke",
        "kir",
        "kpr",
        "seve1",
        "seve2",
        "ta",
        "tdr",
        "te",
        "ve1",
        "ve2",
        "vemin",
        "vfemax",
        "vrmax",
        "vrmin",
    )

    kpr: float | None  # PU
    kir: float | None  # PU
    kdr: float | None  # PU
    tdr: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    ka: float | None  # PU
    ta: float | None  # Seconds
    te: float | None  # Seconds
    vfemax: float | None  # PU
    vemin: float | None  # PU
    ke: float | None  # PU
    kc: float | None  # PU
    kd: float | None  # PU
    ve1: float | None  # PU
    seve1: float | None
    ve2: float | None  # PU
    seve2: float | None

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEAC8B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{5A5BF11A-2D01-4ab7-9F3E-6F9D0EBA1054}",
        attributes=(
            AttrMeta("kpr", "kpr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kir", "kir", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kdr", "kdr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tdr", "tdr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vfemax", "vfemax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vemin", "vemin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve1", "ve1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve1", "seve1", "float", 0, 1, "primitive"),
            AttrMeta("ve2", "ve2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve2", "seve2", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        kpr: float | None = None,
        kir: float | None = None,
        kdr: float | None = None,
        tdr: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        ka: float | None = None,
        ta: float | None = None,
        te: float | None = None,
        vfemax: float | None = None,
        vemin: float | None = None,
        ke: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        ve1: float | None = None,
        seve1: float | None = None,
        ve2: float | None = None,
        seve2: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kpr = kpr
        self.kir = kir
        self.kdr = kdr
        self.tdr = tdr
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.ka = ka
        self.ta = ta
        self.te = te
        self.vfemax = vfemax
        self.vemin = vemin
        self.ke = ke
        self.kc = kc
        self.kd = kd
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2
