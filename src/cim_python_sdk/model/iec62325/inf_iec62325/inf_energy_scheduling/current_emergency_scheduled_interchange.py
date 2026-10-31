"""CIM class CurrentEmergencyScheduledInterchange (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.internal_control_area import (
        InternalControlArea,
    )


class CurrentEmergencyScheduledInterchange(IdentifiedObject):
    """Control area emergency schedules"""

    __slots__ = (
        "_internal_control_area",
        "emergency_schedule_mw",
        "emergency_schedule_ramp_time",
        "emergency_schedule_start_time",
    )

    emergency_schedule_mw: float | None
    emergency_schedule_start_time: _dt.datetime | None
    emergency_schedule_ramp_time: int | None

    internal_control_area: One[InternalControlArea] = One(
        EndMeta(
            name="internal_control_area",
            cim_role="InternalControlArea",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.internal_control_area:InternalControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="current_emergency_si",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CurrentEmergencyScheduledInterchange",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{224611F1-DC22-4b81-933D-EC3B674B1FB8}",
        attributes=(
            AttrMeta("emergency_schedule_mw", "emergencyScheduleMW", "float", 0, 1, "primitive"),
            AttrMeta(
                "emergency_schedule_start_time",
                "emergencyScheduleStartTime",
                "datetime",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "emergency_schedule_ramp_time",
                "emergencyScheduleRampTime",
                "int",
                0,
                1,
                "primitive",
            ),
        ),
        ends=(internal_control_area.meta,),
    )

    def __init__(
        self,
        *,
        emergency_schedule_mw: float | None = None,
        emergency_schedule_start_time: _dt.datetime | None = None,
        emergency_schedule_ramp_time: int | None = None,
        internal_control_area: InternalControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.emergency_schedule_mw = emergency_schedule_mw
        self.emergency_schedule_start_time = emergency_schedule_start_time
        self.emergency_schedule_ramp_time = emergency_schedule_ramp_time
        if internal_control_area is not None:
            self.internal_control_area = internal_control_area
