"""CIM class NonConformLoadGroup (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.load_model.load_group import LoadGroup

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.load_model.non_conform_load import NonConformLoad
    from cim_python_sdk.model.iec61970.base.load_model.non_conform_load_schedule import (
        NonConformLoadSchedule,
    )


class NonConformLoadGroup(LoadGroup):
    """Loads that do not follow a daily and seasonal load variation pattern."""

    __slots__ = ("_energy_consumers", "_non_conform_load_schedules")

    non_conform_load_schedules: Many[NonConformLoadSchedule] = Many(
        EndMeta(
            name="non_conform_load_schedules",
            cim_role="NonConformLoadSchedules",
            target="cim_python_sdk.model.iec61970.base.load_model.non_conform_load_schedule:NonConformLoadSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="non_conform_load_group",
            aggregation="shared",
        )
    )
    energy_consumers: Many[NonConformLoad] = Many(
        EndMeta(
            name="energy_consumers",
            cim_role="EnergyConsumers",
            target="cim_python_sdk.model.iec61970.base.load_model.non_conform_load:NonConformLoad",
            many=True,
            lower=0,
            upper=None,
            inverse="load_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NonConformLoadGroup",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{BE40965D-042B-4901-9F5D-DED85218AF51}",
        ends=(
            non_conform_load_schedules.meta,
            energy_consumers.meta,
        ),
    )

    def __init__(
        self,
        *,
        non_conform_load_schedules: Iterable[NonConformLoadSchedule] | None = None,
        energy_consumers: Iterable[NonConformLoad] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if non_conform_load_schedules is not None:
            NonConformLoadGroup.non_conform_load_schedules.extend(self, non_conform_load_schedules)
        if energy_consumers is not None:
            NonConformLoadGroup.energy_consumers.extend(self, energy_consumers)

    def add_non_conform_load_schedule(
        self, non_conform_load_schedule: NonConformLoadSchedule
    ) -> Self:
        return NonConformLoadGroup.non_conform_load_schedules.add(self, non_conform_load_schedule)

    def remove_non_conform_load_schedule(
        self, non_conform_load_schedule: NonConformLoadSchedule
    ) -> Self:
        return NonConformLoadGroup.non_conform_load_schedules.remove(
            self, non_conform_load_schedule
        )

    def clear_non_conform_load_schedules(self) -> Self:
        return NonConformLoadGroup.non_conform_load_schedules.clear(self)

    def num_non_conform_load_schedule(self) -> int:
        return NonConformLoadGroup.non_conform_load_schedules.count(self)

    def get_non_conform_load_schedule_by_mrid(self, mrid: str) -> NonConformLoadSchedule | None:
        return NonConformLoadGroup.non_conform_load_schedules.get_by_mrid(self, mrid)

    def add_energy_consumer(self, energy_consumer: NonConformLoad) -> Self:
        return NonConformLoadGroup.energy_consumers.add(self, energy_consumer)

    def remove_energy_consumer(self, energy_consumer: NonConformLoad) -> Self:
        return NonConformLoadGroup.energy_consumers.remove(self, energy_consumer)

    def clear_energy_consumers(self) -> Self:
        return NonConformLoadGroup.energy_consumers.clear(self)

    def num_energy_consumer(self) -> int:
        return NonConformLoadGroup.energy_consumers.count(self)

    def get_energy_consumer_by_mrid(self, mrid: str) -> NonConformLoad | None:
        return NonConformLoadGroup.energy_consumers.get_by_mrid(self, mrid)
