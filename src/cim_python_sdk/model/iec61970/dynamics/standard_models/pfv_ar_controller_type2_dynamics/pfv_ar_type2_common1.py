"""CIM class PFVArType2Common1 (TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType2Dynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type2_dynamics.pfv_ar_controller_type2_dynamics import (
    PFVArControllerType2Dynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PFVArType2Common1(PFVArControllerType2Dynamics):
    """Power factor / reactive power regulator. This model represents the power factor or
    reactive power controller such as the Basler SCP-250. The controller measures power
    factor or reactive power (PU on generator rated power) and compares it with the
    operator's set point.

    [Footnote: Basler SCP-250 is an example of a suitable product available commercially.
    This information is given for the convenience of users of this document and does not
    constitute an endorsement by IEC of this product.]"""

    __slots__ = ("j", "ki", "kp", "max", "ref")

    j: bool | None
    kp: float | None  # PU
    ki: float | None  # PU
    max: float | None  # PU
    ref: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PFVArType2Common1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType2Dynamics",
        guid="{8914671E-3A96-45b6-8FA3-77317BAA7893}",
        attributes=(
            AttrMeta("j", "j", "bool", 0, 1, "primitive"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("max", "max", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ref", "ref", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        j: bool | None = None,
        kp: float | None = None,
        ki: float | None = None,
        max: float | None = None,
        ref: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.j = j
        self.kp = kp
        self.ki = ki
        self.max = max
        self.ref = ref
