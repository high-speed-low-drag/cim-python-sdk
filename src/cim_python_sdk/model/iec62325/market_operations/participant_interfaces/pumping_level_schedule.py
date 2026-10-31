"""CIM class PumpingLevelSchedule (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_hourly_product_schedule import (
    BidHourlyProductSchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PumpingLevelSchedule(BidHourlyProductSchedule):
    """The fixed operating level of a Pump Storage Hydro Unit operating as a hydro pump.
    Associated with the energy market product type.

    This schedule is assocated with the hourly parameters in a resource bid associated with
    a specific product within the bid."""

    __slots__ = ("value",)

    value: float | None

    _cim_meta = ClassMeta(
        cim_name="PumpingLevelSchedule",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{29E98791-D733-4f25-8000-8F388D1AD00B}",
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
