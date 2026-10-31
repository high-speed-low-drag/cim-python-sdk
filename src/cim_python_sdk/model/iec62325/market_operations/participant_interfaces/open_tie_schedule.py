"""CIM class OpenTieSchedule (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_hourly_schedule import (
    BidHourlySchedule,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class OpenTieSchedule(BidHourlySchedule):
    """Result of bid validation against conditions that may exist on an interchange that
    becomes disconnected or is heavily discounted with respect the MW flow.

    This schedule is assocated with the hourly parameters in a resource bid."""

    __slots__ = ("value",)

    value: bool | None

    _cim_meta = ClassMeta(
        cim_name="OpenTieSchedule",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{89F66067-6AA6-4ac5-9527-A02455F3698D}",
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
