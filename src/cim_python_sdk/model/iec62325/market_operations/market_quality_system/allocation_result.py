"""CIM class AllocationResult (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.allocation_result_values import (
        AllocationResultValues,
    )


class AllocationResult(CimObject):
    """Models Market clearing results. Indicates market horizon, interval based. Used by a
    market quality system for billing and settlement purposes."""

    __slots__ = (
        "_allocation_result_values",
        "interval_start_time",
        "update_time_stamp",
        "update_user",
    )

    interval_start_time: _dt.datetime | None
    update_user: str | None
    update_time_stamp: _dt.datetime | None

    allocation_result_values: Many[AllocationResultValues] = Many(
        EndMeta(
            name="allocation_result_values",
            cim_role="AllocationResultValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.allocation_result_values:AllocationResultValues",
            many=True,
            lower=1,
            upper=None,
            inverse="allocation_result",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AllocationResult",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{0B5B92EF-D56F-4b91-8CC4-7C4464083896}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
        ),
        ends=(allocation_result_values.meta,),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        update_user: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        allocation_result_values: Iterable[AllocationResultValues] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        self.update_user = update_user
        self.update_time_stamp = update_time_stamp
        if allocation_result_values is not None:
            AllocationResult.allocation_result_values.extend(self, allocation_result_values)

    def add_allocation_result_value(self, allocation_result_value: AllocationResultValues) -> Self:
        return AllocationResult.allocation_result_values.add(self, allocation_result_value)

    def remove_allocation_result_value(
        self, allocation_result_value: AllocationResultValues
    ) -> Self:
        return AllocationResult.allocation_result_values.remove(self, allocation_result_value)

    def clear_allocation_result_values(self) -> Self:
        return AllocationResult.allocation_result_values.clear(self)

    def num_allocation_result_value(self) -> int:
        return AllocationResult.allocation_result_values.count(self)
