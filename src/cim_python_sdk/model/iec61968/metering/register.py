"""CIM class Register (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.channel import Channel
    from cim_python_sdk.model.iec61968.metering.end_device_function import EndDeviceFunction
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61970.base.domain.time_interval import TimeInterval


class Register(IdentifiedObject):
    """A device that indicates or records units of the commodity or other quantity measured."""

    __slots__ = (
        "_channels",
        "_end_device_function",
        "_usage_point",
        "is_virtual",
        "left_digit_count",
        "right_digit_count",
        "tou_tier",
        "tou_tier_name",
    )

    is_virtual: bool | None
    right_digit_count: int | None
    left_digit_count: int | None
    tou_tier: TimeInterval | None
    tou_tier_name: str | None

    usage_point: One[UsagePoint] = One(
        EndMeta(
            name="usage_point",
            cim_role="Usage Point",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=False,
            lower=0,
            upper=1,
            inverse="register",
            aggregation="none",
        )
    )
    channels: Many[Channel] = Many(
        EndMeta(
            name="channels",
            cim_role="Channels",
            target="cim_python_sdk.model.iec61968.metering.channel:Channel",
            many=True,
            lower=0,
            upper=None,
            inverse="register",
            aggregation="none",
        )
    )
    end_device_function: One[EndDeviceFunction] = One(
        EndMeta(
            name="end_device_function",
            cim_role="EndDeviceFunction",
            target="cim_python_sdk.model.iec61968.metering.end_device_function:EndDeviceFunction",
            many=False,
            lower=0,
            upper=1,
            inverse="registers",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Register",
        package="TC57CIM/IEC61968/Metering",
        guid="{66D18B62-79CA-4cdd-A36D-CE77E47EE545}",
        attributes=(
            AttrMeta("is_virtual", "isVirtual", "bool", 0, 1, "primitive"),
            AttrMeta("right_digit_count", "rightDigitCount", "int", 0, 1, "primitive"),
            AttrMeta("left_digit_count", "leftDigitCount", "int", 0, 1, "primitive"),
            AttrMeta("tou_tier", "touTier", "TimeInterval", 0, 1, "compound"),
            AttrMeta("tou_tier_name", "touTierName", "str", 0, 1, "primitive"),
        ),
        ends=(
            usage_point.meta,
            channels.meta,
            end_device_function.meta,
        ),
    )

    def __init__(
        self,
        *,
        is_virtual: bool | None = None,
        right_digit_count: int | None = None,
        left_digit_count: int | None = None,
        tou_tier: TimeInterval | None = None,
        tou_tier_name: str | None = None,
        usage_point: UsagePoint | None = None,
        channels: Iterable[Channel] | None = None,
        end_device_function: EndDeviceFunction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_virtual = is_virtual
        self.right_digit_count = right_digit_count
        self.left_digit_count = left_digit_count
        self.tou_tier = tou_tier
        self.tou_tier_name = tou_tier_name
        if usage_point is not None:
            self.usage_point = usage_point
        if channels is not None:
            Register.channels.extend(self, channels)
        if end_device_function is not None:
            self.end_device_function = end_device_function

    def add_channel(self, channel: Channel) -> Self:
        return Register.channels.add(self, channel)

    def remove_channel(self, channel: Channel) -> Self:
        return Register.channels.remove(self, channel)

    def clear_channels(self) -> Self:
        return Register.channels.clear(self)

    def num_channel(self) -> int:
        return Register.channels.count(self)

    def get_channel_by_mrid(self, mrid: str) -> Channel | None:
        return Register.channels.get_by_mrid(self, mrid)
