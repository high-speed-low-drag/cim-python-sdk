"""CIM class InterchangeSchedule (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.interchange_etc_data import (
        InterchangeETCData,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.check_out_type import (
        CheckOutType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.energy_product_type import (
        EnergyProductType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.inter_tie_direction import (
        InterTieDirection,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_product_type import (
        MarketProductType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie import (
        RegisteredInterTie,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_point import (
        SchedulingPoint,
    )


class InterchangeSchedule(Curve):
    """Interchange schedule class to hold information for interchange schedules such as import
    export type, energy type, and etc."""

    __slots__ = (
        "_inter_tie",
        "_interchange_etc_data",
        "_registered_inter_tie",
        "check_out_type",
        "direction_type",
        "energy_type",
        "interval_length",
        "market_type",
        "operating_date",
        "out_of_market_type",
        "schedule_type",
        "wcr_id",
    )

    check_out_type: CheckOutType | None
    direction_type: InterTieDirection | None
    energy_type: MarketProductType | None
    interval_length: int | None
    market_type: MarketType | None
    operating_date: _dt.datetime | None
    out_of_market_type: bool | None
    schedule_type: EnergyProductType | None
    wcr_id: str | None

    interchange_etc_data: Many[InterchangeETCData] = Many(
        EndMeta(
            name="interchange_etc_data",
            cim_role="InterchangeETCData",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.interchange_etc_data:InterchangeETCData",
            many=True,
            lower=0,
            upper=None,
            inverse="interchange_schedule",
            aggregation="shared",
        )
    )
    registered_inter_tie: One[RegisteredInterTie] = One(
        EndMeta(
            name="registered_inter_tie",
            cim_role="RegisteredInterTie",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie:RegisteredInterTie",
            many=False,
            lower=0,
            upper=1,
            inverse="interchange_schedule",
            aggregation="none",
        )
    )
    inter_tie: One[SchedulingPoint] = One(
        EndMeta(
            name="inter_tie",
            cim_role="InterTie",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_point:SchedulingPoint",
            many=False,
            lower=0,
            upper=1,
            inverse="interchange_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InterchangeSchedule",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{83700D33-E476-4f73-B53C-141249827158}",
        attributes=(
            AttrMeta("check_out_type", "checkOutType", "CheckOutType", 0, 1, "enumeration"),
            AttrMeta("direction_type", "directionType", "InterTieDirection", 0, 1, "enumeration"),
            AttrMeta("energy_type", "energyType", "MarketProductType", 0, 1, "enumeration"),
            AttrMeta("interval_length", "intervalLength", "int", 0, 1, "primitive"),
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
            AttrMeta("operating_date", "operatingDate", "datetime", 0, 1, "primitive"),
            AttrMeta("out_of_market_type", "outOfMarketType", "bool", 0, 1, "primitive"),
            AttrMeta("schedule_type", "scheduleType", "EnergyProductType", 0, 1, "enumeration"),
            AttrMeta("wcr_id", "wcrID", "str", 0, 1, "primitive"),
        ),
        ends=(
            interchange_etc_data.meta,
            registered_inter_tie.meta,
            inter_tie.meta,
        ),
    )

    def __init__(
        self,
        *,
        check_out_type: CheckOutType | None = None,
        direction_type: InterTieDirection | None = None,
        energy_type: MarketProductType | None = None,
        interval_length: int | None = None,
        market_type: MarketType | None = None,
        operating_date: _dt.datetime | None = None,
        out_of_market_type: bool | None = None,
        schedule_type: EnergyProductType | None = None,
        wcr_id: str | None = None,
        interchange_etc_data: Iterable[InterchangeETCData] | None = None,
        registered_inter_tie: RegisteredInterTie | None = None,
        inter_tie: SchedulingPoint | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.check_out_type = check_out_type
        self.direction_type = direction_type
        self.energy_type = energy_type
        self.interval_length = interval_length
        self.market_type = market_type
        self.operating_date = operating_date
        self.out_of_market_type = out_of_market_type
        self.schedule_type = schedule_type
        self.wcr_id = wcr_id
        if interchange_etc_data is not None:
            InterchangeSchedule.interchange_etc_data.extend(self, interchange_etc_data)
        if registered_inter_tie is not None:
            self.registered_inter_tie = registered_inter_tie
        if inter_tie is not None:
            self.inter_tie = inter_tie

    def add_interchange_etc_data(self, interchange_etc_data: InterchangeETCData) -> Self:
        return InterchangeSchedule.interchange_etc_data.add(self, interchange_etc_data)

    def remove_interchange_etc_data(self, interchange_etc_data: InterchangeETCData) -> Self:
        return InterchangeSchedule.interchange_etc_data.remove(self, interchange_etc_data)

    def clear_interchange_etc_data(self) -> Self:
        return InterchangeSchedule.interchange_etc_data.clear(self)

    def num_interchange_etc_data(self) -> int:
        return InterchangeSchedule.interchange_etc_data.count(self)
