"""CIM class BidTimeSeries (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from typing import Any


class BidTimeSeries(TimeSeries):
    """The formal specification of specific characteristics related to a bid."""

    __slots__ = (
        "block_bid",
        "direction",
        "divisible",
        "exclusive_bids_identification",
        "linked_bids_identification",
        "minimum_activation_quantity",
        "priority",
        "status",
        "step_increment_quantity",
    )

    block_bid: str | None
    direction: str | None
    divisible: str | None
    status: str | None
    linked_bids_identification: str | None
    exclusive_bids_identification: str | None
    minimum_activation_quantity: _decimal.Decimal | None
    step_increment_quantity: _decimal.Decimal | None
    priority: int | None

    _cim_meta = ClassMeta(
        cim_name="BidTimeSeries",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{39712DC0-6B13-4680-AF0F-66E08AC6DE63}",
        attributes=(
            AttrMeta("block_bid", "blockBid", "str", 0, 1, "primitive"),
            AttrMeta("direction", "direction", "str", 0, 1, "primitive"),
            AttrMeta("divisible", "divisible", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "str", 0, 1, "primitive"),
            AttrMeta(
                "linked_bids_identification", "linkedBidsIdentification", "str", 0, 1, "primitive"
            ),
            AttrMeta(
                "exclusive_bids_identification",
                "exclusiveBidsIdentification",
                "str",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "minimum_activation_quantity",
                "minimumActivationQuantity",
                "Decimal",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "step_increment_quantity", "stepIncrementQuantity", "Decimal", 0, 1, "primitive"
            ),
            AttrMeta("priority", "priority", "int", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        block_bid: str | None = None,
        direction: str | None = None,
        divisible: str | None = None,
        status: str | None = None,
        linked_bids_identification: str | None = None,
        exclusive_bids_identification: str | None = None,
        minimum_activation_quantity: _decimal.Decimal | None = None,
        step_increment_quantity: _decimal.Decimal | None = None,
        priority: int | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.block_bid = block_bid
        self.direction = direction
        self.divisible = divisible
        self.status = status
        self.linked_bids_identification = linked_bids_identification
        self.exclusive_bids_identification = exclusive_bids_identification
        self.minimum_activation_quantity = minimum_activation_quantity
        self.step_increment_quantity = step_increment_quantity
        self.priority = priority
