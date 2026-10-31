"""CIM class PssRQB (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssRQB(PowerSystemStabilizerDynamics):
    """Power system stabilizer type RQB. This power system stabilizer is intended to be used
    together with excitation system type ExcRQB, which is primarily used in nuclear or
    thermal generating units."""

    __slots__ = ("kdpm", "ki2", "ki3", "ki4", "sibv", "t4f", "t4m", "t4mom", "tomd", "tomsl")

    ki2: float | None
    ki3: float | None
    ki4: float | None
    t4m: float | None  # Seconds
    tomd: float | None  # Seconds
    tomsl: float | None  # Seconds
    t4mom: float | None  # Seconds
    sibv: float | None  # PU
    kdpm: float | None
    t4f: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="PssRQB",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{4B9A2B52-0378-49b2-AB8D-8979ECA37D09}",
        attributes=(
            AttrMeta("ki2", "ki2", "float", 0, 1, "primitive"),
            AttrMeta("ki3", "ki3", "float", 0, 1, "primitive"),
            AttrMeta("ki4", "ki4", "float", 0, 1, "primitive"),
            AttrMeta("t4m", "t4m", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tomd", "tomd", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tomsl", "tomsl", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4mom", "t4mom", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("sibv", "sibv", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kdpm", "kdpm", "float", 0, 1, "primitive"),
            AttrMeta("t4f", "t4f", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ki2: float | None = None,
        ki3: float | None = None,
        ki4: float | None = None,
        t4m: float | None = None,
        tomd: float | None = None,
        tomsl: float | None = None,
        t4mom: float | None = None,
        sibv: float | None = None,
        kdpm: float | None = None,
        t4f: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ki2 = ki2
        self.ki3 = ki3
        self.ki4 = ki4
        self.t4m = t4m
        self.tomd = tomd
        self.tomsl = tomsl
        self.t4mom = t4mom
        self.sibv = sibv
        self.kdpm = kdpm
        self.t4f = t4f
