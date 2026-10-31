"""CIM class ConformLoadGroup (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.load_model.load_group import LoadGroup

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.load_model.conform_load import ConformLoad
    from cim_python_sdk.model.iec61970.base.load_model.conform_load_schedule import (
        ConformLoadSchedule,
    )


class ConformLoadGroup(LoadGroup):
    """A group of loads conforming to an allocation pattern."""

    __slots__ = ("_conform_load_schedules", "_energy_consumers")

    energy_consumers: Many[ConformLoad] = Many(
        EndMeta(
            name="energy_consumers",
            cim_role="EnergyConsumers",
            target="cim_python_sdk.model.iec61970.base.load_model.conform_load:ConformLoad",
            many=True,
            lower=0,
            upper=None,
            inverse="load_group",
            aggregation="none",
        )
    )
    conform_load_schedules: Many[ConformLoadSchedule] = Many(
        EndMeta(
            name="conform_load_schedules",
            cim_role="ConformLoadSchedules",
            target="cim_python_sdk.model.iec61970.base.load_model.conform_load_schedule:ConformLoadSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="conform_load_group",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConformLoadGroup",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{AA76C755-C3AC-494a-A8C9-5D006148E811}",
        ends=(
            energy_consumers.meta,
            conform_load_schedules.meta,
        ),
    )

    def __init__(
        self,
        *,
        energy_consumers: Iterable[ConformLoad] | None = None,
        conform_load_schedules: Iterable[ConformLoadSchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if energy_consumers is not None:
            ConformLoadGroup.energy_consumers.extend(self, energy_consumers)
        if conform_load_schedules is not None:
            ConformLoadGroup.conform_load_schedules.extend(self, conform_load_schedules)

    def add_energy_consumer(self, energy_consumer: ConformLoad) -> Self:
        return ConformLoadGroup.energy_consumers.add(self, energy_consumer)

    def remove_energy_consumer(self, energy_consumer: ConformLoad) -> Self:
        return ConformLoadGroup.energy_consumers.remove(self, energy_consumer)

    def clear_energy_consumers(self) -> Self:
        return ConformLoadGroup.energy_consumers.clear(self)

    def num_energy_consumer(self) -> int:
        return ConformLoadGroup.energy_consumers.count(self)

    def get_energy_consumer_by_mrid(self, mrid: str) -> ConformLoad | None:
        return ConformLoadGroup.energy_consumers.get_by_mrid(self, mrid)

    def add_conform_load_schedule(self, conform_load_schedule: ConformLoadSchedule) -> Self:
        return ConformLoadGroup.conform_load_schedules.add(self, conform_load_schedule)

    def remove_conform_load_schedule(self, conform_load_schedule: ConformLoadSchedule) -> Self:
        return ConformLoadGroup.conform_load_schedules.remove(self, conform_load_schedule)

    def clear_conform_load_schedules(self) -> Self:
        return ConformLoadGroup.conform_load_schedules.clear(self)

    def num_conform_load_schedule(self) -> int:
        return ConformLoadGroup.conform_load_schedules.count(self)

    def get_conform_load_schedule_by_mrid(self, mrid: str) -> ConformLoadSchedule | None:
        return ConformLoadGroup.conform_load_schedules.get_by_mrid(self, mrid)
