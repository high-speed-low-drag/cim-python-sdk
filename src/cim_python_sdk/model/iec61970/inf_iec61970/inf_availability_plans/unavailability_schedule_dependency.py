"""CIM class UnavailabilityScheduleDependency (TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailablity_schedule import (
        UnavailablitySchedule,
    )


class UnavailabilityScheduleDependency(IdentifiedObject):
    """CIM class UnavailabilityScheduleDependency."""

    __slots__ = ("_unavailability_schedule_depends_on", "_unavailability_schedule_impacts")

    unavailability_schedule_impacts: One[UnavailablitySchedule] = One(
        EndMeta(
            name="unavailability_schedule_impacts",
            cim_role="UnavailabilityScheduleImpacts",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailablity_schedule:UnavailablitySchedule",
            many=False,
            lower=1,
            upper=1,
            inverse="depends_on",
            aggregation="none",
        )
    )
    unavailability_schedule_depends_on: One[UnavailablitySchedule] = One(
        EndMeta(
            name="unavailability_schedule_depends_on",
            cim_role="UnavailabilityScheduleDependsOn",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailablity_schedule:UnavailablitySchedule",
            many=False,
            lower=1,
            upper=1,
            inverse="impacts",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UnavailabilityScheduleDependency",
        package="TC57CIM/IEC61970/InfIEC61970/InfAvailabilityPlans",
        guid="{E80A0296-8D99-477a-B80C-843C9ACD52D8}",
        ends=(
            unavailability_schedule_impacts.meta,
            unavailability_schedule_depends_on.meta,
        ),
    )

    def __init__(
        self,
        *,
        unavailability_schedule_impacts: UnavailablitySchedule | None = None,
        unavailability_schedule_depends_on: UnavailablitySchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if unavailability_schedule_impacts is not None:
            self.unavailability_schedule_impacts = unavailability_schedule_impacts
        if unavailability_schedule_depends_on is not None:
            self.unavailability_schedule_depends_on = unavailability_schedule_depends_on
