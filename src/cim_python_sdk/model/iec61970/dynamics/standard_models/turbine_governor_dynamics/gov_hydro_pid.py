"""CIM class GovHydroPID (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydroPID(TurbineGovernorDynamics):
    """PID governor and turbine."""

    __slots__ = (
        "aturb",
        "bturb",
        "db1",
        "db2",
        "eps",
        "gv1",
        "gv2",
        "gv3",
        "gv4",
        "gv5",
        "gv6",
        "input_signal",
        "kd",
        "kg",
        "ki",
        "kp",
        "mwbase",
        "pgv1",
        "pgv2",
        "pgv3",
        "pgv4",
        "pgv5",
        "pgv6",
        "pmax",
        "pmin",
        "r",
        "td",
        "tf",
        "tp",
        "tt",
        "tturb",
        "velcl",
        "velop",
    )

    mwbase: float | None  # ActivePower
    pmax: float | None  # PU
    pmin: float | None  # PU
    r: float | None  # PU
    td: float | None  # Seconds
    tf: float | None  # Seconds
    tp: float | None  # Seconds
    velop: float | None
    velcl: float | None
    kd: float | None  # PU
    kp: float | None  # PU
    ki: float | None  # PU
    kg: float | None  # PU
    tturb: float | None  # Seconds
    aturb: float | None  # PU
    bturb: float | None  # PU
    tt: float | None  # Seconds
    db1: float | None  # Frequency
    input_signal: bool | None
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

    _cim_meta = ClassMeta(
        cim_name="GovHydroPID",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{FEAAA52E-0434-4656-B9A3-2A08B0768840}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PU", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("velop", "velop", "float", 0, 1, "primitive"),
            AttrMeta("velcl", "velcl", "float", 0, 1, "primitive"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tturb", "tturb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("aturb", "aturb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bturb", "bturb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tt", "tt", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("db1", "db1", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("input_signal", "inputSignal", "bool", 0, 1, "primitive"),
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
        tf: float | None = None,
        tp: float | None = None,
        velop: float | None = None,
        velcl: float | None = None,
        kd: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        kg: float | None = None,
        tturb: float | None = None,
        aturb: float | None = None,
        bturb: float | None = None,
        tt: float | None = None,
        db1: float | None = None,
        input_signal: bool | None = None,
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
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.pmax = pmax
        self.pmin = pmin
        self.r = r
        self.td = td
        self.tf = tf
        self.tp = tp
        self.velop = velop
        self.velcl = velcl
        self.kd = kd
        self.kp = kp
        self.ki = ki
        self.kg = kg
        self.tturb = tturb
        self.aturb = aturb
        self.bturb = bturb
        self.tt = tt
        self.db1 = db1
        self.input_signal = input_signal
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
