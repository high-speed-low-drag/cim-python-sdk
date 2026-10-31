"""CIM class UnderexcLimIEEE2 (TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.underexcitation_limiter_dynamics.underexcitation_limiter_dynamics import (
    UnderexcitationLimiterDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class UnderexcLimIEEE2(UnderexcitationLimiterDynamics):
    """Type UEL2 underexcitation limiter which has either a straight-line or multi-segment
    characteristic when plotted in terms of machine reactive power output vs. real power
    output.

    Reference: IEEE UEL2 421.5-2005, 10.2 (limit characteristic lookup table shown in Figure
    10.4 (p 32))."""

    __slots__ = (
        "k1",
        "k2",
        "kfb",
        "kuf",
        "kui",
        "kul",
        "p0",
        "p1",
        "p2",
        "p3",
        "p4",
        "p5",
        "p6",
        "p7",
        "p8",
        "p9",
        "p10",
        "q0",
        "q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "q6",
        "q7",
        "q8",
        "q9",
        "q10",
        "tu1",
        "tu2",
        "tu3",
        "tu4",
        "tul",
        "tup",
        "tuq",
        "tuv",
        "vuimax",
        "vuimin",
        "vulmax",
        "vulmin",
    )

    tuv: float | None  # Seconds
    tup: float | None  # Seconds
    tuq: float | None  # Seconds
    kui: float | None  # PU
    kul: float | None  # PU
    vuimax: float | None  # PU
    vuimin: float | None  # PU
    kuf: float | None  # PU
    kfb: float | None  # PU
    tul: float | None  # Seconds
    tu1: float | None  # Seconds
    tu2: float | None  # Seconds
    tu3: float | None  # Seconds
    tu4: float | None  # Seconds
    vulmax: float | None  # PU
    vulmin: float | None  # PU
    p0: float | None  # PU
    q0: float | None  # PU
    p1: float | None  # PU
    q1: float | None  # PU
    p2: float | None  # PU
    q2: float | None  # PU
    p3: float | None  # PU
    q3: float | None  # PU
    p4: float | None  # PU
    q4: float | None  # PU
    p5: float | None  # PU
    q5: float | None  # PU
    p6: float | None  # PU
    q6: float | None  # PU
    p7: float | None  # PU
    q7: float | None  # PU
    p8: float | None  # PU
    q8: float | None  # PU
    p9: float | None  # PU
    q9: float | None  # PU
    p10: float | None  # PU
    q10: float | None  # PU
    k1: float | None
    k2: float | None

    _cim_meta = ClassMeta(
        cim_name="UnderexcLimIEEE2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics",
        guid="{B375402B-97CA-4cb0-8481-5B4BAD2DC234}",
        attributes=(
            AttrMeta("tuv", "tuv", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tup", "tup", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tuq", "tuq", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kui", "kui", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kul", "kul", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vuimax", "vuimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vuimin", "vuimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kuf", "kuf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kfb", "kfb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tul", "tul", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tu1", "tu1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tu2", "tu2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tu3", "tu3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tu4", "tu4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vulmax", "vulmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vulmin", "vulmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p0", "p0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q0", "q0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p1", "p1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q1", "q1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p2", "p2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q2", "q2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p3", "p3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q3", "q3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p4", "p4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q4", "q4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p5", "p5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q5", "q5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p6", "p6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q6", "q6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p7", "p7", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q7", "q7", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p8", "p8", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q8", "q8", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p9", "p9", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q9", "q9", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p10", "p10", "PU", 0, 1, "cimdatatype"),
            AttrMeta("q10", "q10", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k1", "k1", "float", 0, 1, "primitive"),
            AttrMeta("k2", "k2", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        tuv: float | None = None,
        tup: float | None = None,
        tuq: float | None = None,
        kui: float | None = None,
        kul: float | None = None,
        vuimax: float | None = None,
        vuimin: float | None = None,
        kuf: float | None = None,
        kfb: float | None = None,
        tul: float | None = None,
        tu1: float | None = None,
        tu2: float | None = None,
        tu3: float | None = None,
        tu4: float | None = None,
        vulmax: float | None = None,
        vulmin: float | None = None,
        p0: float | None = None,
        q0: float | None = None,
        p1: float | None = None,
        q1: float | None = None,
        p2: float | None = None,
        q2: float | None = None,
        p3: float | None = None,
        q3: float | None = None,
        p4: float | None = None,
        q4: float | None = None,
        p5: float | None = None,
        q5: float | None = None,
        p6: float | None = None,
        q6: float | None = None,
        p7: float | None = None,
        q7: float | None = None,
        p8: float | None = None,
        q8: float | None = None,
        p9: float | None = None,
        q9: float | None = None,
        p10: float | None = None,
        q10: float | None = None,
        k1: float | None = None,
        k2: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tuv = tuv
        self.tup = tup
        self.tuq = tuq
        self.kui = kui
        self.kul = kul
        self.vuimax = vuimax
        self.vuimin = vuimin
        self.kuf = kuf
        self.kfb = kfb
        self.tul = tul
        self.tu1 = tu1
        self.tu2 = tu2
        self.tu3 = tu3
        self.tu4 = tu4
        self.vulmax = vulmax
        self.vulmin = vulmin
        self.p0 = p0
        self.q0 = q0
        self.p1 = p1
        self.q1 = q1
        self.p2 = p2
        self.q2 = q2
        self.p3 = p3
        self.q3 = q3
        self.p4 = p4
        self.q4 = q4
        self.p5 = p5
        self.q5 = q5
        self.p6 = p6
        self.q6 = q6
        self.p7 = p7
        self.q7 = q7
        self.p8 = p8
        self.q8 = q8
        self.p9 = p9
        self.q9 = q9
        self.p10 = p10
        self.q10 = q10
        self.k1 = k1
        self.k2 = k2
