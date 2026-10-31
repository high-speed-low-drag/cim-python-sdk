"""CIM class IntervalBlock (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.interval_reading import IntervalReading
    from cim_python_sdk.model.iec61968.metering.meter_reading import MeterReading
    from cim_python_sdk.model.iec61968.metering.pending_calculation import PendingCalculation
    from cim_python_sdk.model.iec61968.metering.reading_type import ReadingType


class IntervalBlock(CimObject):
    """Time sequence of readings of the same reading type. Contained interval readings may need
    conversion through the application of an offset and a scalar defined in associated
    pending.

    Table 548 shows all association ends of IntervalBlock with other classes.

    Table 548 – Association ends of Metering::IntervalBlock with other classes

    Associations

    name

    mult to

    type

    description

    0..*

    PendingCalculation

    0..1

    PendingCalculation

    Pending calculation to apply to interval reading values contained by this block (after
    which the resulting reading type is different than the original because it reflects the
    conversion result).

    0..*

    IntervalReadings

    0..*

    IntervalReading

    Interval reading contained in this block.

    0..*

    ReadingType

    0..1

    ReadingType

    Type information for interval reading values contained in this block.

    0..*

    MeterReading

    0..1

    MeterReading

    Meter reading containing this interval block.

    IntervalReading

    Data captured at regular intervals of time. Interval data could be captured as
    incremental data, absolute data, or relative data. The source for the data is usually a
    tariff quantity or an engineering quantity. Data is typically captured in time-tagged,
    uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min.

    Note: Interval Data is sometimes also called "Interval Data Readings" (IDR)."""

    __slots__ = ("_interval_readings", "_meter_reading", "_pending_calculation", "_reading_type")

    interval_readings: Many[IntervalReading] = Many(
        EndMeta(
            name="interval_readings",
            cim_role="IntervalReadings",
            target="cim_python_sdk.model.iec61968.metering.interval_reading:IntervalReading",
            many=True,
            lower=0,
            upper=None,
            inverse="interval_blocks",
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
            inverse="interval_blocks",
            aggregation="none",
        )
    )
    reading_type: One[ReadingType] = One(
        EndMeta(
            name="reading_type",
            cim_role="ReadingType",
            target="cim_python_sdk.model.iec61968.metering.reading_type:ReadingType",
            many=False,
            lower=0,
            upper=1,
            inverse="interval_blocks",
            aggregation="none",
        )
    )
    pending_calculation: One[PendingCalculation] = One(
        EndMeta(
            name="pending_calculation",
            cim_role="PendingCalculation",
            target="cim_python_sdk.model.iec61968.metering.pending_calculation:PendingCalculation",
            many=False,
            lower=0,
            upper=1,
            inverse="interval_blocks",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IntervalBlock",
        package="TC57CIM/IEC61968/Metering",
        guid="{7E23ABA5-5850-49e6-A741-F54C32CA3E2A}",
        ends=(
            interval_readings.meta,
            meter_reading.meta,
            reading_type.meta,
            pending_calculation.meta,
        ),
    )

    def __init__(
        self,
        *,
        interval_readings: Iterable[IntervalReading] | None = None,
        meter_reading: MeterReading | None = None,
        reading_type: ReadingType | None = None,
        pending_calculation: PendingCalculation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if interval_readings is not None:
            IntervalBlock.interval_readings.extend(self, interval_readings)
        if meter_reading is not None:
            self.meter_reading = meter_reading
        if reading_type is not None:
            self.reading_type = reading_type
        if pending_calculation is not None:
            self.pending_calculation = pending_calculation

    def add_interval_reading(self, interval_reading: IntervalReading) -> Self:
        return IntervalBlock.interval_readings.add(self, interval_reading)

    def remove_interval_reading(self, interval_reading: IntervalReading) -> Self:
        return IntervalBlock.interval_readings.remove(self, interval_reading)

    def clear_interval_readings(self) -> Self:
        return IntervalBlock.interval_readings.clear(self)

    def num_interval_reading(self) -> int:
        return IntervalBlock.interval_readings.count(self)

    def get_interval_reading_by_mrid(self, mrid: str) -> IntervalReading | None:
        return IntervalBlock.interval_readings.get_by_mrid(self, mrid)
