"""CIM class DiscExcContIEEEDEC2A (TC57CIM/IEC61970/Dynamics/StandardModels/DiscontinuousExcitationControlDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.discontinuous_excitation_control_dynamics.discontinuous_excitation_control_dynamics import (
    DiscontinuousExcitationControlDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class DiscExcContIEEEDEC2A(DiscontinuousExcitationControlDynamics):
    """IEEE type DEC2A model for discontinuous excitation control. This system provides
    transient excitation boosting via an open-loop control as initiated by a trigger signal
    generated remotely.

    Reference: IEEE 421.5-2005 12.3."""

    __slots__ = ("td1", "td2", "vdmax", "vdmin", "vk")

    vk: float | None  # PU
    td1: float | None  # Seconds
    td2: float | None  # Seconds
    vdmin: float | None  # PU
    vdmax: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="DiscExcContIEEEDEC2A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/DiscontinuousExcitationControlDynamics",
        guid="{15DE3E2D-E9AD-4074-B6F7-4EA21A53D37C}",
        attributes=(
            AttrMeta("vk", "vk", "PU", 0, 1, "cimdatatype"),
            AttrMeta("td1", "td1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("td2", "td2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vdmin", "vdmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vdmax", "vdmax", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        vk: float | None = None,
        td1: float | None = None,
        td2: float | None = None,
        vdmin: float | None = None,
        vdmax: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vk = vk
        self.td1 = td1
        self.td2 = td2
        self.vdmin = vdmin
        self.vdmax = vdmax
