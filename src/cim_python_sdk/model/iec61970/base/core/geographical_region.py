"""CIM class GeographicalRegion (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.sub_geographical_region import (
        SubGeographicalRegion,
    )


class GeographicalRegion(IdentifiedObject):
    """A geographical region of a power system network model."""

    __slots__ = ("_regions",)

    regions: Many[SubGeographicalRegion] = Many(
        EndMeta(
            name="regions",
            cim_role="Regions",
            target="cim_python_sdk.model.iec61970.base.core.sub_geographical_region:SubGeographicalRegion",
            many=True,
            lower=0,
            upper=None,
            inverse="region",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GeographicalRegion",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{F935232D-65FF-4720-BAFB-50639B7CA0AB}",
        ends=(regions.meta,),
    )

    def __init__(
        self,
        *,
        regions: Iterable[SubGeographicalRegion] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if regions is not None:
            GeographicalRegion.regions.extend(self, regions)

    def add_region(self, region: SubGeographicalRegion) -> Self:
        return GeographicalRegion.regions.add(self, region)

    def remove_region(self, region: SubGeographicalRegion) -> Self:
        return GeographicalRegion.regions.remove(self, region)

    def clear_regions(self) -> Self:
        return GeographicalRegion.regions.clear(self)

    def num_region(self) -> int:
        return GeographicalRegion.regions.count(self)

    def get_region_by_mrid(self, mrid: str) -> SubGeographicalRegion | None:
        return GeographicalRegion.regions.get_by_mrid(self, mrid)
