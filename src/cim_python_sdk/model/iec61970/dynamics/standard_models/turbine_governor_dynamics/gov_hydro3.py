"""CIM class GovHydro3 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydro3(TurbineGovernorDynamics):
    """Modified IEEE hydro governor-turbine. This model differs from that defined in the IEEE
    modelling guideline paper in that the limits on gate position and velocity do not permit
    "wind up" of the upstream signals."""

    __slots__ = (
        "at",
        "db1",
        "db2",
        "dturb",
        "eps",
        "governor_control",
        "gv1",
        "gv2",
        "gv3",
        "gv4",
        "gv5",
        "gv6",
        "h0",
        "k1",
        "k2",
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
        "relec",
        "rgate",
        "td",
        "tf",
        "tp",
        "tt",
        "tw",
        "velcl",
        "velop",
    )

    mwbase: float | None  # ActivePower
    pmax: float | None  # PU
    pmin: float | None  # PU
    governor_control: bool | None
    rgate: float | None  # PU
    relec: float | None  # PU
    td: float | None  # Seconds
    tf: float | None  # Seconds
    tp: float | None  # Seconds
    velop: float | None
    velcl: float | None
    k1: float | None  # PU
    k2: float | None  # PU
    ki: float | None  # PU
    kg: float | None  # PU
    tt: float | None  # Seconds
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
        cim_name="GovHydro3",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{EB80B6E9-4479-49dd-AFA2-66D75F934300}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("governor_control", "governorControl", "bool", 0, 1, "primitive"),
            AttrMeta("rgate", "rgate", "PU", 0, 1, "cimdatatype"),
            AttrMeta("relec", "relec", "PU", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("velop", "velop", "float", 0, 1, "primitive"),
            AttrMeta("velcl", "velcl", "float", 0, 1, "primitive"),
            AttrMeta("k1", "k1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tt", "tt", "Seconds", 0, 1, "cimdatatype"),
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
        governor_control: bool | None = None,
        rgate: float | None = None,
        relec: float | None = None,
        td: float | None = None,
        tf: float | None = None,
        tp: float | None = None,
        velop: float | None = None,
        velcl: float | None = None,
        k1: float | None = None,
        k2: float | None = None,
        ki: float | None = None,
        kg: float | None = None,
        tt: float | None = None,
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
        self.governor_control = governor_control
        self.rgate = rgate
        self.relec = relec
        self.td = td
        self.tf = tf
        self.tp = tp
        self.velop = velop
        self.velcl = velcl
        self.k1 = k1
        self.k2 = k2
        self.ki = ki
        self.kg = kg
        self.tt = tt
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
