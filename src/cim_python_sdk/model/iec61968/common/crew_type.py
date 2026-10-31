"""CIM class CrewType (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.crew import Crew


class CrewType(IdentifiedObject):
    """Custom description of the type of crew. This may be used to determine the type of work
    the crew can be assigned to. Examples include repair, tree trimming, switching, etc."""

    __slots__ = ("_crews",)

    crews: Many[Crew] = Many(
        EndMeta(
            name="crews",
            cim_role="Crews",
            target="cim_python_sdk.model.iec61968.common.crew:Crew",
            many=True,
            lower=0,
            upper=None,
            inverse="crew_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CrewType",
        package="TC57CIM/IEC61968/Common",
        guid="{5D649DCB-6D06-49f7-A675-23C3E5B180DC}",
        ends=(crews.meta,),
    )

    def __init__(
        self,
        *,
        crews: Iterable[Crew] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if crews is not None:
            CrewType.crews.extend(self, crews)

    def add_crew(self, crew: Crew) -> Self:
        return CrewType.crews.add(self, crew)

    def remove_crew(self, crew: Crew) -> Self:
        return CrewType.crews.remove(self, crew)

    def clear_crews(self) -> Self:
        return CrewType.crews.clear(self)

    def num_crew(self) -> int:
        return CrewType.crews.count(self)

    def get_crew_by_mrid(self, mrid: str) -> Crew | None:
        return CrewType.crews.get_by_mrid(self, mrid)
