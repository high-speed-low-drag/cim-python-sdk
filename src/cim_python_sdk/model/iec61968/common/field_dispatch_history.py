"""CIM class FieldDispatchHistory (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.crew import Crew
    from cim_python_sdk.model.iec61968.common.field_dispatch_step import FieldDispatchStep
    from cim_python_sdk.model.iec61968.operations.planned_outage import PlannedOutage
    from cim_python_sdk.model.iec61968.operations.unplanned_outage import UnplannedOutage


class FieldDispatchHistory(IdentifiedObject):
    """The history of field dispatch statuses for this work."""

    __slots__ = ("_crew", "_field_dispatch_step", "_planned_outage", "_unplanned_outage")

    field_dispatch_step: Many[FieldDispatchStep] = Many(
        EndMeta(
            name="field_dispatch_step",
            cim_role="FieldDispatchStep",
            target="cim_python_sdk.model.iec61968.common.field_dispatch_step:FieldDispatchStep",
            many=True,
            lower=0,
            upper=None,
            inverse="field_dispatch_history",
            aggregation="none",
        )
    )
    crew: One[Crew] = One(
        EndMeta(
            name="crew",
            cim_role="Crew",
            target="cim_python_sdk.model.iec61968.common.crew:Crew",
            many=False,
            lower=0,
            upper=1,
            inverse="field_dispatch_history",
            aggregation="none",
        )
    )
    planned_outage: One[PlannedOutage] = One(
        EndMeta(
            name="planned_outage",
            cim_role="PlannedOutage",
            target="cim_python_sdk.model.iec61968.operations.planned_outage:PlannedOutage",
            many=False,
            lower=0,
            upper=1,
            inverse="field_dispatch_history",
            aggregation="none",
        )
    )
    unplanned_outage: One[UnplannedOutage] = One(
        EndMeta(
            name="unplanned_outage",
            cim_role="UnplannedOutage",
            target="cim_python_sdk.model.iec61968.operations.unplanned_outage:UnplannedOutage",
            many=False,
            lower=0,
            upper=1,
            inverse="field_dispatch_history",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FieldDispatchHistory",
        package="TC57CIM/IEC61968/Common",
        guid="{6781E967-A300-4e16-825B-50CE206FDC8A}",
        ends=(
            field_dispatch_step.meta,
            crew.meta,
            planned_outage.meta,
            unplanned_outage.meta,
        ),
    )

    def __init__(
        self,
        *,
        field_dispatch_step: Iterable[FieldDispatchStep] | None = None,
        crew: Crew | None = None,
        planned_outage: PlannedOutage | None = None,
        unplanned_outage: UnplannedOutage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if field_dispatch_step is not None:
            FieldDispatchHistory.field_dispatch_step.extend(self, field_dispatch_step)
        if crew is not None:
            self.crew = crew
        if planned_outage is not None:
            self.planned_outage = planned_outage
        if unplanned_outage is not None:
            self.unplanned_outage = unplanned_outage

    def add_field_dispatch_step(self, field_dispatch_step: FieldDispatchStep) -> Self:
        return FieldDispatchHistory.field_dispatch_step.add(self, field_dispatch_step)

    def remove_field_dispatch_step(self, field_dispatch_step: FieldDispatchStep) -> Self:
        return FieldDispatchHistory.field_dispatch_step.remove(self, field_dispatch_step)

    def clear_field_dispatch_step(self) -> Self:
        return FieldDispatchHistory.field_dispatch_step.clear(self)

    def num_field_dispatch_step(self) -> int:
        return FieldDispatchHistory.field_dispatch_step.count(self)
