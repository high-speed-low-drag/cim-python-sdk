"""CIM class ExcIEEEAC7B (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEAC7B(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type AC7B model. The model represents excitation systems which consist
    of an AC alternator with either stationary or rotating rectifiers to produce the DC
    field requirements. It is an upgrade to earlier AC excitation systems, which replace
    only the controls but retain the AC alternator and diode rectifier bridge.

    Reference: IEEE 421.5-2005, 6.7. Note, however, that in IEEE 421.5-2005, the [1 / sTE]
    block is shown as [1 / (1 + sTE)], which is incorrect."""

    __slots__ = (
        "kc",
        "kd",
        "kdr",
        "ke",
        "kf1",
        "kf2",
        "kf3",
        "kia",
        "kir",
        "kl",
        "kp",
        "kpa",
        "kpr",
        "seve1",
        "seve2",
        "tdr",
        "te",
        "tf",
        "vamax",
        "vamin",
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
    kpa: float | None  # PU
    kia: float | None  # PU
    vamax: float | None  # PU
    vamin: float | None  # PU
    kp: float | None  # PU
    kl: float | None  # PU
    te: float | None  # Seconds
    vfemax: float | None  # PU
    vemin: float | None  # PU
    ke: float | None  # PU
    kc: float | None  # PU
    kd: float | None  # PU
    kf1: float | None  # PU
    kf2: float | None  # PU
    kf3: float | None  # PU
    tf: float | None  # Seconds
    ve1: float | None  # PU
    seve1: float | None
    ve2: float | None  # PU
    seve2: float | None

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEAC7B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{7FA5C845-958C-4fde-823A-F43B7912A2C0}",
        attributes=(
            AttrMeta("kpr", "kpr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kir", "kir", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kdr", "kdr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tdr", "tdr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpa", "kpa", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kia", "kia", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kl", "kl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vfemax", "vfemax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vemin", "vemin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf1", "kf1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf2", "kf2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf3", "kf3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
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
        kpa: float | None = None,
        kia: float | None = None,
        vamax: float | None = None,
        vamin: float | None = None,
        kp: float | None = None,
        kl: float | None = None,
        te: float | None = None,
        vfemax: float | None = None,
        vemin: float | None = None,
        ke: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        kf1: float | None = None,
        kf2: float | None = None,
        kf3: float | None = None,
        tf: float | None = None,
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
        self.kpa = kpa
        self.kia = kia
        self.vamax = vamax
        self.vamin = vamin
        self.kp = kp
        self.kl = kl
        self.te = te
        self.vfemax = vfemax
        self.vemin = vemin
        self.ke = ke
        self.kc = kc
        self.kd = kd
        self.kf1 = kf1
        self.kf2 = kf2
        self.kf3 = kf3
        self.tf = tf
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2
