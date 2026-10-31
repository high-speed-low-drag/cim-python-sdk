"""CIM class Outage (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.crew import Crew
    from cim_python_sdk.model.iec61968.common.crew_status_kind import CrewStatusKind
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61968.operations.estimated_restoration_time import (
        EstimatedRestorationTime,
    )
    from cim_python_sdk.model.iec61968.operations.incident import Incident
    from cim_python_sdk.model.iec61968.operations.outage_area import OutageArea
    from cim_python_sdk.model.iec61968.operations.outage_status_kind import OutageStatusKind
    from cim_python_sdk.model.iec61968.operations.service_point_outage_summary import (
        ServicePointOutageSummary,
    )
    from cim_python_sdk.model.iec61968.operations.switch_action import SwitchAction
    from cim_python_sdk.model.iec61968.operations.switching_plan import SwitchingPlan
    from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment
    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec61970.base.faults.fault import Fault


class Outage(Document):
    """Document describing details of an active or planned outage in a part of the electrical
    network.

    A non-planned outage may be created upon:

    - a breaker trip,

    - a fault indicator status change,

    - a meter event indicating customer outage,

    - a reception of one or more customer trouble calls, or

    - an operator command, reflecting information obtained from the field crew.

    Outage restoration may be performed using a switching plan which complements the outage
    information with detailed switching activities, including the relationship to the crew
    and work.

    A planned outage may be created upon:

    - a request for service, maintenance or construction work in the field, or

    - an operator-defined outage for what-if/contingency network analysis."""

    __slots__ = (
        "_crew",
        "_de_energized_usage_point",
        "_energized_usage_point",
        "_equipments",
        "_estimated_restoration_time",
        "_faults",
        "_incident",
        "_outage_area",
        "_outage_isolation_equipment",
        "_planned_switch_actions",
        "_switching_plans",
        "actual_period",
        "community_descriptor",
        "customers_restored",
        "estimated_period",
        "meters_affected",
        "original_customers_served",
        "original_meters_affected",
        "outage_kind",
        "status_kind",
        "summary",
        "utility_disclaimer",
    )

    actual_period: DateTimeInterval | None
    estimated_period: DateTimeInterval | None
    summary: ServicePointOutageSummary | None
    community_descriptor: str | None
    customers_restored: int | None
    original_customers_served: int | None
    meters_affected: int | None
    original_meters_affected: int | None
    utility_disclaimer: str | None
    status_kind: CrewStatusKind | None
    outage_kind: OutageStatusKind | None

    energized_usage_point: Many[UsagePoint] = Many(
        EndMeta(
            name="energized_usage_point",
            cim_role="EnergizedUsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="outage",
            aggregation="none",
        )
    )
    equipments: Many[Equipment] = Many(
        EndMeta(
            name="equipments",
            cim_role="Equipments",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=True,
            lower=0,
            upper=None,
            inverse="outages",
            aggregation="none",
        )
    )
    planned_switch_actions: Many[SwitchAction] = Many(
        EndMeta(
            name="planned_switch_actions",
            cim_role="PlannedSwitchActions",
            target="cim_python_sdk.model.iec61968.operations.switch_action:SwitchAction",
            many=True,
            lower=0,
            upper=None,
            inverse="planned_outage",
            aggregation="none",
        )
    )
    incident: Many[Incident] = Many(
        EndMeta(
            name="incident",
            cim_role="Incident",
            target="cim_python_sdk.model.iec61968.operations.incident:Incident",
            many=True,
            lower=0,
            upper=None,
            inverse="outage",
            aggregation="none",
        )
    )
    de_energized_usage_point: Many[UsagePoint] = Many(
        EndMeta(
            name="de_energized_usage_point",
            cim_role="DeEnergizedUsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="outage_de_energized_usage_point",
            aggregation="none",
        )
    )
    estimated_restoration_time: One[EstimatedRestorationTime] = One(
        EndMeta(
            name="estimated_restoration_time",
            cim_role="EstimatedRestorationTime",
            target="cim_python_sdk.model.iec61968.operations.estimated_restoration_time:EstimatedRestorationTime",
            many=False,
            lower=0,
            upper=1,
            inverse="outage",
            aggregation="none",
        )
    )
    faults: Many[Fault] = Many(
        EndMeta(
            name="faults",
            cim_role="Faults",
            target="cim_python_sdk.model.iec61970.base.faults.fault:Fault",
            many=True,
            lower=0,
            upper=None,
            inverse="outage",
            aggregation="none",
        )
    )
    crew: Many[Crew] = Many(
        EndMeta(
            name="crew",
            cim_role="Crew",
            target="cim_python_sdk.model.iec61968.common.crew:Crew",
            many=True,
            lower=0,
            upper=None,
            inverse="outage",
            aggregation="none",
        )
    )
    switching_plans: Many[SwitchingPlan] = Many(
        EndMeta(
            name="switching_plans",
            cim_role="SwitchingPlans",
            target="cim_python_sdk.model.iec61968.operations.switching_plan:SwitchingPlan",
            many=True,
            lower=0,
            upper=None,
            inverse="outage",
            aggregation="none",
        )
    )
    outage_isolation_equipment: Many[ConductingEquipment] = Many(
        EndMeta(
            name="outage_isolation_equipment",
            cim_role="OutageIsolationEquipment",
            target="cim_python_sdk.model.iec61970.base.core.conducting_equipment:ConductingEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="outage",
            aggregation="none",
        )
    )
    outage_area: Many[OutageArea] = Many(
        EndMeta(
            name="outage_area",
            cim_role="OutageArea",
            target="cim_python_sdk.model.iec61968.operations.outage_area:OutageArea",
            many=True,
            lower=0,
            upper=None,
            inverse="outage",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Outage",
        package="TC57CIM/IEC61968/Operations",
        guid="{F40E2EAD-3BCA-4a17-A41E-A74212822DAA}",
        attributes=(
            AttrMeta("actual_period", "actualPeriod", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("estimated_period", "estimatedPeriod", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("summary", "summary", "ServicePointOutageSummary", 0, 1, "compound"),
            AttrMeta("community_descriptor", "communityDescriptor", "str", 0, 1, "primitive"),
            AttrMeta("customers_restored", "customersRestored", "int", 0, 1, "primitive"),
            AttrMeta(
                "original_customers_served", "originalCustomersServed", "int", 1, 1, "primitive"
            ),
            AttrMeta("meters_affected", "metersAffected", "int", 0, 1, "primitive"),
            AttrMeta(
                "original_meters_affected", "originalMetersAffected", "int", 0, 1, "primitive"
            ),
            AttrMeta("utility_disclaimer", "utilityDisclaimer", "str", 0, 1, "primitive"),
            AttrMeta("status_kind", "statusKind", "CrewStatusKind", 0, 1, "enumeration"),
            AttrMeta("outage_kind", "outageKind", "OutageStatusKind", 0, 1, "enumeration"),
        ),
        ends=(
            energized_usage_point.meta,
            equipments.meta,
            planned_switch_actions.meta,
            incident.meta,
            de_energized_usage_point.meta,
            estimated_restoration_time.meta,
            faults.meta,
            crew.meta,
            switching_plans.meta,
            outage_isolation_equipment.meta,
            outage_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        actual_period: DateTimeInterval | None = None,
        estimated_period: DateTimeInterval | None = None,
        summary: ServicePointOutageSummary | None = None,
        community_descriptor: str | None = None,
        customers_restored: int | None = None,
        original_customers_served: int | None = None,
        meters_affected: int | None = None,
        original_meters_affected: int | None = None,
        utility_disclaimer: str | None = None,
        status_kind: CrewStatusKind | None = None,
        outage_kind: OutageStatusKind | None = None,
        energized_usage_point: Iterable[UsagePoint] | None = None,
        equipments: Iterable[Equipment] | None = None,
        planned_switch_actions: Iterable[SwitchAction] | None = None,
        incident: Iterable[Incident] | None = None,
        de_energized_usage_point: Iterable[UsagePoint] | None = None,
        estimated_restoration_time: EstimatedRestorationTime | None = None,
        faults: Iterable[Fault] | None = None,
        crew: Iterable[Crew] | None = None,
        switching_plans: Iterable[SwitchingPlan] | None = None,
        outage_isolation_equipment: Iterable[ConductingEquipment] | None = None,
        outage_area: Iterable[OutageArea] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.actual_period = actual_period
        self.estimated_period = estimated_period
        self.summary = summary
        self.community_descriptor = community_descriptor
        self.customers_restored = customers_restored
        self.original_customers_served = original_customers_served
        self.meters_affected = meters_affected
        self.original_meters_affected = original_meters_affected
        self.utility_disclaimer = utility_disclaimer
        self.status_kind = status_kind
        self.outage_kind = outage_kind
        if energized_usage_point is not None:
            Outage.energized_usage_point.extend(self, energized_usage_point)
        if equipments is not None:
            Outage.equipments.extend(self, equipments)
        if planned_switch_actions is not None:
            Outage.planned_switch_actions.extend(self, planned_switch_actions)
        if incident is not None:
            Outage.incident.extend(self, incident)
        if de_energized_usage_point is not None:
            Outage.de_energized_usage_point.extend(self, de_energized_usage_point)
        if estimated_restoration_time is not None:
            self.estimated_restoration_time = estimated_restoration_time
        if faults is not None:
            Outage.faults.extend(self, faults)
        if crew is not None:
            Outage.crew.extend(self, crew)
        if switching_plans is not None:
            Outage.switching_plans.extend(self, switching_plans)
        if outage_isolation_equipment is not None:
            Outage.outage_isolation_equipment.extend(self, outage_isolation_equipment)
        if outage_area is not None:
            Outage.outage_area.extend(self, outage_area)

    def add_energized_usage_point(self, energized_usage_point: UsagePoint) -> Self:
        return Outage.energized_usage_point.add(self, energized_usage_point)

    def remove_energized_usage_point(self, energized_usage_point: UsagePoint) -> Self:
        return Outage.energized_usage_point.remove(self, energized_usage_point)

    def clear_energized_usage_point(self) -> Self:
        return Outage.energized_usage_point.clear(self)

    def num_energized_usage_point(self) -> int:
        return Outage.energized_usage_point.count(self)

    def get_energized_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return Outage.energized_usage_point.get_by_mrid(self, mrid)

    def add_equipment(self, equipment: Equipment) -> Self:
        return Outage.equipments.add(self, equipment)

    def remove_equipment(self, equipment: Equipment) -> Self:
        return Outage.equipments.remove(self, equipment)

    def clear_equipments(self) -> Self:
        return Outage.equipments.clear(self)

    def num_equipment(self) -> int:
        return Outage.equipments.count(self)

    def get_equipment_by_mrid(self, mrid: str) -> Equipment | None:
        return Outage.equipments.get_by_mrid(self, mrid)

    def add_planned_switch_action(self, planned_switch_action: SwitchAction) -> Self:
        return Outage.planned_switch_actions.add(self, planned_switch_action)

    def remove_planned_switch_action(self, planned_switch_action: SwitchAction) -> Self:
        return Outage.planned_switch_actions.remove(self, planned_switch_action)

    def clear_planned_switch_actions(self) -> Self:
        return Outage.planned_switch_actions.clear(self)

    def num_planned_switch_action(self) -> int:
        return Outage.planned_switch_actions.count(self)

    def get_planned_switch_action_by_mrid(self, mrid: str) -> SwitchAction | None:
        return Outage.planned_switch_actions.get_by_mrid(self, mrid)

    def add_incident(self, incident: Incident) -> Self:
        return Outage.incident.add(self, incident)

    def remove_incident(self, incident: Incident) -> Self:
        return Outage.incident.remove(self, incident)

    def clear_incident(self) -> Self:
        return Outage.incident.clear(self)

    def num_incident(self) -> int:
        return Outage.incident.count(self)

    def get_incident_by_mrid(self, mrid: str) -> Incident | None:
        return Outage.incident.get_by_mrid(self, mrid)

    def add_de_energized_usage_point(self, de_energized_usage_point: UsagePoint) -> Self:
        return Outage.de_energized_usage_point.add(self, de_energized_usage_point)

    def remove_de_energized_usage_point(self, de_energized_usage_point: UsagePoint) -> Self:
        return Outage.de_energized_usage_point.remove(self, de_energized_usage_point)

    def clear_de_energized_usage_point(self) -> Self:
        return Outage.de_energized_usage_point.clear(self)

    def num_de_energized_usage_point(self) -> int:
        return Outage.de_energized_usage_point.count(self)

    def get_de_energized_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return Outage.de_energized_usage_point.get_by_mrid(self, mrid)

    def add_fault(self, fault: Fault) -> Self:
        return Outage.faults.add(self, fault)

    def remove_fault(self, fault: Fault) -> Self:
        return Outage.faults.remove(self, fault)

    def clear_faults(self) -> Self:
        return Outage.faults.clear(self)

    def num_fault(self) -> int:
        return Outage.faults.count(self)

    def get_fault_by_mrid(self, mrid: str) -> Fault | None:
        return Outage.faults.get_by_mrid(self, mrid)

    def add_crew(self, crew: Crew) -> Self:
        return Outage.crew.add(self, crew)

    def remove_crew(self, crew: Crew) -> Self:
        return Outage.crew.remove(self, crew)

    def clear_crew(self) -> Self:
        return Outage.crew.clear(self)

    def num_crew(self) -> int:
        return Outage.crew.count(self)

    def get_crew_by_mrid(self, mrid: str) -> Crew | None:
        return Outage.crew.get_by_mrid(self, mrid)

    def add_switching_plan(self, switching_plan: SwitchingPlan) -> Self:
        return Outage.switching_plans.add(self, switching_plan)

    def remove_switching_plan(self, switching_plan: SwitchingPlan) -> Self:
        return Outage.switching_plans.remove(self, switching_plan)

    def clear_switching_plans(self) -> Self:
        return Outage.switching_plans.clear(self)

    def num_switching_plan(self) -> int:
        return Outage.switching_plans.count(self)

    def get_switching_plan_by_mrid(self, mrid: str) -> SwitchingPlan | None:
        return Outage.switching_plans.get_by_mrid(self, mrid)

    def add_outage_isolation_equipment(
        self, outage_isolation_equipment: ConductingEquipment
    ) -> Self:
        return Outage.outage_isolation_equipment.add(self, outage_isolation_equipment)

    def remove_outage_isolation_equipment(
        self, outage_isolation_equipment: ConductingEquipment
    ) -> Self:
        return Outage.outage_isolation_equipment.remove(self, outage_isolation_equipment)

    def clear_outage_isolation_equipment(self) -> Self:
        return Outage.outage_isolation_equipment.clear(self)

    def num_outage_isolation_equipment(self) -> int:
        return Outage.outage_isolation_equipment.count(self)

    def get_outage_isolation_equipment_by_mrid(self, mrid: str) -> ConductingEquipment | None:
        return Outage.outage_isolation_equipment.get_by_mrid(self, mrid)

    def add_outage_area(self, outage_area: OutageArea) -> Self:
        return Outage.outage_area.add(self, outage_area)

    def remove_outage_area(self, outage_area: OutageArea) -> Self:
        return Outage.outage_area.remove(self, outage_area)

    def clear_outage_area(self) -> Self:
        return Outage.outage_area.clear(self)

    def num_outage_area(self) -> int:
        return Outage.outage_area.count(self)
