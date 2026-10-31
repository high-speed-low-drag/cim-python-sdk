"""CIM class DCShunt (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.dc.dc_conducting_equipment import DCConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class DCShunt(DCConductingEquipment):
    """A shunt device within the DC system, typically used for filtering. Needed for transient
    and short circuit studies."""

    __slots__ = ("capacitance", "resistance")

    capacitance: float | None  # Capacitance
    resistance: float | None  # Resistance

    _cim_meta = ClassMeta(
        cim_name="DCShunt",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{FF3349AD-8A10-4581-83AC-8906B6F29408}",
        attributes=(
            AttrMeta("capacitance", "capacitance", "Capacitance", 0, 1, "cimdatatype"),
            AttrMeta("resistance", "resistance", "Resistance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        capacitance: float | None = None,
        resistance: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capacitance = capacitance
        self.resistance = resistance
