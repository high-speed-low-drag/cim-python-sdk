"""CIM class CoordinateSystem (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.location import Location


class CoordinateSystem(IdentifiedObject):
    """Coordinate reference system."""

    __slots__ = ("_locations", "crs_urn")

    crs_urn: str | None

    locations: Many[Location] = Many(
        EndMeta(
            name="locations",
            cim_role="Locations",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=True,
            lower=0,
            upper=None,
            inverse="coordinate_system",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CoordinateSystem",
        package="TC57CIM/IEC61968/Common",
        guid="{D7A22063-DBE9-467d-9E72-C32640FABCA0}",
        attributes=(AttrMeta("crs_urn", "crsUrn", "str", 0, 1, "primitive"),),
        ends=(locations.meta,),
    )

    def __init__(
        self,
        *,
        crs_urn: str | None = None,
        locations: Iterable[Location] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.crs_urn = crs_urn
        if locations is not None:
            CoordinateSystem.locations.extend(self, locations)

    def add_location(self, location: Location) -> Self:
        return CoordinateSystem.locations.add(self, location)

    def remove_location(self, location: Location) -> Self:
        return CoordinateSystem.locations.remove(self, location)

    def clear_locations(self) -> Self:
        return CoordinateSystem.locations.clear(self)

    def num_location(self) -> int:
        return CoordinateSystem.locations.count(self)

    def get_location_by_mrid(self, mrid: str) -> Location | None:
        return CoordinateSystem.locations.get_by_mrid(self, mrid)
