"""CIM class MeterWorkTask (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.work.work_task import WorkTask

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.meter import Meter
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint


class MeterWorkTask(WorkTask):
    """Work task involving meters."""

    __slots__ = ("_meter", "_old_meter", "_usage_point")

    old_meter: One[Meter] = One(
        EndMeta(
            name="old_meter",
            cim_role="OldMeter",
            target="cim_python_sdk.model.iec61968.metering.meter:Meter",
            many=False,
            lower=0,
            upper=1,
            inverse="meter_replacement_work_tasks",
            aggregation="none",
        )
    )
    usage_point: One[UsagePoint] = One(
        EndMeta(
            name="usage_point",
            cim_role="UsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=False,
            lower=0,
            upper=1,
            inverse="meter_service_work_tasks",
            aggregation="none",
        )
    )
    meter: One[Meter] = One(
        EndMeta(
            name="meter",
            cim_role="Meter",
            target="cim_python_sdk.model.iec61968.metering.meter:Meter",
            many=False,
            lower=0,
            upper=1,
            inverse="meter_service_work_task",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeterWorkTask",
        package="TC57CIM/IEC61968/Metering",
        guid="{9770E496-51C1-4d53-A219-8138C2701943}",
        ends=(
            old_meter.meta,
            usage_point.meta,
            meter.meta,
        ),
    )

    def __init__(
        self,
        *,
        old_meter: Meter | None = None,
        usage_point: UsagePoint | None = None,
        meter: Meter | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if old_meter is not None:
            self.old_meter = old_meter
        if usage_point is not None:
            self.usage_point = usage_point
        if meter is not None:
            self.meter = meter
