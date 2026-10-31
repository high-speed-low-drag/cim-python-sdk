"""CIM class OutagePlan (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.operations.outage_order import OutageOrder
    from cim_python_sdk.model.iec61968.operations.planned_outage import PlannedOutage
    from cim_python_sdk.model.iec61968.operations.switching_plan import SwitchingPlan
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class OutagePlan(Document):
    """Document containing the definition of planned outages of equipment and/or usage points.
    It will reference switching plans that are used to execute the planned outage."""

    __slots__ = (
        "_customer",
        "_outage_order",
        "_planned_outage",
        "_switching_plan",
        "approved_date_time",
        "cancelled_date_time",
        "planned_period",
        "purpose",
    )

    cancelled_date_time: _dt.datetime | None
    purpose: str | None
    planned_period: DateTimeInterval | None
    approved_date_time: _dt.datetime | None

    switching_plan: One[SwitchingPlan] = One(
        EndMeta(
            name="switching_plan",
            cim_role="SwitchingPlan",
            target="cim_python_sdk.model.iec61968.operations.switching_plan:SwitchingPlan",
            many=False,
            lower=0,
            upper=1,
            inverse="outage_plan",
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
            inverse="outage_plan",
            aggregation="none",
        )
    )
    outage_order: One[OutageOrder] = One(
        EndMeta(
            name="outage_order",
            cim_role="OutageOrder",
            target="cim_python_sdk.model.iec61968.operations.outage_order:OutageOrder",
            many=False,
            lower=0,
            upper=1,
            inverse="outage_plan",
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
            inverse="outage_plan",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OutagePlan",
        package="TC57CIM/IEC61968/Operations",
        guid="{ACA48F97-FA05-4c4d-94AA-226E14FA7E5C}",
        attributes=(
            AttrMeta("cancelled_date_time", "cancelledDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("purpose", "purpose", "str", 0, 1, "primitive"),
            AttrMeta("planned_period", "plannedPeriod", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("approved_date_time", "approvedDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            switching_plan.meta,
            customer.meta,
            outage_order.meta,
            planned_outage.meta,
        ),
    )

    def __init__(
        self,
        *,
        cancelled_date_time: _dt.datetime | None = None,
        purpose: str | None = None,
        planned_period: DateTimeInterval | None = None,
        approved_date_time: _dt.datetime | None = None,
        switching_plan: SwitchingPlan | None = None,
        customer: Iterable[Customer] | None = None,
        outage_order: OutageOrder | None = None,
        planned_outage: PlannedOutage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cancelled_date_time = cancelled_date_time
        self.purpose = purpose
        self.planned_period = planned_period
        self.approved_date_time = approved_date_time
        if switching_plan is not None:
            self.switching_plan = switching_plan
        if customer is not None:
            OutagePlan.customer.extend(self, customer)
        if outage_order is not None:
            self.outage_order = outage_order
        if planned_outage is not None:
            self.planned_outage = planned_outage

    def add_customer(self, customer: Customer) -> Self:
        return OutagePlan.customer.add(self, customer)

    def remove_customer(self, customer: Customer) -> Self:
        return OutagePlan.customer.remove(self, customer)

    def clear_customer(self) -> Self:
        return OutagePlan.customer.clear(self)

    def num_customer(self) -> int:
        return OutagePlan.customer.count(self)

    def get_customer_by_mrid(self, mrid: str) -> Customer | None:
        return OutagePlan.customer.get_by_mrid(self, mrid)
