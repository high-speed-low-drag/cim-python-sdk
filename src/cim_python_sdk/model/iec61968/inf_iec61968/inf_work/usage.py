"""CIM class Usage (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask


class Usage(WorkIdentifiedObject):
    """The way material and assets are used to perform a certain type of work task. The way is
    described in text in the inheritied description attribute."""

    __slots__ = ("_work_task", "status")

    status: Status | None

    work_task: One[OldWorkTask] = One(
        EndMeta(
            name="work_task",
            cim_role="WorkTask",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task:OldWorkTask",
            many=False,
            lower=0,
            upper=1,
            inverse="usages",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Usage",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{D7436092-8424-48ae-A4A5-CDD1D549CD31}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(work_task.meta,),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        work_task: OldWorkTask | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if work_task is not None:
            self.work_task = work_task
