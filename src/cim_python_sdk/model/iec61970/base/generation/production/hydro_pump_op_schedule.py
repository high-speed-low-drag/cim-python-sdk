"""CIM class HydroPumpOpSchedule (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.hydro_pump import HydroPump


class HydroPumpOpSchedule(RegularIntervalSchedule):
    """The hydro pump's Operator-approved current operating schedule (or plan), typically
    produced with the aid of unit commitment type analyses. The unit's operating schedule
    status is typically given as: (0=unavailable) (1=available to startup or shutdown)
    (2=must pump)."""

    __slots__ = ("_hydro_pump",)

    hydro_pump: One[HydroPump] = One(
        EndMeta(
            name="hydro_pump",
            cim_role="HydroPump",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_pump:HydroPump",
            many=False,
            lower=1,
            upper=1,
            inverse="hydro_pump_op_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HydroPumpOpSchedule",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{DC4836E6-546A-4cb7-86AA-82CC7690803D}",
        ends=(hydro_pump.meta,),
    )

    def __init__(
        self,
        *,
        hydro_pump: HydroPump | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if hydro_pump is not None:
            self.hydro_pump = hydro_pump
