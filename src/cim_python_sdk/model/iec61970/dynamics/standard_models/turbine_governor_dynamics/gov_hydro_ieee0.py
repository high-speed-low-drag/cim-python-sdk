"""CIM class GovHydroIEEE0 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydroIEEE0(TurbineGovernorDynamics):
    """IEEE simplified hydro governor-turbine model. Used for mechanical-hydraulic and
    electro-hydraulic turbine governors, with or without steam feedback. Typical values
    given are for mechanical-hydraulic turbine-governor.

    Reference: IEEE Transactions on Power Apparatus and Systems, November/December 1973,
    Volume PAS-92, Number 6, Dynamic Models for Steam and Hydro Turbines in Power System
    Studies, page 1904."""

    __slots__ = ("k", "mwbase", "pmax", "pmin", "t1", "t2", "t3", "t4")

    mwbase: float | None  # ActivePower
    k: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    pmax: float | None  # PU
    pmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovHydroIEEE0",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{A314A5D0-7848-447d-9CF5-9A96F323C788}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("pmax", "pmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
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
        t4: float | None = None,
        pmax: float | None = None,
        pmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.k = k
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.pmax = pmax
        self.pmin = pmin
