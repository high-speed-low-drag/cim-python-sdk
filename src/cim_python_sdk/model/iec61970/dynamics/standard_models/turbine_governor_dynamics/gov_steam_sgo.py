"""CIM class GovSteamSGO (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteamSGO(TurbineGovernorDynamics):
    """Simplified steam turbine governor."""

    __slots__ = ("k1", "k2", "k3", "mwbase", "pmax", "pmin", "t1", "t2", "t3", "t4", "t5", "t6")

    mwbase: float | None  # ActivePower
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    t5: float | None  # Seconds
    t6: float | None  # Seconds
    k1: float | None  # PU
    k2: float | None  # PU
    k3: float | None  # PU
    pmax: float | None  # PU
    pmin: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="GovSteamSGO",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{EEEBBC29-3B6E-49a6-A1C1-354A867CE94F}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k1", "k1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        t5: float | None = None,
        t6: float | None = None,
        k1: float | None = None,
        k2: float | None = None,
        k3: float | None = None,
        pmax: float | None = None,
        pmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.pmax = pmax
        self.pmin = pmin
