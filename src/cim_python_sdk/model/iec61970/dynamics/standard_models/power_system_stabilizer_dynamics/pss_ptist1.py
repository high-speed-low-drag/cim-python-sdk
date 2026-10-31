"""CIM class PssPTIST1 (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssPTIST1(PowerSystemStabilizerDynamics):
    """PTI microprocessor-based stabilizer type 1."""

    __slots__ = ("dtc", "dtf", "dtp", "k", "m", "t1", "t2", "t3", "t4", "tf", "tp")

    m: float | None  # PU
    tf: float | None  # Seconds
    tp: float | None  # Seconds
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    k: float | None  # PU
    dtf: float | None  # Seconds
    dtc: float | None  # Seconds
    dtp: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="PssPTIST1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{229FA810-11BB-4ba2-A87E-BF24CB715940}",
        attributes=(
            AttrMeta("m", "m", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dtf", "dtf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("dtc", "dtc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("dtp", "dtp", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        m: float | None = None,
        tf: float | None = None,
        tp: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        k: float | None = None,
        dtf: float | None = None,
        dtc: float | None = None,
        dtp: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.m = m
        self.tf = tf
        self.tp = tp
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.k = k
        self.dtf = dtf
        self.dtc = dtc
        self.dtp = dtp
