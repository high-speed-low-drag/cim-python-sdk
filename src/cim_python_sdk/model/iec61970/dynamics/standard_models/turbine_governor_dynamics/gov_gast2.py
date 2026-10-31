"""CIM class GovGAST2 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovGAST2(TurbineGovernorDynamics):
    """Gas turbine."""

    __slots__ = (
        "a",
        "af1",
        "af2",
        "b",
        "bf1",
        "bf2",
        "c",
        "cf2",
        "ecr",
        "etd",
        "k3",
        "k4",
        "k5",
        "k6",
        "kf",
        "mwbase",
        "t",
        "t3",
        "t4",
        "t5",
        "tc",
        "tcd",
        "tf",
        "tmax",
        "tmin",
        "tr",
        "trate",
        "tt",
        "w",
        "x",
        "y",
        "z",
    )

    mwbase: float | None  # ActivePower
    w: float | None  # PU
    x: float | None  # Seconds
    y: float | None  # Seconds
    z: int | None
    etd: float | None  # Seconds
    tcd: float | None  # Seconds
    trate: float | None  # ActivePower
    t: float | None  # Seconds
    tmax: float | None  # PU
    tmin: float | None  # PU
    ecr: float | None  # Seconds
    k3: float | None  # PU
    a: float | None
    b: float | None
    c: float | None
    tf: float | None  # Seconds
    kf: float | None  # PU
    k5: float | None  # PU
    k4: float | None  # PU
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    tt: float | None  # Seconds
    t5: float | None  # Seconds
    af1: float | None  # PU
    bf1: float | None  # PU
    af2: float | None  # PU
    bf2: float | None  # PU
    cf2: float | None  # PU
    tr: float | None  # Temperature
    k6: float | None  # PU
    tc: float | None  # Temperature

    _cim_meta = ClassMeta(
        cim_name="GovGAST2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{C2365E2F-CF56-49c5-A63D-1736696A686A}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("w", "w", "PU", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("y", "y", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("z", "z", "int", 0, 1, "primitive"),
            AttrMeta("etd", "etd", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tcd", "tcd", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("trate", "trate", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("t", "t", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tmax", "tmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tmin", "tmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ecr", "ecr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a", "a", "float", 0, 1, "primitive"),
            AttrMeta("b", "b", "float", 0, 1, "primitive"),
            AttrMeta("c", "c", "float", 0, 1, "primitive"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k5", "k5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k4", "k4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tt", "tt", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("af1", "af1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bf1", "bf1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("af2", "af2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bf2", "bf2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cf2", "cf2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tr", "tr", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("k6", "k6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Temperature", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        w: float | None = None,
        x: float | None = None,
        y: float | None = None,
        z: int | None = None,
        etd: float | None = None,
        tcd: float | None = None,
        trate: float | None = None,
        t: float | None = None,
        tmax: float | None = None,
        tmin: float | None = None,
        ecr: float | None = None,
        k3: float | None = None,
        a: float | None = None,
        b: float | None = None,
        c: float | None = None,
        tf: float | None = None,
        kf: float | None = None,
        k5: float | None = None,
        k4: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        tt: float | None = None,
        t5: float | None = None,
        af1: float | None = None,
        bf1: float | None = None,
        af2: float | None = None,
        bf2: float | None = None,
        cf2: float | None = None,
        tr: float | None = None,
        k6: float | None = None,
        tc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.etd = etd
        self.tcd = tcd
        self.trate = trate
        self.t = t
        self.tmax = tmax
        self.tmin = tmin
        self.ecr = ecr
        self.k3 = k3
        self.a = a
        self.b = b
        self.c = c
        self.tf = tf
        self.kf = kf
        self.k5 = k5
        self.k4 = k4
        self.t3 = t3
        self.t4 = t4
        self.tt = tt
        self.t5 = t5
        self.af1 = af1
        self.bf1 = bf1
        self.af2 = af2
        self.bf2 = bf2
        self.cf2 = cf2
        self.tr = tr
        self.k6 = k6
        self.tc = tc
