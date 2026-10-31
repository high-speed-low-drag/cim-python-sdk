"""CIM class GovSteamFV2 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteamFV2(TurbineGovernorDynamics):
    """Steam turbine governor with reheat time constants and modelling of the effects of fast
    valve closing to reduce mechanical power."""

    __slots__ = ("dt", "k", "mwbase", "r", "t1", "t3", "ta", "tb", "tc", "tt", "vmax", "vmin")

    mwbase: float | None  # ActivePower
    t1: float | None  # Seconds
    vmax: float | None  # PU
    k: float | None  # PU
    vmin: float | None  # PU
    dt: float | None  # PU
    t3: float | None  # Seconds
    tt: float | None  # Seconds
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    r: float | None  # PU
    tc: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="GovSteamFV2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{E9DCB0A5-5693-431c-837A-C46A62C00661}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vmax", "vmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmin", "vmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dt", "dt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tt", "tt", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        t1: float | None = None,
        vmax: float | None = None,
        k: float | None = None,
        vmin: float | None = None,
        dt: float | None = None,
        t3: float | None = None,
        tt: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        r: float | None = None,
        tc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.t1 = t1
        self.vmax = vmax
        self.k = k
        self.vmin = vmin
        self.dt = dt
        self.t3 = t3
        self.tt = tt
        self.ta = ta
        self.tb = tb
        self.r = r
        self.tc = tc
