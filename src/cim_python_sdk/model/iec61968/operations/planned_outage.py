"""CIM class PlannedOutage (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.operations.outage import Outage

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.field_dispatch_history import FieldDispatchHistory
    from cim_python_sdk.model.iec61968.operations.operational_updated_rating import (
        OperationalUpdatedRating,
    )
    from cim_python_sdk.model.iec61968.operations.outage_plan import OutagePlan


class PlannedOutage(Outage):
    """CIM class PlannedOutage."""

    __slots__ = ("_field_dispatch_history", "_outage_plan", "_updated_ratings", "reason")

    reason: str | None

    field_dispatch_history: One[FieldDispatchHistory] = One(
        EndMeta(
            name="field_dispatch_history",
            cim_role="FieldDispatchHistory",
            target="cim_python_sdk.model.iec61968.common.field_dispatch_history:FieldDispatchHistory",
            many=False,
            lower=0,
            upper=1,
            inverse="planned_outage",
            aggregation="none",
        )
    )
    updated_ratings: Many[OperationalUpdatedRating] = Many(
        EndMeta(
            name="updated_ratings",
            cim_role="UpdatedRatings",
            target="cim_python_sdk.model.iec61968.operations.operational_updated_rating:OperationalUpdatedRating",
            many=True,
            lower=0,
            upper=None,
            inverse="planned_outage",
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
            inverse="planned_outage",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PlannedOutage",
        package="TC57CIM/IEC61968/Operations",
        guid="{0BCDD7D7-E6DF-41ea-BE54-19C927ADCFF9}",
        attributes=(AttrMeta("reason", "reason", "str", 0, 1, "primitive"),),
        ends=(
            field_dispatch_history.meta,
            updated_ratings.meta,
            outage_plan.meta,
        ),
    )

    def __init__(
        self,
        *,
        reason: str | None = None,
        field_dispatch_history: FieldDispatchHistory | None = None,
        updated_ratings: Iterable[OperationalUpdatedRating] | None = None,
        outage_plan: OutagePlan | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.reason = reason
        if field_dispatch_history is not None:
            self.field_dispatch_history = field_dispatch_history
        if updated_ratings is not None:
            PlannedOutage.updated_ratings.extend(self, updated_ratings)
        if outage_plan is not None:
            self.outage_plan = outage_plan

    def add_updated_rating(self, updated_rating: OperationalUpdatedRating) -> Self:
        return PlannedOutage.updated_ratings.add(self, updated_rating)

    def remove_updated_rating(self, updated_rating: OperationalUpdatedRating) -> Self:
        return PlannedOutage.updated_ratings.remove(self, updated_rating)

    def clear_updated_ratings(self) -> Self:
        return PlannedOutage.updated_ratings.clear(self)

    def num_updated_rating(self) -> int:
        return PlannedOutage.updated_ratings.count(self)

    def get_updated_rating_by_mrid(self, mrid: str) -> OperationalUpdatedRating | None:
        return PlannedOutage.updated_ratings.get_by_mrid(self, mrid)
