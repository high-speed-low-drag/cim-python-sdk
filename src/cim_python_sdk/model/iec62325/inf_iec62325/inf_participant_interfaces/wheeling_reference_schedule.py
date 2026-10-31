"""CIM class WheelingReferenceSchedule (TC57CIM/IEC62325/InfIEC62325/InfParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_hourly_schedule import (
    BidHourlySchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class WheelingReferenceSchedule(BidHourlySchedule):
    """A unique identifier of a wheeling transaction. A wheeling transaction is a balanced
    Energy exchange among Supply and Demand Resources.

    This schedule is assocated with the hourly parameters in a resource bid."""

    __slots__ = ("value",)

    value: str | None

    _cim_meta = ClassMeta(
        cim_name="WheelingReferenceSchedule",
        package="TC57CIM/IEC62325/InfIEC62325/InfParticipantInterfaces",
        guid="{310951F0-7FFD-4314-988D-795F083243A1}",
        attributes=(AttrMeta("value", "value", "str", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        value: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
