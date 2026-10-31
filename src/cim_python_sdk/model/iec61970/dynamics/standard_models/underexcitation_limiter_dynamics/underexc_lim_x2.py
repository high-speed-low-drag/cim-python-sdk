"""CIM class UnderexcLimX2 (TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.underexcitation_limiter_dynamics.underexcitation_limiter_dynamics import (
    UnderexcitationLimiterDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class UnderexcLimX2(UnderexcitationLimiterDynamics):
    """Westinghouse minimum excitation limiter."""

    __slots__ = ("kf2", "km", "melmax", "qo", "r", "tf2", "tm")

    kf2: float | None  # PU
    tf2: float | None  # Seconds
    km: float | None  # PU
    tm: float | None  # Seconds
    melmax: float | None  # PU
    qo: float | None  # PU
    r: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="UnderexcLimX2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics",
        guid="{23F73DA8-DC29-4079-8E17-C845792E00C6}",
        attributes=(
            AttrMeta("kf2", "kf2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf2", "tf2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("km", "km", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tm", "tm", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("melmax", "melmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qo", "qo", "PU", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        kf2: float | None = None,
        tf2: float | None = None,
        km: float | None = None,
        tm: float | None = None,
        melmax: float | None = None,
        qo: float | None = None,
        r: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kf2 = kf2
        self.tf2 = tf2
        self.km = km
        self.tm = tm
        self.melmax = melmax
        self.qo = qo
        self.r = r
