"""CIM class NonConformLoadSchedule (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.load_model.season_day_type_schedule import (
    SeasonDayTypeSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.load_model.non_conform_load_group import (
        NonConformLoadGroup,
    )


class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time
    (X-axis) for non-conforming loads, e.g., large industrial load or power station service
    (where modelled)."""

    __slots__ = ("_non_conform_load_group",)

    non_conform_load_group: One[NonConformLoadGroup] = One(
        EndMeta(
            name="non_conform_load_group",
            cim_role="NonConformLoadGroup",
            target="cim_python_sdk.model.iec61970.base.load_model.non_conform_load_group:NonConformLoadGroup",
            many=False,
            lower=1,
            upper=1,
            inverse="non_conform_load_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NonConformLoadSchedule",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{41B7642C-D924-4ebf-9AE9-4BD3706390FD}",
        ends=(non_conform_load_group.meta,),
    )

    def __init__(
        self,
        *,
        non_conform_load_group: NonConformLoadGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if non_conform_load_group is not None:
            self.non_conform_load_group = non_conform_load_group
