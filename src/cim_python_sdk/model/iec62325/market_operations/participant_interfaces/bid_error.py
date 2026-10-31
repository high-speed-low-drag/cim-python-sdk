"""CIM class BidError (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_product import (
        MarketProduct,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.resource_bid import (
        ResourceBid,
    )


class BidError(IdentifiedObject):
    """This class represent the error information for a bid that is detected during bid
    validation."""

    __slots__ = (
        "_market_product",
        "_resource_bid",
        "component_type",
        "end_time",
        "err_message",
        "err_priority",
        "log_time_stamp",
        "msg_level",
        "rule_id",
        "start_time",
    )

    err_priority: int | None
    err_message: str | None
    rule_id: int | None
    start_time: _dt.datetime | None
    end_time: _dt.datetime | None
    log_time_stamp: _dt.datetime | None
    component_type: str | None
    msg_level: int | None

    resource_bid: Many[ResourceBid] = Many(
        EndMeta(
            name="resource_bid",
            cim_role="ResourceBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.resource_bid:ResourceBid",
            many=True,
            lower=0,
            upper=None,
            inverse="bid_error",
            aggregation="none",
        )
    )
    market_product: One[MarketProduct] = One(
        EndMeta(
            name="market_product",
            cim_role="MarketProduct",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_product:MarketProduct",
            many=False,
            lower=0,
            upper=1,
            inverse="bid_error",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BidError",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{AA5D4965-B660-42ad-BB28-BA85D33E6BC7}",
        attributes=(
            AttrMeta("err_priority", "errPriority", "int", 0, 1, "primitive"),
            AttrMeta("err_message", "errMessage", "str", 0, 1, "primitive"),
            AttrMeta("rule_id", "ruleID", "int", 0, 1, "primitive"),
            AttrMeta("start_time", "startTime", "datetime", 0, 1, "primitive"),
            AttrMeta("end_time", "endTime", "datetime", 0, 1, "primitive"),
            AttrMeta("log_time_stamp", "logTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("component_type", "componentType", "str", 0, 1, "primitive"),
            AttrMeta("msg_level", "msgLevel", "int", 0, 1, "primitive"),
        ),
        ends=(
            resource_bid.meta,
            market_product.meta,
        ),
    )

    def __init__(
        self,
        *,
        err_priority: int | None = None,
        err_message: str | None = None,
        rule_id: int | None = None,
        start_time: _dt.datetime | None = None,
        end_time: _dt.datetime | None = None,
        log_time_stamp: _dt.datetime | None = None,
        component_type: str | None = None,
        msg_level: int | None = None,
        resource_bid: Iterable[ResourceBid] | None = None,
        market_product: MarketProduct | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.err_priority = err_priority
        self.err_message = err_message
        self.rule_id = rule_id
        self.start_time = start_time
        self.end_time = end_time
        self.log_time_stamp = log_time_stamp
        self.component_type = component_type
        self.msg_level = msg_level
        if resource_bid is not None:
            BidError.resource_bid.extend(self, resource_bid)
        if market_product is not None:
            self.market_product = market_product

    def add_resource_bid(self, resource_bid: ResourceBid) -> Self:
        return BidError.resource_bid.add(self, resource_bid)

    def remove_resource_bid(self, resource_bid: ResourceBid) -> Self:
        return BidError.resource_bid.remove(self, resource_bid)

    def clear_resource_bid(self) -> Self:
        return BidError.resource_bid.clear(self)

    def num_resource_bid(self) -> int:
        return BidError.resource_bid.count(self)

    def get_resource_bid_by_mrid(self, mrid: str) -> ResourceBid | None:
        return BidError.resource_bid.get_by_mrid(self, mrid)
