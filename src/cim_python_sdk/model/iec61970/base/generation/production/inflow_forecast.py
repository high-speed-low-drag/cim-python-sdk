"""CIM class InflowForecast (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.regular_interval_schedule import (
    RegularIntervalSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.reservoir import Reservoir


class InflowForecast(RegularIntervalSchedule):
    """Natural water inflow to a reservoir, usually forecasted from predicted rain and
    snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in
    average cubic meters per second over the time increment."""

    __slots__ = ("_reservoir",)

    reservoir: One[Reservoir] = One(
        EndMeta(
            name="reservoir",
            cim_role="Reservoir",
            target="cim_python_sdk.model.iec61970.base.generation.production.reservoir:Reservoir",
            many=False,
            lower=1,
            upper=1,
            inverse="inflow_forecasts",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InflowForecast",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{41CA4275-BBFB-431b-912C-599AC5B2642C}",
        ends=(reservoir.meta,),
    )

    def __init__(
        self,
        *,
        reservoir: Reservoir | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if reservoir is not None:
            self.reservoir = reservoir
