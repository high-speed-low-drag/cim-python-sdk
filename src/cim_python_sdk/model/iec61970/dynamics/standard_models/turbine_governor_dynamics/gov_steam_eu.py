"""CIM class GovSteamEU (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteamEU(TurbineGovernorDynamics):
    """Simplified boiler and steam turbine with PID governor."""

    __slots__ = (
        "chc",
        "cho",
        "cic",
        "cio",
        "db1",
        "db2",
        "hhpmax",
        "ke",
        "kfcor",
        "khp",
        "klp",
        "komegacor",
        "mwbase",
        "pmax",
        "prhmax",
        "simx",
        "tb",
        "tdp",
        "ten",
        "tf",
        "tfp",
        "thp",
        "tip",
        "tlp",
        "tp",
        "trh",
        "tvhp",
        "tvip",
        "tw",
        "wfmax",
        "wfmin",
        "wmax1",
        "wmax2",
        "wwmax",
        "wwmin",
    )

    mwbase: float | None  # ActivePower
    tp: float | None  # Seconds
    ke: float | None  # PU
    tip: float | None  # Seconds
    tdp: float | None  # Seconds
    tfp: float | None  # Seconds
    tf: float | None  # Seconds
    kfcor: float | None  # PU
    db1: float | None  # PU
    wfmax: float | None  # PU
    wfmin: float | None  # PU
    pmax: float | None  # PU
    ten: float | None  # Seconds
    tw: float | None  # Seconds
    komegacor: float | None  # PU
    db2: float | None  # PU
    wwmax: float | None  # PU
    wwmin: float | None  # PU
    wmax1: float | None  # PU
    wmax2: float | None  # PU
    tvhp: float | None  # Seconds
    cho: float | None
    chc: float | None
    hhpmax: float | None  # PU
    tvip: float | None  # Seconds
    cio: float | None  # PU
    cic: float | None  # PU
    simx: float | None  # PU
    thp: float | None  # Seconds
    trh: float | None  # Seconds
    tlp: float | None  # Seconds
    prhmax: float | None  # PU
    khp: float | None  # PU
    klp: float | None  # PU
    tb: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="GovSteamEU",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{7046E843-1875-488a-B066-069ADD277955}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tip", "tip", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tdp", "tdp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tfp", "tfp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kfcor", "kfcor", "PU", 0, 1, "cimdatatype"),
            AttrMeta("db1", "db1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("wfmax", "wfmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("wfmin", "wfmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ten", "ten", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw", "tw", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("komegacor", "komegacor", "PU", 0, 1, "cimdatatype"),
            AttrMeta("db2", "db2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("wwmax", "wwmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("wwmin", "wwmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("wmax1", "wmax1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("wmax2", "wmax2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tvhp", "tvhp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("cho", "cho", "float", 0, 1, "primitive"),
            AttrMeta("chc", "chc", "float", 0, 1, "primitive"),
            AttrMeta("hhpmax", "hhpmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tvip", "tvip", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("cio", "cio", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cic", "cic", "PU", 0, 1, "cimdatatype"),
            AttrMeta("simx", "simx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("thp", "thp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("trh", "trh", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tlp", "tlp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("prhmax", "prhmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("khp", "khp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("klp", "klp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        tp: float | None = None,
        ke: float | None = None,
        tip: float | None = None,
        tdp: float | None = None,
        tfp: float | None = None,
        tf: float | None = None,
        kfcor: float | None = None,
        db1: float | None = None,
        wfmax: float | None = None,
        wfmin: float | None = None,
        pmax: float | None = None,
        ten: float | None = None,
        tw: float | None = None,
        komegacor: float | None = None,
        db2: float | None = None,
        wwmax: float | None = None,
        wwmin: float | None = None,
        wmax1: float | None = None,
        wmax2: float | None = None,
        tvhp: float | None = None,
        cho: float | None = None,
        chc: float | None = None,
        hhpmax: float | None = None,
        tvip: float | None = None,
        cio: float | None = None,
        cic: float | None = None,
        simx: float | None = None,
        thp: float | None = None,
        trh: float | None = None,
        tlp: float | None = None,
        prhmax: float | None = None,
        khp: float | None = None,
        klp: float | None = None,
        tb: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.tp = tp
        self.ke = ke
        self.tip = tip
        self.tdp = tdp
        self.tfp = tfp
        self.tf = tf
        self.kfcor = kfcor
        self.db1 = db1
        self.wfmax = wfmax
        self.wfmin = wfmin
        self.pmax = pmax
        self.ten = ten
        self.tw = tw
        self.komegacor = komegacor
        self.db2 = db2
        self.wwmax = wwmax
        self.wwmin = wwmin
        self.wmax1 = wmax1
        self.wmax2 = wmax2
        self.tvhp = tvhp
        self.cho = cho
        self.chc = chc
        self.hhpmax = hhpmax
        self.tvip = tvip
        self.cio = cio
        self.cic = cic
        self.simx = simx
        self.thp = thp
        self.trh = trh
        self.tlp = tlp
        self.prhmax = prhmax
        self.khp = khp
        self.klp = klp
        self.tb = tb
