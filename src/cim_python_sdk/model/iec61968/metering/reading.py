"""CIM class Reading (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.metering.base_reading import BaseReading

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.meter_reading import MeterReading
    from cim_python_sdk.model.iec61968.metering.reading_reason_kind import ReadingReasonKind
    from cim_python_sdk.model.iec61968.metering.reading_type import ReadingType


class Reading(BaseReading):
    """Specific value measured by a meter or other asset, or calculated by a system. Each
    Reading is associated with a specific ReadingType."""

    __slots__ = ("_meter_readings", "_reading_type", "position", "reason", "value_missing")

    reason: ReadingReasonKind | None
    position: int | None
    value_missing: bool | None

    meter_readings: Many[MeterReading] = Many(
        EndMeta(
            name="meter_readings",
            cim_role="MeterReadings",
            target="cim_python_sdk.model.iec61968.metering.meter_reading:MeterReading",
            many=True,
            lower=0,
            upper=None,
            inverse="readings",
            aggregation="none",
        )
    )
    reading_type: One[ReadingType] = One(
        EndMeta(
            name="reading_type",
            cim_role="ReadingType",
            target="cim_python_sdk.model.iec61968.metering.reading_type:ReadingType",
            many=False,
            lower=1,
            upper=1,
            inverse="readings",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Reading",
        package="TC57CIM/IEC61968/Metering",
        guid="{7E8C3166-9471-4e2c-8BC5-082F9D4B2F53}",
        attributes=(
            AttrMeta("reason", "reason", "ReadingReasonKind", 0, 1, "enumeration"),
            AttrMeta("position", "position", "int", 0, 1, "primitive"),
            AttrMeta("value_missing", "valueMissing", "bool", 0, 1, "primitive"),
        ),
        ends=(
            meter_readings.meta,
            reading_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        reason: ReadingReasonKind | None = None,
        position: int | None = None,
        value_missing: bool | None = None,
        meter_readings: Iterable[MeterReading] | None = None,
        reading_type: ReadingType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.reason = reason
        self.position = position
        self.value_missing = value_missing
        if meter_readings is not None:
            Reading.meter_readings.extend(self, meter_readings)
        if reading_type is not None:
            self.reading_type = reading_type

    def add_meter_reading(self, meter_reading: MeterReading) -> Self:
        return Reading.meter_readings.add(self, meter_reading)

    def remove_meter_reading(self, meter_reading: MeterReading) -> Self:
        return Reading.meter_readings.remove(self, meter_reading)

    def clear_meter_readings(self) -> Self:
        return Reading.meter_readings.clear(self)

    def num_meter_reading(self) -> int:
        return Reading.meter_readings.count(self)

    def get_meter_reading_by_mrid(self, mrid: str) -> MeterReading | None:
        return Reading.meter_readings.get_by_mrid(self, mrid)
