"""CIM class ExcAVR7 (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcAVR7(ExcitationSystemDynamics):
    """IVO excitation system."""

    __slots__ = (
        "a1",
        "a2",
        "a3",
        "a4",
        "a5",
        "a6",
        "k1",
        "k3",
        "k5",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
        "vmax1",
        "vmax3",
        "vmax5",
        "vmin1",
        "vmin3",
        "vmin5",
    )

    k1: float | None  # PU
    a1: float | None  # PU
    a2: float | None  # PU
    t1: float | None  # Seconds
    t2: float | None  # Seconds
    vmax1: float | None  # PU
    vmin1: float | None  # PU
    k3: float | None  # PU
    a3: float | None  # PU
    a4: float | None  # PU
    t3: float | None  # Seconds
    t4: float | None  # Seconds
    vmax3: float | None  # PU
    vmin3: float | None  # PU
    k5: float | None  # PU
    a5: float | None  # PU
    a6: float | None  # PU
    t5: float | None  # Seconds
    t6: float | None  # Seconds
    vmax5: float | None  # PU
    vmin5: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcAVR7",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{73844DAB-C2BA-416d-A10A-1BAC8B6E73EA}",
        attributes=(
            AttrMeta("k1", "k1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a1", "a1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a2", "a2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t2", "t2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vmax1", "vmax1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmin1", "vmin1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a3", "a3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a4", "a4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t3", "t3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4", "t4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vmax3", "vmax3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmin3", "vmin3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k5", "k5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a5", "a5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("a6", "a6", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t5", "t5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t6", "t6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vmax5", "vmax5", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmin5", "vmin5", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        k1: float | None = None,
        a1: float | None = None,
        a2: float | None = None,
        t1: float | None = None,
        t2: float | None = None,
        vmax1: float | None = None,
        vmin1: float | None = None,
        k3: float | None = None,
        a3: float | None = None,
        a4: float | None = None,
        t3: float | None = None,
        t4: float | None = None,
        vmax3: float | None = None,
        vmin3: float | None = None,
        k5: float | None = None,
        a5: float | None = None,
        a6: float | None = None,
        t5: float | None = None,
        t6: float | None = None,
        vmax5: float | None = None,
        vmin5: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.k1 = k1
        self.a1 = a1
        self.a2 = a2
        self.t1 = t1
        self.t2 = t2
        self.vmax1 = vmax1
        self.vmin1 = vmin1
        self.k3 = k3
        self.a3 = a3
        self.a4 = a4
        self.t3 = t3
        self.t4 = t4
        self.vmax3 = vmax3
        self.vmin3 = vmin3
        self.k5 = k5
        self.a5 = a5
        self.a6 = a6
        self.t5 = t5
        self.t6 = t6
        self.vmax5 = vmax5
        self.vmin5 = vmin5
