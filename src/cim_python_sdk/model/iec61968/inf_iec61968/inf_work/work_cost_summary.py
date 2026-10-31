"""CIM class WorkCostSummary (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail


class WorkCostSummary(WorkDocument):
    """A roll up by cost type for the entire cost of a work order. For example, total labor."""

    __slots__ = ("_work_cost_detail",)

    work_cost_detail: One[WorkCostDetail] = One(
        EndMeta(
            name="work_cost_detail",
            cim_role="WorkCostDetail",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail:WorkCostDetail",
            many=False,
            lower=0,
            upper=1,
            inverse="work_cost_summary",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WorkCostSummary",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{4A747178-90E7-4b6a-9DCD-44FC59138A34}",
        ends=(work_cost_detail.meta,),
    )

    def __init__(
        self,
        *,
        work_cost_detail: WorkCostDetail | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if work_cost_detail is not None:
            self.work_cost_detail = work_cost_detail
