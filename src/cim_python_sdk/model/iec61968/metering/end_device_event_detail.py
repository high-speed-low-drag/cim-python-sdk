"""CIM class EndDeviceEventDetail (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.end_device_event import EndDeviceEvent
    from cim_python_sdk.model.iec61970.base.domain.string_quantity import StringQuantity


class EndDeviceEventDetail(CimObject):
    """Name-value pair, specific to end device events."""

    __slots__ = ("_end_device_event", "name", "value")

    name: str | None
    value: StringQuantity | None

    end_device_event: One[EndDeviceEvent] = One(
        EndMeta(
            name="end_device_event",
            cim_role="EndDeviceEvent",
            target="cim_python_sdk.model.iec61968.metering.end_device_event:EndDeviceEvent",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device_event_details",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDeviceEventDetail",
        package="TC57CIM/IEC61968/Metering",
        guid="{912FE8C4-6F96-4b12-A966-1CD1F895FFD3}",
        attributes=(
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
            AttrMeta("value", "value", "StringQuantity", 0, 1, "compound"),
        ),
        ends=(end_device_event.meta,),
    )

    def __init__(
        self,
        *,
        name: str | None = None,
        value: StringQuantity | None = None,
        end_device_event: EndDeviceEvent | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.value = value
        if end_device_event is not None:
            self.end_device_event = end_device_event
