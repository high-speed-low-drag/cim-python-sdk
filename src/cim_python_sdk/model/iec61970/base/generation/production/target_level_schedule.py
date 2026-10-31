"""CIM class TargetLevelSchedule (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.reservoir import Reservoir


class TargetLevelSchedule(Curve):
    """Reservoir water level targets from advanced studies or "rule curves". Typically in one
    hour increments for up to 10 days."""

    __slots__ = ("_reservoir", "high_level_limit", "low_level_limit")

    high_level_limit: float | None  # WaterLevel
    low_level_limit: float | None  # WaterLevel

    reservoir: One[Reservoir] = One(
        EndMeta(
            name="reservoir",
            cim_role="Reservoir",
            target="cim_python_sdk.model.iec61970.base.generation.production.reservoir:Reservoir",
            many=False,
            lower=1,
            upper=1,
            inverse="target_level_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TargetLevelSchedule",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{0BF4BBDA-CADE-4a85-B8CB-F0C4A18075BF}",
        attributes=(
            AttrMeta("high_level_limit", "highLevelLimit", "WaterLevel", 0, 1, "cimdatatype"),
            AttrMeta("low_level_limit", "lowLevelLimit", "WaterLevel", 0, 1, "cimdatatype"),
        ),
        ends=(reservoir.meta,),
    )

    def __init__(
        self,
        *,
        high_level_limit: float | None = None,
        low_level_limit: float | None = None,
        reservoir: Reservoir | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.high_level_limit = high_level_limit
        self.low_level_limit = low_level_limit
        if reservoir is not None:
            self.reservoir = reservoir
