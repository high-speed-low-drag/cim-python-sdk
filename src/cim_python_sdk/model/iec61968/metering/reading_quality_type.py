"""CIM class ReadingQualityType (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.reading_quality import ReadingQuality


class ReadingQualityType(IdentifiedObject):
    """Detailed description for a quality of a reading value, produced by an end device or a
    system. Values in attributes allow for creation of the recommended codes to be used for
    identifying reading value quality codes as follows: <systemId>.<category>.<subCategory>."""

    __slots__ = ("_reading_qualities", "category", "sub_category", "system_id")

    system_id: str | None
    category: str | None
    sub_category: str | None

    reading_qualities: Many[ReadingQuality] = Many(
        EndMeta(
            name="reading_qualities",
            cim_role="ReadingQualities",
            target="cim_python_sdk.model.iec61968.metering.reading_quality:ReadingQuality",
            many=True,
            lower=0,
            upper=None,
            inverse="reading_quality_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReadingQualityType",
        package="TC57CIM/IEC61968/Metering",
        guid="{20EE2D53-52C6-4a74-8009-F135C62FE4F8}",
        attributes=(
            AttrMeta("system_id", "systemId", "str", 0, 1, "primitive"),
            AttrMeta("category", "category", "str", 0, 1, "primitive"),
            AttrMeta("sub_category", "subCategory", "str", 0, 1, "primitive"),
        ),
        ends=(reading_qualities.meta,),
    )

    def __init__(
        self,
        *,
        system_id: str | None = None,
        category: str | None = None,
        sub_category: str | None = None,
        reading_qualities: Iterable[ReadingQuality] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.system_id = system_id
        self.category = category
        self.sub_category = sub_category
        if reading_qualities is not None:
            ReadingQualityType.reading_qualities.extend(self, reading_qualities)

    def add_reading_quality(self, reading_quality: ReadingQuality) -> Self:
        return ReadingQualityType.reading_qualities.add(self, reading_quality)

    def remove_reading_quality(self, reading_quality: ReadingQuality) -> Self:
        return ReadingQualityType.reading_qualities.remove(self, reading_quality)

    def clear_reading_qualities(self) -> Self:
        return ReadingQualityType.reading_qualities.clear(self)

    def num_reading_quality(self) -> int:
        return ReadingQualityType.reading_qualities.count(self)
