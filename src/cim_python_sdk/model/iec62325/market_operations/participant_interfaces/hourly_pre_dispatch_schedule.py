"""CIM class HourlyPreDispatchSchedule (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_hourly_schedule import (
    BidHourlySchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class HourlyPreDispatchSchedule(BidHourlySchedule):
    """An indicator specifying that a resource shall have an Hourly Pre-Dispatch. The resource
    could be a RegisteredGenerator or a RegisteredInterTie.

    This schedule is assocated with the hourly parameters in a resource bid."""

    __slots__ = ("value",)

    value: bool | None

    _cim_meta = ClassMeta(
        cim_name="HourlyPreDispatchSchedule",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{43F206DA-24E9-4900-A416-2CD5AA7B5571}",
        attributes=(AttrMeta("value", "value", "bool", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        value: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
