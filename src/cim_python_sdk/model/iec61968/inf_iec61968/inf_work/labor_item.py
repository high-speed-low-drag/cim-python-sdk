"""CIM class LaborItem (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person import OldPerson
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail


class LaborItem(WorkIdentifiedObject):
    """Labor used for work order."""

    __slots__ = (
        "_erp_persons",
        "_work_cost_detail",
        "_work_task",
        "activity_code",
        "cost",
        "labor_duration",
        "labor_rate",
        "status",
    )

    activity_code: str | None
    labor_duration: float | None  # Hours
    labor_rate: float | None  # CostRate
    cost: _decimal.Decimal | None  # Money
    status: Status | None

    work_cost_detail: One[WorkCostDetail] = One(
        EndMeta(
            name="work_cost_detail",
            cim_role="WorkCostDetail",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail:WorkCostDetail",
            many=False,
            lower=1,
            upper=1,
            inverse="labor_items",
            aggregation="none",
        )
    )
    erp_persons: Many[OldPerson] = Many(
        EndMeta(
            name="erp_persons",
            cim_role="ErpPersons",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person:OldPerson",
            many=True,
            lower=0,
            upper=None,
            inverse="labor_items",
            aggregation="none",
        )
    )
    work_task: One[OldWorkTask] = One(
        EndMeta(
            name="work_task",
            cim_role="WorkTask",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task:OldWorkTask",
            many=False,
            lower=0,
            upper=1,
            inverse="labor_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LaborItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{87B7FAF3-F823-4d17-8C7E-B3C24A3C9829}",
        attributes=(
            AttrMeta("activity_code", "activityCode", "str", 0, 1, "primitive"),
            AttrMeta("labor_duration", "laborDuration", "Hours", 0, 1, "cimdatatype"),
            AttrMeta("labor_rate", "laborRate", "CostRate", 0, 1, "cimdatatype"),
            AttrMeta("cost", "cost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            work_cost_detail.meta,
            erp_persons.meta,
            work_task.meta,
        ),
    )

    def __init__(
        self,
        *,
        activity_code: str | None = None,
        labor_duration: float | None = None,
        labor_rate: float | None = None,
        cost: _decimal.Decimal | None = None,
        status: Status | None = None,
        work_cost_detail: WorkCostDetail | None = None,
        erp_persons: Iterable[OldPerson] | None = None,
        work_task: OldWorkTask | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.activity_code = activity_code
        self.labor_duration = labor_duration
        self.labor_rate = labor_rate
        self.cost = cost
        self.status = status
        if work_cost_detail is not None:
            self.work_cost_detail = work_cost_detail
        if erp_persons is not None:
            LaborItem.erp_persons.extend(self, erp_persons)
        if work_task is not None:
            self.work_task = work_task

    def add_erp_person(self, erp_person: OldPerson) -> Self:
        return LaborItem.erp_persons.add(self, erp_person)

    def remove_erp_person(self, erp_person: OldPerson) -> Self:
        return LaborItem.erp_persons.remove(self, erp_person)

    def clear_erp_persons(self) -> Self:
        return LaborItem.erp_persons.clear(self)

    def num_erp_person(self) -> int:
        return LaborItem.erp_persons.count(self)

    def get_erp_person_by_mrid(self, mrid: str) -> OldPerson | None:
        return LaborItem.erp_persons.get_by_mrid(self, mrid)
