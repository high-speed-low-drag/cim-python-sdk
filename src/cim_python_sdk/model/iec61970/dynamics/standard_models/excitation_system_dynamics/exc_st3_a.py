"""CIM class ExcST3A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcST3A(ExcitationSystemDynamics):
    """Modified IEEE ST3A static excitation system with added speed multiplier."""

    __slots__ = (
        "efdmax",
        "kc",
        "kg",
        "ki",
        "kj",
        "km",
        "kp",
        "ks",
        "ks1",
        "tb",
        "tc",
        "thetap",
        "tm",
        "vbmax",
        "vgmax",
        "vimax",
        "vimin",
        "vrmax",
        "vrmin",
        "xl",
    )

    vimax: float | None  # PU
    vimin: float | None  # PU
    kj: float | None  # PU
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    efdmax: float | None  # PU
    km: float | None  # PU
    tm: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    kg: float | None  # PU
    kp: float | None  # PU
    thetap: float | None  # AngleDegrees
    ki: float | None  # PU
    kc: float | None  # PU
    xl: float | None  # PU
    vbmax: float | None  # PU
    vgmax: float | None  # PU
    ks: float | None  # PU
    ks1: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcST3A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{9FA72263-AE74-4911-969F-64971BC90618}",
        attributes=(
            AttrMeta("vimax", "vimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimin", "vimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kj", "kj", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efdmax", "efdmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("km", "km", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tm", "tm", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("thetap", "thetap", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xl", "xl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vbmax", "vbmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vgmax", "vgmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks1", "ks1", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        vimax: float | None = None,
        vimin: float | None = None,
        kj: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        efdmax: float | None = None,
        km: float | None = None,
        tm: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        kg: float | None = None,
        kp: float | None = None,
        thetap: float | None = None,
        ki: float | None = None,
        kc: float | None = None,
        xl: float | None = None,
        vbmax: float | None = None,
        vgmax: float | None = None,
        ks: float | None = None,
        ks1: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vimax = vimax
        self.vimin = vimin
        self.kj = kj
        self.tb = tb
        self.tc = tc
        self.efdmax = efdmax
        self.km = km
        self.tm = tm
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.kg = kg
        self.kp = kp
        self.thetap = thetap
        self.ki = ki
        self.kc = kc
        self.xl = xl
        self.vbmax = vbmax
        self.vgmax = vgmax
        self.ks = ks
        self.ks1 = ks1
