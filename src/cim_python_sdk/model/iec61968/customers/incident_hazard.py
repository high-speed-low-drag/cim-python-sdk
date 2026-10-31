"""CIM class IncidentHazard (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.hazard import Hazard

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket
    from cim_python_sdk.model.iec61968.operations.incident import Incident


class IncidentHazard(Hazard):
    """Hazardous situation associated with an incident. Examples are line down, gas leak, fire,
    etc."""

    __slots__ = ("_incident_incident_hazard", "_trouble_ticket_incident_hazard")

    incident_incident_hazard: One[Incident] = One(
        EndMeta(
            name="incident_incident_hazard",
            cim_role="Incident",
            target="cim_python_sdk.model.iec61968.operations.incident:Incident",
            many=False,
            lower=0,
            upper=1,
            inverse="incident_hazard",
            aggregation="none",
        )
    )
    trouble_ticket_incident_hazard: One[TroubleTicket] = One(
        EndMeta(
            name="trouble_ticket_incident_hazard",
            cim_role="TroubleTicket",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=False,
            lower=0,
            upper=1,
            inverse="incident_hazard",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IncidentHazard",
        package="TC57CIM/IEC61968/Customers",
        guid="{298E6C6D-2A99-4a63-A5D7-64FE018C3EB9}",
        ends=(
            incident_incident_hazard.meta,
            trouble_ticket_incident_hazard.meta,
        ),
    )

    def __init__(
        self,
        *,
        incident_incident_hazard: Incident | None = None,
        trouble_ticket_incident_hazard: TroubleTicket | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if incident_incident_hazard is not None:
            self.incident_incident_hazard = incident_incident_hazard
        if trouble_ticket_incident_hazard is not None:
            self.trouble_ticket_incident_hazard = trouble_ticket_incident_hazard
