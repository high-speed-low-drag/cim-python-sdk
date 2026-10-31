"""CIM class UnderexcLimX1 (TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.underexcitation_limiter_dynamics.underexcitation_limiter_dynamics import (
    UnderexcitationLimiterDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class UnderexcLimX1(UnderexcitationLimiterDynamics):
    """Allis-Chalmers minimum excitation limiter."""

    __slots__ = ("k", "kf2", "km", "melmax", "tf2", "tm")

    kf2: float | None  # PU
    tf2: float | None  # Seconds
    km: float | None  # PU
    tm: float | None  # Seconds
    melmax: float | None  # PU
    k: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="UnderexcLimX1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics",
        guid="{15AF875B-D1DA-4f94-9694-AB5C0F490BB0}",
        attributes=(
            AttrMeta("kf2", "kf2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf2", "tf2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("km", "km", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tm", "tm", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("melmax", "melmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
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
        k: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kf2 = kf2
        self.tf2 = tf2
        self.km = km
        self.tm = tm
        self.melmax = melmax
        self.k = k
