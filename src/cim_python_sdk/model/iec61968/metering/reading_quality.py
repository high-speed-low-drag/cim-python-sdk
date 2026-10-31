"""CIM class ReadingQuality (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.base_reading import BaseReading
    from cim_python_sdk.model.iec61968.metering.reading_quality_type import ReadingQualityType


class ReadingQuality(CimObject):
    """Quality of a specific reading value or interval reading value. Note that more than one
    quality may be applicable to a given reading. Typically not used unless problems or
    unusual conditions occur (i.e., quality for each reading is assumed to be good unless
    stated otherwise in associated reading quality type). It can also be used with the
    corresponding reading quality type to indicate that the validation has been performed
    and succeeded."""

    __slots__ = ("_reading", "_reading_quality_type", "comment", "source", "time_stamp")

    time_stamp: _dt.datetime | None
    source: str | None
    comment: str | None

    reading_quality_type: One[ReadingQualityType] = One(
        EndMeta(
            name="reading_quality_type",
            cim_role="ReadingQualityType",
            target="cim_python_sdk.model.iec61968.metering.reading_quality_type:ReadingQualityType",
            many=False,
            lower=1,
            upper=1,
            inverse="reading_qualities",
            aggregation="none",
        )
    )
    reading: One[BaseReading] = One(
        EndMeta(
            name="reading",
            cim_role="Reading",
            target="cim_python_sdk.model.iec61968.metering.base_reading:BaseReading",
            many=False,
            lower=0,
            upper=1,
            inverse="reading_qualities",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReadingQuality",
        package="TC57CIM/IEC61968/Metering",
        guid="{4AB2B23E-75A5-41d5-A46F-B9D414AFBD38}",
        attributes=(
            AttrMeta("time_stamp", "timeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("source", "source", "str", 0, 1, "primitive"),
            AttrMeta("comment", "comment", "str", 0, 1, "primitive"),
        ),
        ends=(
            reading_quality_type.meta,
            reading.meta,
        ),
    )

    def __init__(
        self,
        *,
        time_stamp: _dt.datetime | None = None,
        source: str | None = None,
        comment: str | None = None,
        reading_quality_type: ReadingQualityType | None = None,
        reading: BaseReading | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time_stamp = time_stamp
        self.source = source
        self.comment = comment
        if reading_quality_type is not None:
            self.reading_quality_type = reading_quality_type
        if reading is not None:
            self.reading = reading
