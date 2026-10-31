"""CIM class OutageOrder (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.operations.outage_plan import OutagePlan


class OutageOrder(Document):
    """Transmits an outage plan to a crew in order for the planned outage to be executed."""

    __slots__ = ("_location", "_outage_plan")

    comment: str | None

    location: Many[Location] = Many(
        EndMeta(
            name="location",
            cim_role="Location",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=True,
            lower=0,
            upper=None,
            inverse="outage_order",
            aggregation="none",
        )
    )
    outage_plan: One[OutagePlan] = One(
        EndMeta(
            name="outage_plan",
            cim_role="OutagePlan",
            target="cim_python_sdk.model.iec61968.operations.outage_plan:OutagePlan",
            many=False,
            lower=0,
            upper=1,
            inverse="outage_order",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OutageOrder",
        package="TC57CIM/IEC61968/Operations",
        guid="{E92F410F-17D3-497b-B612-3B1693031AA4}",
        attributes=(AttrMeta("comment", "comment", "str", 0, 1, "primitive"),),
        ends=(
            location.meta,
            outage_plan.meta,
        ),
    )

    def __init__(
        self,
        *,
        comment: str | None = None,
        location: Iterable[Location] | None = None,
        outage_plan: OutagePlan | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.comment = comment
        if location is not None:
            OutageOrder.location.extend(self, location)
        if outage_plan is not None:
            self.outage_plan = outage_plan

    def add_location(self, location: Location) -> Self:
        return OutageOrder.location.add(self, location)

    def remove_location(self, location: Location) -> Self:
        return OutageOrder.location.remove(self, location)

    def clear_location(self) -> Self:
        return OutageOrder.location.clear(self)

    def num_location(self) -> int:
        return OutageOrder.location.count(self)

    def get_location_by_mrid(self, mrid: str) -> Location | None:
        return OutageOrder.location.get_by_mrid(self, mrid)
