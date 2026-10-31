"""CIM class Route (TC57CIM/IEC61968/InfIEC61968/InfLocations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew import OldCrew


class Route(IdentifiedObject):
    """Route that is followed, for example by service crews."""

    __slots__ = ("_crews", "_locations", "status", "type")

    type: str | None
    status: Status | None

    locations: Many[Location] = Many(
        EndMeta(
            name="locations",
            cim_role="Locations",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=True,
            lower=0,
            upper=None,
            inverse="routes",
            aggregation="none",
        )
    )
    crews: Many[OldCrew] = Many(
        EndMeta(
            name="crews",
            cim_role="Crews",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew:OldCrew",
            many=True,
            lower=0,
            upper=None,
            inverse="route",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Route",
        package="TC57CIM/IEC61968/InfIEC61968/InfLocations",
        guid="{97D5A1C9-7293-4f53-9E36-6436203F3080}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            locations.meta,
            crews.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        status: Status | None = None,
        locations: Iterable[Location] | None = None,
        crews: Iterable[OldCrew] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.status = status
        if locations is not None:
            Route.locations.extend(self, locations)
        if crews is not None:
            Route.crews.extend(self, crews)

    def add_location(self, location: Location) -> Self:
        return Route.locations.add(self, location)

    def remove_location(self, location: Location) -> Self:
        return Route.locations.remove(self, location)

    def clear_locations(self) -> Self:
        return Route.locations.clear(self)

    def num_location(self) -> int:
        return Route.locations.count(self)

    def get_location_by_mrid(self, mrid: str) -> Location | None:
        return Route.locations.get_by_mrid(self, mrid)

    def add_crew(self, crew: OldCrew) -> Self:
        return Route.crews.add(self, crew)

    def remove_crew(self, crew: OldCrew) -> Self:
        return Route.crews.remove(self, crew)

    def clear_crews(self) -> Self:
        return Route.crews.clear(self)

    def num_crew(self) -> int:
        return Route.crews.count(self)

    def get_crew_by_mrid(self, mrid: str) -> OldCrew | None:
        return Route.crews.get_by_mrid(self, mrid)
