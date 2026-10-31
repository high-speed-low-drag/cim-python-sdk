"""CIM class ExcPIC (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcPIC(ExcitationSystemDynamics):
    """Proportional/integral regulator excitation system. This model can be used to represent
    excitation systems with a proportional-integral (PI) voltage regulator controller."""

    __slots__ = (
        "e1",
        "e2",
        "efdmax",
        "efdmin",
        "ka",
        "kc",
        "ke",
        "kf",
        "ki",
        "kp",
        "se1",
        "se2",
        "ta1",
        "ta2",
        "ta3",
        "ta4",
        "te",
        "tf1",
        "tf2",
        "vr1",
        "vr2",
        "vrmax",
        "vrmin",
    )

    ka: float | None  # PU
    ta1: float | None  # Seconds
    vr1: float | None  # PU
    vr2: float | None  # PU
    ta2: float | None  # Seconds
    ta3: float | None  # Seconds
    ta4: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    kf: float | None  # PU
    tf1: float | None  # Seconds
    tf2: float | None  # Seconds
    efdmax: float | None  # PU
    efdmin: float | None  # PU
    ke: float | None  # PU
    te: float | None  # Seconds
    e1: float | None  # PU
    se1: float | None  # PU
    e2: float | None  # PU
    se2: float | None  # PU
    kp: float | None  # PU
    ki: float | None  # PU
    kc: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcPIC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{059AD67D-F00F-4fff-A769-4267112802A1}",
        attributes=(
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta1", "ta1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vr1", "vr1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vr2", "vr2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta2", "ta2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ta3", "ta3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ta4", "ta4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf1", "tf1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf2", "tf2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efdmax", "efdmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdmin", "efdmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("e1", "e1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("se1", "se1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("e2", "e2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("se2", "se2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ka: float | None = None,
        ta1: float | None = None,
        vr1: float | None = None,
        vr2: float | None = None,
        ta2: float | None = None,
        ta3: float | None = None,
        ta4: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        kf: float | None = None,
        tf1: float | None = None,
        tf2: float | None = None,
        efdmax: float | None = None,
        efdmin: float | None = None,
        ke: float | None = None,
        te: float | None = None,
        e1: float | None = None,
        se1: float | None = None,
        e2: float | None = None,
        se2: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        kc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ka = ka
        self.ta1 = ta1
        self.vr1 = vr1
        self.vr2 = vr2
        self.ta2 = ta2
        self.ta3 = ta3
        self.ta4 = ta4
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.kf = kf
        self.tf1 = tf1
        self.tf2 = tf2
        self.efdmax = efdmax
        self.efdmin = efdmin
        self.ke = ke
        self.te = te
        self.e1 = e1
        self.se1 = se1
        self.e2 = e2
        self.se2 = se2
        self.kp = kp
        self.ki = ki
        self.kc = kc
