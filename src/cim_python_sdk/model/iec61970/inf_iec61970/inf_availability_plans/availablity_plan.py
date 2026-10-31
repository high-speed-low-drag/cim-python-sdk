"""CIM class AvailablityPlan (TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailablity_schedule import (
        UnavailablitySchedule,
    )


class AvailablityPlan(IdentifiedObject):
    """The collection of all the availability schedules for a given time range. Only one
    availability plan shall be valid for the same period."""

    __slots__ = ("_unavailablity_schedules", "valid_period")

    valid_period: DateTimeInterval | None

    unavailablity_schedules: Many[UnavailablitySchedule] = Many(
        EndMeta(
            name="unavailablity_schedules",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailablity_schedule:UnavailablitySchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="availablity_plan",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AvailablityPlan",
        package="TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans",
        guid="{00A82713-6144-4fa4-AB22-ABA57C04F3E6}",
        attributes=(AttrMeta("valid_period", "validPeriod", "DateTimeInterval", 0, 1, "compound"),),
        ends=(unavailablity_schedules.meta,),
    )

    def __init__(
        self,
        *,
        valid_period: DateTimeInterval | None = None,
        unavailablity_schedules: Iterable[UnavailablitySchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.valid_period = valid_period
        if unavailablity_schedules is not None:
            AvailablityPlan.unavailablity_schedules.extend(self, unavailablity_schedules)

    def add_unavailablity_schedule(self, unavailablity_schedule: UnavailablitySchedule) -> Self:
        return AvailablityPlan.unavailablity_schedules.add(self, unavailablity_schedule)

    def remove_unavailablity_schedule(self, unavailablity_schedule: UnavailablitySchedule) -> Self:
        return AvailablityPlan.unavailablity_schedules.remove(self, unavailablity_schedule)

    def clear_unavailablity_schedules(self) -> Self:
        return AvailablityPlan.unavailablity_schedules.clear(self)

    def num_unavailablity_schedule(self) -> int:
        return AvailablityPlan.unavailablity_schedules.count(self)

    def get_unavailablity_schedule_by_mrid(self, mrid: str) -> UnavailablitySchedule | None:
        return AvailablityPlan.unavailablity_schedules.get_by_mrid(self, mrid)
