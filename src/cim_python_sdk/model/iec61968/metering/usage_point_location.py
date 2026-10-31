"""CIM class UsagePointLocation (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.location import Location

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint


class UsagePointLocation(Location):
    """Location of an individual usage point."""

    __slots__ = ("_usage_points", "access_method", "remark", "site_access_problem")

    access_method: str | None
    site_access_problem: str | None
    remark: str | None

    usage_points: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_points",
            cim_role="UsagePoints",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_point_location",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UsagePointLocation",
        package="TC57CIM/IEC61968/Metering",
        guid="{355DF23F-F5D0-43f8-A206-1831971FB617}",
        attributes=(
            AttrMeta("access_method", "accessMethod", "str", 0, 1, "primitive"),
            AttrMeta("site_access_problem", "siteAccessProblem", "str", 0, 1, "primitive"),
            AttrMeta("remark", "remark", "str", 0, 1, "primitive"),
        ),
        ends=(usage_points.meta,),
    )

    def __init__(
        self,
        *,
        access_method: str | None = None,
        site_access_problem: str | None = None,
        remark: str | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.access_method = access_method
        self.site_access_problem = site_access_problem
        self.remark = remark
        if usage_points is not None:
            UsagePointLocation.usage_points.extend(self, usage_points)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return UsagePointLocation.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return UsagePointLocation.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return UsagePointLocation.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return UsagePointLocation.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return UsagePointLocation.usage_points.get_by_mrid(self, mrid)
