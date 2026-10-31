"""CIM class GovSteamIEEE1 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteamIEEE1(TurbineGovernorDynamics):
    """IEEE steam turbine governor model.

    Reference: IEEE Transactions on Power Apparatus and Systems, November/December 1973,
    Volume PAS-92, Number 6, Dynamic Models for Steam and Hydro Turbines in Power System
    Studies, page 1904."""

    __slots__ = (
        "k",
        "k1",
        "k2",
        "k3",
        "k4",
        "k5",
        "k6",
        "k7",
        "k8",
        "mwbase",
        "pmax",
        "pmin",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
        "t7",
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
    k1: float | None
    k2: float | None
    t5: float | None  # Seconds
    k3: float | None
    k4: float | None
    t6: float | None  # Seconds
    k5: float | None
    k6: float | None
    t7: float | None  # Seconds
    k7: float | None
    k8: float | None

    _cim_meta = ClassMeta(
        cim_name="GovSteamIEEE1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{0C56115D-6698-4d80-ACEC-59C9609E8EB6}",
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
            AttrMeta("k1", "k1", "float", 0, 1, "primitive"),
            AttrMeta("k2", "k2", "float", 0, 1, "primitive"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "float", 0, 1, "primitive"),
            AttrMeta("k4", "k4", "float", 0, 1, "primitive"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k5", "k5", "float", 0, 1, "primitive"),
            AttrMeta("k6", "k6", "float", 0, 1, "primitive"),
            AttrMeta("t7", "t7", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k7", "k7", "float", 0, 1, "primitive"),
            AttrMeta("k8", "k8", "float", 0, 1, "primitive"),
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
        k2: float | None = None,
        t5: float | None = None,
        k3: float | None = None,
        k4: float | None = None,
        t6: float | None = None,
        k5: float | None = None,
        k6: float | None = None,
        t7: float | None = None,
        k7: float | None = None,
        k8: float | None = None,
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
        self.k2 = k2
        self.t5 = t5
        self.k3 = k3
        self.k4 = k4
        self.t6 = t6
        self.k5 = k5
        self.k6 = k6
        self.t7 = t7
        self.k7 = k7
        self.k8 = k8
