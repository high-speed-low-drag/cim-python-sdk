"""CIM class ScheduledLimitDependency (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_dependency import (
    LimitDependency,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_value import (
        ScheduledLimitValue,
    )


class ScheduledLimitDependency(LimitDependency):
    """CIM class ScheduledLimitDependency."""

    __slots__ = ("_scheduled_limit_values",)

    scheduled_limit_values: Many[ScheduledLimitValue] = Many(
        EndMeta(
            name="scheduled_limit_values",
            cim_role="ScheduledLimitValues",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_value:ScheduledLimitValue",
            many=True,
            lower=0,
            upper=None,
            inverse="scheduled_limit_dependency",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ScheduledLimitDependency",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{75574C0E-2A86-47a4-8D58-14D494EA033F}",
        ends=(scheduled_limit_values.meta,),
    )

    def __init__(
        self,
        *,
        scheduled_limit_values: Iterable[ScheduledLimitValue] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if scheduled_limit_values is not None:
            ScheduledLimitDependency.scheduled_limit_values.extend(self, scheduled_limit_values)

    def add_scheduled_limit_value(self, scheduled_limit_value: ScheduledLimitValue) -> Self:
        return ScheduledLimitDependency.scheduled_limit_values.add(self, scheduled_limit_value)

    def remove_scheduled_limit_value(self, scheduled_limit_value: ScheduledLimitValue) -> Self:
        return ScheduledLimitDependency.scheduled_limit_values.remove(self, scheduled_limit_value)

    def clear_scheduled_limit_values(self) -> Self:
        return ScheduledLimitDependency.scheduled_limit_values.clear(self)

    def num_scheduled_limit_value(self) -> int:
        return ScheduledLimitDependency.scheduled_limit_values.count(self)

    def get_scheduled_limit_value_by_mrid(self, mrid: str) -> ScheduledLimitValue | None:
        return ScheduledLimitDependency.scheduled_limit_values.get_by_mrid(self, mrid)
