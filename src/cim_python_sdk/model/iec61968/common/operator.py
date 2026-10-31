"""CIM class Operator (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.operation_person_role import OperationPersonRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.incident import Incident
    from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction


class Operator(OperationPersonRole):
    """Control room operator."""

    __slots__ = ("_incidents", "_switching_steps")

    switching_steps: Many[SwitchingAction] = Many(
        EndMeta(
            name="switching_steps",
            cim_role="SwitchingSteps",
            target="cim_python_sdk.model.iec61968.operations.switching_action:SwitchingAction",
            many=True,
            lower=0,
            upper=None,
            inverse="operator",
            aggregation="none",
        )
    )
    incidents: Many[Incident] = Many(
        EndMeta(
            name="incidents",
            cim_role="Incidents",
            target="cim_python_sdk.model.iec61968.operations.incident:Incident",
            many=True,
            lower=0,
            upper=None,
            inverse="owner",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Operator",
        package="TC57CIM/IEC61968/Common",
        guid="{1D6E83CC-11B8-4c82-B832-D1B0BC8A2E04}",
        ends=(
            switching_steps.meta,
            incidents.meta,
        ),
    )

    def __init__(
        self,
        *,
        switching_steps: Iterable[SwitchingAction] | None = None,
        incidents: Iterable[Incident] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if switching_steps is not None:
            Operator.switching_steps.extend(self, switching_steps)
        if incidents is not None:
            Operator.incidents.extend(self, incidents)

    def add_switching_step(self, switching_step: SwitchingAction) -> Self:
        return Operator.switching_steps.add(self, switching_step)

    def remove_switching_step(self, switching_step: SwitchingAction) -> Self:
        return Operator.switching_steps.remove(self, switching_step)

    def clear_switching_steps(self) -> Self:
        return Operator.switching_steps.clear(self)

    def num_switching_step(self) -> int:
        return Operator.switching_steps.count(self)

    def get_switching_step_by_mrid(self, mrid: str) -> SwitchingAction | None:
        return Operator.switching_steps.get_by_mrid(self, mrid)

    def add_incident(self, incident: Incident) -> Self:
        return Operator.incidents.add(self, incident)

    def remove_incident(self, incident: Incident) -> Self:
        return Operator.incidents.remove(self, incident)

    def clear_incidents(self) -> Self:
        return Operator.incidents.clear(self)

    def num_incident(self) -> int:
        return Operator.incidents.count(self)

    def get_incident_by_mrid(self, mrid: str) -> Incident | None:
        return Operator.incidents.get_by_mrid(self, mrid)
