"""CIM class LinearShuntCompensatorPhase (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.shunt_compensator_phase import ShuntCompensatorPhase

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class LinearShuntCompensatorPhase(ShuntCompensatorPhase):
    """A per phase linear shunt compensator has banks or sections with equal admittance values."""

    __slots__ = ("b_per_section", "g_per_section")

    b_per_section: float | None  # Susceptance
    g_per_section: float | None  # Conductance

    _cim_meta = ClassMeta(
        cim_name="LinearShuntCompensatorPhase",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{15B42F89-92AF-4830-BC3C-4CD7FB779043}",
        attributes=(
            AttrMeta("b_per_section", "bPerSection", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("g_per_section", "gPerSection", "Conductance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        b_per_section: float | None = None,
        g_per_section: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b_per_section = b_per_section
        self.g_per_section = g_per_section
