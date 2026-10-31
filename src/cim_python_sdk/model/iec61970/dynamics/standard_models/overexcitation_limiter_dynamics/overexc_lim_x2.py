"""CIM class OverexcLimX2 (TC57CIM/IEC61970/Dynamics/StandardModels/OverexcitationLimiterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.overexcitation_limiter_dynamics.overexcitation_limiter_dynamics import (
    OverexcitationLimiterDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class OverexcLimX2(OverexcitationLimiterDynamics):
    """Field voltage or current overexcitation limiter designed to protect the generator field
    of an AC machine with automatic excitation control from overheating due to prolonged
    overexcitation."""

    __slots__ = ("efd1", "efd2", "efd3", "efddes", "efdrated", "kmx", "m", "t1", "t2", "t3", "vlow")

    m: bool | None
    efdrated: float | None  # PU
    efd1: float | None  # PU
    t1: float | None  # Seconds
    efd2: float | None  # PU
    t2: float | None  # Seconds
    efd3: float | None  # PU
    t3: float | None  # Seconds
    efddes: float | None  # PU
    kmx: float | None  # PU
    vlow: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="OverexcLimX2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/OverexcitationLimiterDynamics",
        guid="{50B12A55-58EB-4286-9D29-934B2E7E9539}",
        attributes=(
            AttrMeta("m", "m", "bool", 0, 1, "primitive"),
            AttrMeta("efdrated", "efdrated", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efd1", "efd1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efd2", "efd2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efd3", "efd3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efddes", "efddes", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kmx", "kmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vlow", "vlow", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        m: bool | None = None,
        efdrated: float | None = None,
        efd1: float | None = None,
        t1: float | None = None,
        efd2: float | None = None,
        t2: float | None = None,
        efd3: float | None = None,
        t3: float | None = None,
        efddes: float | None = None,
        kmx: float | None = None,
        vlow: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.m = m
        self.efdrated = efdrated
        self.efd1 = efd1
        self.t1 = t1
        self.efd2 = efd2
        self.t2 = t2
        self.efd3 = efd3
        self.t3 = t3
        self.efddes = efddes
        self.kmx = kmx
        self.vlow = vlow
