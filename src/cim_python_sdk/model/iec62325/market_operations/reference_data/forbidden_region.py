"""CIM class ForbiddenRegion (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource


class ForbiddenRegion(IdentifiedObject):
    """Forbbiden region is operating ranges where the units are unable to maintain steady
    operation without causing equipment damage. The four attributes that define a forbidden
    region are the low MW, the High MW, the crossing time, and the crossing cost."""

    __slots__ = ("_registered_resource", "cross_time", "crossing_cost", "high_mw", "low_mw")

    crossing_cost: float | None
    cross_time: int | None
    high_mw: float | None
    low_mw: float | None

    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="forbidden_region",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ForbiddenRegion",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{EA690114-4848-42f6-ACE5-C639BB0C8BC5}",
        attributes=(
            AttrMeta("crossing_cost", "crossingCost", "float", 0, 1, "primitive"),
            AttrMeta("cross_time", "crossTime", "int", 0, 1, "primitive"),
            AttrMeta("high_mw", "highMW", "float", 0, 1, "primitive"),
            AttrMeta("low_mw", "lowMW", "float", 0, 1, "primitive"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        crossing_cost: float | None = None,
        cross_time: int | None = None,
        high_mw: float | None = None,
        low_mw: float | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.crossing_cost = crossing_cost
        self.cross_time = cross_time
        self.high_mw = high_mw
        self.low_mw = low_mw
        if registered_resource is not None:
            ForbiddenRegion.registered_resource.extend(self, registered_resource)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ForbiddenRegion.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ForbiddenRegion.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return ForbiddenRegion.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return ForbiddenRegion.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return ForbiddenRegion.registered_resource.get_by_mrid(self, mrid)
