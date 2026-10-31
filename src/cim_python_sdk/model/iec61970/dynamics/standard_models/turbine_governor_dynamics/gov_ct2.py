"""CIM class GovCT2 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.droop_signal_feedback_kind import (
        DroopSignalFeedbackKind,
    )


class GovCT2(TurbineGovernorDynamics):
    """General governor with frequency-dependent fuel flow limit. This model is a modification
    of the GovCT1 model in order to represent the frequency-dependent fuel flow limit of a
    specific gas turbine manufacturer."""

    __slots__ = (
        "aset",
        "db",
        "dm",
        "flim1",
        "flim2",
        "flim3",
        "flim4",
        "flim5",
        "flim6",
        "flim7",
        "flim8",
        "flim9",
        "flim10",
        "ka",
        "kdgov",
        "kigov",
        "kiload",
        "kimw",
        "kpgov",
        "kpload",
        "kturb",
        "ldref",
        "maxerr",
        "minerr",
        "mwbase",
        "plim1",
        "plim2",
        "plim3",
        "plim4",
        "plim5",
        "plim6",
        "plim7",
        "plim8",
        "plim9",
        "plim10",
        "prate",
        "r",
        "rclose",
        "rdown",
        "ropen",
        "rselect",
        "rup",
        "ta",
        "tact",
        "tb",
        "tc",
        "tdgov",
        "teng",
        "tfload",
        "tpelec",
        "tsa",
        "tsb",
        "vmax",
        "vmin",
        "wfnl",
        "wfspd",
    )

    aset: float | None
    db: float | None  # PU
    dm: float | None  # PU
    flim1: float | None  # Frequency
    flim10: float | None  # Frequency
    flim2: float | None  # Frequency
    flim3: float | None  # Frequency
    flim4: float | None  # Frequency
    flim5: float | None  # Frequency
    flim6: float | None  # Frequency
    flim7: float | None  # Frequency
    flim8: float | None  # Frequency
    flim9: float | None  # Frequency
    ka: float | None  # PU
    kdgov: float | None  # PU
    kigov: float | None  # PU
    kiload: float | None  # PU
    kimw: float | None  # PU
    kpgov: float | None  # PU
    kpload: float | None  # PU
    kturb: float | None  # PU
    ldref: float | None  # PU
    maxerr: float | None  # PU
    minerr: float | None  # PU
    mwbase: float | None  # ActivePower
    plim1: float | None  # PU
    plim10: float | None  # PU
    plim2: float | None  # PU
    plim3: float | None  # PU
    plim4: float | None  # PU
    plim5: float | None  # PU
    plim6: float | None  # PU
    plim7: float | None  # PU
    plim8: float | None  # PU
    plim9: float | None  # PU
    prate: float | None  # PU
    r: float | None  # PU
    rclose: float | None
    rdown: float | None  # PU
    ropen: float | None
    rselect: DroopSignalFeedbackKind | None
    rup: float | None  # PU
    ta: float | None  # Seconds
    tact: float | None  # Seconds
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    tdgov: float | None  # Seconds
    teng: float | None  # Seconds
    tfload: float | None  # Seconds
    tpelec: float | None  # Seconds
    tsa: float | None  # Seconds
    tsb: float | None  # Seconds
    vmax: float | None  # PU
    vmin: float | None  # PU
    wfnl: float | None  # PU
    wfspd: bool | None

    _cim_meta = ClassMeta(
        cim_name="GovCT2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{0A73B225-89A2-4f10-A1F2-E0FEB59F2980}",
        attributes=(
            AttrMeta("aset", "aset", "float", 0, 1, "primitive"),
            AttrMeta("db", "db", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dm", "dm", "PU", 0, 1, "cimdatatype"),
            AttrMeta("flim1", "flim1", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("flim10", "flim10", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("flim2", "flim2", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("flim3", "flim3", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("flim4", "flim4", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("flim5", "flim5", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("flim6", "flim6", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("flim7", "flim7", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("flim8", "flim8", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("flim9", "flim9", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kdgov", "kdgov", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kigov", "kigov", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kiload", "kiload", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kimw", "kimw", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpgov", "kpgov", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpload", "kpload", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kturb", "kturb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ldref", "ldref", "PU", 0, 1, "cimdatatype"),
            AttrMeta("maxerr", "maxerr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("minerr", "minerr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("plim1", "plim1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("plim10", "plim10", "PU", 0, 1, "cimdatatype"),
            AttrMeta("plim2", "plim2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("plim3", "plim3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("plim4", "plim4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("plim5", "plim5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("plim6", "plim6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("plim7", "plim7", "PU", 0, 1, "cimdatatype"),
            AttrMeta("plim8", "plim8", "PU", 0, 1, "cimdatatype"),
            AttrMeta("plim9", "plim9", "PU", 0, 1, "cimdatatype"),
            AttrMeta("prate", "prate", "PU", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rclose", "rclose", "float", 0, 1, "primitive"),
            AttrMeta("rdown", "rdown", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ropen", "ropen", "float", 0, 1, "primitive"),
            AttrMeta("rselect", "rselect", "DroopSignalFeedbackKind", 0, 1, "enumeration"),
            AttrMeta("rup", "rup", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tact", "tact", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tdgov", "tdgov", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("teng", "teng", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tfload", "tfload", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tpelec", "tpelec", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tsa", "tsa", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tsb", "tsb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vmax", "vmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmin", "vmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("wfnl", "wfnl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("wfspd", "wfspd", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        aset: float | None = None,
        db: float | None = None,
        dm: float | None = None,
        flim1: float | None = None,
        flim10: float | None = None,
        flim2: float | None = None,
        flim3: float | None = None,
        flim4: float | None = None,
        flim5: float | None = None,
        flim6: float | None = None,
        flim7: float | None = None,
        flim8: float | None = None,
        flim9: float | None = None,
        ka: float | None = None,
        kdgov: float | None = None,
        kigov: float | None = None,
        kiload: float | None = None,
        kimw: float | None = None,
        kpgov: float | None = None,
        kpload: float | None = None,
        kturb: float | None = None,
        ldref: float | None = None,
        maxerr: float | None = None,
        minerr: float | None = None,
        mwbase: float | None = None,
        plim1: float | None = None,
        plim10: float | None = None,
        plim2: float | None = None,
        plim3: float | None = None,
        plim4: float | None = None,
        plim5: float | None = None,
        plim6: float | None = None,
        plim7: float | None = None,
        plim8: float | None = None,
        plim9: float | None = None,
        prate: float | None = None,
        r: float | None = None,
        rclose: float | None = None,
        rdown: float | None = None,
        ropen: float | None = None,
        rselect: DroopSignalFeedbackKind | None = None,
        rup: float | None = None,
        ta: float | None = None,
        tact: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        tdgov: float | None = None,
        teng: float | None = None,
        tfload: float | None = None,
        tpelec: float | None = None,
        tsa: float | None = None,
        tsb: float | None = None,
        vmax: float | None = None,
        vmin: float | None = None,
        wfnl: float | None = None,
        wfspd: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.aset = aset
        self.db = db
        self.dm = dm
        self.flim1 = flim1
        self.flim10 = flim10
        self.flim2 = flim2
        self.flim3 = flim3
        self.flim4 = flim4
        self.flim5 = flim5
        self.flim6 = flim6
        self.flim7 = flim7
        self.flim8 = flim8
        self.flim9 = flim9
        self.ka = ka
        self.kdgov = kdgov
        self.kigov = kigov
        self.kiload = kiload
        self.kimw = kimw
        self.kpgov = kpgov
        self.kpload = kpload
        self.kturb = kturb
        self.ldref = ldref
        self.maxerr = maxerr
        self.minerr = minerr
        self.mwbase = mwbase
        self.plim1 = plim1
        self.plim10 = plim10
        self.plim2 = plim2
        self.plim3 = plim3
        self.plim4 = plim4
        self.plim5 = plim5
        self.plim6 = plim6
        self.plim7 = plim7
        self.plim8 = plim8
        self.plim9 = plim9
        self.prate = prate
        self.r = r
        self.rclose = rclose
        self.rdown = rdown
        self.ropen = ropen
        self.rselect = rselect
        self.rup = rup
        self.ta = ta
        self.tact = tact
        self.tb = tb
        self.tc = tc
        self.tdgov = tdgov
        self.teng = teng
        self.tfload = tfload
        self.tpelec = tpelec
        self.tsa = tsa
        self.tsb = tsb
        self.vmax = vmax
        self.vmin = vmin
        self.wfnl = wfnl
        self.wfspd = wfspd
