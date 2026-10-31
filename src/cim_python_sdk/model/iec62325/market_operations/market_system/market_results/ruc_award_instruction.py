"""CIM class RUCAwardInstruction (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_clearing import (
        ResourceAwardClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_product_type import (
        MarketProductType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType


class RUCAwardInstruction(CimObject):
    """This class models the information about the RUC awards."""

    __slots__ = (
        "_clearing_resource_award",
        "_registered_resource",
        "cleared_price",
        "market_product_type",
        "ruc_award",
        "ruc_capacity",
        "ruc_schedule",
        "update_time_stamp",
        "update_type",
        "update_user",
    )

    cleared_price: float | None
    market_product_type: MarketProductType | None
    ruc_award: float | None
    ruc_capacity: float | None
    ruc_schedule: float | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None
    update_user: str | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="ruc_award_instruction",
            aggregation="none",
        )
    )
    clearing_resource_award: Many[ResourceAwardClearing] = Many(
        EndMeta(
            name="clearing_resource_award",
            cim_role="ClearingResourceAward",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_clearing:ResourceAwardClearing",
            many=True,
            lower=1,
            upper=None,
            inverse="ruc_award_instruction",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RUCAwardInstruction",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{FF4C9484-9951-43e7-9216-7585CD85AFFC}",
        attributes=(
            AttrMeta("cleared_price", "clearedPrice", "float", 0, 1, "primitive"),
            AttrMeta(
                "market_product_type", "marketProductType", "MarketProductType", 0, 1, "enumeration"
            ),
            AttrMeta("ruc_award", "RUCAward", "float", 0, 1, "primitive"),
            AttrMeta("ruc_capacity", "RUCCapacity", "float", 0, 1, "primitive"),
            AttrMeta("ruc_schedule", "RUCSchedule", "float", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
        ),
        ends=(
            registered_resource.meta,
            clearing_resource_award.meta,
        ),
    )

    def __init__(
        self,
        *,
        cleared_price: float | None = None,
        market_product_type: MarketProductType | None = None,
        ruc_award: float | None = None,
        ruc_capacity: float | None = None,
        ruc_schedule: float | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        update_user: str | None = None,
        registered_resource: RegisteredResource | None = None,
        clearing_resource_award: Iterable[ResourceAwardClearing] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cleared_price = cleared_price
        self.market_product_type = market_product_type
        self.ruc_award = ruc_award
        self.ruc_capacity = ruc_capacity
        self.ruc_schedule = ruc_schedule
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        self.update_user = update_user
        if registered_resource is not None:
            self.registered_resource = registered_resource
        if clearing_resource_award is not None:
            RUCAwardInstruction.clearing_resource_award.extend(self, clearing_resource_award)

    def add_clearing_resource_award(self, clearing_resource_award: ResourceAwardClearing) -> Self:
        return RUCAwardInstruction.clearing_resource_award.add(self, clearing_resource_award)

    def remove_clearing_resource_award(
        self, clearing_resource_award: ResourceAwardClearing
    ) -> Self:
        return RUCAwardInstruction.clearing_resource_award.remove(self, clearing_resource_award)

    def clear_clearing_resource_award(self) -> Self:
        return RUCAwardInstruction.clearing_resource_award.clear(self)

    def num_clearing_resource_award(self) -> int:
        return RUCAwardInstruction.clearing_resource_award.count(self)

    def get_clearing_resource_award_by_mrid(self, mrid: str) -> ResourceAwardClearing | None:
        return RUCAwardInstruction.clearing_resource_award.get_by_mrid(self, mrid)
