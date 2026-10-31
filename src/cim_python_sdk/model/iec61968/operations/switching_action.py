"""CIM class SwitchingAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.crew import Crew
    from cim_python_sdk.model.iec61968.common.operator import Operator
    from cim_python_sdk.model.iec61968.operations.switching_event import SwitchingEvent
    from cim_python_sdk.model.iec61968.operations.switching_plan import SwitchingPlan
    from cim_python_sdk.model.iec61968.operations.switching_step import SwitchingStep
    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode


class SwitchingAction(IdentifiedObject):
    """Atomic switching action."""

    __slots__ = (
        "_crew",
        "_operator",
        "_switching_event",
        "_switching_plan",
        "_switching_step",
        "executed_date_time",
        "issued_date_time",
        "phases",
        "planned_date_time",
    )

    planned_date_time: _dt.datetime | None
    executed_date_time: _dt.datetime | None
    phases: PhaseCode | None
    issued_date_time: _dt.datetime | None

    switching_plan: One[SwitchingPlan] = One(
        EndMeta(
            name="switching_plan",
            cim_role="SwitchingPlan",
            target="cim_python_sdk.model.iec61968.operations.switching_plan:SwitchingPlan",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_action",
            aggregation="none",
        )
    )
    operator: One[Operator] = One(
        EndMeta(
            name="operator",
            cim_role="Operator",
            target="cim_python_sdk.model.iec61968.common.operator:Operator",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_steps",
            aggregation="none",
        )
    )
    crew: Many[Crew] = Many(
        EndMeta(
            name="crew",
            cim_role="Crew",
            target="cim_python_sdk.model.iec61968.common.crew:Crew",
            many=True,
            lower=0,
            upper=None,
            inverse="switching_action",
            aggregation="none",
        )
    )
    switching_step: One[SwitchingStep] = One(
        EndMeta(
            name="switching_step",
            cim_role="SwitchingStep",
            target="cim_python_sdk.model.iec61968.operations.switching_step:SwitchingStep",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_action",
            aggregation="none",
        )
    )
    switching_event: One[SwitchingEvent] = One(
        EndMeta(
            name="switching_event",
            cim_role="SwitchingEvent",
            target="cim_python_sdk.model.iec61968.operations.switching_event:SwitchingEvent",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchingAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{71CB75D5-6E45-4438-90A2-B15C918B1BB3}",
        attributes=(
            AttrMeta("planned_date_time", "plannedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("executed_date_time", "executedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("phases", "phases", "PhaseCode", 0, 1, "enumeration"),
            AttrMeta("issued_date_time", "issuedDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            switching_plan.meta,
            operator.meta,
            crew.meta,
            switching_step.meta,
            switching_event.meta,
        ),
    )

    def __init__(
        self,
        *,
        planned_date_time: _dt.datetime | None = None,
        executed_date_time: _dt.datetime | None = None,
        phases: PhaseCode | None = None,
        issued_date_time: _dt.datetime | None = None,
        switching_plan: SwitchingPlan | None = None,
        operator: Operator | None = None,
        crew: Iterable[Crew] | None = None,
        switching_step: SwitchingStep | None = None,
        switching_event: SwitchingEvent | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.planned_date_time = planned_date_time
        self.executed_date_time = executed_date_time
        self.phases = phases
        self.issued_date_time = issued_date_time
        if switching_plan is not None:
            self.switching_plan = switching_plan
        if operator is not None:
            self.operator = operator
        if crew is not None:
            SwitchingAction.crew.extend(self, crew)
        if switching_step is not None:
            self.switching_step = switching_step
        if switching_event is not None:
            self.switching_event = switching_event

    def add_crew(self, crew: Crew) -> Self:
        return SwitchingAction.crew.add(self, crew)

    def remove_crew(self, crew: Crew) -> Self:
        return SwitchingAction.crew.remove(self, crew)

    def clear_crew(self) -> Self:
        return SwitchingAction.crew.clear(self)

    def num_crew(self) -> int:
        return SwitchingAction.crew.count(self)

    def get_crew_by_mrid(self, mrid: str) -> Crew | None:
        return SwitchingAction.crew.get_by_mrid(self, mrid)
