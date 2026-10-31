"""CIM class Capability (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.craft import Craft
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew import OldCrew
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class Capability(WorkIdentifiedObject):
    """Capabilities of a crew."""

    __slots__ = (
        "_crafts",
        "_crew",
        "_work_tasks",
        "performance_factor",
        "status",
        "type",
        "validity_interval",
    )

    type: str | None
    validity_interval: DateTimeInterval | None
    performance_factor: str | None
    status: Status | None

    crafts: Many[Craft] = Many(
        EndMeta(
            name="crafts",
            cim_role="Crafts",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.craft:Craft",
            many=True,
            lower=0,
            upper=None,
            inverse="capabilities",
            aggregation="none",
        )
    )
    work_tasks: Many[OldWorkTask] = Many(
        EndMeta(
            name="work_tasks",
            cim_role="WorkTasks",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task:OldWorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="capabilities",
            aggregation="none",
        )
    )
    crew: One[OldCrew] = One(
        EndMeta(
            name="crew",
            cim_role="Crew",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew:OldCrew",
            many=False,
            lower=0,
            upper=1,
            inverse="capabilities",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Capability",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{7620D5D2-6E91-4d2e-A316-706E8B4EA0C3}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("validity_interval", "validityInterval", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("performance_factor", "performanceFactor", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            crafts.meta,
            work_tasks.meta,
            crew.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        validity_interval: DateTimeInterval | None = None,
        performance_factor: str | None = None,
        status: Status | None = None,
        crafts: Iterable[Craft] | None = None,
        work_tasks: Iterable[OldWorkTask] | None = None,
        crew: OldCrew | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.validity_interval = validity_interval
        self.performance_factor = performance_factor
        self.status = status
        if crafts is not None:
            Capability.crafts.extend(self, crafts)
        if work_tasks is not None:
            Capability.work_tasks.extend(self, work_tasks)
        if crew is not None:
            self.crew = crew

    def add_craft(self, craft: Craft) -> Self:
        return Capability.crafts.add(self, craft)

    def remove_craft(self, craft: Craft) -> Self:
        return Capability.crafts.remove(self, craft)

    def clear_crafts(self) -> Self:
        return Capability.crafts.clear(self)

    def num_craft(self) -> int:
        return Capability.crafts.count(self)

    def get_craft_by_mrid(self, mrid: str) -> Craft | None:
        return Capability.crafts.get_by_mrid(self, mrid)

    def add_work_task(self, work_task: OldWorkTask) -> Self:
        return Capability.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: OldWorkTask) -> Self:
        return Capability.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return Capability.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return Capability.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> OldWorkTask | None:
        return Capability.work_tasks.get_by_mrid(self, mrid)
