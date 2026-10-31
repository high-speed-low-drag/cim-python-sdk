"""CIM class VCompIEEEType1 (TC57CIM/IEC61970/Dynamics/StandardModels/VoltageCompensatorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.voltage_compensator_dynamics import (
    VoltageCompensatorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class VCompIEEEType1(VoltageCompensatorDynamics):
    """Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This
    model is common to all excitation system models described in the IEEE Standard.

    Parameter details:

    - If Rc and Xc are set to zero, the load compensation is not employed and the behaviour
    is as a simple sensing circuit.

    - If all parameters (Rc, Xc and Tr) are set to zero, the standard model VCompIEEEType1
    is bypassed.

    Reference: IEEE 421.5-2005 4."""

    __slots__ = ("rc", "tr", "xc")

    rc: float | None  # PU
    xc: float | None  # PU
    tr: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="VCompIEEEType1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/VoltageCompensatorDynamics",
        guid="{58FEC809-4186-40e8-AFE8-88EE546426C2}",
        attributes=(
            AttrMeta("rc", "rc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xc", "xc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tr", "tr", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        rc: float | None = None,
        xc: float | None = None,
        tr: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rc = rc
        self.xc = xc
        self.tr = tr
