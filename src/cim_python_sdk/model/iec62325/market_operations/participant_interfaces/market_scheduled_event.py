"""CIM class MarketScheduledEvent (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.major_charge_group import (
        MajorChargeGroup,
    )


class MarketScheduledEvent(IdentifiedObject):
    """Signifies an event to trigger one or more activities, such as reading a meter,
    recalculating a bill, requesting work, when generating units shall be scheduled for
    maintenance, when a transformer is scheduled to be refurbished, etc."""

    __slots__ = ("_major_charge_group", "category", "duration", "status")

    category: str | None
    duration: float | None  # Seconds
    status: Status | None

    major_charge_group: One[MajorChargeGroup] = One(
        EndMeta(
            name="major_charge_group",
            cim_role="MajorChargeGroup",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.major_charge_group:MajorChargeGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_scheduled_event",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketScheduledEvent",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{62C99EEC-52F8-41aa-9D1D-0F6DA2351A74}",
        attributes=(
            AttrMeta("category", "category", "str", 0, 1, "primitive"),
            AttrMeta("duration", "duration", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(major_charge_group.meta,),
    )

    def __init__(
        self,
        *,
        category: str | None = None,
        duration: float | None = None,
        status: Status | None = None,
        major_charge_group: MajorChargeGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.category = category
        self.duration = duration
        self.status = status
        if major_charge_group is not None:
            self.major_charge_group = major_charge_group
