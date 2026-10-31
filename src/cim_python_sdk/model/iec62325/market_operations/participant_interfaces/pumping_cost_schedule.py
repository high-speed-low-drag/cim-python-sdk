"""CIM class PumpingCostSchedule (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_hourly_product_schedule import (
    BidHourlyProductSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PumpingCostSchedule(BidHourlyProductSchedule):
    """The operating cost of a Pump Storage Hydro Unit operating as a hydro pump.

    This schedule is assocated with the hourly parameters in a resource bid associated with
    a specific product within the bid."""

    __slots__ = ("value",)

    value: float | None

    _cim_meta = ClassMeta(
        cim_name="PumpingCostSchedule",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{744A31CD-0CC4-4a29-807F-629CEA19B426}",
        attributes=(AttrMeta("value", "value", "float", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        value: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
