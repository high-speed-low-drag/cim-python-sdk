"""CIM class SwitchSchedule (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.load_model.season_day_type_schedule import (
    SeasonDayTypeSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.switch import Switch


class SwitchSchedule(SeasonDayTypeSchedule):
    """A schedule of switch positions. If RegularTimePoint.value1 is 0, the switch is open. If
    1, the switch is closed."""

    __slots__ = ("_switch",)

    switch: One[Switch] = One(
        EndMeta(
            name="switch",
            cim_role="Switch",
            target="cim_python_sdk.model.iec61970.base.wires.switch:Switch",
            many=False,
            lower=1,
            upper=1,
            inverse="switch_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchSchedule",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{3C7AD112-5779-4f2a-8A87-ABB7FBA99EBF}",
        ends=(switch.meta,),
    )

    def __init__(
        self,
        *,
        switch: Switch | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if switch is not None:
            self.switch = switch
