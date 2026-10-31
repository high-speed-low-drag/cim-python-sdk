"""CIM class UnderexcLimIEEE1 (TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.underexcitation_limiter_dynamics.underexcitation_limiter_dynamics import (
    UnderexcitationLimiterDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
    """Type UEL1 model which has a circular limit boundary when plotted in terms of machine
    reactive power vs. real power output.

    Reference: IEEE UEL1 421.5-2005, 10.1."""

    __slots__ = (
        "kuc",
        "kuf",
        "kui",
        "kul",
        "kur",
        "tu1",
        "tu2",
        "tu3",
        "tu4",
        "vucmax",
        "vuimax",
        "vuimin",
        "vulmax",
        "vulmin",
        "vurmax",
    )

    kur: float | None  # PU
    kuc: float | None  # PU
    kuf: float | None  # PU
    vurmax: float | None  # PU
    vucmax: float | None  # PU
    kui: float | None  # PU
    kul: float | None  # PU
    vuimax: float | None  # PU
    vuimin: float | None  # PU
    tu1: float | None  # Seconds
    tu2: float | None  # Seconds
    tu3: float | None  # Seconds
    tu4: float | None  # Seconds
    vulmax: float | None  # PU
    vulmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="UnderexcLimIEEE1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics",
        guid="{8B14239E-961A-4d9a-817F-2F67CE6CDBC7}",
        attributes=(
            AttrMeta("kur", "kur", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kuc", "kuc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kuf", "kuf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vurmax", "vurmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vucmax", "vucmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kui", "kui", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kul", "kul", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vuimax", "vuimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vuimin", "vuimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tu1", "tu1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tu2", "tu2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tu3", "tu3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tu4", "tu4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vulmax", "vulmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vulmin", "vulmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        kur: float | None = None,
        kuc: float | None = None,
        kuf: float | None = None,
        vurmax: float | None = None,
        vucmax: float | None = None,
        kui: float | None = None,
        kul: float | None = None,
        vuimax: float | None = None,
        vuimin: float | None = None,
        tu1: float | None = None,
        tu2: float | None = None,
        tu3: float | None = None,
        tu4: float | None = None,
        vulmax: float | None = None,
        vulmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kur = kur
        self.kuc = kuc
        self.kuf = kuf
        self.vurmax = vurmax
        self.vucmax = vucmax
        self.kui = kui
        self.kul = kul
        self.vuimax = vuimax
        self.vuimin = vuimin
        self.tu1 = tu1
        self.tu2 = tu2
        self.tu3 = tu3
        self.tu4 = tu4
        self.vulmax = vulmax
        self.vulmin = vulmin
