"""CIM class ExcAVR1 (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAVR1(ExcitationSystemDynamics):
    """Italian excitation system corresponding to IEEE (1968) type 1 model. It represents an
    exciter dynamo and electromechanical regulator."""

    __slots__ = ("e1", "e2", "ka", "kf", "se1", "se2", "ta", "tb", "te", "tf", "vrmn", "vrmx")

    ka: float | None
    vrmn: float | None  # PU
    vrmx: float | None  # PU
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    te: float | None  # Seconds
    e1: float | None  # PU
    se1: float | None
    e2: float | None  # PU
    se2: float | None
    kf: float | None
    tf: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="ExcAVR1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{D52F6976-E896-4a1d-97FE-B20145E07A4A}",
        attributes=(
            AttrMeta("ka", "ka", "float", 0, 1, "primitive"),
            AttrMeta("vrmn", "vrmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmx", "vrmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("e1", "e1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("se1", "se1", "float", 0, 1, "primitive"),
            AttrMeta("e2", "e2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("se2", "se2", "float", 0, 1, "primitive"),
            AttrMeta("kf", "kf", "float", 0, 1, "primitive"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ka: float | None = None,
        vrmn: float | None = None,
        vrmx: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        te: float | None = None,
        e1: float | None = None,
        se1: float | None = None,
        e2: float | None = None,
        se2: float | None = None,
        kf: float | None = None,
        tf: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ka = ka
        self.vrmn = vrmn
        self.vrmx = vrmx
        self.ta = ta
        self.tb = tb
        self.te = te
        self.e1 = e1
        self.se1 = se1
        self.e2 = e2
        self.se2 = se2
        self.kf = kf
        self.tf = tf
