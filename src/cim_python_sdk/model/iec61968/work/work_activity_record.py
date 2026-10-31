"""CIM class WorkActivityRecord (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.work.base_work import BaseWork


class WorkActivityRecord(ActivityRecord):
    """Records information about the status of work or work task at a point in time."""

    __slots__ = ("_base_work", "percent_complete")

    percent_complete: float | None  # PerCent

    base_work: One[BaseWork] = One(
        EndMeta(
            name="base_work",
            cim_role="BaseWork",
            target="cim_python_sdk.model.iec61968.work.base_work:BaseWork",
            many=False,
            lower=0,
            upper=1,
            inverse="work_activity_records",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WorkActivityRecord",
        package="TC57CIM/IEC61968/Work",
        guid="{3EF37F50-3992-4300-A522-C3799AEA62EE}",
        attributes=(
            AttrMeta("percent_complete", "percentComplete", "PerCent", 0, 1, "cimdatatype"),
        ),
        ends=(base_work.meta,),
    )

    def __init__(
        self,
        *,
        percent_complete: float | None = None,
        base_work: BaseWork | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.percent_complete = percent_complete
        if base_work is not None:
            self.base_work = base_work
