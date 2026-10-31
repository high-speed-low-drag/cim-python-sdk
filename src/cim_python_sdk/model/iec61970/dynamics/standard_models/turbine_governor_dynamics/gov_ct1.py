"""CIM class GovCT1 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

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


class GovCT1(TurbineGovernorDynamics):
    """General model for any prime mover with a PID governor, used primarily for combustion
    turbine and combined cycle units.

    This model can be used to represent a variety of prime movers controlled by PID
    governors. It is suitable, for example, for the representation of:

    - gas turbine and single shaft combined cycle turbines

    - diesel engines with modern electronic or digital governors

    - steam turbines where steam is supplied from a large boiler drum or a large header
    whose pressure is substantially constant over the period under study

    - simple hydro turbines in dam configurations where the water column length is short and
    water inertia effects are minimal.

    Additional information on this model is available in the 2012 IEEE report, Dynamic
    Models for Turbine-Governors in Power System Studies, 3.1.2.3 pages 3-4 (GGOV1)."""

    __slots__ = (
        "aset",
        "db",
        "dm",
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
        cim_name="GovCT1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{EC304C29-08AD-426b-BEBF-8167E8655879}",
        attributes=(
            AttrMeta("aset", "aset", "float", 0, 1, "primitive"),
            AttrMeta("db", "db", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dm", "dm", "PU", 0, 1, "cimdatatype"),
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
