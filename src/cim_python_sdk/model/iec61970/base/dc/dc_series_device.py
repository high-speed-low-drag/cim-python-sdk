"""CIM class DCSeriesDevice (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.dc.dc_conducting_equipment import DCConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class DCSeriesDevice(DCConductingEquipment):
    """A series device within the DC system, typically a reactor used for filtering or
    smoothing. Needed for transient and short circuit studies."""

    __slots__ = ("inductance", "resistance")

    inductance: float | None  # Inductance
    resistance: float | None  # Resistance

    _cim_meta = ClassMeta(
        cim_name="DCSeriesDevice",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{9E35D55D-1A94-4f1e-9313-1A6D03CB91B1}",
        attributes=(
            AttrMeta("inductance", "inductance", "Inductance", 0, 1, "cimdatatype"),
            AttrMeta("resistance", "resistance", "Resistance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        inductance: float | None = None,
        resistance: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.inductance = inductance
        self.resistance = resistance
