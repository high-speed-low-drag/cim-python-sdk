"""CIM class InternalControlArea (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.current_emergency_scheduled_interchange import (
        CurrentEmergencyScheduledInterchange,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.current_scheduled_interchange import (
        CurrentScheduledInterchange,
    )


class InternalControlArea(IdentifiedObject):
    """There is one internal control area in the system, which is the single control area in
    the primary network company. Real time generation control affects only the internal
    control area."""

    __slots__ = ("_current_emergency_si", "_current_scheduled_interchange")

    current_scheduled_interchange: One[CurrentScheduledInterchange] = One(
        EndMeta(
            name="current_scheduled_interchange",
            cim_role="CurrentScheduledInterchange",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.current_scheduled_interchange:CurrentScheduledInterchange",
            many=False,
            lower=0,
            upper=1,
            inverse="internal_control_area",
            aggregation="none",
        )
    )
    current_emergency_si: Many[CurrentEmergencyScheduledInterchange] = Many(
        EndMeta(
            name="current_emergency_si",
            cim_role="CurrentEmergencySI",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.current_emergency_scheduled_interchange:CurrentEmergencyScheduledInterchange",
            many=True,
            lower=0,
            upper=None,
            inverse="internal_control_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InternalControlArea",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{6C4C9F2E-840A-4d68-8F9B-BE9B806AB713}",
        ends=(
            current_scheduled_interchange.meta,
            current_emergency_si.meta,
        ),
    )

    def __init__(
        self,
        *,
        current_scheduled_interchange: CurrentScheduledInterchange | None = None,
        current_emergency_si: Iterable[CurrentEmergencyScheduledInterchange] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if current_scheduled_interchange is not None:
            self.current_scheduled_interchange = current_scheduled_interchange
        if current_emergency_si is not None:
            InternalControlArea.current_emergency_si.extend(self, current_emergency_si)

    def add_current_emergency_si(
        self, current_emergency_si: CurrentEmergencyScheduledInterchange
    ) -> Self:
        return InternalControlArea.current_emergency_si.add(self, current_emergency_si)

    def remove_current_emergency_si(
        self, current_emergency_si: CurrentEmergencyScheduledInterchange
    ) -> Self:
        return InternalControlArea.current_emergency_si.remove(self, current_emergency_si)

    def clear_current_emergency_si(self) -> Self:
        return InternalControlArea.current_emergency_si.clear(self)

    def num_current_emergency_si(self) -> int:
        return InternalControlArea.current_emergency_si.count(self)

    def get_current_emergency_si_by_mrid(
        self, mrid: str
    ) -> CurrentEmergencyScheduledInterchange | None:
        return InternalControlArea.current_emergency_si.get_by_mrid(self, mrid)
