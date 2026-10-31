"""CIM class MktMeasurement (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.violation_limit import (
        ViolationLimit,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.dynamic_schedule import (
        DynamicSchedule,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_reservation.tie_point import TiePoint
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode


class MktMeasurement(Measurement):
    """Subclass of IEC61970:Meas:Measurement."""

    __slots__ = (
        "_by_tie_point",
        "_dynamic_schedule",
        "_for_tie_point",
        "_pnode",
        "_violation_limit",
    )

    dynamic_schedule: Many[DynamicSchedule] = Many(
        EndMeta(
            name="dynamic_schedule",
            cim_role="DynamicSchedule",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.dynamic_schedule:DynamicSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_measurement",
            aggregation="none",
        )
    )
    by_tie_point: One[TiePoint] = One(
        EndMeta(
            name="by_tie_point",
            cim_role="ByTiePoint",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_reservation.tie_point:TiePoint",
            many=False,
            lower=1,
            upper=1,
            inverse="by_mkt_measurement",
            aggregation="none",
        )
    )
    pnode: One[Pnode] = One(
        EndMeta(
            name="pnode",
            cim_role="Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_measurement",
            aggregation="none",
        )
    )
    violation_limit: Many[ViolationLimit] = Many(
        EndMeta(
            name="violation_limit",
            cim_role="ViolationLimit",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.violation_limit:ViolationLimit",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_measurement",
            aggregation="none",
        )
    )
    for_tie_point: One[TiePoint] = One(
        EndMeta(
            name="for_tie_point",
            cim_role="ForTiePoint",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_reservation.tie_point:TiePoint",
            many=False,
            lower=1,
            upper=1,
            inverse="for_mkt_measurement",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktMeasurement",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{F792A9D7-1097-4bf1-8B00-E894C6CD2AFA}",
        ends=(
            dynamic_schedule.meta,
            by_tie_point.meta,
            pnode.meta,
            violation_limit.meta,
            for_tie_point.meta,
        ),
    )

    def __init__(
        self,
        *,
        dynamic_schedule: Iterable[DynamicSchedule] | None = None,
        by_tie_point: TiePoint | None = None,
        pnode: Pnode | None = None,
        violation_limit: Iterable[ViolationLimit] | None = None,
        for_tie_point: TiePoint | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dynamic_schedule is not None:
            MktMeasurement.dynamic_schedule.extend(self, dynamic_schedule)
        if by_tie_point is not None:
            self.by_tie_point = by_tie_point
        if pnode is not None:
            self.pnode = pnode
        if violation_limit is not None:
            MktMeasurement.violation_limit.extend(self, violation_limit)
        if for_tie_point is not None:
            self.for_tie_point = for_tie_point

    def add_dynamic_schedule(self, dynamic_schedule: DynamicSchedule) -> Self:
        return MktMeasurement.dynamic_schedule.add(self, dynamic_schedule)

    def remove_dynamic_schedule(self, dynamic_schedule: DynamicSchedule) -> Self:
        return MktMeasurement.dynamic_schedule.remove(self, dynamic_schedule)

    def clear_dynamic_schedule(self) -> Self:
        return MktMeasurement.dynamic_schedule.clear(self)

    def num_dynamic_schedule(self) -> int:
        return MktMeasurement.dynamic_schedule.count(self)

    def get_dynamic_schedule_by_mrid(self, mrid: str) -> DynamicSchedule | None:
        return MktMeasurement.dynamic_schedule.get_by_mrid(self, mrid)

    def add_violation_limit(self, violation_limit: ViolationLimit) -> Self:
        return MktMeasurement.violation_limit.add(self, violation_limit)

    def remove_violation_limit(self, violation_limit: ViolationLimit) -> Self:
        return MktMeasurement.violation_limit.remove(self, violation_limit)

    def clear_violation_limit(self) -> Self:
        return MktMeasurement.violation_limit.clear(self)

    def num_violation_limit(self) -> int:
        return MktMeasurement.violation_limit.count(self)

    def get_violation_limit_by_mrid(self, mrid: str) -> ViolationLimit | None:
        return MktMeasurement.violation_limit.get_by_mrid(self, mrid)
