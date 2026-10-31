"""CIM class ConformLoadSchedule (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.load_model.season_day_type_schedule import (
    SeasonDayTypeSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.load_model.conform_load_group import ConformLoadGroup


class ConformLoadSchedule(SeasonDayTypeSchedule):
    """A curve of load versus time (X-axis) showing the active power values (Y1-axis) and
    reactive power (Y2-axis) for each unit of the period covered. This curve represents a
    typical pattern of load over the time period for a given day type and season."""

    __slots__ = ("_conform_load_group",)

    conform_load_group: One[ConformLoadGroup] = One(
        EndMeta(
            name="conform_load_group",
            cim_role="ConformLoadGroup",
            target="cim_python_sdk.model.iec61970.base.load_model.conform_load_group:ConformLoadGroup",
            many=False,
            lower=1,
            upper=1,
            inverse="conform_load_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConformLoadSchedule",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{36B21936-3BDC-4e05-BD1E-6938243903AA}",
        ends=(conform_load_group.meta,),
    )

    def __init__(
        self,
        *,
        conform_load_group: ConformLoadGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if conform_load_group is not None:
            self.conform_load_group = conform_load_group
