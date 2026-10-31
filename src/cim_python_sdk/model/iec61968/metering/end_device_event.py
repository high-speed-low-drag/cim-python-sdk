"""CIM class EndDeviceEvent (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.end_device import EndDevice
    from cim_python_sdk.model.iec61968.metering.end_device_event_detail import EndDeviceEventDetail
    from cim_python_sdk.model.iec61968.metering.end_device_event_type import EndDeviceEventType
    from cim_python_sdk.model.iec61968.metering.meter_reading import MeterReading
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint


class EndDeviceEvent(ActivityRecord):
    """Event detected by a device function associated with the end device."""

    __slots__ = (
        "_end_device",
        "_end_device_event_details",
        "_end_device_event_type",
        "_meter_reading",
        "_usage_point",
        "issuer_id",
        "issuer_tracking_id",
        "user_id",
    )

    user_id: str | None
    issuer_tracking_id: str | None
    issuer_id: str | None

    end_device: One[EndDevice] = One(
        EndMeta(
            name="end_device",
            cim_role="EndDevice",
            target="cim_python_sdk.model.iec61968.metering.end_device:EndDevice",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device_events",
            aggregation="none",
        )
    )
    end_device_event_details: Many[EndDeviceEventDetail] = Many(
        EndMeta(
            name="end_device_event_details",
            cim_role="EndDeviceEventDetails",
            target="cim_python_sdk.model.iec61968.metering.end_device_event_detail:EndDeviceEventDetail",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_event",
            aggregation="none",
        )
    )
    end_device_event_type: One[EndDeviceEventType] = One(
        EndMeta(
            name="end_device_event_type",
            cim_role="EndDeviceEventType",
            target="cim_python_sdk.model.iec61968.metering.end_device_event_type:EndDeviceEventType",
            many=False,
            lower=1,
            upper=1,
            inverse="end_device_events",
            aggregation="none",
        )
    )
    usage_point: One[UsagePoint] = One(
        EndMeta(
            name="usage_point",
            cim_role="UsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device_events",
            aggregation="none",
        )
    )
    meter_reading: One[MeterReading] = One(
        EndMeta(
            name="meter_reading",
            cim_role="MeterReading",
            target="cim_python_sdk.model.iec61968.metering.meter_reading:MeterReading",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device_events",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDeviceEvent",
        package="TC57CIM/IEC61968/Metering",
        guid="{8788133B-E8AC-4df3-B820-7941507682EA}",
        attributes=(
            AttrMeta("user_id", "userID", "str", 0, 1, "primitive"),
            AttrMeta("issuer_tracking_id", "issuerTrackingID", "str", 0, 1, "primitive"),
            AttrMeta("issuer_id", "issuerID", "str", 0, 1, "primitive"),
        ),
        ends=(
            end_device.meta,
            end_device_event_details.meta,
            end_device_event_type.meta,
            usage_point.meta,
            meter_reading.meta,
        ),
    )

    def __init__(
        self,
        *,
        user_id: str | None = None,
        issuer_tracking_id: str | None = None,
        issuer_id: str | None = None,
        end_device: EndDevice | None = None,
        end_device_event_details: Iterable[EndDeviceEventDetail] | None = None,
        end_device_event_type: EndDeviceEventType | None = None,
        usage_point: UsagePoint | None = None,
        meter_reading: MeterReading | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.user_id = user_id
        self.issuer_tracking_id = issuer_tracking_id
        self.issuer_id = issuer_id
        if end_device is not None:
            self.end_device = end_device
        if end_device_event_details is not None:
            EndDeviceEvent.end_device_event_details.extend(self, end_device_event_details)
        if end_device_event_type is not None:
            self.end_device_event_type = end_device_event_type
        if usage_point is not None:
            self.usage_point = usage_point
        if meter_reading is not None:
            self.meter_reading = meter_reading

    def add_end_device_event_detail(self, end_device_event_detail: EndDeviceEventDetail) -> Self:
        return EndDeviceEvent.end_device_event_details.add(self, end_device_event_detail)

    def remove_end_device_event_detail(self, end_device_event_detail: EndDeviceEventDetail) -> Self:
        return EndDeviceEvent.end_device_event_details.remove(self, end_device_event_detail)

    def clear_end_device_event_details(self) -> Self:
        return EndDeviceEvent.end_device_event_details.clear(self)

    def num_end_device_event_detail(self) -> int:
        return EndDeviceEvent.end_device_event_details.count(self)
