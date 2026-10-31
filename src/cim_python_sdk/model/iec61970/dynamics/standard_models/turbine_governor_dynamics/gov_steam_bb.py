"""CIM class GovSteamBB (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteamBB(TurbineGovernorDynamics):
    """European governor model."""

    __slots__ = (
        "fcut",
        "k2",
        "k3",
        "kd",
        "kg",
        "kls",
        "kp",
        "ks",
        "peflag",
        "pmax",
        "pmin",
        "t1",
        "t4",
        "t5",
        "t6",
        "td",
        "tn",
    )

    fcut: float | None  # PU
    ks: float | None  # PU
    kls: float | None  # PU
    kg: float | None  # PU
    t1: float | None  # Seconds
    kp: float | None  # PU
    tn: float | None  # Seconds
    kd: float | None  # PU
    td: float | None  # Seconds
    pmax: float | None  # PU
    pmin: float | None  # PU
    t4: float | None  # Seconds
    k2: float | None  # PU
    t5: float | None  # Seconds
    k3: float | None  # PU
    t6: float | None  # Seconds
    peflag: bool | None

    _cim_meta = ClassMeta(
        cim_name="GovSteamBB",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{BAF42F15-B5DF-4b1f-B240-5A70C71826A4}",
        attributes=(
            AttrMeta("fcut", "fcut", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kls", "kls", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tn", "tn", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kd", "kd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("peflag", "peflag", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        fcut: float | None = None,
        ks: float | None = None,
        kls: float | None = None,
        kg: float | None = None,
        t1: float | None = None,
        kp: float | None = None,
        tn: float | None = None,
        kd: float | None = None,
        td: float | None = None,
        pmax: float | None = None,
        pmin: float | None = None,
        t4: float | None = None,
        k2: float | None = None,
        t5: float | None = None,
        k3: float | None = None,
        t6: float | None = None,
        peflag: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.fcut = fcut
        self.ks = ks
        self.kls = kls
        self.kg = kg
        self.t1 = t1
        self.kp = kp
        self.tn = tn
        self.kd = kd
        self.td = td
        self.pmax = pmax
        self.pmin = pmin
        self.t4 = t4
        self.k2 = k2
        self.t5 = t5
        self.k3 = k3
        self.t6 = t6
        self.peflag = peflag
