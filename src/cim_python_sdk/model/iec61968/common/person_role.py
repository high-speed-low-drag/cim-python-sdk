"""CIM class PersonRole (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.appointment import Appointment
    from cim_python_sdk.model.iec61968.common.configuration_event import ConfigurationEvent
    from cim_python_sdk.model.iec61968.common.person import Person


class PersonRole(IdentifiedObject):
    """CIM class PersonRole."""

    __slots__ = ("_appointments", "_configuration_events", "_person")

    person: One[Person] = One(
        EndMeta(
            name="person",
            cim_role="Person",
            target="cim_python_sdk.model.iec61968.common.person:Person",
            many=False,
            lower=0,
            upper=1,
            inverse="roles",
            aggregation="none",
        )
    )
    configuration_events: Many[ConfigurationEvent] = Many(
        EndMeta(
            name="configuration_events",
            cim_role="ConfigurationEvents",
            target="cim_python_sdk.model.iec61968.common.configuration_event:ConfigurationEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="changed_person_role",
            aggregation="none",
        )
    )
    appointments: Many[Appointment] = Many(
        EndMeta(
            name="appointments",
            cim_role="Appointments",
            target="cim_python_sdk.model.iec61968.common.appointment:Appointment",
            many=True,
            lower=0,
            upper=None,
            inverse="persons",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PersonRole",
        package="TC57CIM/IEC61968/Common",
        guid="{E24A8569-EF9C-450b-8B2D-2AB8A6CFAD85}",
        ends=(
            person.meta,
            configuration_events.meta,
            appointments.meta,
        ),
    )

    def __init__(
        self,
        *,
        person: Person | None = None,
        configuration_events: Iterable[ConfigurationEvent] | None = None,
        appointments: Iterable[Appointment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if person is not None:
            self.person = person
        if configuration_events is not None:
            PersonRole.configuration_events.extend(self, configuration_events)
        if appointments is not None:
            PersonRole.appointments.extend(self, appointments)

    def add_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return PersonRole.configuration_events.add(self, configuration_event)

    def remove_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return PersonRole.configuration_events.remove(self, configuration_event)

    def clear_configuration_events(self) -> Self:
        return PersonRole.configuration_events.clear(self)

    def num_configuration_event(self) -> int:
        return PersonRole.configuration_events.count(self)

    def get_configuration_event_by_mrid(self, mrid: str) -> ConfigurationEvent | None:
        return PersonRole.configuration_events.get_by_mrid(self, mrid)

    def add_appointment(self, appointment: Appointment) -> Self:
        return PersonRole.appointments.add(self, appointment)

    def remove_appointment(self, appointment: Appointment) -> Self:
        return PersonRole.appointments.remove(self, appointment)

    def clear_appointments(self) -> Self:
        return PersonRole.appointments.clear(self)

    def num_appointment(self) -> int:
        return PersonRole.appointments.count(self)

    def get_appointment_by_mrid(self, mrid: str) -> Appointment | None:
        return PersonRole.appointments.get_by_mrid(self, mrid)
