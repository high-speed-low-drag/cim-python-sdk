"""CIM class OldCrew (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.crew import Crew

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.route import Route
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.assignment import Assignment
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.capability import Capability
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.shift_pattern import ShiftPattern


class OldCrew(Crew):
    """A crew is a group of people with specific skills, tools, and vehicles."""

    __slots__ = ("_assignments", "_capabilities", "_locations", "_route", "_shift_patterns", "type")

    type: str | None

    shift_patterns: Many[ShiftPattern] = Many(
        EndMeta(
            name="shift_patterns",
            cim_role="ShiftPatterns",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.shift_pattern:ShiftPattern",
            many=True,
            lower=0,
            upper=None,
            inverse="crews",
            aggregation="none",
        )
    )
    locations: Many[Location] = Many(
        EndMeta(
            name="locations",
            cim_role="Locations",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=True,
            lower=0,
            upper=None,
            inverse="crews",
            aggregation="none",
        )
    )
    capabilities: Many[Capability] = Many(
        EndMeta(
            name="capabilities",
            cim_role="Capabilities",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.capability:Capability",
            many=True,
            lower=0,
            upper=None,
            inverse="crew",
            aggregation="none",
        )
    )
    assignments: Many[Assignment] = Many(
        EndMeta(
            name="assignments",
            cim_role="Assignments",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.assignment:Assignment",
            many=True,
            lower=0,
            upper=None,
            inverse="crews",
            aggregation="none",
        )
    )
    route: One[Route] = One(
        EndMeta(
            name="route",
            cim_role="Route",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.route:Route",
            many=False,
            lower=0,
            upper=1,
            inverse="crews",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OldCrew",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{DDDFE85B-09C2-4ae1-85F8-E85572AB27F8}",
        attributes=(AttrMeta("type", "type", "str", 0, 1, "primitive"),),
        ends=(
            shift_patterns.meta,
            locations.meta,
            capabilities.meta,
            assignments.meta,
            route.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        shift_patterns: Iterable[ShiftPattern] | None = None,
        locations: Iterable[Location] | None = None,
        capabilities: Iterable[Capability] | None = None,
        assignments: Iterable[Assignment] | None = None,
        route: Route | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        if shift_patterns is not None:
            OldCrew.shift_patterns.extend(self, shift_patterns)
        if locations is not None:
            OldCrew.locations.extend(self, locations)
        if capabilities is not None:
            OldCrew.capabilities.extend(self, capabilities)
        if assignments is not None:
            OldCrew.assignments.extend(self, assignments)
        if route is not None:
            self.route = route

    def add_shift_pattern(self, shift_pattern: ShiftPattern) -> Self:
        return OldCrew.shift_patterns.add(self, shift_pattern)

    def remove_shift_pattern(self, shift_pattern: ShiftPattern) -> Self:
        return OldCrew.shift_patterns.remove(self, shift_pattern)

    def clear_shift_patterns(self) -> Self:
        return OldCrew.shift_patterns.clear(self)

    def num_shift_pattern(self) -> int:
        return OldCrew.shift_patterns.count(self)

    def get_shift_pattern_by_mrid(self, mrid: str) -> ShiftPattern | None:
        return OldCrew.shift_patterns.get_by_mrid(self, mrid)

    def add_locations(self, locations: Location) -> Self:
        return OldCrew.locations.add(self, locations)

    def remove_locations(self, locations: Location) -> Self:
        return OldCrew.locations.remove(self, locations)

    def clear_locations(self) -> Self:
        return OldCrew.locations.clear(self)

    def num_locations(self) -> int:
        return OldCrew.locations.count(self)

    def get_locations_by_mrid(self, mrid: str) -> Location | None:
        return OldCrew.locations.get_by_mrid(self, mrid)

    def add_capability(self, capability: Capability) -> Self:
        return OldCrew.capabilities.add(self, capability)

    def remove_capability(self, capability: Capability) -> Self:
        return OldCrew.capabilities.remove(self, capability)

    def clear_capabilities(self) -> Self:
        return OldCrew.capabilities.clear(self)

    def num_capability(self) -> int:
        return OldCrew.capabilities.count(self)

    def get_capability_by_mrid(self, mrid: str) -> Capability | None:
        return OldCrew.capabilities.get_by_mrid(self, mrid)

    def add_assignment(self, assignment: Assignment) -> Self:
        return OldCrew.assignments.add(self, assignment)

    def remove_assignment(self, assignment: Assignment) -> Self:
        return OldCrew.assignments.remove(self, assignment)

    def clear_assignments(self) -> Self:
        return OldCrew.assignments.clear(self)

    def num_assignment(self) -> int:
        return OldCrew.assignments.count(self)

    def get_assignment_by_mrid(self, mrid: str) -> Assignment | None:
        return OldCrew.assignments.get_by_mrid(self, mrid)
