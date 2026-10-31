"""CIM class BatteryUnit (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.generation.production.power_electronics_unit import (
    PowerElectronicsUnit,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.battery_state_kind import (
        BatteryStateKind,
    )


class BatteryUnit(PowerElectronicsUnit):
    """An electrochemical energy storage device."""

    __slots__ = ("battery_state", "rated_e", "stored_e")

    battery_state: BatteryStateKind | None
    rated_e: float | None  # RealEnergy
    stored_e: float | None  # RealEnergy

    _cim_meta = ClassMeta(
        cim_name="BatteryUnit",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{8DEBA1CF-D08F-4587-8EC0-237B5DDBBD5C}",
        attributes=(
            AttrMeta("battery_state", "batteryState", "BatteryStateKind", 0, 1, "enumeration"),
            AttrMeta("rated_e", "ratedE", "RealEnergy", 0, 1, "cimdatatype"),
            AttrMeta("stored_e", "storedE", "RealEnergy", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        battery_state: BatteryStateKind | None = None,
        rated_e: float | None = None,
        stored_e: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.battery_state = battery_state
        self.rated_e = rated_e
        self.stored_e = stored_e
