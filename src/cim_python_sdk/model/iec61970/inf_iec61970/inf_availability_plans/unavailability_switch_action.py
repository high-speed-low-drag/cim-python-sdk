"""CIM class UnavailabilitySwitchAction (TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.switch import Switch
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.equipment_unavailability_schedule import (
        EquipmentUnavailabilitySchedule,
    )


class UnavailabilitySwitchAction(IdentifiedObject):
    """Relevant switching action for supporting the availability (or unavailability) plans.
    This could open or close a switch that is not directly connected to the unavailable
    equipment ."""

    __slots__ = ("_equipment_unavailability_schedule", "_switch", "open")

    open: bool | None

    switch: One[Switch] = One(
        EndMeta(
            name="switch",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.base.wires.switch:Switch",
            many=False,
            lower=1,
            upper=1,
            inverse="unavailability_switch_actions",
            aggregation="none",
        )
    )
    equipment_unavailability_schedule: One[EquipmentUnavailabilitySchedule] = One(
        EndMeta(
            name="equipment_unavailability_schedule",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.equipment_unavailability_schedule:EquipmentUnavailabilitySchedule",
            many=False,
            lower=1,
            upper=1,
            inverse="unavailability_switch_actions",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UnavailabilitySwitchAction",
        package="TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans",
        guid="{C46CA7EF-4F22-4fb4-B39C-F71193CAE3AE}",
        attributes=(AttrMeta("open", "open", "bool", 0, 1, "primitive"),),
        ends=(
            switch.meta,
            equipment_unavailability_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        open: bool | None = None,
        switch: Switch | None = None,
        equipment_unavailability_schedule: EquipmentUnavailabilitySchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.open = open
        if switch is not None:
            self.switch = switch
        if equipment_unavailability_schedule is not None:
            self.equipment_unavailability_schedule = equipment_unavailability_schedule
