"""CIM class Assignment (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew import OldCrew
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class Assignment(WorkDocument):
    """An assignment is given to an ErpPerson, Crew, Organisation, Equipment Item, Tool, etc.
    and may be used to perform Work, WorkTasks, Procedures, etc. TimeSchedules may be set up
    directly for Assignments or indirectly via the associated WorkTask. Note that these
    associations are all inherited through the recursive relationship on Document."""

    __slots__ = ("_crews", "effective_period")

    effective_period: DateTimeInterval | None

    crews: Many[OldCrew] = Many(
        EndMeta(
            name="crews",
            cim_role="Crews",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew:OldCrew",
            many=True,
            lower=0,
            upper=None,
            inverse="assignments",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Assignment",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{DAB328F7-94C5-4470-8228-B5EC63800CD2}",
        attributes=(
            AttrMeta("effective_period", "effectivePeriod", "DateTimeInterval", 0, 1, "compound"),
        ),
        ends=(crews.meta,),
    )

    def __init__(
        self,
        *,
        effective_period: DateTimeInterval | None = None,
        crews: Iterable[OldCrew] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.effective_period = effective_period
        if crews is not None:
            Assignment.crews.extend(self, crews)

    def add_crew(self, crew: OldCrew) -> Self:
        return Assignment.crews.add(self, crew)

    def remove_crew(self, crew: OldCrew) -> Self:
        return Assignment.crews.remove(self, crew)

    def clear_crews(self) -> Self:
        return Assignment.crews.clear(self)

    def num_crew(self) -> int:
        return Assignment.crews.count(self)

    def get_crew_by_mrid(self, mrid: str) -> OldCrew | None:
        return Assignment.crews.get_by_mrid(self, mrid)
