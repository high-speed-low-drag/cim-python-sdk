"""CIM class CrewMember (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.operation_person_role import OperationPersonRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.crew import Crew


class CrewMember(OperationPersonRole):
    """Member of a crew."""

    __slots__ = ("_crew",)

    crew: One[Crew] = One(
        EndMeta(
            name="crew",
            cim_role="Crew",
            target="cim_python_sdk.model.iec61968.common.crew:Crew",
            many=False,
            lower=0,
            upper=1,
            inverse="crew_members",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CrewMember",
        package="TC57CIM/IEC61968/Common",
        guid="{4A7EA6E5-C75B-4670-B62D-3011D27EC685}",
        ends=(crew.meta,),
    )

    def __init__(
        self,
        *,
        crew: Crew | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if crew is not None:
            self.crew = crew
