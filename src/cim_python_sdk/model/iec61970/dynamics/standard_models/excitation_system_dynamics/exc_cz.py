"""CIM class ExcCZ (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcCZ(ExcitationSystemDynamics):
    """Czech proportion/integral exciter."""

    __slots__ = ("efdmax", "efdmin", "ka", "ke", "kp", "ta", "tc", "te", "vrmax", "vrmin")

    kp: float | None  # PU
    tc: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    ka: float | None  # PU
    ta: float | None  # Seconds
    ke: float | None  # PU
    te: float | None  # Seconds
    efdmax: float | None  # PU
    efdmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcCZ",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{EA437F0B-982E-4c6e-A9CF-C619F70D7E11}",
        attributes=(
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efdmax", "efdmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdmin", "efdmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        kp: float | None = None,
        tc: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        ka: float | None = None,
        ta: float | None = None,
        ke: float | None = None,
        te: float | None = None,
        efdmax: float | None = None,
        efdmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kp = kp
        self.tc = tc
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.ka = ka
        self.ta = ta
        self.ke = ke
        self.te = te
        self.efdmax = efdmax
        self.efdmin = efdmin
