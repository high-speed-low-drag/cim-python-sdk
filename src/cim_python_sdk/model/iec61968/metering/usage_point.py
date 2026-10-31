"""CIM class UsagePoint (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.configuration_event import ConfigurationEvent
    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.customers.pricing_structure import PricingStructure
    from cim_python_sdk.model.iec61968.customers.service_category import ServiceCategory
    from cim_python_sdk.model.iec61968.customers.service_location import ServiceLocation
    from cim_python_sdk.model.iec61968.metering.ami_billing_ready_kind import AmiBillingReadyKind
    from cim_python_sdk.model.iec61968.metering.end_device import EndDevice
    from cim_python_sdk.model.iec61968.metering.end_device_control import EndDeviceControl
    from cim_python_sdk.model.iec61968.metering.end_device_event import EndDeviceEvent
    from cim_python_sdk.model.iec61968.metering.meter_read_schedule import MeterReadSchedule
    from cim_python_sdk.model.iec61968.metering.meter_reading import MeterReading
    from cim_python_sdk.model.iec61968.metering.meter_work_task import MeterWorkTask
    from cim_python_sdk.model.iec61968.metering.metrology_requirement import MetrologyRequirement
    from cim_python_sdk.model.iec61968.metering.register import Register
    from cim_python_sdk.model.iec61968.metering.service_multiplier import ServiceMultiplier
    from cim_python_sdk.model.iec61968.metering.usage_point_connected_kind import (
        UsagePointConnectedKind,
    )
    from cim_python_sdk.model.iec61968.metering.usage_point_group import UsagePointGroup
    from cim_python_sdk.model.iec61968.metering.usage_point_location import UsagePointLocation
    from cim_python_sdk.model.iec61968.operations.outage import Outage
    from cim_python_sdk.model.iec61968.operations.planned_outage_notification import (
        PlannedOutageNotification,
    )
    from cim_python_sdk.model.iec61968.payment_metering.service_supplier import ServiceSupplier
    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment
    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode
    from cim_python_sdk.model.iec61970.base.domain.decimal_quantity import DecimalQuantity
    from cim_python_sdk.model.iec62325.market_common.environmental_monitoring_station import (
        EnvironmentalMonitoringStation,
    )


class UsagePoint(IdentifiedObject):
    """Logical or physical point in the network to which readings or events may be attributed.
    Used at the place where a physical or virtual meter may be located; however, it is not
    required that a meter be present."""

    __slots__ = (
        "_configuration_events",
        "_customer_agreement",
        "_end_device_controls",
        "_end_device_events",
        "_end_devices",
        "_environmental_monitoring_station",
        "_equipments",
        "_meter_read_schedule",
        "_meter_readings",
        "_meter_service_work_tasks",
        "_metrology_requirements",
        "_outage",
        "_outage_de_energized_usage_point",
        "_planned_outage_notification",
        "_pricing_structures",
        "_register",
        "_service_category",
        "_service_location",
        "_service_multipliers",
        "_service_supplier",
        "_usage_point_groups",
        "_usage_point_location",
        "ami_billing_ready",
        "check_billing",
        "connection_category",
        "connection_state",
        "disconnection_method",
        "estimated_load",
        "grounded",
        "is_sdp",
        "is_virtual",
        "minimal_usage_expected",
        "nominal_service_voltage",
        "outage_region",
        "phase_code",
        "phase_count",
        "physical_connection_capacity",
        "rated_current",
        "rated_power",
        "read_cycle",
        "read_route",
        "service_delivery_remark",
        "service_priority",
    )

    is_sdp: bool | None
    is_virtual: bool | None
    phase_code: PhaseCode | None
    grounded: bool | None
    service_priority: str | None
    service_delivery_remark: str | None
    estimated_load: float | None  # CurrentFlow
    check_billing: bool | None
    rated_current: float | None  # CurrentFlow
    nominal_service_voltage: float | None  # Voltage
    rated_power: float | None  # ActivePower
    outage_region: str | None
    read_cycle: str | None
    read_route: str | None
    ami_billing_ready: AmiBillingReadyKind | None
    connection_state: UsagePointConnectedKind | None
    minimal_usage_expected: bool | None
    disconnection_method: str | None
    physical_connection_capacity: DecimalQuantity | None
    connection_category: str | None
    phase_count: int | None

    register: Many[Register] = Many(
        EndMeta(
            name="register",
            cim_role="Register",
            target="cim_python_sdk.model.iec61968.metering.register:Register",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_point",
            aggregation="none",
        )
    )
    meter_read_schedule: One[MeterReadSchedule] = One(
        EndMeta(
            name="meter_read_schedule",
            cim_role="MeterReadSchedule",
            target="cim_python_sdk.model.iec61968.metering.meter_read_schedule:MeterReadSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="usage_point",
            aggregation="none",
        )
    )
    customer_agreement: One[CustomerAgreement] = One(
        EndMeta(
            name="customer_agreement",
            cim_role="CustomerAgreement",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=False,
            lower=0,
            upper=1,
            inverse="usage_points",
            aggregation="none",
        )
    )
    environmental_monitoring_station: One[EnvironmentalMonitoringStation] = One(
        EndMeta(
            name="environmental_monitoring_station",
            cim_role="EnvironmentalMonitoringStation",
            target="cim_python_sdk.model.iec62325.market_common.environmental_monitoring_station:EnvironmentalMonitoringStation",
            many=False,
            lower=0,
            upper=1,
            inverse="usage_point",
            aggregation="none",
        )
    )
    outage: Many[Outage] = Many(
        EndMeta(
            name="outage",
            cim_role="Outage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=True,
            lower=0,
            upper=None,
            inverse="energized_usage_point",
            aggregation="none",
        )
    )
    metrology_requirements: Many[MetrologyRequirement] = Many(
        EndMeta(
            name="metrology_requirements",
            cim_role="MetrologyRequirements",
            target="cim_python_sdk.model.iec61968.metering.metrology_requirement:MetrologyRequirement",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_points",
            aggregation="none",
        )
    )
    meter_service_work_tasks: Many[MeterWorkTask] = Many(
        EndMeta(
            name="meter_service_work_tasks",
            cim_role="MeterServiceWorkTasks",
            target="cim_python_sdk.model.iec61968.metering.meter_work_task:MeterWorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_point",
            aggregation="none",
        )
    )
    usage_point_groups: Many[UsagePointGroup] = Many(
        EndMeta(
            name="usage_point_groups",
            cim_role="UsagePointGroups",
            target="cim_python_sdk.model.iec61968.metering.usage_point_group:UsagePointGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_points",
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
            inverse="usage_points",
            aggregation="none",
        )
    )
    service_supplier: One[ServiceSupplier] = One(
        EndMeta(
            name="service_supplier",
            cim_role="ServiceSupplier",
            target="cim_python_sdk.model.iec61968.payment_metering.service_supplier:ServiceSupplier",
            many=False,
            lower=0,
            upper=1,
            inverse="usage_points",
            aggregation="none",
        )
    )
    end_devices: Many[EndDevice] = Many(
        EndMeta(
            name="end_devices",
            cim_role="EndDevices",
            target="cim_python_sdk.model.iec61968.metering.end_device:EndDevice",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_point",
            aggregation="none",
        )
    )
    service_multipliers: Many[ServiceMultiplier] = Many(
        EndMeta(
            name="service_multipliers",
            cim_role="ServiceMultipliers",
            target="cim_python_sdk.model.iec61968.metering.service_multiplier:ServiceMultiplier",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_point",
            aggregation="none",
        )
    )
    end_device_controls: Many[EndDeviceControl] = Many(
        EndMeta(
            name="end_device_controls",
            cim_role="EndDeviceControls",
            target="cim_python_sdk.model.iec61968.metering.end_device_control:EndDeviceControl",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_points",
            aggregation="none",
        )
    )
    end_device_events: Many[EndDeviceEvent] = Many(
        EndMeta(
            name="end_device_events",
            cim_role="EndDeviceEvents",
            target="cim_python_sdk.model.iec61968.metering.end_device_event:EndDeviceEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_point",
            aggregation="none",
        )
    )
    outage_de_energized_usage_point: Many[Outage] = Many(
        EndMeta(
            name="outage_de_energized_usage_point",
            cim_role="Outage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=True,
            lower=0,
            upper=None,
            inverse="de_energized_usage_point",
            aggregation="none",
        )
    )
    planned_outage_notification: Many[PlannedOutageNotification] = Many(
        EndMeta(
            name="planned_outage_notification",
            cim_role="PlannedOutageNotification",
            target="cim_python_sdk.model.iec61968.operations.planned_outage_notification:PlannedOutageNotification",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_point",
            aggregation="none",
        )
    )
    service_location: One[ServiceLocation] = One(
        EndMeta(
            name="service_location",
            cim_role="ServiceLocation",
            target="cim_python_sdk.model.iec61968.customers.service_location:ServiceLocation",
            many=False,
            lower=0,
            upper=1,
            inverse="usage_points",
            aggregation="none",
        )
    )
    usage_point_location: One[UsagePointLocation] = One(
        EndMeta(
            name="usage_point_location",
            cim_role="UsagePointLocation",
            target="cim_python_sdk.model.iec61968.metering.usage_point_location:UsagePointLocation",
            many=False,
            lower=0,
            upper=1,
            inverse="usage_points",
            aggregation="none",
        )
    )
    configuration_events: Many[ConfigurationEvent] = Many(
        EndMeta(
            name="configuration_events",
            cim_role="ConfigurationEvents",
            target="cim_python_sdk.model.iec61968.common.configuration_event:ConfigurationEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="changed_usage_point",
            aggregation="none",
        )
    )
    pricing_structures: Many[PricingStructure] = Many(
        EndMeta(
            name="pricing_structures",
            cim_role="PricingStructures",
            target="cim_python_sdk.model.iec61968.customers.pricing_structure:PricingStructure",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_points",
            aggregation="none",
        )
    )
    service_category: One[ServiceCategory] = One(
        EndMeta(
            name="service_category",
            cim_role="ServiceCategory",
            target="cim_python_sdk.model.iec61968.customers.service_category:ServiceCategory",
            many=False,
            lower=0,
            upper=1,
            inverse="usage_points",
            aggregation="none",
        )
    )
    meter_readings: Many[MeterReading] = Many(
        EndMeta(
            name="meter_readings",
            cim_role="MeterReadings",
            target="cim_python_sdk.model.iec61968.metering.meter_reading:MeterReading",
            many=True,
            lower=0,
            upper=None,
            inverse="usage_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UsagePoint",
        package="TC57CIM/IEC61968/Metering",
        guid="{54796D9B-C2B0-4186-99CB-70E4CEF64C85}",
        attributes=(
            AttrMeta("is_sdp", "isSdp", "bool", 0, 1, "primitive"),
            AttrMeta("is_virtual", "isVirtual", "bool", 0, 1, "primitive"),
            AttrMeta("phase_code", "phaseCode", "PhaseCode", 0, 1, "enumeration"),
            AttrMeta("grounded", "grounded", "bool", 0, 1, "primitive"),
            AttrMeta("service_priority", "servicePriority", "str", 0, 1, "primitive"),
            AttrMeta("service_delivery_remark", "serviceDeliveryRemark", "str", 0, 1, "primitive"),
            AttrMeta("estimated_load", "estimatedLoad", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("check_billing", "checkBilling", "bool", 0, 1, "primitive"),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta(
                "nominal_service_voltage", "nominalServiceVoltage", "Voltage", 0, 1, "cimdatatype"
            ),
            AttrMeta("rated_power", "ratedPower", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("outage_region", "outageRegion", "str", 0, 1, "primitive"),
            AttrMeta("read_cycle", "readCycle", "str", 0, 1, "primitive"),
            AttrMeta("read_route", "readRoute", "str", 0, 1, "primitive"),
            AttrMeta(
                "ami_billing_ready", "amiBillingReady", "AmiBillingReadyKind", 0, 1, "enumeration"
            ),
            AttrMeta(
                "connection_state",
                "connectionState",
                "UsagePointConnectedKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("minimal_usage_expected", "minimalUsageExpected", "bool", 0, 1, "primitive"),
            AttrMeta("disconnection_method", "disconnectionMethod", "str", 0, 1, "primitive"),
            AttrMeta(
                "physical_connection_capacity",
                "physicalConnectionCapacity",
                "DecimalQuantity",
                0,
                1,
                "compound",
            ),
            AttrMeta("connection_category", "connectionCategory", "str", 0, 1, "primitive"),
            AttrMeta("phase_count", "phaseCount", "int", 0, 1, "primitive"),
        ),
        ends=(
            register.meta,
            meter_read_schedule.meta,
            customer_agreement.meta,
            environmental_monitoring_station.meta,
            outage.meta,
            metrology_requirements.meta,
            meter_service_work_tasks.meta,
            usage_point_groups.meta,
            equipments.meta,
            service_supplier.meta,
            end_devices.meta,
            service_multipliers.meta,
            end_device_controls.meta,
            end_device_events.meta,
            outage_de_energized_usage_point.meta,
            planned_outage_notification.meta,
            service_location.meta,
            usage_point_location.meta,
            configuration_events.meta,
            pricing_structures.meta,
            service_category.meta,
            meter_readings.meta,
        ),
    )

    def __init__(
        self,
        *,
        is_sdp: bool | None = None,
        is_virtual: bool | None = None,
        phase_code: PhaseCode | None = None,
        grounded: bool | None = None,
        service_priority: str | None = None,
        service_delivery_remark: str | None = None,
        estimated_load: float | None = None,
        check_billing: bool | None = None,
        rated_current: float | None = None,
        nominal_service_voltage: float | None = None,
        rated_power: float | None = None,
        outage_region: str | None = None,
        read_cycle: str | None = None,
        read_route: str | None = None,
        ami_billing_ready: AmiBillingReadyKind | None = None,
        connection_state: UsagePointConnectedKind | None = None,
        minimal_usage_expected: bool | None = None,
        disconnection_method: str | None = None,
        physical_connection_capacity: DecimalQuantity | None = None,
        connection_category: str | None = None,
        phase_count: int | None = None,
        register: Iterable[Register] | None = None,
        meter_read_schedule: MeterReadSchedule | None = None,
        customer_agreement: CustomerAgreement | None = None,
        environmental_monitoring_station: EnvironmentalMonitoringStation | None = None,
        outage: Iterable[Outage] | None = None,
        metrology_requirements: Iterable[MetrologyRequirement] | None = None,
        meter_service_work_tasks: Iterable[MeterWorkTask] | None = None,
        usage_point_groups: Iterable[UsagePointGroup] | None = None,
        equipments: Iterable[Equipment] | None = None,
        service_supplier: ServiceSupplier | None = None,
        end_devices: Iterable[EndDevice] | None = None,
        service_multipliers: Iterable[ServiceMultiplier] | None = None,
        end_device_controls: Iterable[EndDeviceControl] | None = None,
        end_device_events: Iterable[EndDeviceEvent] | None = None,
        outage_de_energized_usage_point: Iterable[Outage] | None = None,
        planned_outage_notification: Iterable[PlannedOutageNotification] | None = None,
        service_location: ServiceLocation | None = None,
        usage_point_location: UsagePointLocation | None = None,
        configuration_events: Iterable[ConfigurationEvent] | None = None,
        pricing_structures: Iterable[PricingStructure] | None = None,
        service_category: ServiceCategory | None = None,
        meter_readings: Iterable[MeterReading] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_sdp = is_sdp
        self.is_virtual = is_virtual
        self.phase_code = phase_code
        self.grounded = grounded
        self.service_priority = service_priority
        self.service_delivery_remark = service_delivery_remark
        self.estimated_load = estimated_load
        self.check_billing = check_billing
        self.rated_current = rated_current
        self.nominal_service_voltage = nominal_service_voltage
        self.rated_power = rated_power
        self.outage_region = outage_region
        self.read_cycle = read_cycle
        self.read_route = read_route
        self.ami_billing_ready = ami_billing_ready
        self.connection_state = connection_state
        self.minimal_usage_expected = minimal_usage_expected
        self.disconnection_method = disconnection_method
        self.physical_connection_capacity = physical_connection_capacity
        self.connection_category = connection_category
        self.phase_count = phase_count
        if register is not None:
            UsagePoint.register.extend(self, register)
        if meter_read_schedule is not None:
            self.meter_read_schedule = meter_read_schedule
        if customer_agreement is not None:
            self.customer_agreement = customer_agreement
        if environmental_monitoring_station is not None:
            self.environmental_monitoring_station = environmental_monitoring_station
        if outage is not None:
            UsagePoint.outage.extend(self, outage)
        if metrology_requirements is not None:
            UsagePoint.metrology_requirements.extend(self, metrology_requirements)
        if meter_service_work_tasks is not None:
            UsagePoint.meter_service_work_tasks.extend(self, meter_service_work_tasks)
        if usage_point_groups is not None:
            UsagePoint.usage_point_groups.extend(self, usage_point_groups)
        if equipments is not None:
            UsagePoint.equipments.extend(self, equipments)
        if service_supplier is not None:
            self.service_supplier = service_supplier
        if end_devices is not None:
            UsagePoint.end_devices.extend(self, end_devices)
        if service_multipliers is not None:
            UsagePoint.service_multipliers.extend(self, service_multipliers)
        if end_device_controls is not None:
            UsagePoint.end_device_controls.extend(self, end_device_controls)
        if end_device_events is not None:
            UsagePoint.end_device_events.extend(self, end_device_events)
        if outage_de_energized_usage_point is not None:
            UsagePoint.outage_de_energized_usage_point.extend(self, outage_de_energized_usage_point)
        if planned_outage_notification is not None:
            UsagePoint.planned_outage_notification.extend(self, planned_outage_notification)
        if service_location is not None:
            self.service_location = service_location
        if usage_point_location is not None:
            self.usage_point_location = usage_point_location
        if configuration_events is not None:
            UsagePoint.configuration_events.extend(self, configuration_events)
        if pricing_structures is not None:
            UsagePoint.pricing_structures.extend(self, pricing_structures)
        if service_category is not None:
            self.service_category = service_category
        if meter_readings is not None:
            UsagePoint.meter_readings.extend(self, meter_readings)

    def add_register(self, register: Register) -> Self:
        return UsagePoint.register.add(self, register)

    def remove_register(self, register: Register) -> Self:
        return UsagePoint.register.remove(self, register)

    def clear_register(self) -> Self:
        return UsagePoint.register.clear(self)

    def num_register(self) -> int:
        return UsagePoint.register.count(self)

    def get_register_by_mrid(self, mrid: str) -> Register | None:
        return UsagePoint.register.get_by_mrid(self, mrid)

    def add_outage(self, outage: Outage) -> Self:
        return UsagePoint.outage.add(self, outage)

    def remove_outage(self, outage: Outage) -> Self:
        return UsagePoint.outage.remove(self, outage)

    def clear_outage(self) -> Self:
        return UsagePoint.outage.clear(self)

    def num_outage(self) -> int:
        return UsagePoint.outage.count(self)

    def get_outage_by_mrid(self, mrid: str) -> Outage | None:
        return UsagePoint.outage.get_by_mrid(self, mrid)

    def add_metrology_requirement(self, metrology_requirement: MetrologyRequirement) -> Self:
        return UsagePoint.metrology_requirements.add(self, metrology_requirement)

    def remove_metrology_requirement(self, metrology_requirement: MetrologyRequirement) -> Self:
        return UsagePoint.metrology_requirements.remove(self, metrology_requirement)

    def clear_metrology_requirements(self) -> Self:
        return UsagePoint.metrology_requirements.clear(self)

    def num_metrology_requirement(self) -> int:
        return UsagePoint.metrology_requirements.count(self)

    def get_metrology_requirement_by_mrid(self, mrid: str) -> MetrologyRequirement | None:
        return UsagePoint.metrology_requirements.get_by_mrid(self, mrid)

    def add_meter_service_work_task(self, meter_service_work_task: MeterWorkTask) -> Self:
        return UsagePoint.meter_service_work_tasks.add(self, meter_service_work_task)

    def remove_meter_service_work_task(self, meter_service_work_task: MeterWorkTask) -> Self:
        return UsagePoint.meter_service_work_tasks.remove(self, meter_service_work_task)

    def clear_meter_service_work_tasks(self) -> Self:
        return UsagePoint.meter_service_work_tasks.clear(self)

    def num_meter_service_work_task(self) -> int:
        return UsagePoint.meter_service_work_tasks.count(self)

    def get_meter_service_work_task_by_mrid(self, mrid: str) -> MeterWorkTask | None:
        return UsagePoint.meter_service_work_tasks.get_by_mrid(self, mrid)

    def add_usage_point_group(self, usage_point_group: UsagePointGroup) -> Self:
        return UsagePoint.usage_point_groups.add(self, usage_point_group)

    def remove_usage_point_group(self, usage_point_group: UsagePointGroup) -> Self:
        return UsagePoint.usage_point_groups.remove(self, usage_point_group)

    def clear_usage_point_groups(self) -> Self:
        return UsagePoint.usage_point_groups.clear(self)

    def num_usage_point_group(self) -> int:
        return UsagePoint.usage_point_groups.count(self)

    def get_usage_point_group_by_mrid(self, mrid: str) -> UsagePointGroup | None:
        return UsagePoint.usage_point_groups.get_by_mrid(self, mrid)

    def add_equipment(self, equipment: Equipment) -> Self:
        return UsagePoint.equipments.add(self, equipment)

    def remove_equipment(self, equipment: Equipment) -> Self:
        return UsagePoint.equipments.remove(self, equipment)

    def clear_equipments(self) -> Self:
        return UsagePoint.equipments.clear(self)

    def num_equipment(self) -> int:
        return UsagePoint.equipments.count(self)

    def get_equipment_by_mrid(self, mrid: str) -> Equipment | None:
        return UsagePoint.equipments.get_by_mrid(self, mrid)

    def add_end_device(self, end_device: EndDevice) -> Self:
        return UsagePoint.end_devices.add(self, end_device)

    def remove_end_device(self, end_device: EndDevice) -> Self:
        return UsagePoint.end_devices.remove(self, end_device)

    def clear_end_devices(self) -> Self:
        return UsagePoint.end_devices.clear(self)

    def num_end_device(self) -> int:
        return UsagePoint.end_devices.count(self)

    def get_end_device_by_mrid(self, mrid: str) -> EndDevice | None:
        return UsagePoint.end_devices.get_by_mrid(self, mrid)

    def add_service_multiplier(self, service_multiplier: ServiceMultiplier) -> Self:
        return UsagePoint.service_multipliers.add(self, service_multiplier)

    def remove_service_multiplier(self, service_multiplier: ServiceMultiplier) -> Self:
        return UsagePoint.service_multipliers.remove(self, service_multiplier)

    def clear_service_multipliers(self) -> Self:
        return UsagePoint.service_multipliers.clear(self)

    def num_service_multiplier(self) -> int:
        return UsagePoint.service_multipliers.count(self)

    def get_service_multiplier_by_mrid(self, mrid: str) -> ServiceMultiplier | None:
        return UsagePoint.service_multipliers.get_by_mrid(self, mrid)

    def add_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return UsagePoint.end_device_controls.add(self, end_device_control)

    def remove_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return UsagePoint.end_device_controls.remove(self, end_device_control)

    def clear_end_device_controls(self) -> Self:
        return UsagePoint.end_device_controls.clear(self)

    def num_end_device_control(self) -> int:
        return UsagePoint.end_device_controls.count(self)

    def get_end_device_control_by_mrid(self, mrid: str) -> EndDeviceControl | None:
        return UsagePoint.end_device_controls.get_by_mrid(self, mrid)

    def add_end_device_event(self, end_device_event: EndDeviceEvent) -> Self:
        return UsagePoint.end_device_events.add(self, end_device_event)

    def remove_end_device_event(self, end_device_event: EndDeviceEvent) -> Self:
        return UsagePoint.end_device_events.remove(self, end_device_event)

    def clear_end_device_events(self) -> Self:
        return UsagePoint.end_device_events.clear(self)

    def num_end_device_event(self) -> int:
        return UsagePoint.end_device_events.count(self)

    def get_end_device_event_by_mrid(self, mrid: str) -> EndDeviceEvent | None:
        return UsagePoint.end_device_events.get_by_mrid(self, mrid)

    def add_outage_de_energized_usage_point(self, outage_de_energized_usage_point: Outage) -> Self:
        return UsagePoint.outage_de_energized_usage_point.add(self, outage_de_energized_usage_point)

    def remove_outage_de_energized_usage_point(
        self, outage_de_energized_usage_point: Outage
    ) -> Self:
        return UsagePoint.outage_de_energized_usage_point.remove(
            self, outage_de_energized_usage_point
        )

    def clear_outage_de_energized_usage_point(self) -> Self:
        return UsagePoint.outage_de_energized_usage_point.clear(self)

    def num_outage_de_energized_usage_point(self) -> int:
        return UsagePoint.outage_de_energized_usage_point.count(self)

    def get_outage_de_energized_usage_point_by_mrid(self, mrid: str) -> Outage | None:
        return UsagePoint.outage_de_energized_usage_point.get_by_mrid(self, mrid)

    def add_planned_outage_notification(
        self, planned_outage_notification: PlannedOutageNotification
    ) -> Self:
        return UsagePoint.planned_outage_notification.add(self, planned_outage_notification)

    def remove_planned_outage_notification(
        self, planned_outage_notification: PlannedOutageNotification
    ) -> Self:
        return UsagePoint.planned_outage_notification.remove(self, planned_outage_notification)

    def clear_planned_outage_notification(self) -> Self:
        return UsagePoint.planned_outage_notification.clear(self)

    def num_planned_outage_notification(self) -> int:
        return UsagePoint.planned_outage_notification.count(self)

    def get_planned_outage_notification_by_mrid(
        self, mrid: str
    ) -> PlannedOutageNotification | None:
        return UsagePoint.planned_outage_notification.get_by_mrid(self, mrid)

    def add_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return UsagePoint.configuration_events.add(self, configuration_event)

    def remove_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return UsagePoint.configuration_events.remove(self, configuration_event)

    def clear_configuration_events(self) -> Self:
        return UsagePoint.configuration_events.clear(self)

    def num_configuration_event(self) -> int:
        return UsagePoint.configuration_events.count(self)

    def get_configuration_event_by_mrid(self, mrid: str) -> ConfigurationEvent | None:
        return UsagePoint.configuration_events.get_by_mrid(self, mrid)

    def add_pricing_structure(self, pricing_structure: PricingStructure) -> Self:
        return UsagePoint.pricing_structures.add(self, pricing_structure)

    def remove_pricing_structure(self, pricing_structure: PricingStructure) -> Self:
        return UsagePoint.pricing_structures.remove(self, pricing_structure)

    def clear_pricing_structures(self) -> Self:
        return UsagePoint.pricing_structures.clear(self)

    def num_pricing_structure(self) -> int:
        return UsagePoint.pricing_structures.count(self)

    def get_pricing_structure_by_mrid(self, mrid: str) -> PricingStructure | None:
        return UsagePoint.pricing_structures.get_by_mrid(self, mrid)

    def add_meter_reading(self, meter_reading: MeterReading) -> Self:
        return UsagePoint.meter_readings.add(self, meter_reading)

    def remove_meter_reading(self, meter_reading: MeterReading) -> Self:
        return UsagePoint.meter_readings.remove(self, meter_reading)

    def clear_meter_readings(self) -> Self:
        return UsagePoint.meter_readings.clear(self)

    def num_meter_reading(self) -> int:
        return UsagePoint.meter_readings.count(self)

    def get_meter_reading_by_mrid(self, mrid: str) -> MeterReading | None:
        return UsagePoint.meter_readings.get_by_mrid(self, mrid)
