"""CIM class TroubleReporter (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.operation_person_role import OperationPersonRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket


class TroubleReporter(OperationPersonRole):
    """Type of Person reporting the Trouble - Customer, First Responder, Passer-by, etc."""

    __slots__ = ("_trouble_ticket", "trouble_reporter_type")

    trouble_reporter_type: str | None

    trouble_ticket: Many[TroubleTicket] = Many(
        EndMeta(
            name="trouble_ticket",
            cim_role="TroubleTicket",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=True,
            lower=0,
            upper=None,
            inverse="trouble_reporter",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TroubleReporter",
        package="TC57CIM/IEC61968/Common",
        guid="{AA17CF00-FA20-4aac-A5A8-BFBD1DA287A1}",
        attributes=(
            AttrMeta("trouble_reporter_type", "troubleReporterType", "str", 1, 1, "primitive"),
        ),
        ends=(trouble_ticket.meta,),
    )

    def __init__(
        self,
        *,
        trouble_reporter_type: str | None = None,
        trouble_ticket: Iterable[TroubleTicket] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.trouble_reporter_type = trouble_reporter_type
        if trouble_ticket is not None:
            TroubleReporter.trouble_ticket.extend(self, trouble_ticket)

    def add_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return TroubleReporter.trouble_ticket.add(self, trouble_ticket)

    def remove_trouble_ticket(self, trouble_ticket: TroubleTicket) -> Self:
        return TroubleReporter.trouble_ticket.remove(self, trouble_ticket)

    def clear_trouble_ticket(self) -> Self:
        return TroubleReporter.trouble_ticket.clear(self)

    def num_trouble_ticket(self) -> int:
        return TroubleReporter.trouble_ticket.count(self)

    def get_trouble_ticket_by_mrid(self, mrid: str) -> TroubleTicket | None:
        return TroubleReporter.trouble_ticket.get_by_mrid(self, mrid)
