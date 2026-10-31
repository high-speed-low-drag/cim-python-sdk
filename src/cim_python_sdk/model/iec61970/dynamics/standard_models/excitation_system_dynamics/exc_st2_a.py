"""CIM class ExcST2A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcST2A(ExcitationSystemDynamics):
    """Modified IEEE ST2A static excitation system with another lead-lag block added to match
    the model defined by WECC."""

    __slots__ = (
        "efdmax",
        "ka",
        "kc",
        "ke",
        "kf",
        "ki",
        "kp",
        "ta",
        "tb",
        "tc",
        "te",
        "tf",
        "uelin",
        "vrmax",
        "vrmin",
    )

    ka: float | None  # PU
    ta: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    ke: float | None  # PU
    te: float | None  # Seconds
    kf: float | None  # PU
    tf: float | None  # Seconds
    kp: float | None  # PU
    ki: float | None  # PU
    kc: float | None  # PU
    efdmax: float | None  # PU
    uelin: bool | None
    tb: float | None  # Seconds
    tc: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="ExcST2A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{5F48CA29-4D28-45f2-A46C-A49FA24CCB5F}",
        attributes=(
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdmax", "efdmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("uelin", "uelin", "bool", 0, 1, "primitive"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ka: float | None = None,
        ta: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        ke: float | None = None,
        te: float | None = None,
        kf: float | None = None,
        tf: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        kc: float | None = None,
        efdmax: float | None = None,
        uelin: bool | None = None,
        tb: float | None = None,
        tc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ka = ka
        self.ta = ta
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.ke = ke
        self.te = te
        self.kf = kf
        self.tf = tf
        self.kp = kp
        self.ki = ki
        self.kc = kc
        self.efdmax = efdmax
        self.uelin = uelin
        self.tb = tb
        self.tc = tc
