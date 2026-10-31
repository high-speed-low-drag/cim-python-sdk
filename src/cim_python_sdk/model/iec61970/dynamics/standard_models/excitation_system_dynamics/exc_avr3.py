"""CIM class ExcAVR3 (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAVR3(ExcitationSystemDynamics):
    """Italian excitation system. It represents an exciter dynamo and electric regulator."""

    __slots__ = ("e1", "e2", "ka", "se1", "se2", "t1", "t2", "t3", "t4", "te", "vrmn", "vrmx")

    ka: float | None
    vrmn: float | None  # PU
    vrmx: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    te: float | None  # Seconds
    e1: float | None  # PU
    se1: float | None
    e2: float | None  # PU
    se2: float | None

    _cim_meta = ClassMeta(
        cim_name="ExcAVR3",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{D364518B-D877-42ff-8227-1625F54175F8}",
        attributes=(
            AttrMeta("ka", "ka", "float", 0, 1, "primitive"),
            AttrMeta("vrmn", "vrmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmx", "vrmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("e1", "e1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("se1", "se1", "float", 0, 1, "primitive"),
            AttrMeta("e2", "e2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("se2", "se2", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        ka: float | None = None,
        vrmn: float | None = None,
        vrmx: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        te: float | None = None,
        e1: float | None = None,
        se1: float | None = None,
        e2: float | None = None,
        se2: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ka = ka
        self.vrmn = vrmn
        self.vrmx = vrmx
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.te = te
        self.e1 = e1
        self.se1 = se1
        self.e2 = e2
        self.se2 = se2
