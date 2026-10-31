"""CIM class GovGAST (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovGAST(TurbineGovernorDynamics):
    """Single shaft gas turbine."""

    __slots__ = ("at", "dturb", "kt", "mwbase", "r", "t1", "t2", "t3", "vmax", "vmin")

    mwbase: float | None  # ActivePower
    r: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    at: float | None  # PU
    kt: float | None  # PU
    vmax: float | None  # PU
    vmin: float | None  # PU
    dturb: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovGAST",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{07B79378-ECC2-4394-8357-92C171D89683}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("at", "at", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kt", "kt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmax", "vmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmin", "vmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dturb", "dturb", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        r: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        at: float | None = None,
        kt: float | None = None,
        vmax: float | None = None,
        vmin: float | None = None,
        dturb: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.r = r
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.at = at
        self.kt = kt
        self.vmax = vmax
        self.vmin = vmin
        self.dturb = dturb
