"""CIM class ExcAC5A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAC5A(ExcitationSystemDynamics):
    """Modified IEEE AC5A alternator-supplied rectifier excitation system with different
    minimum controller output."""

    __slots__ = (
        "a",
        "efd1",
        "efd2",
        "ka",
        "ke",
        "kf",
        "ks",
        "seefd1",
        "seefd2",
        "ta",
        "tb",
        "tc",
        "te",
        "tf1",
        "tf2",
        "tf3",
        "vrmax",
        "vrmin",
    )

    ka: float | None  # PU
    ks: float | None  # PU
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    ta: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    ke: float | None  # PU
    te: float | None  # Seconds
    kf: float | None  # PU
    tf1: float | None  # Seconds
    tf2: float | None  # Seconds
    tf3: float | None  # Seconds
    efd1: float | None  # PU
    seefd1: float | None
    efd2: float | None  # PU
    seefd2: float | None
    a: float | None

    _cim_meta = ClassMeta(
        cim_name="ExcAC5A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{A407821B-2FF5-4e1f-992E-BCDDC0EEB4F7}",
        attributes=(
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf1", "tf1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf2", "tf2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf3", "tf3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efd1", "efd1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seefd1", "seefd1", "float", 0, 1, "primitive"),
            AttrMeta("efd2", "efd2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seefd2", "seefd2", "float", 0, 1, "primitive"),
            AttrMeta("a", "a", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        ka: float | None = None,
        ks: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        ta: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        ke: float | None = None,
        te: float | None = None,
        kf: float | None = None,
        tf1: float | None = None,
        tf2: float | None = None,
        tf3: float | None = None,
        efd1: float | None = None,
        seefd1: float | None = None,
        efd2: float | None = None,
        seefd2: float | None = None,
        a: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ka = ka
        self.ks = ks
        self.tb = tb
        self.tc = tc
        self.ta = ta
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.ke = ke
        self.te = te
        self.kf = kf
        self.tf1 = tf1
        self.tf2 = tf2
        self.tf3 = tf3
        self.efd1 = efd1
        self.seefd1 = seefd1
        self.efd2 = efd2
        self.seefd2 = seefd2
        self.a = a
