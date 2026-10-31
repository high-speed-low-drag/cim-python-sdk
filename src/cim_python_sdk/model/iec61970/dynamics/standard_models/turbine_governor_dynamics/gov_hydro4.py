"""CIM class GovHydro4 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.gov_hydro4_model_kind import (
        GovHydro4ModelKind,
    )


class GovHydro4(TurbineGovernorDynamics):
    """Hydro turbine and governor. Represents plants with straight-forward penstock
    configurations and hydraulic governors of the traditional 'dashpot' type. This model can
    be used to represent simple, Francis/Pelton or Kaplan turbines."""

    __slots__ = (
        "at",
        "bgv0",
        "bgv1",
        "bgv2",
        "bgv3",
        "bgv4",
        "bgv5",
        "bmax",
        "db1",
        "db2",
        "dturb",
        "eps",
        "gmax",
        "gmin",
        "gv0",
        "gv1",
        "gv2",
        "gv3",
        "gv4",
        "gv5",
        "hdam",
        "model",
        "mwbase",
        "pgv0",
        "pgv1",
        "pgv2",
        "pgv3",
        "pgv4",
        "pgv5",
        "qnl",
        "rperm",
        "rtemp",
        "tblade",
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
    gmax: float | None  # PU
    gmin: float | None  # PU
    rperm: float | None  # Seconds
    rtemp: float | None  # Seconds
    tr: float | None  # Seconds
    tw: float | None  # Seconds
    at: float | None  # PU
    dturb: float | None  # PU
    hdam: float | None  # PU
    qnl: float | None  # PU
    db1: float | None  # Frequency
    eps: float | None  # Frequency
    db2: float | None  # ActivePower
    gv0: float | None  # PU
    pgv0: float | None  # PU
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
    bgv0: float | None  # PU
    bgv1: float | None  # PU
    bgv2: float | None  # PU
    bgv3: float | None  # PU
    bgv4: float | None  # PU
    bgv5: float | None  # PU
    bmax: float | None
    tblade: float | None  # Seconds
    model: GovHydro4ModelKind | None

    _cim_meta = ClassMeta(
        cim_name="GovHydro4",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{4E8A3071-7AC6-490c-A12C-5BD140E8D992}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uo", "uo", "float", 0, 1, "primitive"),
            AttrMeta("uc", "uc", "float", 0, 1, "primitive"),
            AttrMeta("gmax", "gmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gmin", "gmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rperm", "rperm", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("rtemp", "rtemp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tr", "tr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw", "tw", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("at", "at", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dturb", "dturb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("hdam", "hdam", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qnl", "qnl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("db1", "db1", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("eps", "eps", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("db2", "db2", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("gv0", "gv0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv0", "pgv0", "PU", 0, 1, "cimdatatype"),
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
            AttrMeta("bgv0", "bgv0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bgv1", "bgv1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bgv2", "bgv2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bgv3", "bgv3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bgv4", "bgv4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bgv5", "bgv5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("bmax", "bmax", "float", 0, 1, "primitive"),
            AttrMeta("tblade", "tblade", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("model", "model", "GovHydro4ModelKind", 0, 1, "enumeration"),
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
        gmax: float | None = None,
        gmin: float | None = None,
        rperm: float | None = None,
        rtemp: float | None = None,
        tr: float | None = None,
        tw: float | None = None,
        at: float | None = None,
        dturb: float | None = None,
        hdam: float | None = None,
        qnl: float | None = None,
        db1: float | None = None,
        eps: float | None = None,
        db2: float | None = None,
        gv0: float | None = None,
        pgv0: float | None = None,
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
        bgv0: float | None = None,
        bgv1: float | None = None,
        bgv2: float | None = None,
        bgv3: float | None = None,
        bgv4: float | None = None,
        bgv5: float | None = None,
        bmax: float | None = None,
        tblade: float | None = None,
        model: GovHydro4ModelKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.tg = tg
        self.tp = tp
        self.uo = uo
        self.uc = uc
        self.gmax = gmax
        self.gmin = gmin
        self.rperm = rperm
        self.rtemp = rtemp
        self.tr = tr
        self.tw = tw
        self.at = at
        self.dturb = dturb
        self.hdam = hdam
        self.qnl = qnl
        self.db1 = db1
        self.eps = eps
        self.db2 = db2
        self.gv0 = gv0
        self.pgv0 = pgv0
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
        self.bgv0 = bgv0
        self.bgv1 = bgv1
        self.bgv2 = bgv2
        self.bgv3 = bgv3
        self.bgv4 = bgv4
        self.bgv5 = bgv5
        self.bmax = bmax
        self.tblade = tblade
        self.model = model
