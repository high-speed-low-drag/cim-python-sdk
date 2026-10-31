"""CIM class GovGASTWD (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovGASTWD(TurbineGovernorDynamics):
    """Woodward™ gas turbine governor.

    [Footnote: Woodward gas turbines are an example of suitable products available
    commercially. This information is given for the convenience of users of this document
    and does not constitute an endorsement by IEC of these products.]"""

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
        "kd",
        "kdroop",
        "kf",
        "ki",
        "kp",
        "mwbase",
        "t",
        "t3",
        "t4",
        "t5",
        "tc",
        "tcd",
        "td",
        "tf",
        "tmax",
        "tmin",
        "tr",
        "trate",
        "tt",
    )

    mwbase: float | None  # ActivePower
    kdroop: float | None  # PU
    kp: float | None  # PU
    ki: float | None  # PU
    kd: float | None  # PU
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
    td: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="GovGASTWD",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{659A678F-7407-4f04-82AE-D55250A64A93}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("kdroop", "kdroop", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
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
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        kdroop: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        kd: float | None = None,
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
        td: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.kdroop = kdroop
        self.kp = kp
        self.ki = ki
        self.kd = kd
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
        self.td = td
