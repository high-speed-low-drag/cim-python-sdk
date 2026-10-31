"""CIM class GovGAST1 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovGAST1(TurbineGovernorDynamics):
    """Modified single shaft gas turbine."""

    __slots__ = (
        "a",
        "b",
        "db1",
        "db2",
        "eps",
        "fidle",
        "gv1",
        "gv2",
        "gv3",
        "gv4",
        "gv5",
        "gv6",
        "ka",
        "kt",
        "lmax",
        "loadinc",
        "ltrate",
        "mwbase",
        "pgv1",
        "pgv2",
        "pgv3",
        "pgv4",
        "pgv5",
        "pgv6",
        "r",
        "rmax",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "tltr",
        "vmax",
        "vmin",
    )

    mwbase: float | None  # ActivePower
    r: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    lmax: float | None  # PU
    kt: float | None  # PU
    vmax: float | None  # PU
    vmin: float | None  # PU
    fidle: float | None  # PU
    rmax: float | None
    loadinc: float | None  # PU
    tltr: float | None  # Seconds
    ltrate: float | None
    a: float | None
    b: float | None
    db1: float | None  # Frequency
    eps: float | None  # Frequency
    db2: float | None  # ActivePower
    gv1: float | None  # PU
    pgv1: float | None  # PU
    gv2: float | None  # PU
    pgv2: float | None  # PU
    gv3: float | None  # PU
    pgv3: float | None  # PU
    gv4: float | None  # PU
    pgv4: float | None  # PU
    gv5: float | None  # PU
    pgv5: float | None  # PU
    gv6: float | None  # PU
    pgv6: float | None  # PU
    ka: float | None  # PU
    t4: float | None  # Seconds
    t5: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="GovGAST1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{B63B3483-F3C3-4acb-B076-AE361754C3C1}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("lmax", "lmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kt", "kt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmax", "vmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmin", "vmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fidle", "fidle", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rmax", "rmax", "float", 0, 1, "primitive"),
            AttrMeta("loadinc", "loadinc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tltr", "tltr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ltrate", "ltrate", "float", 0, 1, "primitive"),
            AttrMeta("a", "a", "float", 0, 1, "primitive"),
            AttrMeta("b", "b", "float", 0, 1, "primitive"),
            AttrMeta("db1", "db1", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("eps", "eps", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("db2", "db2", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("gv1", "gv1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv1", "pgv1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv2", "gv2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv2", "pgv2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv3", "gv3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv3", "pgv3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv4", "gv4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv4", "pgv4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv5", "gv5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv5", "pgv5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv6", "gv6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv6", "pgv6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        r: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        lmax: float | None = None,
        kt: float | None = None,
        vmax: float | None = None,
        vmin: float | None = None,
        fidle: float | None = None,
        rmax: float | None = None,
        loadinc: float | None = None,
        tltr: float | None = None,
        ltrate: float | None = None,
        a: float | None = None,
        b: float | None = None,
        db1: float | None = None,
        eps: float | None = None,
        db2: float | None = None,
        gv1: float | None = None,
        pgv1: float | None = None,
        gv2: float | None = None,
        pgv2: float | None = None,
        gv3: float | None = None,
        pgv3: float | None = None,
        gv4: float | None = None,
        pgv4: float | None = None,
        gv5: float | None = None,
        pgv5: float | None = None,
        gv6: float | None = None,
        pgv6: float | None = None,
        ka: float | None = None,
        t4: float | None = None,
        t5: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.r = r
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.lmax = lmax
        self.kt = kt
        self.vmax = vmax
        self.vmin = vmin
        self.fidle = fidle
        self.rmax = rmax
        self.loadinc = loadinc
        self.tltr = tltr
        self.ltrate = ltrate
        self.a = a
        self.b = b
        self.db1 = db1
        self.eps = eps
        self.db2 = db2
        self.gv1 = gv1
        self.pgv1 = pgv1
        self.gv2 = gv2
        self.pgv2 = pgv2
        self.gv3 = gv3
        self.pgv3 = pgv3
        self.gv4 = gv4
        self.pgv4 = pgv4
        self.gv5 = gv5
        self.pgv5 = pgv5
        self.gv6 = gv6
        self.pgv6 = pgv6
        self.ka = ka
        self.t4 = t4
        self.t5 = t5
