"""CIM class GovHydroPID2 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydroPID2(TurbineGovernorDynamics):
    """Hydro turbine and governor. Represents plants with straightforward penstock
    configurations and "three term" electro-hydraulic governors (i.e. WoodwardTM
    electronic).

    [Footnote: Woodward electronic governors are an example of suitable products available
    commercially. This information is given for the convenience of users of this document
    and does not constitute an endorsement by IEC of these products.]"""

    __slots__ = (
        "atw",
        "d",
        "feedback_signal",
        "g0",
        "g1",
        "g2",
        "gmax",
        "gmin",
        "kd",
        "ki",
        "kp",
        "mwbase",
        "p1",
        "p2",
        "p3",
        "rperm",
        "ta",
        "tb",
        "treg",
        "tw",
        "velmax",
        "velmin",
    )

    mwbase: float | None  # ActivePower
    treg: float | None  # Seconds
    rperm: float | None  # PU
    kp: float | None  # PU
    ki: float | None
    kd: float | None  # PU
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    velmax: float | None
    velmin: float | None
    gmax: float | None  # PU
    gmin: float | None  # PU
    tw: float | None  # Seconds
    d: float | None  # PU
    g0: float | None  # PU
    g1: float | None  # PU
    p1: float | None  # PU
    g2: float | None  # PU
    p2: float | None  # PU
    p3: float | None  # PU
    atw: float | None  # PU
    feedback_signal: bool | None

    _cim_meta = ClassMeta(
        cim_name="GovHydroPID2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{7BD580D8-6A60-452c-A8B8-3D5C4376B87A}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("treg", "treg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("rperm", "rperm", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "float", 0, 1, "primitive"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("velmax", "velmax", "float", 0, 1, "primitive"),
            AttrMeta("velmin", "velmin", "float", 0, 1, "primitive"),
            AttrMeta("gmax", "gmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gmin", "gmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tw", "tw", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("d", "d", "PU", 0, 1, "cimdatatype"),
            AttrMeta("g0", "g0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("g1", "g1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p1", "p1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("g2", "g2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p2", "p2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p3", "p3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("atw", "atw", "PU", 0, 1, "cimdatatype"),
            AttrMeta("feedback_signal", "feedbackSignal", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        treg: float | None = None,
        rperm: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        kd: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        velmax: float | None = None,
        velmin: float | None = None,
        gmax: float | None = None,
        gmin: float | None = None,
        tw: float | None = None,
        d: float | None = None,
        g0: float | None = None,
        g1: float | None = None,
        p1: float | None = None,
        g2: float | None = None,
        p2: float | None = None,
        p3: float | None = None,
        atw: float | None = None,
        feedback_signal: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.treg = treg
        self.rperm = rperm
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.ta = ta
        self.tb = tb
        self.velmax = velmax
        self.velmin = velmin
        self.gmax = gmax
        self.gmin = gmin
        self.tw = tw
        self.d = d
        self.g0 = g0
        self.g1 = g1
        self.p1 = p1
        self.g2 = g2
        self.p2 = p2
        self.p3 = p3
        self.atw = atw
        self.feedback_signal = feedback_signal
