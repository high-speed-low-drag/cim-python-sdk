"""CIM class ContractorItem (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable import ErpPayable
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail


class ContractorItem(WorkIdentifiedObject):
    """Contractor information for work task."""

    __slots__ = (
        "_erp_payables",
        "_work_cost_detail",
        "_work_task",
        "activity_code",
        "bid_amount",
        "cost",
        "status",
    )

    activity_code: str | None
    bid_amount: _decimal.Decimal | None  # Money
    cost: _decimal.Decimal | None  # Money
    status: Status | None

    work_task: One[OldWorkTask] = One(
        EndMeta(
            name="work_task",
            cim_role="WorkTask",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task:OldWorkTask",
            many=False,
            lower=0,
            upper=1,
            inverse="contractor_items",
            aggregation="none",
        )
    )
    work_cost_detail: One[WorkCostDetail] = One(
        EndMeta(
            name="work_cost_detail",
            cim_role="WorkCostDetail",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail:WorkCostDetail",
            many=False,
            lower=1,
            upper=1,
            inverse="contractor_items",
            aggregation="none",
        )
    )
    erp_payables: Many[ErpPayable] = Many(
        EndMeta(
            name="erp_payables",
            cim_role="ErpPayables",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable:ErpPayable",
            many=True,
            lower=0,
            upper=None,
            inverse="contractor_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ContractorItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{5B20C21D-1D33-446d-B8E8-8F3096006156}",
        attributes=(
            AttrMeta("activity_code", "activityCode", "str", 0, 1, "primitive"),
            AttrMeta("bid_amount", "bidAmount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("cost", "cost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            work_task.meta,
            work_cost_detail.meta,
            erp_payables.meta,
        ),
    )

    def __init__(
        self,
        *,
        activity_code: str | None = None,
        bid_amount: _decimal.Decimal | None = None,
        cost: _decimal.Decimal | None = None,
        status: Status | None = None,
        work_task: OldWorkTask | None = None,
        work_cost_detail: WorkCostDetail | None = None,
        erp_payables: Iterable[ErpPayable] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.activity_code = activity_code
        self.bid_amount = bid_amount
        self.cost = cost
        self.status = status
        if work_task is not None:
            self.work_task = work_task
        if work_cost_detail is not None:
            self.work_cost_detail = work_cost_detail
        if erp_payables is not None:
            ContractorItem.erp_payables.extend(self, erp_payables)

    def add_erp_payable(self, erp_payable: ErpPayable) -> Self:
        return ContractorItem.erp_payables.add(self, erp_payable)

    def remove_erp_payable(self, erp_payable: ErpPayable) -> Self:
        return ContractorItem.erp_payables.remove(self, erp_payable)

    def clear_erp_payables(self) -> Self:
        return ContractorItem.erp_payables.clear(self)

    def num_erp_payable(self) -> int:
        return ContractorItem.erp_payables.count(self)

    def get_erp_payable_by_mrid(self, mrid: str) -> ErpPayable | None:
        return ContractorItem.erp_payables.get_by_mrid(self, mrid)
