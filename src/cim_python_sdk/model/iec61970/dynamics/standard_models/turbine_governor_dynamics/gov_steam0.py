"""CIM class GovSteam0 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovSteam0(TurbineGovernorDynamics):
    """A simplified steam turbine governor."""

    __slots__ = ("dt", "mwbase", "r", "t1", "t2", "t3", "vmax", "vmin")

    mwbase: float | None  # ActivePower
    r: float | None  # PU
    t1: float | None  # Seconds
    vmax: float | None  # PU
    vmin: float | None  # PU
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    dt: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovSteam0",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{498AA55A-0254-4b68-921D-AD322CD62C4E}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vmax", "vmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmin", "vmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("dt", "dt", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        r: float | None = None,
        t1: float | None = None,
        vmax: float | None = None,
        vmin: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        dt: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.r = r
        self.t1 = t1
        self.vmax = vmax
        self.vmin = vmin
        self.t2 = t2
        self.t3 = t3
        self.dt = dt
