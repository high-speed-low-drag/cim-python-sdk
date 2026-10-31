"""CIM class MeterReading (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.metering.end_device_event import EndDeviceEvent
    from cim_python_sdk.model.iec61968.metering.interval_block import IntervalBlock
    from cim_python_sdk.model.iec61968.metering.meter import Meter
    from cim_python_sdk.model.iec61968.metering.reading import Reading
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class MeterReading(IdentifiedObject):
    """Set of values obtained from the meter."""

    __slots__ = (
        "_customer_agreement",
        "_end_device_events",
        "_interval_blocks",
        "_meter",
        "_readings",
        "_usage_point",
        "is_coincident_trigger",
        "values_interval",
    )

    values_interval: DateTimeInterval | None
    is_coincident_trigger: bool | None

    interval_blocks: Many[IntervalBlock] = Many(
        EndMeta(
            name="interval_blocks",
            cim_role="IntervalBlocks",
            target="cim_python_sdk.model.iec61968.metering.interval_block:IntervalBlock",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_reading",
            aggregation="none",
        )
    )
    readings: Many[Reading] = Many(
        EndMeta(
            name="readings",
            cim_role="Readings",
            target="cim_python_sdk.model.iec61968.metering.reading:Reading",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_readings",
            aggregation="none",
        )
    )
    customer_agreement: One[CustomerAgreement] = One(
        EndMeta(
            name="customer_agreement",
            cim_role="CustomerAgreement",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=False,
            lower=0,
            upper=1,
            inverse="meter_readings",
            aggregation="none",
        )
    )
    meter: One[Meter] = One(
        EndMeta(
            name="meter",
            cim_role="Meter",
            target="cim_python_sdk.model.iec61968.metering.meter:Meter",
            many=False,
            lower=0,
            upper=1,
            inverse="meter_readings",
            aggregation="none",
        )
    )
    end_device_events: Many[EndDeviceEvent] = Many(
        EndMeta(
            name="end_device_events",
            cim_role="EndDeviceEvents",
            target="cim_python_sdk.model.iec61968.metering.end_device_event:EndDeviceEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_reading",
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
            inverse="meter_readings",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeterReading",
        package="TC57CIM/IEC61968/Metering",
        guid="{115DC4EA-8B92-4bfa-B8BE-4AC3A83934CD}",
        attributes=(
            AttrMeta("values_interval", "valuesInterval", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("is_coincident_trigger", "isCoincidentTrigger", "bool", 0, 1, "primitive"),
        ),
        ends=(
            interval_blocks.meta,
            readings.meta,
            customer_agreement.meta,
            meter.meta,
            end_device_events.meta,
            usage_point.meta,
        ),
    )

    def __init__(
        self,
        *,
        values_interval: DateTimeInterval | None = None,
        is_coincident_trigger: bool | None = None,
        interval_blocks: Iterable[IntervalBlock] | None = None,
        readings: Iterable[Reading] | None = None,
        customer_agreement: CustomerAgreement | None = None,
        meter: Meter | None = None,
        end_device_events: Iterable[EndDeviceEvent] | None = None,
        usage_point: UsagePoint | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.values_interval = values_interval
        self.is_coincident_trigger = is_coincident_trigger
        if interval_blocks is not None:
            MeterReading.interval_blocks.extend(self, interval_blocks)
        if readings is not None:
            MeterReading.readings.extend(self, readings)
        if customer_agreement is not None:
            self.customer_agreement = customer_agreement
        if meter is not None:
            self.meter = meter
        if end_device_events is not None:
            MeterReading.end_device_events.extend(self, end_device_events)
        if usage_point is not None:
            self.usage_point = usage_point

    def add_interval_block(self, interval_block: IntervalBlock) -> Self:
        return MeterReading.interval_blocks.add(self, interval_block)

    def remove_interval_block(self, interval_block: IntervalBlock) -> Self:
        return MeterReading.interval_blocks.remove(self, interval_block)

    def clear_interval_blocks(self) -> Self:
        return MeterReading.interval_blocks.clear(self)

    def num_interval_block(self) -> int:
        return MeterReading.interval_blocks.count(self)

    def add_reading(self, reading: Reading) -> Self:
        return MeterReading.readings.add(self, reading)

    def remove_reading(self, reading: Reading) -> Self:
        return MeterReading.readings.remove(self, reading)

    def clear_readings(self) -> Self:
        return MeterReading.readings.clear(self)

    def num_reading(self) -> int:
        return MeterReading.readings.count(self)

    def get_reading_by_mrid(self, mrid: str) -> Reading | None:
        return MeterReading.readings.get_by_mrid(self, mrid)

    def add_end_device_event(self, end_device_event: EndDeviceEvent) -> Self:
        return MeterReading.end_device_events.add(self, end_device_event)

    def remove_end_device_event(self, end_device_event: EndDeviceEvent) -> Self:
        return MeterReading.end_device_events.remove(self, end_device_event)

    def clear_end_device_events(self) -> Self:
        return MeterReading.end_device_events.clear(self)

    def num_end_device_event(self) -> int:
        return MeterReading.end_device_events.count(self)

    def get_end_device_event_by_mrid(self, mrid: str) -> EndDeviceEvent | None:
        return MeterReading.end_device_events.get_by_mrid(self, mrid)
