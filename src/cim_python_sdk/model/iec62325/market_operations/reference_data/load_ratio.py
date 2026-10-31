"""CIM class LoadRatio (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator import (
        SchedulingCoordinator,
    )


class LoadRatio(CimObject):
    """Representing the ratio of the load share for the associated SC."""

    __slots__ = ("_scheduling_coordinator", "interval_end_time", "interval_start_time", "share")

    interval_start_time: _dt.datetime | None
    interval_end_time: _dt.datetime | None
    share: float | None  # PerCent

    scheduling_coordinator: One[SchedulingCoordinator] = One(
        EndMeta(
            name="scheduling_coordinator",
            cim_role="SchedulingCoordinator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator:SchedulingCoordinator",
            many=False,
            lower=0,
            upper=1,
            inverse="load_ratio",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadRatio",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{1D3E872B-9078-493e-B9BF-A61556AEA453}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("interval_end_time", "intervalEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("share", "share", "PerCent", 0, 1, "cimdatatype"),
        ),
        ends=(scheduling_coordinator.meta,),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        interval_end_time: _dt.datetime | None = None,
        share: float | None = None,
        scheduling_coordinator: SchedulingCoordinator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        self.interval_end_time = interval_end_time
        self.share = share
        if scheduling_coordinator is not None:
            self.scheduling_coordinator = scheduling_coordinator
