"""CIM class GovHydro1 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydro1(TurbineGovernorDynamics):
    """Basic hydro turbine governor."""

    __slots__ = (
        "at",
        "dturb",
        "gmax",
        "gmin",
        "hdam",
        "mwbase",
        "qnl",
        "rperm",
        "rtemp",
        "tf",
        "tg",
        "tr",
        "tw",
        "velm",
    )

    mwbase: float | None  # ActivePower
    rperm: float | None  # PU
    rtemp: float | None  # PU
    tr: float | None  # Seconds
    tf: float | None  # Seconds
    tg: float | None  # Seconds
    velm: float | None
    gmax: float | None  # PU
    gmin: float | None  # PU
    tw: float | None  # Seconds
    at: float | None  # PU
    dturb: float | None  # PU
    qnl: float | None  # PU
    hdam: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovHydro1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{43B50912-F9F9-458f-AFDF-36ADB06FB9A6}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("rperm", "rperm", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rtemp", "rtemp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tr", "tr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("velm", "velm", "float", 0, 1, "primitive"),
            AttrMeta("gmax", "gmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gmin", "gmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tw", "tw", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("at", "at", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dturb", "dturb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qnl", "qnl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("hdam", "hdam", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        rperm: float | None = None,
        rtemp: float | None = None,
        tr: float | None = None,
        tf: float | None = None,
        tg: float | None = None,
        velm: float | None = None,
        gmax: float | None = None,
        gmin: float | None = None,
        tw: float | None = None,
        at: float | None = None,
        dturb: float | None = None,
        qnl: float | None = None,
        hdam: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.rperm = rperm
        self.rtemp = rtemp
        self.tr = tr
        self.tf = tf
        self.tg = tg
        self.velm = velm
        self.gmax = gmax
        self.gmin = gmin
        self.tw = tw
        self.at = at
        self.dturb = dturb
        self.qnl = qnl
        self.hdam = hdam
