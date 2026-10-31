"""CIM class GovSteamFV4 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteamFV4(TurbineGovernorDynamics):
    """Detailed electro-hydraulic governor for steam unit."""

    __slots__ = (
        "cpsmn",
        "cpsmx",
        "crmn",
        "crmx",
        "kdc",
        "kf1",
        "kf3",
        "khp",
        "kic",
        "kip",
        "kit",
        "kmp1",
        "kmp2",
        "kpc",
        "kpp",
        "kpt",
        "krc",
        "ksh",
        "lpi",
        "lps",
        "mnef",
        "mxef",
        "pr1",
        "pr2",
        "psmn",
        "rsmimn",
        "rsmimx",
        "rvgmn",
        "rvgmx",
        "srmn",
        "srmx",
        "srsmp",
        "svmn",
        "svmx",
        "ta",
        "tam",
        "tc",
        "tcm",
        "tdc",
        "tf1",
        "tf2",
        "thp",
        "tmp",
        "trh",
        "tv",
        "ty",
        "y",
        "yhpmn",
        "yhpmx",
        "ympmn",
        "ympmx",
    )

    kf1: float | None  # PU
    kf3: float | None  # PU
    lps: float | None  # PU
    lpi: float | None  # PU
    mxef: float | None  # PU
    mnef: float | None  # PU
    crmx: float | None  # PU
    crmn: float | None  # PU
    kpt: float | None  # PU
    kit: float | None  # PU
    rvgmx: float | None  # PU
    rvgmn: float | None  # PU
    svmx: float | None
    svmn: float | None
    srmx: float | None  # PU
    srmn: float | None  # PU
    kpp: float | None  # PU
    kip: float | None  # PU
    rsmimx: float | None  # PU
    rsmimn: float | None  # PU
    kmp1: float | None  # PU
    kmp2: float | None  # PU
    srsmp: float | None  # PU
    ta: float | None  # Seconds
    tc: float | None  # Seconds
    ty: float | None  # Seconds
    yhpmx: float | None  # PU
    yhpmn: float | None  # PU
    tam: float | None  # Seconds
    tcm: float | None  # Seconds
    ympmx: float | None  # PU
    ympmn: float | None  # PU
    y: float | None  # PU
    thp: float | None  # Seconds
    trh: float | None  # Seconds
    tmp: float | None  # Seconds
    khp: float | None  # PU
    pr1: float | None  # PU
    pr2: float | None  # PU
    psmn: float | None  # PU
    kpc: float | None  # PU
    kic: float | None  # PU
    kdc: float | None  # PU
    tdc: float | None  # Seconds
    cpsmx: float | None  # PU
    cpsmn: float | None  # PU
    krc: float | None  # PU
    tf1: float | None  # Seconds
    tf2: float | None  # Seconds
    tv: float | None  # Seconds
    ksh: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovSteamFV4",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{5ACC759A-302F-4057-9506-893267597F7F}",
        attributes=(
            AttrMeta("kf1", "kf1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf3", "kf3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("lps", "lps", "PU", 0, 1, "cimdatatype"),
            AttrMeta("lpi", "lpi", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mxef", "mxef", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mnef", "mnef", "PU", 0, 1, "cimdatatype"),
            AttrMeta("crmx", "crmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("crmn", "crmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpt", "kpt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kit", "kit", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rvgmx", "rvgmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rvgmn", "rvgmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("svmx", "svmx", "float", 0, 1, "primitive"),
            AttrMeta("svmn", "svmn", "float", 0, 1, "primitive"),
            AttrMeta("srmx", "srmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("srmn", "srmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpp", "kpp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kip", "kip", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rsmimx", "rsmimx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rsmimn", "rsmimn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kmp1", "kmp1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kmp2", "kmp2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("srsmp", "srsmp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ty", "ty", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("yhpmx", "yhpmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("yhpmn", "yhpmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tam", "tam", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tcm", "tcm", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ympmx", "ympmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ympmn", "ympmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("y", "y", "PU", 0, 1, "cimdatatype"),
            AttrMeta("thp", "thp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("trh", "trh", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tmp", "tmp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("khp", "khp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pr1", "pr1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pr2", "pr2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("psmn", "psmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpc", "kpc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kic", "kic", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kdc", "kdc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tdc", "tdc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("cpsmx", "cpsmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cpsmn", "cpsmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("krc", "krc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf1", "tf1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf2", "tf2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tv", "tv", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ksh", "ksh", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        kf1: float | None = None,
        kf3: float | None = None,
        lps: float | None = None,
        lpi: float | None = None,
        mxef: float | None = None,
        mnef: float | None = None,
        crmx: float | None = None,
        crmn: float | None = None,
        kpt: float | None = None,
        kit: float | None = None,
        rvgmx: float | None = None,
        rvgmn: float | None = None,
        svmx: float | None = None,
        svmn: float | None = None,
        srmx: float | None = None,
        srmn: float | None = None,
        kpp: float | None = None,
        kip: float | None = None,
        rsmimx: float | None = None,
        rsmimn: float | None = None,
        kmp1: float | None = None,
        kmp2: float | None = None,
        srsmp: float | None = None,
        ta: float | None = None,
        tc: float | None = None,
        ty: float | None = None,
        yhpmx: float | None = None,
        yhpmn: float | None = None,
        tam: float | None = None,
        tcm: float | None = None,
        ympmx: float | None = None,
        ympmn: float | None = None,
        y: float | None = None,
        thp: float | None = None,
        trh: float | None = None,
        tmp: float | None = None,
        khp: float | None = None,
        pr1: float | None = None,
        pr2: float | None = None,
        psmn: float | None = None,
        kpc: float | None = None,
        kic: float | None = None,
        kdc: float | None = None,
        tdc: float | None = None,
        cpsmx: float | None = None,
        cpsmn: float | None = None,
        krc: float | None = None,
        tf1: float | None = None,
        tf2: float | None = None,
        tv: float | None = None,
        ksh: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kf1 = kf1
        self.kf3 = kf3
        self.lps = lps
        self.lpi = lpi
        self.mxef = mxef
        self.mnef = mnef
        self.crmx = crmx
        self.crmn = crmn
        self.kpt = kpt
        self.kit = kit
        self.rvgmx = rvgmx
        self.rvgmn = rvgmn
        self.svmx = svmx
        self.svmn = svmn
        self.srmx = srmx
        self.srmn = srmn
        self.kpp = kpp
        self.kip = kip
        self.rsmimx = rsmimx
        self.rsmimn = rsmimn
        self.kmp1 = kmp1
        self.kmp2 = kmp2
        self.srsmp = srsmp
        self.ta = ta
        self.tc = tc
        self.ty = ty
        self.yhpmx = yhpmx
        self.yhpmn = yhpmn
        self.tam = tam
        self.tcm = tcm
        self.ympmx = ympmx
        self.ympmn = ympmn
        self.y = y
        self.thp = thp
        self.trh = trh
        self.tmp = tmp
        self.khp = khp
        self.pr1 = pr1
        self.pr2 = pr2
        self.psmn = psmn
        self.kpc = kpc
        self.kic = kic
        self.kdc = kdc
        self.tdc = tdc
        self.cpsmx = cpsmx
        self.cpsmn = cpsmn
        self.krc = krc
        self.tf1 = tf1
        self.tf2 = tf2
        self.tv = tv
        self.ksh = ksh
