"""CIM class EndDeviceEventType (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.end_device_event import EndDeviceEvent


class EndDeviceEventType(IdentifiedObject):
    """Detailed description for an event produced by an end device. Values in attributes allow
    for creation of recommended codes to be used for identifying end device events as
    follows: <type>.<domain>.<subDomain>.<eventOrAction>."""

    __slots__ = ("_end_device_events", "domain", "event_or_action", "sub_domain", "type")

    type: str | None
    domain: str | None
    sub_domain: str | None
    event_or_action: str | None

    end_device_events: Many[EndDeviceEvent] = Many(
        EndMeta(
            name="end_device_events",
            cim_role="EndDeviceEvents",
            target="cim_python_sdk.model.iec61968.metering.end_device_event:EndDeviceEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_event_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDeviceEventType",
        package="TC57CIM/IEC61968/Metering",
        guid="{EFC40D9F-D56D-4433-B46E-2FE1A129CF89}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("domain", "domain", "str", 0, 1, "primitive"),
            AttrMeta("sub_domain", "subDomain", "str", 0, 1, "primitive"),
            AttrMeta("event_or_action", "eventOrAction", "str", 0, 1, "primitive"),
        ),
        ends=(end_device_events.meta,),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        domain: str | None = None,
        sub_domain: str | None = None,
        event_or_action: str | None = None,
        end_device_events: Iterable[EndDeviceEvent] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.domain = domain
        self.sub_domain = sub_domain
        self.event_or_action = event_or_action
        if end_device_events is not None:
            EndDeviceEventType.end_device_events.extend(self, end_device_events)

    def add_end_device_event(self, end_device_event: EndDeviceEvent) -> Self:
        return EndDeviceEventType.end_device_events.add(self, end_device_event)

    def remove_end_device_event(self, end_device_event: EndDeviceEvent) -> Self:
        return EndDeviceEventType.end_device_events.remove(self, end_device_event)

    def clear_end_device_events(self) -> Self:
        return EndDeviceEventType.end_device_events.clear(self)

    def num_end_device_event(self) -> int:
        return EndDeviceEventType.end_device_events.count(self)

    def get_end_device_event_by_mrid(self, mrid: str) -> EndDeviceEvent | None:
        return EndDeviceEventType.end_device_events.get_by_mrid(self, mrid)
