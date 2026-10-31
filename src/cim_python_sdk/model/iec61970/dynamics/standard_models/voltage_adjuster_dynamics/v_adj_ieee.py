"""CIM class VAdjIEEE (TC57CIM/IEC61970/Dynamics/StandardModels/VoltageAdjusterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_adjuster_dynamics.voltage_adjuster_dynamics import (
    VoltageAdjusterDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class VAdjIEEE(VoltageAdjusterDynamics):
    """IEEE voltage adjuster which is used to represent the voltage adjuster in either a power
    factor or VAr control system.

    Reference: IEEE 421.5-2005, 11.1."""

    __slots__ = ("adjslew", "taoff", "taon", "vadjf", "vadjmax", "vadjmin")

    vadjf: float | None
    adjslew: float | None
    vadjmax: float | None  # PU
    vadjmin: float | None  # PU
    taon: float | None  # Seconds
    taoff: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="VAdjIEEE",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/VoltageAdjusterDynamics",
        guid="{C517D5B9-8DE4-4809-A2CC-2FA6902EDBCD}",
        attributes=(
            AttrMeta("vadjf", "vadjf", "float", 0, 1, "primitive"),
            AttrMeta("adjslew", "adjslew", "float", 0, 1, "primitive"),
            AttrMeta("vadjmax", "vadjmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vadjmin", "vadjmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("taon", "taon", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("taoff", "taoff", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        vadjf: float | None = None,
        adjslew: float | None = None,
        vadjmax: float | None = None,
        vadjmin: float | None = None,
        taon: float | None = None,
        taoff: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vadjf = vadjf
        self.adjslew = adjslew
        self.vadjmax = vadjmax
        self.vadjmin = vadjmin
        self.taon = taon
        self.taoff = taoff
