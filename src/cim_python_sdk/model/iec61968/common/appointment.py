"""CIM class Appointment (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.person_role import PersonRole
    from cim_python_sdk.model.iec61968.work.work import Work
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class Appointment(IdentifiedObject):
    """Meeting time and location."""

    __slots__ = ("_persons", "_works", "call_ahead", "meeting_interval")

    meeting_interval: DateTimeInterval | None
    call_ahead: bool | None

    works: Many[Work] = Many(
        EndMeta(
            name="works",
            cim_role="Works",
            target="cim_python_sdk.model.iec61968.work.work:Work",
            many=True,
            lower=0,
            upper=None,
            inverse="appointments",
            aggregation="none",
        )
    )
    persons: Many[PersonRole] = Many(
        EndMeta(
            name="persons",
            cim_role="Persons",
            target="cim_python_sdk.model.iec61968.common.person_role:PersonRole",
            many=True,
            lower=0,
            upper=None,
            inverse="appointments",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Appointment",
        package="TC57CIM/IEC61968/Common",
        guid="{C68E73D7-812C-4261-A207-A9781C6DB752}",
        attributes=(
            AttrMeta("meeting_interval", "meetingInterval", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("call_ahead", "callAhead", "bool", 0, 1, "primitive"),
        ),
        ends=(
            works.meta,
            persons.meta,
        ),
    )

    def __init__(
        self,
        *,
        meeting_interval: DateTimeInterval | None = None,
        call_ahead: bool | None = None,
        works: Iterable[Work] | None = None,
        persons: Iterable[PersonRole] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.meeting_interval = meeting_interval
        self.call_ahead = call_ahead
        if works is not None:
            Appointment.works.extend(self, works)
        if persons is not None:
            Appointment.persons.extend(self, persons)

    def add_work(self, work: Work) -> Self:
        return Appointment.works.add(self, work)

    def remove_work(self, work: Work) -> Self:
        return Appointment.works.remove(self, work)

    def clear_works(self) -> Self:
        return Appointment.works.clear(self)

    def num_work(self) -> int:
        return Appointment.works.count(self)

    def get_work_by_mrid(self, mrid: str) -> Work | None:
        return Appointment.works.get_by_mrid(self, mrid)

    def add_person(self, person: PersonRole) -> Self:
        return Appointment.persons.add(self, person)

    def remove_person(self, person: PersonRole) -> Self:
        return Appointment.persons.remove(self, person)

    def clear_persons(self) -> Self:
        return Appointment.persons.clear(self)

    def num_person(self) -> int:
        return Appointment.persons.count(self)

    def get_person_by_mrid(self, mrid: str) -> PersonRole | None:
        return Appointment.persons.get_by_mrid(self, mrid)
