"""CIM class CurrentScheduledInterchange (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.internal_control_area import (
        InternalControlArea,
    )


class CurrentScheduledInterchange(CimObject):
    """Control area current net tie (scheduled interchange) sent to real time dispatch."""

    __slots__ = ("_internal_control_area", "current_net_tie_mw", "use_emergency_schedule")

    current_net_tie_mw: float | None
    use_emergency_schedule: bool | None

    internal_control_area: One[InternalControlArea] = One(
        EndMeta(
            name="internal_control_area",
            cim_role="InternalControlArea",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.internal_control_area:InternalControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="current_scheduled_interchange",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CurrentScheduledInterchange",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{AAA6979C-B99A-4b9c-9C68-79BCB4C539AF}",
        attributes=(
            AttrMeta("current_net_tie_mw", "currentNetTieMW", "float", 0, 1, "primitive"),
            AttrMeta("use_emergency_schedule", "useEmergencySchedule", "bool", 0, 1, "primitive"),
        ),
        ends=(internal_control_area.meta,),
    )

    def __init__(
        self,
        *,
        current_net_tie_mw: float | None = None,
        use_emergency_schedule: bool | None = None,
        internal_control_area: InternalControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.current_net_tie_mw = current_net_tie_mw
        self.use_emergency_schedule = use_emergency_schedule
        if internal_control_area is not None:
            self.internal_control_area = internal_control_area
