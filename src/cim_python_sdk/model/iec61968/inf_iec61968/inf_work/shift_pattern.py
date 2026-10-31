"""CIM class ShiftPattern (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew import OldCrew
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class ShiftPattern(WorkIdentifiedObject):
    """The patterns of shifts worked by people or crews."""

    __slots__ = ("_crews", "assignment_type", "cycle_count", "status", "validity_interval")

    assignment_type: str | None
    cycle_count: int | None
    validity_interval: DateTimeInterval | None
    status: Status | None

    crews: Many[OldCrew] = Many(
        EndMeta(
            name="crews",
            cim_role="Crews",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew:OldCrew",
            many=True,
            lower=0,
            upper=None,
            inverse="shift_patterns",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ShiftPattern",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{5D821447-C660-4d55-8241-966E9C8F0359}",
        attributes=(
            AttrMeta("assignment_type", "assignmentType", "str", 0, 1, "primitive"),
            AttrMeta("cycle_count", "cycleCount", "int", 0, 1, "primitive"),
            AttrMeta("validity_interval", "validityInterval", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(crews.meta,),
    )

    def __init__(
        self,
        *,
        assignment_type: str | None = None,
        cycle_count: int | None = None,
        validity_interval: DateTimeInterval | None = None,
        status: Status | None = None,
        crews: Iterable[OldCrew] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.assignment_type = assignment_type
        self.cycle_count = cycle_count
        self.validity_interval = validity_interval
        self.status = status
        if crews is not None:
            ShiftPattern.crews.extend(self, crews)

    def add_crew(self, crew: OldCrew) -> Self:
        return ShiftPattern.crews.add(self, crew)

    def remove_crew(self, crew: OldCrew) -> Self:
        return ShiftPattern.crews.remove(self, crew)

    def clear_crews(self) -> Self:
        return ShiftPattern.crews.clear(self)

    def num_crew(self) -> int:
        return ShiftPattern.crews.count(self)

    def get_crew_by_mrid(self, mrid: str) -> OldCrew | None:
        return ShiftPattern.crews.get_by_mrid(self, mrid)
