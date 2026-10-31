"""CIM class BaseReading (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.reading_quality import ReadingQuality
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class BaseReading(MeasurementValue):
    """Common representation for reading values. Note that a reading value may have multiple
    qualities, as produced by various systems ('ReadingQuality.source')."""

    __slots__ = ("_reading_qualities", "reported_date_time", "source", "time_period", "value")

    value: str | None
    source: str | None
    time_period: DateTimeInterval | None
    reported_date_time: _dt.datetime | None

    reading_qualities: Many[ReadingQuality] = Many(
        EndMeta(
            name="reading_qualities",
            cim_role="ReadingQualities",
            target="cim_python_sdk.model.iec61968.metering.reading_quality:ReadingQuality",
            many=True,
            lower=0,
            upper=None,
            inverse="reading",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BaseReading",
        package="TC57CIM/IEC61968/Metering",
        guid="{65C0D3F7-9A2B-47ed-8E6B-6F552338C7FA}",
        attributes=(
            AttrMeta("value", "value", "str", 0, 1, "primitive"),
            AttrMeta("source", "source", "str", 0, 1, "primitive"),
            AttrMeta("time_period", "timePeriod", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("reported_date_time", "reportedDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(reading_qualities.meta,),
    )

    def __init__(
        self,
        *,
        value: str | None = None,
        source: str | None = None,
        time_period: DateTimeInterval | None = None,
        reported_date_time: _dt.datetime | None = None,
        reading_qualities: Iterable[ReadingQuality] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
        self.source = source
        self.time_period = time_period
        self.reported_date_time = reported_date_time
        if reading_qualities is not None:
            BaseReading.reading_qualities.extend(self, reading_qualities)

    def add_reading_quality(self, reading_quality: ReadingQuality) -> Self:
        return BaseReading.reading_qualities.add(self, reading_quality)

    def remove_reading_quality(self, reading_quality: ReadingQuality) -> Self:
        return BaseReading.reading_qualities.remove(self, reading_quality)

    def clear_reading_qualities(self) -> Self:
        return BaseReading.reading_qualities.clear(self)

    def num_reading_quality(self) -> int:
        return BaseReading.reading_qualities.count(self)
