"""CIM class Hazard (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket
    from cim_python_sdk.model.iec61968.operations.incident import Incident


class Hazard(IdentifiedObject):
    """An object or a condition that is a danger for causing loss or perils to an asset and/or
    people."""

    __slots__ = ("_incident", "_trouble_ticket", "status", "type")

    type: str | None
    status: Status | None

    trouble_ticket: One[TroubleTicket] = One(
        EndMeta(
            name="trouble_ticket",
            cim_role="TroubleTicket",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=False,
            lower=0,
            upper=1,
            inverse="hazard",
            aggregation="none",
        )
    )
    incident: One[Incident] = One(
        EndMeta(
            name="incident",
            cim_role="Incident",
            target="cim_python_sdk.model.iec61968.operations.incident:Incident",
            many=False,
            lower=0,
            upper=1,
            inverse="hazard",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Hazard",
        package="TC57CIM/IEC61968/Common",
        guid="{387A5492-C5F8-4537-9F38-36348F45D3F9}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            trouble_ticket.meta,
            incident.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        status: Status | None = None,
        trouble_ticket: TroubleTicket | None = None,
        incident: Incident | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.status = status
        if trouble_ticket is not None:
            self.trouble_ticket = trouble_ticket
        if incident is not None:
            self.incident = incident
