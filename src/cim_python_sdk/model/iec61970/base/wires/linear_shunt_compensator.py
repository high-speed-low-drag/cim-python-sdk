"""CIM class LinearShuntCompensator (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.shunt_compensator import ShuntCompensator

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class LinearShuntCompensator(ShuntCompensator):
    """A linear shunt compensator has banks or sections with equal admittance values."""

    __slots__ = ("b0_per_section", "b_per_section", "g0_per_section", "g_per_section")

    b0_per_section: float | None  # Susceptance
    b_per_section: float | None  # Susceptance
    g0_per_section: float | None  # Conductance
    g_per_section: float | None  # Conductance

    _cim_meta = ClassMeta(
        cim_name="LinearShuntCompensator",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{94E82A47-069F-4e2b-A4FA-8CFD5E140FD7}",
        attributes=(
            AttrMeta("b0_per_section", "b0PerSection", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("b_per_section", "bPerSection", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("g0_per_section", "g0PerSection", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("g_per_section", "gPerSection", "Conductance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        b0_per_section: float | None = None,
        b_per_section: float | None = None,
        g0_per_section: float | None = None,
        g_per_section: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b0_per_section = b0_per_section
        self.b_per_section = b_per_section
        self.g0_per_section = g0_per_section
        self.g_per_section = g_per_section
