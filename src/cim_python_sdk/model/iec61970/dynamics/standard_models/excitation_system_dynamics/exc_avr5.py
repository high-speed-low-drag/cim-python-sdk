"""CIM class ExcAVR5 (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAVR5(ExcitationSystemDynamics):
    """Manual excitation control with field circuit resistance. This model can be used as a
    very simple representation of manual voltage control."""

    __slots__ = ("ka", "rex", "ta")

    ka: float | None  # PU
    ta: float | None  # Seconds
    rex: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcAVR5",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{6E6ABF9C-E5AE-4ae0-A338-2F4EA53270E8}",
        attributes=(
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("rex", "rex", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ka: float | None = None,
        ta: float | None = None,
        rex: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ka = ka
        self.ta = ta
        self.rex = rex
