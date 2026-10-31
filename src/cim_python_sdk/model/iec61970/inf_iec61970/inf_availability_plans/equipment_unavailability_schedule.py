"""CIM class EquipmentUnavailabilitySchedule (TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailability_switch_action import (
        UnavailabilitySwitchAction,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailablity_schedule import (
        UnavailablitySchedule,
    )


class EquipmentUnavailabilitySchedule(IdentifiedObject):
    """CIM class EquipmentUnavailabilitySchedule."""

    __slots__ = ("_equipment", "_unavailability_switch_actions", "_unavailablity_schedule")

    unavailability_switch_actions: Many[UnavailabilitySwitchAction] = Many(
        EndMeta(
            name="unavailability_switch_actions",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailability_switch_action:UnavailabilitySwitchAction",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment_unavailability_schedule",
            aggregation="none",
        )
    )
    equipment: One[Equipment] = One(
        EndMeta(
            name="equipment",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=False,
            lower=0,
            upper=1,
            inverse="equipment_unavailability_schedules",
            aggregation="none",
        )
    )
    unavailablity_schedule: One[UnavailablitySchedule] = One(
        EndMeta(
            name="unavailablity_schedule",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailablity_schedule:UnavailablitySchedule",
            many=False,
            lower=1,
            upper=1,
            inverse="equipment_unavailability_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EquipmentUnavailabilitySchedule",
        package="TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans",
        guid="{B7828F5D-2ACC-425f-8E67-D4C050E46EEE}",
        ends=(
            unavailability_switch_actions.meta,
            equipment.meta,
            unavailablity_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        unavailability_switch_actions: Iterable[UnavailabilitySwitchAction] | None = None,
        equipment: Equipment | None = None,
        unavailablity_schedule: UnavailablitySchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if unavailability_switch_actions is not None:
            EquipmentUnavailabilitySchedule.unavailability_switch_actions.extend(
                self, unavailability_switch_actions
            )
        if equipment is not None:
            self.equipment = equipment
        if unavailablity_schedule is not None:
            self.unavailablity_schedule = unavailablity_schedule

    def add_unavailability_switch_action(
        self, unavailability_switch_action: UnavailabilitySwitchAction
    ) -> Self:
        return EquipmentUnavailabilitySchedule.unavailability_switch_actions.add(
            self, unavailability_switch_action
        )

    def remove_unavailability_switch_action(
        self, unavailability_switch_action: UnavailabilitySwitchAction
    ) -> Self:
        return EquipmentUnavailabilitySchedule.unavailability_switch_actions.remove(
            self, unavailability_switch_action
        )

    def clear_unavailability_switch_actions(self) -> Self:
        return EquipmentUnavailabilitySchedule.unavailability_switch_actions.clear(self)

    def num_unavailability_switch_action(self) -> int:
        return EquipmentUnavailabilitySchedule.unavailability_switch_actions.count(self)

    def get_unavailability_switch_action_by_mrid(
        self, mrid: str
    ) -> UnavailabilitySwitchAction | None:
        return EquipmentUnavailabilitySchedule.unavailability_switch_actions.get_by_mrid(self, mrid)
