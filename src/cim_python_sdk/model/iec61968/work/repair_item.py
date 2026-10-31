"""CIM class RepairItem (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.work.breaker_repair_item_kind import BreakerRepairItemKind
    from cim_python_sdk.model.iec61968.work.repair_work_task import RepairWorkTask
    from cim_python_sdk.model.iec61968.work.transformer_repair_item_kind import (
        TransformerRepairItemKind,
    )


class RepairItem(CimObject):
    """Asset component to be repaired or problem area to be corrected."""

    __slots__ = ("_repair_work_task", "breaker_repair_item", "transformer_repair_item")

    breaker_repair_item: BreakerRepairItemKind | None
    transformer_repair_item: TransformerRepairItemKind | None

    repair_work_task: Many[RepairWorkTask] = Many(
        EndMeta(
            name="repair_work_task",
            cim_role="RepairWorkTask",
            target="cim_python_sdk.model.iec61968.work.repair_work_task:RepairWorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="breaker_repair_item",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RepairItem",
        package="TC57CIM/IEC61968/Work",
        guid="{6A3C3555-E931-4806-8142-46836248309A}",
        attributes=(
            AttrMeta(
                "breaker_repair_item",
                "breakerRepairItem",
                "BreakerRepairItemKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "transformer_repair_item",
                "transformerRepairItem",
                "TransformerRepairItemKind",
                0,
                1,
                "enumeration",
            ),
        ),
        ends=(repair_work_task.meta,),
    )

    def __init__(
        self,
        *,
        breaker_repair_item: BreakerRepairItemKind | None = None,
        transformer_repair_item: TransformerRepairItemKind | None = None,
        repair_work_task: Iterable[RepairWorkTask] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.breaker_repair_item = breaker_repair_item
        self.transformer_repair_item = transformer_repair_item
        if repair_work_task is not None:
            RepairItem.repair_work_task.extend(self, repair_work_task)

    def add_repair_work_task(self, repair_work_task: RepairWorkTask) -> Self:
        return RepairItem.repair_work_task.add(self, repair_work_task)

    def remove_repair_work_task(self, repair_work_task: RepairWorkTask) -> Self:
        return RepairItem.repair_work_task.remove(self, repair_work_task)

    def clear_repair_work_task(self) -> Self:
        return RepairItem.repair_work_task.clear(self)

    def num_repair_work_task(self) -> int:
        return RepairItem.repair_work_task.count(self)

    def get_repair_work_task_by_mrid(self, mrid: str) -> RepairWorkTask | None:
        return RepairItem.repair_work_task.get_by_mrid(self, mrid)
