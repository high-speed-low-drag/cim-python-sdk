"""CIM class GovSteamFV3 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteamFV3(TurbineGovernorDynamics):
    """Simplified GovSteamIEEE1 steam turbine governor with Prmax limit and fast valving."""

    __slots__ = (
        "gv1",
        "gv2",
        "gv3",
        "gv4",
        "gv5",
        "gv6",
        "k",
        "k1",
        "k2",
        "k3",
        "mwbase",
        "pgv1",
        "pgv2",
        "pgv3",
        "pgv4",
        "pgv5",
        "pgv6",
        "pmax",
        "pmin",
        "prmax",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
        "ta",
        "tb",
        "tc",
        "uc",
        "uo",
    )

    mwbase: float | None  # ActivePower
    k: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    uo: float | None
    uc: float | None
    pmax: float | None  # PU
    pmin: float | None  # PU
    t4: float | None  # Seconds
    k1: float | None  # PU
    t5: float | None  # Seconds
    k2: float | None  # PU
    t6: float | None  # Seconds
    k3: float | None  # PU
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    prmax: float | None  # PU
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
        cim_name="GovSteamFV3",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{885FC264-5D92-465a-881C-12B87113ABA7}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uo", "uo", "float", 0, 1, "primitive"),
            AttrMeta("uc", "uc", "float", 0, 1, "primitive"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k1", "k1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("prmax", "prmax", "PU", 0, 1, "cimdatatype"),
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
        k: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        uo: float | None = None,
        uc: float | None = None,
        pmax: float | None = None,
        pmin: float | None = None,
        t4: float | None = None,
        k1: float | None = None,
        t5: float | None = None,
        k2: float | None = None,
        t6: float | None = None,
        k3: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        prmax: float | None = None,
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
        self.k = k
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.uo = uo
        self.uc = uc
        self.pmax = pmax
        self.pmin = pmin
        self.t4 = t4
        self.k1 = k1
        self.t5 = t5
        self.k2 = k2
        self.t6 = t6
        self.k3 = k3
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.prmax = prmax
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
