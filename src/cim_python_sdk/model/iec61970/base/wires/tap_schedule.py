"""CIM class TapSchedule (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.load_model.season_day_type_schedule import (
    SeasonDayTypeSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.tap_changer import TapChanger


class TapSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a tap step."""

    __slots__ = ("_tap_changer",)

    tap_changer: One[TapChanger] = One(
        EndMeta(
            name="tap_changer",
            cim_role="TapChanger",
            target="cim_python_sdk.model.iec61970.base.wires.tap_changer:TapChanger",
            many=False,
            lower=1,
            upper=1,
            inverse="tap_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TapSchedule",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{204A4D0D-C13F-4c97-BBE8-EEE743ACDA3F}",
        ends=(tap_changer.meta,),
    )

    def __init__(
        self,
        *,
        tap_changer: TapChanger | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if tap_changer is not None:
            self.tap_changer = tap_changer
