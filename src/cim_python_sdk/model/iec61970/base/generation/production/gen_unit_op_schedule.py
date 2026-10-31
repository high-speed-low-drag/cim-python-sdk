"""CIM class GenUnitOpSchedule (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import (
        GeneratingUnit,
    )


class GenUnitOpSchedule(RegularIntervalSchedule):
    """The generating unit's Operator-approved current operating schedule (or plan), typically
    produced with the aid of unit commitment type analyses. The X-axis represents absolute
    time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must
    run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed
    power value where required."""

    __slots__ = ("_generating_unit",)

    generating_unit: One[GeneratingUnit] = One(
        EndMeta(
            name="generating_unit",
            cim_role="GeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.generating_unit:GeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="gen_unit_op_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GenUnitOpSchedule",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{FF8AAD42-67F3-4310-A1D0-9E3500E69261}",
        ends=(generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        generating_unit: GeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if generating_unit is not None:
            self.generating_unit = generating_unit
