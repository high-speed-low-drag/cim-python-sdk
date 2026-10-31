"""CIM class SwitchingOrder (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.operations.switching_plan import SwitchingPlan
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class SwitchingOrder(Document):
    """Transmits a switching plan to a crew in order for the plan to be executed."""

    __slots__ = ("_location", "_switching_plan", "planned_execution_interval")

    comment: str | None
    planned_execution_interval: DateTimeInterval | None

    location: Many[Location] = Many(
        EndMeta(
            name="location",
            cim_role="Location",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=True,
            lower=0,
            upper=None,
            inverse="switching_order",
            aggregation="none",
        )
    )
    switching_plan: One[SwitchingPlan] = One(
        EndMeta(
            name="switching_plan",
            cim_role="SwitchingPlan",
            target="cim_python_sdk.model.iec61968.operations.switching_plan:SwitchingPlan",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_order",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchingOrder",
        package="TC57CIM/IEC61968/Operations",
        guid="{C75D1EAD-CEA6-450d-9C1A-A5C3AE78911D}",
        attributes=(
            AttrMeta("comment", "comment", "str", 0, 1, "primitive"),
            AttrMeta(
                "planned_execution_interval",
                "plannedExecutionInterval",
                "DateTimeInterval",
                0,
                1,
                "compound",
            ),
        ),
        ends=(
            location.meta,
            switching_plan.meta,
        ),
    )

    def __init__(
        self,
        *,
        comment: str | None = None,
        planned_execution_interval: DateTimeInterval | None = None,
        location: Iterable[Location] | None = None,
        switching_plan: SwitchingPlan | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.comment = comment
        self.planned_execution_interval = planned_execution_interval
        if location is not None:
            SwitchingOrder.location.extend(self, location)
        if switching_plan is not None:
            self.switching_plan = switching_plan

    def add_location(self, location: Location) -> Self:
        return SwitchingOrder.location.add(self, location)

    def remove_location(self, location: Location) -> Self:
        return SwitchingOrder.location.remove(self, location)

    def clear_location(self) -> Self:
        return SwitchingOrder.location.clear(self)

    def num_location(self) -> int:
        return SwitchingOrder.location.count(self)

    def get_location_by_mrid(self, mrid: str) -> Location | None:
        return SwitchingOrder.location.get_by_mrid(self, mrid)
