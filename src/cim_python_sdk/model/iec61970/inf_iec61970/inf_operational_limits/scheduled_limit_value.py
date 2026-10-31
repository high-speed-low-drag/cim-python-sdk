"""CIM class ScheduledLimitValue (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.load_model.season import Season
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_dependency import (
        ScheduledLimitDependency,
    )


class ScheduledLimitValue(IdentifiedObject):
    """A limit that is applicable during a scheduled time period."""

    __slots__ = ("_scheduled_limit_dependency", "_season")

    season: One[Season] = One(
        EndMeta(
            name="season",
            cim_role="Season",
            target="cim_python_sdk.model.iec61970.base.load_model.season:Season",
            many=False,
            lower=0,
            upper=1,
            inverse="scheduled_limits",
            aggregation="none",
        )
    )
    scheduled_limit_dependency: One[ScheduledLimitDependency] = One(
        EndMeta(
            name="scheduled_limit_dependency",
            cim_role="ScheduledLimitDependency",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_dependency:ScheduledLimitDependency",
            many=False,
            lower=1,
            upper=1,
            inverse="scheduled_limit_values",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ScheduledLimitValue",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{93BE7FA6-D43E-4844-8A9A-A9F7F84B37E5}",
        ends=(
            season.meta,
            scheduled_limit_dependency.meta,
        ),
    )

    def __init__(
        self,
        *,
        season: Season | None = None,
        scheduled_limit_dependency: ScheduledLimitDependency | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if season is not None:
            self.season = season
        if scheduled_limit_dependency is not None:
            self.scheduled_limit_dependency = scheduled_limit_dependency
