"""CIM class OneCallRequest (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.work.work_location import WorkLocation


class OneCallRequest(WorkDocument):
    """A request for other utilities to mark their underground facilities prior to commencement
    of construction and/or maintenance."""

    __slots__ = ("_work_locations", "explosives_used", "marked_indicator", "marking_instruction")

    marked_indicator: bool | None
    explosives_used: bool | None
    marking_instruction: str | None

    work_locations: Many[WorkLocation] = Many(
        EndMeta(
            name="work_locations",
            cim_role="WorkLocations",
            target="cim_python_sdk.model.iec61968.work.work_location:WorkLocation",
            many=True,
            lower=0,
            upper=None,
            inverse="one_call_request",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OneCallRequest",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{8C193B90-CD98-4398-919A-155CDCEEC197}",
        attributes=(
            AttrMeta("marked_indicator", "markedIndicator", "bool", 0, 1, "primitive"),
            AttrMeta("explosives_used", "explosivesUsed", "bool", 0, 1, "primitive"),
            AttrMeta("marking_instruction", "markingInstruction", "str", 0, 1, "primitive"),
        ),
        ends=(work_locations.meta,),
    )

    def __init__(
        self,
        *,
        marked_indicator: bool | None = None,
        explosives_used: bool | None = None,
        marking_instruction: str | None = None,
        work_locations: Iterable[WorkLocation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.marked_indicator = marked_indicator
        self.explosives_used = explosives_used
        self.marking_instruction = marking_instruction
        if work_locations is not None:
            OneCallRequest.work_locations.extend(self, work_locations)

    def add_work_location(self, work_location: WorkLocation) -> Self:
        return OneCallRequest.work_locations.add(self, work_location)

    def remove_work_location(self, work_location: WorkLocation) -> Self:
        return OneCallRequest.work_locations.remove(self, work_location)

    def clear_work_locations(self) -> Self:
        return OneCallRequest.work_locations.clear(self)

    def num_work_location(self) -> int:
        return OneCallRequest.work_locations.count(self)

    def get_work_location_by_mrid(self, mrid: str) -> WorkLocation | None:
        return OneCallRequest.work_locations.get_by_mrid(self, mrid)
