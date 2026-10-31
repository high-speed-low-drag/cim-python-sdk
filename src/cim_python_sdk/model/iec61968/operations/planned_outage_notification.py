"""CIM class PlannedOutageNotification (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61968.operations.switching_plan import SwitchingPlan


class PlannedOutageNotification(Document):
    """This class will be used to generate call ahead lists for customers who will be affected
    by a planned outage."""

    __slots__ = ("_customer", "_switching_plan", "_usage_point")

    usage_point: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_point",
            cim_role="UsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="planned_outage_notification",
            aggregation="none",
        )
    )
    customer: Many[Customer] = Many(
        EndMeta(
            name="customer",
            cim_role="Customer",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=True,
            lower=0,
            upper=None,
            inverse="planned_outage_notification",
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
            inverse="planned_outage_notification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PlannedOutageNotification",
        package="TC57CIM/IEC61968/Operations",
        guid="{0F285974-FB1F-4b4b-A71D-C8DB1B4F9389}",
        ends=(
            usage_point.meta,
            customer.meta,
            switching_plan.meta,
        ),
    )

    def __init__(
        self,
        *,
        usage_point: Iterable[UsagePoint] | None = None,
        customer: Iterable[Customer] | None = None,
        switching_plan: SwitchingPlan | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if usage_point is not None:
            PlannedOutageNotification.usage_point.extend(self, usage_point)
        if customer is not None:
            PlannedOutageNotification.customer.extend(self, customer)
        if switching_plan is not None:
            self.switching_plan = switching_plan

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return PlannedOutageNotification.usage_point.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return PlannedOutageNotification.usage_point.remove(self, usage_point)

    def clear_usage_point(self) -> Self:
        return PlannedOutageNotification.usage_point.clear(self)

    def num_usage_point(self) -> int:
        return PlannedOutageNotification.usage_point.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return PlannedOutageNotification.usage_point.get_by_mrid(self, mrid)

    def add_customer(self, customer: Customer) -> Self:
        return PlannedOutageNotification.customer.add(self, customer)

    def remove_customer(self, customer: Customer) -> Self:
        return PlannedOutageNotification.customer.remove(self, customer)

    def clear_customer(self) -> Self:
        return PlannedOutageNotification.customer.clear(self)

    def num_customer(self) -> int:
        return PlannedOutageNotification.customer.count(self)

    def get_customer_by_mrid(self, mrid: str) -> Customer | None:
        return PlannedOutageNotification.customer.get_by_mrid(self, mrid)
