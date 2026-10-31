"""CIM class UnderexcLim2Simplified (TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.underexcitation_limiter_dynamics.underexcitation_limiter_dynamics import (
    UnderexcitationLimiterDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class UnderexcLim2Simplified(UnderexcitationLimiterDynamics):
    """Simplified type UEL2 underexcitation limiter. This model can be derived from
    UnderexcLimIEEE2. The limit characteristic (look –up table) is a single straight-line,
    the same as UnderexcLimIEEE2 (see Figure 10.4 (p 32), IEEE 421.5-2005 Section 10.2)."""

    __slots__ = ("kui", "p0", "p1", "q0", "q1", "vuimax", "vuimin")

    q0: float | None  # PU
    q1: float | None  # PU
    p0: float | None  # PU
    p1: float | None  # PU
    kui: float | None  # PU
    vuimin: float | None  # PU
    vuimax: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="UnderexcLim2Simplified",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics",
        guid="{C334B6E0-A80B-4211-BE69-4B7D894E379F}",
        attributes=(
            AttrMeta("q0", "q0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q1", "q1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p0", "p0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p1", "p1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kui", "kui", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vuimin", "vuimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vuimax", "vuimax", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        q0: float | None = None,
        q1: float | None = None,
        p0: float | None = None,
        p1: float | None = None,
        kui: float | None = None,
        vuimin: float | None = None,
        vuimax: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.q0 = q0
        self.q1 = q1
        self.p0 = p0
        self.p1 = p1
        self.kui = kui
        self.vuimin = vuimin
        self.vuimax = vuimax
