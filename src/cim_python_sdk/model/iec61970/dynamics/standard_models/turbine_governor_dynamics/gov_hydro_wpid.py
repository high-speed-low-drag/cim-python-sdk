"""CIM class GovHydroWPID (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydroWPID(TurbineGovernorDynamics):
    """WoodwardTM PID hydro governor.

    [Footnote: Woodward PID hydro governors are an example of suitable products available
    commercially. This information is given for the convenience of users of this document
    and does not constitute an endorsement by IEC of these products.]"""

    __slots__ = (
        "d",
        "gatmax",
        "gatmin",
        "gv1",
        "gv2",
        "gv3",
        "kd",
        "ki",
        "kp",
        "mwbase",
        "pgv1",
        "pgv2",
        "pgv3",
        "pmax",
        "pmin",
        "reg",
        "ta",
        "tb",
        "treg",
        "tw",
        "velmax",
        "velmin",
    )

    mwbase: float | None  # ActivePower
    treg: float | None  # Seconds
    reg: float | None  # PU
    kp: float | None  # PU
    ki: float | None  # PU
    kd: float | None  # PU
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    velmax: float | None  # PU
    velmin: float | None  # PU
    gatmax: float | None  # PU
    gatmin: float | None  # PU
    tw: float | None  # Seconds
    pmax: float | None  # PU
    pmin: float | None  # PU
    d: float | None  # PU
    gv3: float | None  # PU
    gv1: float | None  # PU
    pgv1: float | None  # PU
    gv2: float | None  # PU
    pgv2: float | None  # PU
    pgv3: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovHydroWPID",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{61178980-5C8E-4adf-925A-DF8A56CCE23B}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("treg", "treg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("reg", "reg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("velmax", "velmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("velmin", "velmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gatmax", "gatmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gatmin", "gatmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tw", "tw", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("d", "d", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv3", "gv3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv1", "gv1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv1", "pgv1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("gv2", "gv2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv2", "pgv2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pgv3", "pgv3", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        treg: float | None = None,
        reg: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        kd: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        velmax: float | None = None,
        velmin: float | None = None,
        gatmax: float | None = None,
        gatmin: float | None = None,
        tw: float | None = None,
        pmax: float | None = None,
        pmin: float | None = None,
        d: float | None = None,
        gv3: float | None = None,
        gv1: float | None = None,
        pgv1: float | None = None,
        gv2: float | None = None,
        pgv2: float | None = None,
        pgv3: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.treg = treg
        self.reg = reg
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.ta = ta
        self.tb = tb
        self.velmax = velmax
        self.velmin = velmin
        self.gatmax = gatmax
        self.gatmin = gatmin
        self.tw = tw
        self.pmax = pmax
        self.pmin = pmin
        self.d = d
        self.gv3 = gv3
        self.gv1 = gv1
        self.pgv1 = pgv1
        self.gv2 = gv2
        self.pgv2 = pgv2
        self.pgv3 = pgv3
