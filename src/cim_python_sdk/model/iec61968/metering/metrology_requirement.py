"""CIM class MetrologyRequirement (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.reading_reason_kind import ReadingReasonKind
    from cim_python_sdk.model.iec61968.metering.reading_type import ReadingType
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint


class MetrologyRequirement(IdentifiedObject):
    """A specification of the metering requirements for a particular point within a network."""

    __slots__ = ("_reading_types", "_usage_points", "reason")

    reason: ReadingReasonKind | None

    usage_points: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_points",
            cim_role="UsagePoints",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="metrology_requirements",
            aggregation="none",
        )
    )
    reading_types: Many[ReadingType] = Many(
        EndMeta(
            name="reading_types",
            cim_role="ReadingTypes",
            target="cim_python_sdk.model.iec61968.metering.reading_type:ReadingType",
            many=True,
            lower=1,
            upper=None,
            inverse="metrology_requirements",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MetrologyRequirement",
        package="TC57CIM/IEC61968/Metering",
        guid="{E81DF00E-E1C5-414a-852C-D627D2A1A51E}",
        attributes=(AttrMeta("reason", "reason", "ReadingReasonKind", 0, 1, "enumeration"),),
        ends=(
            usage_points.meta,
            reading_types.meta,
        ),
    )

    def __init__(
        self,
        *,
        reason: ReadingReasonKind | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        reading_types: Iterable[ReadingType] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.reason = reason
        if usage_points is not None:
            MetrologyRequirement.usage_points.extend(self, usage_points)
        if reading_types is not None:
            MetrologyRequirement.reading_types.extend(self, reading_types)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return MetrologyRequirement.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return MetrologyRequirement.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return MetrologyRequirement.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return MetrologyRequirement.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return MetrologyRequirement.usage_points.get_by_mrid(self, mrid)

    def add_reading_type(self, reading_type: ReadingType) -> Self:
        return MetrologyRequirement.reading_types.add(self, reading_type)

    def remove_reading_type(self, reading_type: ReadingType) -> Self:
        return MetrologyRequirement.reading_types.remove(self, reading_type)

    def clear_reading_types(self) -> Self:
        return MetrologyRequirement.reading_types.clear(self)

    def num_reading_type(self) -> int:
        return MetrologyRequirement.reading_types.count(self)

    def get_reading_type_by_mrid(self, mrid: str) -> ReadingType | None:
        return MetrologyRequirement.reading_types.get_by_mrid(self, mrid)
