"""CIM class GovHydro2 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydro2(TurbineGovernorDynamics):
    """IEEE hydro turbine governor with straightforward penstock configuration and
    hydraulic-dashpot governor."""

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
        "kturb",
        "mwbase",
        "pgv1",
        "pgv2",
        "pgv3",
        "pgv4",
        "pgv5",
        "pgv6",
        "pmax",
        "pmin",
        "rperm",
        "rtemp",
        "tg",
        "tp",
        "tr",
        "tw",
        "uc",
        "uo",
    )

    mwbase: float | None  # ActivePower
    tg: float | None  # Seconds
    tp: float | None  # Seconds
    uo: float | None
    uc: float | None
    pmax: float | None  # PU
    pmin: float | None  # PU
    rperm: float | None  # PU
    rtemp: float | None  # PU
    tr: float | None  # Seconds
    tw: float | None  # Seconds
    kturb: float | None  # PU
    aturb: float | None  # PU
    bturb: float | None  # PU
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

    _cim_meta = ClassMeta(
        cim_name="GovHydro2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{A9B869A0-0669-477d-BA5B-55EE790D8878}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uo", "uo", "float", 0, 1, "primitive"),
            AttrMeta("uc", "uc", "float", 0, 1, "primitive"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rperm", "rperm", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rtemp", "rtemp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tr", "tr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw", "tw", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kturb", "kturb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("aturb", "aturb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bturb", "bturb", "PU", 0, 1, "cimdatatype"),
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
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        tg: float | None = None,
        tp: float | None = None,
        uo: float | None = None,
        uc: float | None = None,
        pmax: float | None = None,
        pmin: float | None = None,
        rperm: float | None = None,
        rtemp: float | None = None,
        tr: float | None = None,
        tw: float | None = None,
        kturb: float | None = None,
        aturb: float | None = None,
        bturb: float | None = None,
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
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.tg = tg
        self.tp = tp
        self.uo = uo
        self.uc = uc
        self.pmax = pmax
        self.pmin = pmin
        self.rperm = rperm
        self.rtemp = rtemp
        self.tr = tr
        self.tw = tw
        self.kturb = kturb
        self.aturb = aturb
        self.bturb = bturb
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
