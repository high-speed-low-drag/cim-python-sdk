"""CIM class FaultCauseType (TC57CIM/IEC61970/Base/Faults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.configuration_event import ConfigurationEvent
    from cim_python_sdk.model.iec61970.base.faults.fault import Fault


class FaultCauseType(IdentifiedObject):
    """Type of cause of the fault."""

    __slots__ = ("_configuration_event", "_faults")

    faults: Many[Fault] = Many(
        EndMeta(
            name="faults",
            cim_role="Faults",
            target="cim_python_sdk.model.iec61970.base.faults.fault:Fault",
            many=True,
            lower=0,
            upper=None,
            inverse="fault_cause_types",
            aggregation="none",
        )
    )
    configuration_event: Many[ConfigurationEvent] = Many(
        EndMeta(
            name="configuration_event",
            cim_role="ConfigurationEvent",
            target="cim_python_sdk.model.iec61968.common.configuration_event:ConfigurationEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="fault_cause_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FaultCauseType",
        package="TC57CIM/IEC61970/Base/Faults",
        guid="{FA0CB393-8E7C-411c-B4F1-14073D940EED}",
        ends=(
            faults.meta,
            configuration_event.meta,
        ),
    )

    def __init__(
        self,
        *,
        faults: Iterable[Fault] | None = None,
        configuration_event: Iterable[ConfigurationEvent] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if faults is not None:
            FaultCauseType.faults.extend(self, faults)
        if configuration_event is not None:
            FaultCauseType.configuration_event.extend(self, configuration_event)

    def add_fault(self, fault: Fault) -> Self:
        return FaultCauseType.faults.add(self, fault)

    def remove_fault(self, fault: Fault) -> Self:
        return FaultCauseType.faults.remove(self, fault)

    def clear_faults(self) -> Self:
        return FaultCauseType.faults.clear(self)

    def num_fault(self) -> int:
        return FaultCauseType.faults.count(self)

    def get_fault_by_mrid(self, mrid: str) -> Fault | None:
        return FaultCauseType.faults.get_by_mrid(self, mrid)

    def add_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return FaultCauseType.configuration_event.add(self, configuration_event)

    def remove_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return FaultCauseType.configuration_event.remove(self, configuration_event)

    def clear_configuration_event(self) -> Self:
        return FaultCauseType.configuration_event.clear(self)

    def num_configuration_event(self) -> int:
        return FaultCauseType.configuration_event.count(self)

    def get_configuration_event_by_mrid(self, mrid: str) -> ConfigurationEvent | None:
        return FaultCauseType.configuration_event.get_by_mrid(self, mrid)
