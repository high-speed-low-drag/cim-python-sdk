"""CIM class OrganisationRole (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.configuration_event import ConfigurationEvent
    from cim_python_sdk.model.iec61968.common.organisation import Organisation


class OrganisationRole(IdentifiedObject):
    """Identifies a way in which an organisation may participate in the utility enterprise
    (e.g., customer, manufacturer, etc)."""

    __slots__ = ("_configuration_events", "_organisation")

    organisation: One[Organisation] = One(
        EndMeta(
            name="organisation",
            cim_role="Organisation",
            target="cim_python_sdk.model.iec61968.common.organisation:Organisation",
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
            inverse="changed_organisation_role",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OrganisationRole",
        package="TC57CIM/IEC61968/Common",
        guid="{01405DC2-1603-450e-BE69-A6C7E7629423}",
        ends=(
            organisation.meta,
            configuration_events.meta,
        ),
    )

    def __init__(
        self,
        *,
        organisation: Organisation | None = None,
        configuration_events: Iterable[ConfigurationEvent] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if organisation is not None:
            self.organisation = organisation
        if configuration_events is not None:
            OrganisationRole.configuration_events.extend(self, configuration_events)

    def add_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return OrganisationRole.configuration_events.add(self, configuration_event)

    def remove_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return OrganisationRole.configuration_events.remove(self, configuration_event)

    def clear_configuration_events(self) -> Self:
        return OrganisationRole.configuration_events.clear(self)

    def num_configuration_event(self) -> int:
        return OrganisationRole.configuration_events.count(self)

    def get_configuration_event_by_mrid(self, mrid: str) -> ConfigurationEvent | None:
        return OrganisationRole.configuration_events.get_by_mrid(self, mrid)
