"""CIM class PSREvent (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.psr_event_kind import PSREventKind
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource


class PSREvent(ActivityRecord):
    """Event recording the change in operational status of a power system resource (PSR); may
    be for an event that has already occurred or for a planned activity."""

    __slots__ = ("_power_system_resource", "kind")

    kind: PSREventKind | None

    power_system_resource: One[PowerSystemResource] = One(
        EndMeta(
            name="power_system_resource",
            cim_role="PowerSystemResource",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=False,
            lower=0,
            upper=1,
            inverse="psr_events",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PSREvent",
        package="TC57CIM/IEC61968/Operations",
        guid="{F9B560A6-357D-47b6-8F38-4BD42BE286C4}",
        attributes=(AttrMeta("kind", "kind", "PSREventKind", 0, 1, "enumeration"),),
        ends=(power_system_resource.meta,),
    )

    def __init__(
        self,
        *,
        kind: PSREventKind | None = None,
        power_system_resource: PowerSystemResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
