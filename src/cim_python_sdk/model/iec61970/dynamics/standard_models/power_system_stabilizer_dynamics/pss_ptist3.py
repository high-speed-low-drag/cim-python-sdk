"""CIM class PssPTIST3 (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssPTIST3(PowerSystemStabilizerDynamics):
    """PTI microprocessor-based stabilizer type 3."""

    __slots__ = (
        "a0",
        "a1",
        "a2",
        "a3",
        "a4",
        "a5",
        "al",
        "athres",
        "b0",
        "b1",
        "b2",
        "b3",
        "b4",
        "b5",
        "dl",
        "dtc",
        "dtf",
        "dtp",
        "isw",
        "k",
        "lthres",
        "m",
        "nav",
        "ncl",
        "ncr",
        "pmin",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
        "tf",
        "tp",
    )

    m: float | None  # PU
    tf: float | None  # Seconds
    tp: float | None  # Seconds
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    k: float | None  # PU
    dtf: float | None  # Seconds
    dtc: float | None  # Seconds
    dtp: float | None  # Seconds
    t5: float | None  # Seconds
    t6: float | None  # Seconds
    a0: float | None  # PU
    a1: float | None  # PU
    a2: float | None  # PU
    b0: float | None  # PU
    b1: float | None  # PU
    b2: float | None  # PU
    a3: float | None  # PU
    a4: float | None  # PU
    a5: float | None  # PU
    b3: float | None  # PU
    b4: float | None  # PU
    b5: float | None  # PU
    athres: float | None  # PU
    dl: float | None  # PU
    al: float | None  # PU
    lthres: float | None  # PU
    pmin: float | None  # PU
    isw: bool | None
    nav: float | None
    ncl: float | None
    ncr: float | None

    _cim_meta = ClassMeta(
        cim_name="PssPTIST3",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{D0383527-C7C2-43b3-BDA2-2185C523E0C2}",
        attributes=(
            AttrMeta("m", "m", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dtf", "dtf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("dtc", "dtc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("dtp", "dtp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("a0", "a0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a1", "a1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a2", "a2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("b0", "b0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("b1", "b1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("b2", "b2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a3", "a3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a4", "a4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a5", "a5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("b3", "b3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("b4", "b4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("b5", "b5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("athres", "athres", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dl", "dl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("al", "al", "PU", 0, 1, "cimdatatype"),
            AttrMeta("lthres", "lthres", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("isw", "isw", "bool", 0, 1, "primitive"),
            AttrMeta("nav", "nav", "float", 0, 1, "primitive"),
            AttrMeta("ncl", "ncl", "float", 0, 1, "primitive"),
            AttrMeta("ncr", "ncr", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        m: float | None = None,
        tf: float | None = None,
        tp: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        k: float | None = None,
        dtf: float | None = None,
        dtc: float | None = None,
        dtp: float | None = None,
        t5: float | None = None,
        t6: float | None = None,
        a0: float | None = None,
        a1: float | None = None,
        a2: float | None = None,
        b0: float | None = None,
        b1: float | None = None,
        b2: float | None = None,
        a3: float | None = None,
        a4: float | None = None,
        a5: float | None = None,
        b3: float | None = None,
        b4: float | None = None,
        b5: float | None = None,
        athres: float | None = None,
        dl: float | None = None,
        al: float | None = None,
        lthres: float | None = None,
        pmin: float | None = None,
        isw: bool | None = None,
        nav: float | None = None,
        ncl: float | None = None,
        ncr: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.m = m
        self.tf = tf
        self.tp = tp
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.k = k
        self.dtf = dtf
        self.dtc = dtc
        self.dtp = dtp
        self.t5 = t5
        self.t6 = t6
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.athres = athres
        self.dl = dl
        self.al = al
        self.lthres = lthres
        self.pmin = pmin
        self.isw = isw
        self.nav = nav
        self.ncl = ncl
        self.ncr = ncr
