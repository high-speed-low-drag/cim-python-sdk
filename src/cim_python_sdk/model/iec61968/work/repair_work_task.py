"""CIM class RepairWorkTask (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.work.work_task import WorkTask

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.work.repair_item import RepairItem


class RepairWorkTask(WorkTask):
    """Work task for asset repair. Costs associated with this are considered corrective
    maintenance (CM) costs."""

    __slots__ = ("_breaker_repair_item", "emergency")

    emergency: bool | None

    breaker_repair_item: Many[RepairItem] = Many(
        EndMeta(
            name="breaker_repair_item",
            cim_role="BreakerRepairItem",
            target="cim_python_sdk.model.iec61968.work.repair_item:RepairItem",
            many=True,
            lower=0,
            upper=None,
            inverse="repair_work_task",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RepairWorkTask",
        package="TC57CIM/IEC61968/Work",
        guid="{827FA145-0271-4e69-A97A-ABC22B89391F}",
        attributes=(AttrMeta("emergency", "emergency", "bool", 0, 1, "primitive"),),
        ends=(breaker_repair_item.meta,),
    )

    def __init__(
        self,
        *,
        emergency: bool | None = None,
        breaker_repair_item: Iterable[RepairItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.emergency = emergency
        if breaker_repair_item is not None:
            RepairWorkTask.breaker_repair_item.extend(self, breaker_repair_item)

    def add_breaker_repair_item(self, breaker_repair_item: RepairItem) -> Self:
        return RepairWorkTask.breaker_repair_item.add(self, breaker_repair_item)

    def remove_breaker_repair_item(self, breaker_repair_item: RepairItem) -> Self:
        return RepairWorkTask.breaker_repair_item.remove(self, breaker_repair_item)

    def clear_breaker_repair_item(self) -> Self:
        return RepairWorkTask.breaker_repair_item.clear(self)

    def num_breaker_repair_item(self) -> int:
        return RepairWorkTask.breaker_repair_item.count(self)
