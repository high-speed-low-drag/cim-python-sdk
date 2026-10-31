"""CIM class PssSTAB2A (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssSTAB2A(PowerSystemStabilizerDynamics):
    """Power system stabilizer part of an ABB excitation system.

    [Footnote: ABB excitation systems are an example of suitable products available
    commercially. This information is given for the convenience of users of this document
    and does not constitute an endorsement by IEC of these products.]"""

    __slots__ = ("hlim", "k2", "k3", "k4", "k5", "t2", "t3", "t5")

    k2: float | None  # PU
    k3: float | None  # PU
    k4: float | None  # PU
    k5: float | None  # PU
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t5: float | None  # Seconds
    hlim: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PssSTAB2A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{8BDE4EF4-4308-4c14-AB44-89290DDC8FE0}",
        attributes=(
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k4", "k4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k5", "k5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("hlim", "hlim", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        k2: float | None = None,
        k3: float | None = None,
        k4: float | None = None,
        k5: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t5: float | None = None,
        hlim: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.k5 = k5
        self.t2 = t2
        self.t3 = t3
        self.t5 = t5
        self.hlim = hlim
