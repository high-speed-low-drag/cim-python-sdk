"""CIM class SwitchingPlanRequest (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.organisation import Organisation
    from cim_python_sdk.model.iec61968.operations.switching_plan import SwitchingPlan
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class SwitchingPlanRequest(Document):
    """A document used to request that a switching plan be created for a particular purpose."""

    __slots__ = (
        "_requesting_organization",
        "_switching_plan",
        "equipment_to_be_isolated",
        "forward_switching_date_time_interval",
        "grounding_points",
        "isolation_area",
        "isolation_points",
        "outage_date_time_interval",
        "purpose",
        "reverse_switching_date_time_interval",
        "switching_request_details",
    )

    forward_switching_date_time_interval: DateTimeInterval | None
    reverse_switching_date_time_interval: DateTimeInterval | None
    switching_request_details: str | None
    purpose: str | None
    comment: str | None
    isolation_area: str | None
    equipment_to_be_isolated: str | None
    isolation_points: str | None
    grounding_points: str | None
    outage_date_time_interval: DateTimeInterval | None

    switching_plan: Many[SwitchingPlan] = Many(
        EndMeta(
            name="switching_plan",
            cim_role="SwitchingPlan",
            target="cim_python_sdk.model.iec61968.operations.switching_plan:SwitchingPlan",
            many=True,
            lower=0,
            upper=None,
            inverse="switching_plan_request",
            aggregation="none",
        )
    )
    requesting_organization: One[Organisation] = One(
        EndMeta(
            name="requesting_organization",
            cim_role="RequestingOrganization",
            target="cim_python_sdk.model.iec61968.common.organisation:Organisation",
            many=False,
            lower=0,
            upper=1,
            inverse="switching_plan_request",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchingPlanRequest",
        package="TC57CIM/IEC61968/Operations",
        guid="{9551E330-072D-49d3-A419-8EE4560D91F2}",
        attributes=(
            AttrMeta(
                "forward_switching_date_time_interval",
                "forwardSwitchingDateTimeInterval",
                "DateTimeInterval",
                1,
                1,
                "compound",
            ),
            AttrMeta(
                "reverse_switching_date_time_interval",
                "reverseSwitchingDateTimeInterval",
                "DateTimeInterval",
                1,
                1,
                "compound",
            ),
            AttrMeta(
                "switching_request_details", "switchingRequestDetails", "str", 1, 1, "primitive"
            ),
            AttrMeta("purpose", "purpose", "str", 1, 1, "primitive"),
            AttrMeta("comment", "comment", "str", 0, 1, "primitive"),
            AttrMeta("isolation_area", "isolationArea", "str", 0, 1, "primitive"),
            AttrMeta("equipment_to_be_isolated", "equipmentToBeIsolated", "str", 0, 1, "primitive"),
            AttrMeta("isolation_points", "isolationPoints", "str", 0, 1, "primitive"),
            AttrMeta("grounding_points", "groundingPoints", "str", 0, 1, "primitive"),
            AttrMeta(
                "outage_date_time_interval",
                "outageDateTimeInterval",
                "DateTimeInterval",
                0,
                1,
                "compound",
            ),
        ),
        ends=(
            switching_plan.meta,
            requesting_organization.meta,
        ),
    )

    def __init__(
        self,
        *,
        forward_switching_date_time_interval: DateTimeInterval | None = None,
        reverse_switching_date_time_interval: DateTimeInterval | None = None,
        switching_request_details: str | None = None,
        purpose: str | None = None,
        comment: str | None = None,
        isolation_area: str | None = None,
        equipment_to_be_isolated: str | None = None,
        isolation_points: str | None = None,
        grounding_points: str | None = None,
        outage_date_time_interval: DateTimeInterval | None = None,
        switching_plan: Iterable[SwitchingPlan] | None = None,
        requesting_organization: Organisation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.forward_switching_date_time_interval = forward_switching_date_time_interval
        self.reverse_switching_date_time_interval = reverse_switching_date_time_interval
        self.switching_request_details = switching_request_details
        self.purpose = purpose
        self.comment = comment
        self.isolation_area = isolation_area
        self.equipment_to_be_isolated = equipment_to_be_isolated
        self.isolation_points = isolation_points
        self.grounding_points = grounding_points
        self.outage_date_time_interval = outage_date_time_interval
        if switching_plan is not None:
            SwitchingPlanRequest.switching_plan.extend(self, switching_plan)
        if requesting_organization is not None:
            self.requesting_organization = requesting_organization

    def add_switching_plan(self, switching_plan: SwitchingPlan) -> Self:
        return SwitchingPlanRequest.switching_plan.add(self, switching_plan)

    def remove_switching_plan(self, switching_plan: SwitchingPlan) -> Self:
        return SwitchingPlanRequest.switching_plan.remove(self, switching_plan)

    def clear_switching_plan(self) -> Self:
        return SwitchingPlanRequest.switching_plan.clear(self)

    def num_switching_plan(self) -> int:
        return SwitchingPlanRequest.switching_plan.count(self)

    def get_switching_plan_by_mrid(self, mrid: str) -> SwitchingPlan | None:
        return SwitchingPlanRequest.switching_plan.get_by_mrid(self, mrid)
