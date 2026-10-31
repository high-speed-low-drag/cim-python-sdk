"""CIM class CurrentRelay (TC57CIM/IEC61970/Base/Protection). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.protection.protection_equipment import ProtectionEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class CurrentRelay(ProtectionEquipment):
    """A device that checks current flow values in any direction or designated direction."""

    __slots__ = (
        "current_limit1",
        "current_limit2",
        "current_limit3",
        "inverse_time_flag",
        "time_delay1",
        "time_delay2",
        "time_delay3",
    )

    current_limit1: float | None  # CurrentFlow
    current_limit2: float | None  # CurrentFlow
    current_limit3: float | None  # CurrentFlow
    inverse_time_flag: bool | None
    time_delay1: float | None  # Seconds
    time_delay2: float | None  # Seconds
    time_delay3: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="CurrentRelay",
        package="TC57CIM/IEC61970/Base/Protection",
        guid="{247B2098-278F-499e-ABC4-69CDCCCC7DAF}",
        attributes=(
            AttrMeta("current_limit1", "currentLimit1", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("current_limit2", "currentLimit2", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("current_limit3", "currentLimit3", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("inverse_time_flag", "inverseTimeFlag", "bool", 0, 1, "primitive"),
            AttrMeta("time_delay1", "timeDelay1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("time_delay2", "timeDelay2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("time_delay3", "timeDelay3", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        current_limit1: float | None = None,
        current_limit2: float | None = None,
        current_limit3: float | None = None,
        inverse_time_flag: bool | None = None,
        time_delay1: float | None = None,
        time_delay2: float | None = None,
        time_delay3: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.current_limit1 = current_limit1
        self.current_limit2 = current_limit2
        self.current_limit3 = current_limit3
        self.inverse_time_flag = inverse_time_flag
        self.time_delay1 = time_delay1
        self.time_delay2 = time_delay2
        self.time_delay3 = time_delay3
