"""CIM class GovHydroR (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydroR(TurbineGovernorDynamics):
    """Fourth order lead-lag governor and hydro turbine."""

    __slots__ = (
        "at",
        "db1",
        "db2",
        "dturb",
        "eps",
        "gmax",
        "gmin",
        "gv1",
        "gv2",
        "gv3",
        "gv4",
        "gv5",
        "gv6",
        "h0",
        "input_signal",
        "kg",
        "ki",
        "mwbase",
        "pgv1",
        "pgv2",
        "pgv3",
        "pgv4",
        "pgv5",
        "pgv6",
        "pmax",
        "pmin",
        "qnl",
        "r",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
        "t7",
        "t8",
        "td",
        "tp",
        "tt",
        "tw",
        "velcl",
        "velop",
    )

    mwbase: float | None  # ActivePower
    pmax: float | None  # PU
    pmin: float | None  # PU
    r: float | None  # PU
    td: float | None  # Seconds
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    t5: float | None  # Seconds
    t6: float | None  # Seconds
    t7: float | None  # Seconds
    t8: float | None  # Seconds
    tp: float | None  # Seconds
    velop: float | None
    velcl: float | None
    ki: float | None  # PU
    kg: float | None  # PU
    gmax: float | None  # PU
    gmin: float | None  # PU
    tt: float | None  # Seconds
    input_signal: bool | None
    db1: float | None  # Frequency
    eps: float | None  # Frequency
    db2: float | None  # ActivePower
    tw: float | None  # Seconds
    at: float | None  # PU
    dturb: float | None  # PU
    qnl: float | None  # PU
    h0: float | None  # PU
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

    _cim_meta = ClassMeta(
        cim_name="GovHydroR",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{38EF4670-8EAE-4d49-8476-65B3666140D4}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PU", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t7", "t7", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t8", "t8", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("velop", "velop", "float", 0, 1, "primitive"),
            AttrMeta("velcl", "velcl", "float", 0, 1, "primitive"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gmax", "gmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gmin", "gmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tt", "tt", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("input_signal", "inputSignal", "bool", 0, 1, "primitive"),
            AttrMeta("db1", "db1", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("eps", "eps", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("db2", "db2", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("tw", "tw", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("at", "at", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dturb", "dturb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qnl", "qnl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("h0", "h0", "PU", 0, 1, "cimdatatype"),
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
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        pmax: float | None = None,
        pmin: float | None = None,
        r: float | None = None,
        td: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        t5: float | None = None,
        t6: float | None = None,
        t7: float | None = None,
        t8: float | None = None,
        tp: float | None = None,
        velop: float | None = None,
        velcl: float | None = None,
        ki: float | None = None,
        kg: float | None = None,
        gmax: float | None = None,
        gmin: float | None = None,
        tt: float | None = None,
        input_signal: bool | None = None,
        db1: float | None = None,
        eps: float | None = None,
        db2: float | None = None,
        tw: float | None = None,
        at: float | None = None,
        dturb: float | None = None,
        qnl: float | None = None,
        h0: float | None = None,
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
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.pmax = pmax
        self.pmin = pmin
        self.r = r
        self.td = td
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8
        self.tp = tp
        self.velop = velop
        self.velcl = velcl
        self.ki = ki
        self.kg = kg
        self.gmax = gmax
        self.gmin = gmin
        self.tt = tt
        self.input_signal = input_signal
        self.db1 = db1
        self.eps = eps
        self.db2 = db2
        self.tw = tw
        self.at = at
        self.dturb = dturb
        self.qnl = qnl
        self.h0 = h0
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
