"""CIM class ExcST1A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcST1A(ExcitationSystemDynamics):
    """Modification of an old IEEE ST1A static excitation system without overexcitation limiter
    (OEL) and underexcitation limiter (UEL)."""

    __slots__ = (
        "ilr",
        "ka",
        "kc",
        "kf",
        "klr",
        "ta",
        "tb",
        "tb1",
        "tc",
        "tc1",
        "tf",
        "vamax",
        "vamin",
        "vimax",
        "vimin",
        "vrmax",
        "vrmin",
        "xe",
    )

    vimax: float | None  # PU
    vimin: float | None  # PU
    tc: float | None  # Seconds
    tb: float | None  # Seconds
    ka: float | None  # PU
    ta: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    kc: float | None  # PU
    kf: float | None  # PU
    tf: float | None  # Seconds
    tc1: float | None  # Seconds
    tb1: float | None  # Seconds
    vamax: float | None  # PU
    vamin: float | None  # PU
    ilr: float | None  # PU
    klr: float | None  # PU
    xe: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcST1A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{704F07B6-4C3F-40eb-8C13-F964EDFE8BE9}",
        attributes=(
            AttrMeta("vimax", "vimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimin", "vimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc1", "tc1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb1", "tb1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ilr", "ilr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("klr", "klr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xe", "xe", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        vimax: float | None = None,
        vimin: float | None = None,
        tc: float | None = None,
        tb: float | None = None,
        ka: float | None = None,
        ta: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        kc: float | None = None,
        kf: float | None = None,
        tf: float | None = None,
        tc1: float | None = None,
        tb1: float | None = None,
        vamax: float | None = None,
        vamin: float | None = None,
        ilr: float | None = None,
        klr: float | None = None,
        xe: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vimax = vimax
        self.vimin = vimin
        self.tc = tc
        self.tb = tb
        self.ka = ka
        self.ta = ta
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.kc = kc
        self.kf = kf
        self.tf = tf
        self.tc1 = tc1
        self.tb1 = tb1
        self.vamax = vamax
        self.vamin = vamin
        self.ilr = ilr
        self.klr = klr
        self.xe = xe
