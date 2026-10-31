"""CIM class SteamSendoutSchedule (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.cogeneration_plant import (
        CogenerationPlant,
    )


class SteamSendoutSchedule(RegularIntervalSchedule):
    """The cogeneration plant's steam sendout schedule in volume per time unit."""

    __slots__ = ("_cogeneration_plant",)

    cogeneration_plant: One[CogenerationPlant] = One(
        EndMeta(
            name="cogeneration_plant",
            cim_role="CogenerationPlant",
            target="cim_python_sdk.model.iec61970.base.generation.production.cogeneration_plant:CogenerationPlant",
            many=False,
            lower=1,
            upper=1,
            inverse="steam_sendout_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SteamSendoutSchedule",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{4C02B840-80C5-4d55-AB0D-3006749FD6A5}",
        ends=(cogeneration_plant.meta,),
    )

    def __init__(
        self,
        *,
        cogeneration_plant: CogenerationPlant | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if cogeneration_plant is not None:
            self.cogeneration_plant = cogeneration_plant
