"""CIM class DCGround (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.dc.dc_conducting_equipment import DCConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class DCGround(DCConductingEquipment):
    """A ground within a DC system."""

    __slots__ = ("inductance", "r")

    inductance: float | None  # Inductance
    r: float | None  # Resistance

    _cim_meta = ClassMeta(
        cim_name="DCGround",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{9C3BBD85-5358-4fb4-A4B5-9A1BB7278445}",
        attributes=(
            AttrMeta("inductance", "inductance", "Inductance", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        inductance: float | None = None,
        r: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.inductance = inductance
        self.r = r
