"""CIM class EquivalentShunt (TC57CIM/IEC61970/Base/Equivalents). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.equivalents.equivalent_equipment import EquivalentEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class EquivalentShunt(EquivalentEquipment):
    """The class represents equivalent shunts."""

    __slots__ = ("b", "g")

    b: float | None  # Susceptance
    g: float | None  # Conductance

    _cim_meta = ClassMeta(
        cim_name="EquivalentShunt",
        package="TC57CIM/IEC61970/Base/Equivalents",
        guid="{78A11A2E-59D2-4823-9137-ACBA6B6BC4FC}",
        attributes=(
            AttrMeta("b", "b", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("g", "g", "Conductance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        b: float | None = None,
        g: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b = b
        self.g = g
