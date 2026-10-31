"""CIM class PssSK (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssSK(PowerSystemStabilizerDynamics):
    """Slovakian PSS with three inputs."""

    __slots__ = ("k1", "k2", "k3", "t1", "t2", "t3", "t4", "t5", "t6", "vsmax", "vsmin")

    k1: float | None  # PU
    k2: float | None  # PU
    k3: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    t5: float | None  # Seconds
    t6: float | None  # Seconds
    vsmax: float | None  # PU
    vsmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PssSK",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{93E7D9BA-C95F-4303-8490-5F00FA1C4983}",
        attributes=(
            AttrMeta("k1", "k1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vsmax", "vsmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vsmin", "vsmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        k1: float | None = None,
        k2: float | None = None,
        k3: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        t5: float | None = None,
        t6: float | None = None,
        vsmax: float | None = None,
        vsmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.vsmax = vsmax
        self.vsmin = vsmin
