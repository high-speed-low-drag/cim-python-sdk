"""CIM class OverexcLim2 (TC57CIM/IEC61970/Dynamics/StandardModels/OverexcitationLimiterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.overexcitation_limiter_dynamics.overexcitation_limiter_dynamics import (
    OverexcitationLimiterDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class OverexcLim2(OverexcitationLimiterDynamics):
    """Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the
    excitation set-point by means of a non-windup integral regulator.

    Irated is the rated machine excitation current (calculated from nameplate conditions:
    Vnom, Pnom, CosPhinom)."""

    __slots__ = ("ifdlim", "koi", "voimax", "voimin")

    koi: float | None  # PU
    voimax: float | None  # PU
    voimin: float | None  # PU
    ifdlim: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="OverexcLim2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/OverexcitationLimiterDynamics",
        guid="{C6018567-991D-4489-8F77-66EB34417ABD}",
        attributes=(
            AttrMeta("koi", "koi", "PU", 0, 1, "cimdatatype"),
            AttrMeta("voimax", "voimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("voimin", "voimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ifdlim", "ifdlim", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        koi: float | None = None,
        voimax: float | None = None,
        voimin: float | None = None,
        ifdlim: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.koi = koi
        self.voimax = voimax
        self.voimin = voimin
        self.ifdlim = ifdlim
