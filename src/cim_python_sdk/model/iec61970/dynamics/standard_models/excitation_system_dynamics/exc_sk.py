"""CIM class ExcSK (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcSK(ExcitationSystemDynamics):
    """Slovakian excitation system. UEL and secondary voltage control are included in this
    model. When this model is used, there cannot be a separate underexcitation limiter or
    VAr controller model."""

    __slots__ = (
        "efdmax",
        "efdmin",
        "emax",
        "emin",
        "k",
        "k1",
        "k2",
        "kc",
        "kce",
        "kd",
        "kgob",
        "kp",
        "kqi",
        "kqob",
        "kqp",
        "nq",
        "qconoff",
        "qz",
        "remote",
        "sbase",
        "tc",
        "te",
        "ti",
        "tp",
        "tr",
        "uimax",
        "uimin",
        "urmax",
        "urmin",
        "vtmax",
        "vtmin",
        "yp",
    )

    efdmax: float | None  # PU
    efdmin: float | None  # PU
    emax: float | None  # PU
    emin: float | None  # PU
    k: float | None  # PU
    k1: float | None  # PU
    k2: float | None  # PU
    kc: float | None  # PU
    kce: float | None  # PU
    kd: float | None  # PU
    kgob: float | None  # PU
    kp: float | None  # PU
    kqi: float | None  # PU
    kqob: float | None  # PU
    kqp: float | None  # PU
    nq: float | None  # PU
    qconoff: bool | None
    qz: float | None  # PU
    remote: bool | None
    sbase: float | None  # ApparentPower
    tc: float | None  # Seconds
    te: float | None  # Seconds
    ti: float | None  # Seconds
    tp: float | None  # Seconds
    tr: float | None  # Seconds
    uimax: float | None  # PU
    uimin: float | None  # PU
    urmax: float | None  # PU
    urmin: float | None  # PU
    vtmax: float | None  # PU
    vtmin: float | None  # PU
    yp: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcSK",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{1EE78E1C-0446-48dd-87E8-AA4990E99CB7}",
        attributes=(
            AttrMeta("efdmax", "efdmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdmin", "efdmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("emax", "emax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("emin", "emin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k1", "k1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kce", "kce", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kgob", "kgob", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kqi", "kqi", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kqob", "kqob", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kqp", "kqp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("nq", "nq", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qconoff", "qconoff", "bool", 0, 1, "primitive"),
            AttrMeta("qz", "qz", "PU", 0, 1, "cimdatatype"),
            AttrMeta("remote", "remote", "bool", 0, 1, "primitive"),
            AttrMeta("sbase", "sbase", "ApparentPower", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ti", "ti", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tr", "tr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uimax", "uimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("uimin", "uimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("urmax", "urmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("urmin", "urmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vtmax", "vtmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vtmin", "vtmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("yp", "yp", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        efdmax: float | None = None,
        efdmin: float | None = None,
        emax: float | None = None,
        emin: float | None = None,
        k: float | None = None,
        k1: float | None = None,
        k2: float | None = None,
        kc: float | None = None,
        kce: float | None = None,
        kd: float | None = None,
        kgob: float | None = None,
        kp: float | None = None,
        kqi: float | None = None,
        kqob: float | None = None,
        kqp: float | None = None,
        nq: float | None = None,
        qconoff: bool | None = None,
        qz: float | None = None,
        remote: bool | None = None,
        sbase: float | None = None,
        tc: float | None = None,
        te: float | None = None,
        ti: float | None = None,
        tp: float | None = None,
        tr: float | None = None,
        uimax: float | None = None,
        uimin: float | None = None,
        urmax: float | None = None,
        urmin: float | None = None,
        vtmax: float | None = None,
        vtmin: float | None = None,
        yp: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.efdmax = efdmax
        self.efdmin = efdmin
        self.emax = emax
        self.emin = emin
        self.k = k
        self.k1 = k1
        self.k2 = k2
        self.kc = kc
        self.kce = kce
        self.kd = kd
        self.kgob = kgob
        self.kp = kp
        self.kqi = kqi
        self.kqob = kqob
        self.kqp = kqp
        self.nq = nq
        self.qconoff = qconoff
        self.qz = qz
        self.remote = remote
        self.sbase = sbase
        self.tc = tc
        self.te = te
        self.ti = ti
        self.tp = tp
        self.tr = tr
        self.uimax = uimax
        self.uimin = uimin
        self.urmax = urmax
        self.urmin = urmin
        self.vtmax = vtmax
        self.vtmin = vtmin
        self.yp = yp
