"""CIM class SchedulingPoint (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.interchange_schedule import (
        InterchangeSchedule,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class SchedulingPoint(IdentifiedObject):
    """Connection to other organizations at the boundary of the ISO/RTO."""

    __slots__ = ("_flowgate", "_interchange_schedule", "_registered_resource")

    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=0,
            upper=1,
            inverse="inter_tie",
            aggregation="none",
        )
    )
    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="inter_tie",
            aggregation="none",
        )
    )
    interchange_schedule: Many[InterchangeSchedule] = Many(
        EndMeta(
            name="interchange_schedule",
            cim_role="InterchangeSchedule",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.interchange_schedule:InterchangeSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="inter_tie",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SchedulingPoint",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{D577CAB9-7258-4a51-8AFD-60D5FB2EE2FD}",
        ends=(
            flowgate.meta,
            registered_resource.meta,
            interchange_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        flowgate: Flowgate | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        interchange_schedule: Iterable[InterchangeSchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if flowgate is not None:
            self.flowgate = flowgate
        if registered_resource is not None:
            SchedulingPoint.registered_resource.extend(self, registered_resource)
        if interchange_schedule is not None:
            SchedulingPoint.interchange_schedule.extend(self, interchange_schedule)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return SchedulingPoint.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return SchedulingPoint.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return SchedulingPoint.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return SchedulingPoint.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return SchedulingPoint.registered_resource.get_by_mrid(self, mrid)

    def add_interchange_schedule(self, interchange_schedule: InterchangeSchedule) -> Self:
        return SchedulingPoint.interchange_schedule.add(self, interchange_schedule)

    def remove_interchange_schedule(self, interchange_schedule: InterchangeSchedule) -> Self:
        return SchedulingPoint.interchange_schedule.remove(self, interchange_schedule)

    def clear_interchange_schedule(self) -> Self:
        return SchedulingPoint.interchange_schedule.clear(self)

    def num_interchange_schedule(self) -> int:
        return SchedulingPoint.interchange_schedule.count(self)

    def get_interchange_schedule_by_mrid(self, mrid: str) -> InterchangeSchedule | None:
        return SchedulingPoint.interchange_schedule.get_by_mrid(self, mrid)
