"""CIM class UnavailablitySchedule (TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.availablity_plan import (
        AvailablityPlan,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.equipment_unavailability_schedule import (
        EquipmentUnavailabilitySchedule,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailability_schedule_dependency import (
        UnavailabilityScheduleDependency,
    )


class UnavailablitySchedule(IdentifiedObject):
    """A schedule of unavailability for one or more specified equipment that need to follow the
    same scheduling periods."""

    __slots__ = (
        "_availablity_plan",
        "_depends_on",
        "_equipment_unavailability_schedules",
        "_impacts",
    )

    depends_on: Many[UnavailabilityScheduleDependency] = Many(
        EndMeta(
            name="depends_on",
            cim_role="DependsOn",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailability_schedule_dependency:UnavailabilityScheduleDependency",
            many=True,
            lower=0,
            upper=None,
            inverse="unavailability_schedule_impacts",
            aggregation="none",
        )
    )
    impacts: Many[UnavailabilityScheduleDependency] = Many(
        EndMeta(
            name="impacts",
            cim_role="Impacts",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailability_schedule_dependency:UnavailabilityScheduleDependency",
            many=True,
            lower=0,
            upper=None,
            inverse="unavailability_schedule_depends_on",
            aggregation="none",
        )
    )
    availablity_plan: One[AvailablityPlan] = One(
        EndMeta(
            name="availablity_plan",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.availablity_plan:AvailablityPlan",
            many=False,
            lower=0,
            upper=1,
            inverse="unavailablity_schedules",
            aggregation="none",
        )
    )
    equipment_unavailability_schedules: Many[EquipmentUnavailabilitySchedule] = Many(
        EndMeta(
            name="equipment_unavailability_schedules",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.equipment_unavailability_schedule:EquipmentUnavailabilitySchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="unavailablity_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UnavailablitySchedule",
        package="TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans",
        guid="{0495DBAE-5061-4469-954B-91269347261E}",
        ends=(
            depends_on.meta,
            impacts.meta,
            availablity_plan.meta,
            equipment_unavailability_schedules.meta,
        ),
    )

    def __init__(
        self,
        *,
        depends_on: Iterable[UnavailabilityScheduleDependency] | None = None,
        impacts: Iterable[UnavailabilityScheduleDependency] | None = None,
        availablity_plan: AvailablityPlan | None = None,
        equipment_unavailability_schedules: Iterable[EquipmentUnavailabilitySchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if depends_on is not None:
            UnavailablitySchedule.depends_on.extend(self, depends_on)
        if impacts is not None:
            UnavailablitySchedule.impacts.extend(self, impacts)
        if availablity_plan is not None:
            self.availablity_plan = availablity_plan
        if equipment_unavailability_schedules is not None:
            UnavailablitySchedule.equipment_unavailability_schedules.extend(
                self, equipment_unavailability_schedules
            )

    def add_depends_on(self, depends_on: UnavailabilityScheduleDependency) -> Self:
        return UnavailablitySchedule.depends_on.add(self, depends_on)

    def remove_depends_on(self, depends_on: UnavailabilityScheduleDependency) -> Self:
        return UnavailablitySchedule.depends_on.remove(self, depends_on)

    def clear_depends_on(self) -> Self:
        return UnavailablitySchedule.depends_on.clear(self)

    def num_depends_on(self) -> int:
        return UnavailablitySchedule.depends_on.count(self)

    def get_depends_on_by_mrid(self, mrid: str) -> UnavailabilityScheduleDependency | None:
        return UnavailablitySchedule.depends_on.get_by_mrid(self, mrid)

    def add_impact(self, impact: UnavailabilityScheduleDependency) -> Self:
        return UnavailablitySchedule.impacts.add(self, impact)

    def remove_impact(self, impact: UnavailabilityScheduleDependency) -> Self:
        return UnavailablitySchedule.impacts.remove(self, impact)

    def clear_impacts(self) -> Self:
        return UnavailablitySchedule.impacts.clear(self)

    def num_impact(self) -> int:
        return UnavailablitySchedule.impacts.count(self)

    def get_impact_by_mrid(self, mrid: str) -> UnavailabilityScheduleDependency | None:
        return UnavailablitySchedule.impacts.get_by_mrid(self, mrid)

    def add_equipment_unavailability_schedule(
        self, equipment_unavailability_schedule: EquipmentUnavailabilitySchedule
    ) -> Self:
        return UnavailablitySchedule.equipment_unavailability_schedules.add(
            self, equipment_unavailability_schedule
        )

    def remove_equipment_unavailability_schedule(
        self, equipment_unavailability_schedule: EquipmentUnavailabilitySchedule
    ) -> Self:
        return UnavailablitySchedule.equipment_unavailability_schedules.remove(
            self, equipment_unavailability_schedule
        )

    def clear_equipment_unavailability_schedules(self) -> Self:
        return UnavailablitySchedule.equipment_unavailability_schedules.clear(self)

    def num_equipment_unavailability_schedule(self) -> int:
        return UnavailablitySchedule.equipment_unavailability_schedules.count(self)

    def get_equipment_unavailability_schedule_by_mrid(
        self, mrid: str
    ) -> EquipmentUnavailabilitySchedule | None:
        return UnavailablitySchedule.equipment_unavailability_schedules.get_by_mrid(self, mrid)
