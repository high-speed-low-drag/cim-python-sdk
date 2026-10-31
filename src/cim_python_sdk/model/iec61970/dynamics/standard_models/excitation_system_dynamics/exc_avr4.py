"""CIM class ExcAVR4 (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAVR4(ExcitationSystemDynamics):
    """Italian excitation system. It represents a static exciter and electric voltage
    regulator."""

    __slots__ = (
        "imul",
        "ka",
        "ke",
        "kif",
        "t1",
        "t1if",
        "t2",
        "t3",
        "t4",
        "tif",
        "vfmn",
        "vfmx",
        "vrmn",
        "vrmx",
    )

    ka: float | None
    vrmn: float | None  # PU
    vrmx: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    ke: float | None
    vfmx: float | None  # PU
    vfmn: float | None  # PU
    kif: float | None
    tif: float | None  # Seconds
    t1if: float | None  # Seconds
    imul: bool | None

    _cim_meta = ClassMeta(
        cim_name="ExcAVR4",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{3A5F8C1A-125E-4a31-A9C0-E47A651225AE}",
        attributes=(
            AttrMeta("ka", "ka", "float", 0, 1, "primitive"),
            AttrMeta("vrmn", "vrmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmx", "vrmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "float", 0, 1, "primitive"),
            AttrMeta("vfmx", "vfmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vfmn", "vfmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kif", "kif", "float", 0, 1, "primitive"),
            AttrMeta("tif", "tif", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t1if", "t1if", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("imul", "imul", "bool", 0, 1, "primitive"),
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
        ke: float | None = None,
        vfmx: float | None = None,
        vfmn: float | None = None,
        kif: float | None = None,
        tif: float | None = None,
        t1if: float | None = None,
        imul: bool | None = None,
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
        self.ke = ke
        self.vfmx = vfmx
        self.vfmn = vfmn
        self.kif = kif
        self.tif = tif
        self.t1if = t1if
        self.imul = imul
