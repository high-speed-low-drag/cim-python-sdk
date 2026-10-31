"""CIM class ASRequirements (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.reserve_demand_curve import (
        ReserveDemandCurve,
    )


class ASRequirements(CimObject):
    """Models Ancillary Service Requirements. Describes interval for which the requirement is
    applicable."""

    __slots__ = ("_reserve_demand_curve", "interval_start_time")

    interval_start_time: _dt.datetime | None

    reserve_demand_curve: Many[ReserveDemandCurve] = Many(
        EndMeta(
            name="reserve_demand_curve",
            cim_role="ReserveDemandCurve",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.reserve_demand_curve:ReserveDemandCurve",
            many=True,
            lower=1,
            upper=None,
            inverse="as_requirements",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ASRequirements",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{876735DA-B8B1-43b7-B00A-722B8BB05BD7}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(reserve_demand_curve.meta,),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        reserve_demand_curve: Iterable[ReserveDemandCurve] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        if reserve_demand_curve is not None:
            ASRequirements.reserve_demand_curve.extend(self, reserve_demand_curve)

    def add_reserve_demand_curve(self, reserve_demand_curve: ReserveDemandCurve) -> Self:
        return ASRequirements.reserve_demand_curve.add(self, reserve_demand_curve)

    def remove_reserve_demand_curve(self, reserve_demand_curve: ReserveDemandCurve) -> Self:
        return ASRequirements.reserve_demand_curve.remove(self, reserve_demand_curve)

    def clear_reserve_demand_curve(self) -> Self:
        return ASRequirements.reserve_demand_curve.clear(self)

    def num_reserve_demand_curve(self) -> int:
        return ASRequirements.reserve_demand_curve.count(self)

    def get_reserve_demand_curve_by_mrid(self, mrid: str) -> ReserveDemandCurve | None:
        return ASRequirements.reserve_demand_curve.get_by_mrid(self, mrid)
