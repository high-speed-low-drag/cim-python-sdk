"""CIM class ExcOEX3T (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcOEX3T(ExcitationSystemDynamics):
    """Modified IEEE type ST1 excitation system with semi-continuous and acting terminal
    voltage limiter."""

    __slots__ = (
        "e1",
        "e2",
        "ka",
        "kc",
        "kd",
        "ke",
        "kf",
        "see1",
        "see2",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
        "te",
        "tf",
        "vrmax",
        "vrmin",
    )

    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    ka: float | None  # PU
    t5: float | None  # Seconds
    t6: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    te: float | None  # Seconds
    kf: float | None  # PU
    tf: float | None  # Seconds
    kc: float | None  # PU
    kd: float | None  # PU
    ke: float | None  # PU
    e1: float | None  # PU
    see1: float | None  # PU
    e2: float | None  # PU
    see2: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcOEX3T",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{886558CE-899B-4d55-BB83-B7F73C5F663F}",
        attributes=(
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("e1", "e1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("see1", "see1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("e2", "e2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("see2", "see2", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        ka: float | None = None,
        t5: float | None = None,
        t6: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        te: float | None = None,
        kf: float | None = None,
        tf: float | None = None,
        kc: float | None = None,
        kd: float | None = None,
        ke: float | None = None,
        e1: float | None = None,
        see1: float | None = None,
        e2: float | None = None,
        see2: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.ka = ka
        self.t5 = t5
        self.t6 = t6
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.te = te
        self.kf = kf
        self.tf = tf
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.e1 = e1
        self.see1 = see1
        self.e2 = e2
        self.see2 = see2
