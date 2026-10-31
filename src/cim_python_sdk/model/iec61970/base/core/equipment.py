"""CIM class Equipment (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61968.operations.operational_restriction import (
        OperationalRestriction,
    )
    from cim_python_sdk.model.iec61968.operations.outage import Outage
    from cim_python_sdk.model.iec61970.base.contingency.contingency_equipment import (
        ContingencyEquipment,
    )
    from cim_python_sdk.model.iec61970.base.core.equipment_container import EquipmentContainer
    from cim_python_sdk.model.iec61970.base.faults.fault import Fault
    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_set import (
        OperationalLimitSet,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.equipment_unavailability_schedule import (
        EquipmentUnavailabilitySchedule,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.equipment_limit_series_component import (
        EquipmentLimitSeriesComponent,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_dependency import (
        LimitDependency,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.weather_station import (
        WeatherStation,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_equipment import PinEquipment
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_equipment import (
        ProtectiveActionEquipment,
    )


class Equipment(PowerSystemResource):
    """The parts of a power system that are physical devices, electronic or mechanical."""

    __slots__ = (
        "_additional_equipment_container",
        "_contingency_equipment",
        "_eqiupment_limit_series_component",
        "_equipment_container",
        "_equipment_unavailability_schedules",
        "_faults",
        "_limit_dependency_model",
        "_operational_limit_set",
        "_operational_restrictions",
        "_outages",
        "_pin_equipment",
        "_protective_action_equipment",
        "_usage_points",
        "_weather_station",
        "aggregate",
        "in_service",
        "network_analysis_enabled",
        "normally_in_service",
    )

    aggregate: bool | None
    in_service: bool | None
    network_analysis_enabled: bool | None
    normally_in_service: bool | None

    usage_points: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_points",
            cim_role="UsagePoints",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="equipments",
            aggregation="none",
        )
    )
    additional_equipment_container: Many[EquipmentContainer] = Many(
        EndMeta(
            name="additional_equipment_container",
            cim_role="AdditionalEquipmentContainer",
            target="cim_python_sdk.model.iec61970.base.core.equipment_container:EquipmentContainer",
            many=True,
            lower=0,
            upper=None,
            inverse="additional_grouped_equipment",
            aggregation="none",
        )
    )
    equipment_container: One[EquipmentContainer] = One(
        EndMeta(
            name="equipment_container",
            cim_role="EquipmentContainer",
            target="cim_python_sdk.model.iec61970.base.core.equipment_container:EquipmentContainer",
            many=False,
            lower=0,
            upper=1,
            inverse="equipments",
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
            inverse="faulty_equipment",
            aggregation="none",
        )
    )
    outages: Many[Outage] = Many(
        EndMeta(
            name="outages",
            cim_role="Outages",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=True,
            lower=0,
            upper=None,
            inverse="equipments",
            aggregation="none",
        )
    )
    pin_equipment: Many[PinEquipment] = Many(
        EndMeta(
            name="pin_equipment",
            cim_role="PinEquipment",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_equipment:PinEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment",
            aggregation="none",
        )
    )
    contingency_equipment: Many[ContingencyEquipment] = Many(
        EndMeta(
            name="contingency_equipment",
            cim_role="ContingencyEquipment",
            target="cim_python_sdk.model.iec61970.base.contingency.contingency_equipment:ContingencyEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment",
            aggregation="none",
        )
    )
    operational_restrictions: Many[OperationalRestriction] = Many(
        EndMeta(
            name="operational_restrictions",
            cim_role="OperationalRestrictions",
            target="cim_python_sdk.model.iec61968.operations.operational_restriction:OperationalRestriction",
            many=True,
            lower=0,
            upper=None,
            inverse="equipments",
            aggregation="none",
        )
    )
    operational_limit_set: Many[OperationalLimitSet] = Many(
        EndMeta(
            name="operational_limit_set",
            cim_role="OperationalLimitSet",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_set:OperationalLimitSet",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment",
            aggregation="none",
        )
    )
    protective_action_equipment: Many[ProtectiveActionEquipment] = Many(
        EndMeta(
            name="protective_action_equipment",
            cim_role="ProtectiveActionEquipment",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_equipment:ProtectiveActionEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment",
            aggregation="none",
        )
    )
    weather_station: Many[WeatherStation] = Many(
        EndMeta(
            name="weather_station",
            cim_role="WeatherStation",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.weather_station:WeatherStation",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment",
            aggregation="none",
        )
    )
    limit_dependency_model: Many[LimitDependency] = Many(
        EndMeta(
            name="limit_dependency_model",
            cim_role="LimitDependencyModel",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_dependency:LimitDependency",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment",
            aggregation="shared",
        )
    )
    eqiupment_limit_series_component: Many[EquipmentLimitSeriesComponent] = Many(
        EndMeta(
            name="eqiupment_limit_series_component",
            cim_role="EqiupmentLimitSeriesComponent",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.equipment_limit_series_component:EquipmentLimitSeriesComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment",
            aggregation="none",
        )
    )
    equipment_unavailability_schedules: Many[EquipmentUnavailabilitySchedule] = Many(
        EndMeta(
            name="equipment_unavailability_schedules",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.equipment_unavailability_schedule:EquipmentUnavailabilitySchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Equipment",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{F8DD8DAC-3545-4660-9CA5-794881CC6591}",
        attributes=(
            AttrMeta("aggregate", "aggregate", "bool", 0, 1, "primitive"),
            AttrMeta("in_service", "inService", "bool", 0, 1, "primitive"),
            AttrMeta(
                "network_analysis_enabled", "networkAnalysisEnabled", "bool", 0, 1, "primitive"
            ),
            AttrMeta("normally_in_service", "normallyInService", "bool", 0, 1, "primitive"),
        ),
        ends=(
            usage_points.meta,
            additional_equipment_container.meta,
            equipment_container.meta,
            faults.meta,
            outages.meta,
            pin_equipment.meta,
            contingency_equipment.meta,
            operational_restrictions.meta,
            operational_limit_set.meta,
            protective_action_equipment.meta,
            weather_station.meta,
            limit_dependency_model.meta,
            eqiupment_limit_series_component.meta,
            equipment_unavailability_schedules.meta,
        ),
    )

    def __init__(
        self,
        *,
        aggregate: bool | None = None,
        in_service: bool | None = None,
        network_analysis_enabled: bool | None = None,
        normally_in_service: bool | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        additional_equipment_container: Iterable[EquipmentContainer] | None = None,
        equipment_container: EquipmentContainer | None = None,
        faults: Iterable[Fault] | None = None,
        outages: Iterable[Outage] | None = None,
        pin_equipment: Iterable[PinEquipment] | None = None,
        contingency_equipment: Iterable[ContingencyEquipment] | None = None,
        operational_restrictions: Iterable[OperationalRestriction] | None = None,
        operational_limit_set: Iterable[OperationalLimitSet] | None = None,
        protective_action_equipment: Iterable[ProtectiveActionEquipment] | None = None,
        weather_station: Iterable[WeatherStation] | None = None,
        limit_dependency_model: Iterable[LimitDependency] | None = None,
        eqiupment_limit_series_component: Iterable[EquipmentLimitSeriesComponent] | None = None,
        equipment_unavailability_schedules: Iterable[EquipmentUnavailabilitySchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.aggregate = aggregate
        self.in_service = in_service
        self.network_analysis_enabled = network_analysis_enabled
        self.normally_in_service = normally_in_service
        if usage_points is not None:
            Equipment.usage_points.extend(self, usage_points)
        if additional_equipment_container is not None:
            Equipment.additional_equipment_container.extend(self, additional_equipment_container)
        if equipment_container is not None:
            self.equipment_container = equipment_container
        if faults is not None:
            Equipment.faults.extend(self, faults)
        if outages is not None:
            Equipment.outages.extend(self, outages)
        if pin_equipment is not None:
            Equipment.pin_equipment.extend(self, pin_equipment)
        if contingency_equipment is not None:
            Equipment.contingency_equipment.extend(self, contingency_equipment)
        if operational_restrictions is not None:
            Equipment.operational_restrictions.extend(self, operational_restrictions)
        if operational_limit_set is not None:
            Equipment.operational_limit_set.extend(self, operational_limit_set)
        if protective_action_equipment is not None:
            Equipment.protective_action_equipment.extend(self, protective_action_equipment)
        if weather_station is not None:
            Equipment.weather_station.extend(self, weather_station)
        if limit_dependency_model is not None:
            Equipment.limit_dependency_model.extend(self, limit_dependency_model)
        if eqiupment_limit_series_component is not None:
            Equipment.eqiupment_limit_series_component.extend(
                self, eqiupment_limit_series_component
            )
        if equipment_unavailability_schedules is not None:
            Equipment.equipment_unavailability_schedules.extend(
                self, equipment_unavailability_schedules
            )

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return Equipment.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return Equipment.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return Equipment.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return Equipment.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return Equipment.usage_points.get_by_mrid(self, mrid)

    def add_additional_equipment_container(
        self, additional_equipment_container: EquipmentContainer
    ) -> Self:
        return Equipment.additional_equipment_container.add(self, additional_equipment_container)

    def remove_additional_equipment_container(
        self, additional_equipment_container: EquipmentContainer
    ) -> Self:
        return Equipment.additional_equipment_container.remove(self, additional_equipment_container)

    def clear_additional_equipment_container(self) -> Self:
        return Equipment.additional_equipment_container.clear(self)

    def num_additional_equipment_container(self) -> int:
        return Equipment.additional_equipment_container.count(self)

    def get_additional_equipment_container_by_mrid(self, mrid: str) -> EquipmentContainer | None:
        return Equipment.additional_equipment_container.get_by_mrid(self, mrid)

    def add_fault(self, fault: Fault) -> Self:
        return Equipment.faults.add(self, fault)

    def remove_fault(self, fault: Fault) -> Self:
        return Equipment.faults.remove(self, fault)

    def clear_faults(self) -> Self:
        return Equipment.faults.clear(self)

    def num_fault(self) -> int:
        return Equipment.faults.count(self)

    def get_fault_by_mrid(self, mrid: str) -> Fault | None:
        return Equipment.faults.get_by_mrid(self, mrid)

    def add_outage(self, outage: Outage) -> Self:
        return Equipment.outages.add(self, outage)

    def remove_outage(self, outage: Outage) -> Self:
        return Equipment.outages.remove(self, outage)

    def clear_outages(self) -> Self:
        return Equipment.outages.clear(self)

    def num_outage(self) -> int:
        return Equipment.outages.count(self)

    def get_outage_by_mrid(self, mrid: str) -> Outage | None:
        return Equipment.outages.get_by_mrid(self, mrid)

    def add_pin_equipment(self, pin_equipment: PinEquipment) -> Self:
        return Equipment.pin_equipment.add(self, pin_equipment)

    def remove_pin_equipment(self, pin_equipment: PinEquipment) -> Self:
        return Equipment.pin_equipment.remove(self, pin_equipment)

    def clear_pin_equipment(self) -> Self:
        return Equipment.pin_equipment.clear(self)

    def num_pin_equipment(self) -> int:
        return Equipment.pin_equipment.count(self)

    def get_pin_equipment_by_mrid(self, mrid: str) -> PinEquipment | None:
        return Equipment.pin_equipment.get_by_mrid(self, mrid)

    def add_contingency_equipment(self, contingency_equipment: ContingencyEquipment) -> Self:
        return Equipment.contingency_equipment.add(self, contingency_equipment)

    def remove_contingency_equipment(self, contingency_equipment: ContingencyEquipment) -> Self:
        return Equipment.contingency_equipment.remove(self, contingency_equipment)

    def clear_contingency_equipment(self) -> Self:
        return Equipment.contingency_equipment.clear(self)

    def num_contingency_equipment(self) -> int:
        return Equipment.contingency_equipment.count(self)

    def get_contingency_equipment_by_mrid(self, mrid: str) -> ContingencyEquipment | None:
        return Equipment.contingency_equipment.get_by_mrid(self, mrid)

    def add_operational_restriction(self, operational_restriction: OperationalRestriction) -> Self:
        return Equipment.operational_restrictions.add(self, operational_restriction)

    def remove_operational_restriction(
        self, operational_restriction: OperationalRestriction
    ) -> Self:
        return Equipment.operational_restrictions.remove(self, operational_restriction)

    def clear_operational_restrictions(self) -> Self:
        return Equipment.operational_restrictions.clear(self)

    def num_operational_restriction(self) -> int:
        return Equipment.operational_restrictions.count(self)

    def get_operational_restriction_by_mrid(self, mrid: str) -> OperationalRestriction | None:
        return Equipment.operational_restrictions.get_by_mrid(self, mrid)

    def add_operational_limit_set(self, operational_limit_set: OperationalLimitSet) -> Self:
        return Equipment.operational_limit_set.add(self, operational_limit_set)

    def remove_operational_limit_set(self, operational_limit_set: OperationalLimitSet) -> Self:
        return Equipment.operational_limit_set.remove(self, operational_limit_set)

    def clear_operational_limit_set(self) -> Self:
        return Equipment.operational_limit_set.clear(self)

    def num_operational_limit_set(self) -> int:
        return Equipment.operational_limit_set.count(self)

    def get_operational_limit_set_by_mrid(self, mrid: str) -> OperationalLimitSet | None:
        return Equipment.operational_limit_set.get_by_mrid(self, mrid)

    def add_protective_action_equipment(
        self, protective_action_equipment: ProtectiveActionEquipment
    ) -> Self:
        return Equipment.protective_action_equipment.add(self, protective_action_equipment)

    def remove_protective_action_equipment(
        self, protective_action_equipment: ProtectiveActionEquipment
    ) -> Self:
        return Equipment.protective_action_equipment.remove(self, protective_action_equipment)

    def clear_protective_action_equipment(self) -> Self:
        return Equipment.protective_action_equipment.clear(self)

    def num_protective_action_equipment(self) -> int:
        return Equipment.protective_action_equipment.count(self)

    def get_protective_action_equipment_by_mrid(
        self, mrid: str
    ) -> ProtectiveActionEquipment | None:
        return Equipment.protective_action_equipment.get_by_mrid(self, mrid)

    def add_weather_station(self, weather_station: WeatherStation) -> Self:
        return Equipment.weather_station.add(self, weather_station)

    def remove_weather_station(self, weather_station: WeatherStation) -> Self:
        return Equipment.weather_station.remove(self, weather_station)

    def clear_weather_station(self) -> Self:
        return Equipment.weather_station.clear(self)

    def num_weather_station(self) -> int:
        return Equipment.weather_station.count(self)

    def get_weather_station_by_mrid(self, mrid: str) -> WeatherStation | None:
        return Equipment.weather_station.get_by_mrid(self, mrid)

    def add_limit_dependency_model(self, limit_dependency_model: LimitDependency) -> Self:
        return Equipment.limit_dependency_model.add(self, limit_dependency_model)

    def remove_limit_dependency_model(self, limit_dependency_model: LimitDependency) -> Self:
        return Equipment.limit_dependency_model.remove(self, limit_dependency_model)

    def clear_limit_dependency_model(self) -> Self:
        return Equipment.limit_dependency_model.clear(self)

    def num_limit_dependency_model(self) -> int:
        return Equipment.limit_dependency_model.count(self)

    def get_limit_dependency_model_by_mrid(self, mrid: str) -> LimitDependency | None:
        return Equipment.limit_dependency_model.get_by_mrid(self, mrid)

    def add_eqiupment_limit_series_component(
        self, eqiupment_limit_series_component: EquipmentLimitSeriesComponent
    ) -> Self:
        return Equipment.eqiupment_limit_series_component.add(
            self, eqiupment_limit_series_component
        )

    def remove_eqiupment_limit_series_component(
        self, eqiupment_limit_series_component: EquipmentLimitSeriesComponent
    ) -> Self:
        return Equipment.eqiupment_limit_series_component.remove(
            self, eqiupment_limit_series_component
        )

    def clear_eqiupment_limit_series_component(self) -> Self:
        return Equipment.eqiupment_limit_series_component.clear(self)

    def num_eqiupment_limit_series_component(self) -> int:
        return Equipment.eqiupment_limit_series_component.count(self)

    def get_eqiupment_limit_series_component_by_mrid(
        self, mrid: str
    ) -> EquipmentLimitSeriesComponent | None:
        return Equipment.eqiupment_limit_series_component.get_by_mrid(self, mrid)

    def add_equipment_unavailability_schedule(
        self, equipment_unavailability_schedule: EquipmentUnavailabilitySchedule
    ) -> Self:
        return Equipment.equipment_unavailability_schedules.add(
            self, equipment_unavailability_schedule
        )

    def remove_equipment_unavailability_schedule(
        self, equipment_unavailability_schedule: EquipmentUnavailabilitySchedule
    ) -> Self:
        return Equipment.equipment_unavailability_schedules.remove(
            self, equipment_unavailability_schedule
        )

    def clear_equipment_unavailability_schedules(self) -> Self:
        return Equipment.equipment_unavailability_schedules.clear(self)

    def num_equipment_unavailability_schedule(self) -> int:
        return Equipment.equipment_unavailability_schedules.count(self)

    def get_equipment_unavailability_schedule_by_mrid(
        self, mrid: str
    ) -> EquipmentUnavailabilitySchedule | None:
        return Equipment.equipment_unavailability_schedules.get_by_mrid(self, mrid)
