"""CIM class GovGAST4 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovGAST4(TurbineGovernorDynamics):
    """Generic turbogas."""

    __slots__ = ("bp", "ktm", "mnef", "mxef", "rymn", "rymx", "ta", "tc", "tcm", "tm", "ty")

    bp: float | None  # PU
    ty: float | None  # Seconds
    ta: float | None  # Seconds
    tc: float | None  # Seconds
    tcm: float | None  # Seconds
    ktm: float | None  # PU
    tm: float | None  # Seconds
    rymx: float | None  # PU
    rymn: float | None  # PU
    mxef: float | None  # PU
    mnef: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovGAST4",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{77197C40-C093-43f7-B2FA-434AC89EE019}",
        attributes=(
            AttrMeta("bp", "bp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ty", "ty", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tcm", "tcm", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ktm", "ktm", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tm", "tm", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("rymx", "rymx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rymn", "rymn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mxef", "mxef", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mnef", "mnef", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        bp: float | None = None,
        ty: float | None = None,
        ta: float | None = None,
        tc: float | None = None,
        tcm: float | None = None,
        ktm: float | None = None,
        tm: float | None = None,
        rymx: float | None = None,
        rymn: float | None = None,
        mxef: float | None = None,
        mnef: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bp = bp
        self.ty = ty
        self.ta = ta
        self.tc = tc
        self.tcm = tcm
        self.ktm = ktm
        self.tm = tm
        self.rymx = rymx
        self.rymn = rymn
        self.mxef = mxef
        self.mnef = mnef
