"""CIM class ExcNI (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcNI(ExcitationSystemDynamics):
    """Bus or solid fed SCR (silicon-controlled rectifier) bridge excitation system model type
    NI (NVE)."""

    __slots__ = ("bus_fed_selector", "ka", "kf", "r", "ta", "tf1", "tf2", "tr", "vrmax", "vrmin")

    bus_fed_selector: bool | None
    tr: float | None  # Seconds
    ka: float | None  # PU
    ta: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    kf: float | None  # PU
    tf2: float | None  # Seconds
    tf1: float | None  # Seconds
    r: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcNI",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{0CD180C8-EE66-4407-B672-6462C586CCC5}",
        attributes=(
            AttrMeta("bus_fed_selector", "busFedSelector", "bool", 0, 1, "primitive"),
            AttrMeta("tr", "tr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf2", "tf2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf1", "tf1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        bus_fed_selector: bool | None = None,
        tr: float | None = None,
        ka: float | None = None,
        ta: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        kf: float | None = None,
        tf2: float | None = None,
        tf1: float | None = None,
        r: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bus_fed_selector = bus_fed_selector
        self.tr = tr
        self.ka = ka
        self.ta = ta
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.kf = kf
        self.tf2 = tf2
        self.tf1 = tf1
        self.r = r
