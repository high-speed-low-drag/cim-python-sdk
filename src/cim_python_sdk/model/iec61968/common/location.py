"""CIM class Location (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.asset_location_hazard import AssetLocationHazard
    from cim_python_sdk.model.iec61968.common.configuration_event import ConfigurationEvent
    from cim_python_sdk.model.iec61968.common.coordinate_system import CoordinateSystem
    from cim_python_sdk.model.iec61968.common.crew import Crew
    from cim_python_sdk.model.iec61968.common.electronic_address import ElectronicAddress
    from cim_python_sdk.model.iec61968.common.position_point import PositionPoint
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.common.street_address import StreetAddress
    from cim_python_sdk.model.iec61968.common.telephone_number import TelephoneNumber
    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew import OldCrew
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property import LandProperty
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.route import Route
    from cim_python_sdk.model.iec61968.operations.incident import Incident
    from cim_python_sdk.model.iec61968.operations.outage_order import OutageOrder
    from cim_python_sdk.model.iec61968.operations.switching_order import SwitchingOrder
    from cim_python_sdk.model.iec61968.operations.trouble_order import TroubleOrder
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource
    from cim_python_sdk.model.iec61970.base.faults.fault import Fault
    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement
    from cim_python_sdk.model.iec62325.environmental.environmental_location_type import (
        EnvironmentalLocationType,
    )
    from cim_python_sdk.model.iec62325.market_common.environmental_monitoring_station import (
        EnvironmentalMonitoringStation,
    )


class Location(IdentifiedObject):
    """The place, scene, or point of something where someone or something has been, is, and/or
    will be at a given moment in time. It can be defined with one or more position points
    (coordinates) in a given coordinate system."""

    __slots__ = (
        "_assets",
        "_configuration_events",
        "_coordinate_system",
        "_crew",
        "_crews",
        "_environmental_location_kind",
        "_environmental_monitoring_station",
        "_fault",
        "_hazards",
        "_incident",
        "_land_properties",
        "_measurements",
        "_outage_order",
        "_position_points",
        "_power_system_resources",
        "_routes",
        "_switching_order",
        "_trouble_order",
        "_trouble_ticket",
        "direction",
        "electronic_address",
        "geo_info_reference",
        "main_address",
        "phone1",
        "phone2",
        "secondary_address",
        "status",
        "type",
    )

    type: str | None
    main_address: StreetAddress | None
    secondary_address: StreetAddress | None
    phone1: TelephoneNumber | None
    phone2: TelephoneNumber | None
    electronic_address: ElectronicAddress | None
    geo_info_reference: str | None
    direction: str | None
    status: Status | None

    environmental_location_kind: Many[EnvironmentalLocationType] = Many(
        EndMeta(
            name="environmental_location_kind",
            cim_role="EnvironmentalLocationKind",
            target="cim_python_sdk.model.iec62325.environmental.environmental_location_type:EnvironmentalLocationType",
            many=True,
            lower=0,
            upper=None,
            inverse="location",
            aggregation="none",
        )
    )
    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="location",
            aggregation="none",
        )
    )
    environmental_monitoring_station: Many[EnvironmentalMonitoringStation] = Many(
        EndMeta(
            name="environmental_monitoring_station",
            cim_role="EnvironmentalMonitoringStation",
            target="cim_python_sdk.model.iec62325.market_common.environmental_monitoring_station:EnvironmentalMonitoringStation",
            many=True,
            lower=0,
            upper=None,
            inverse="location",
            aggregation="none",
        )
    )
    trouble_order: One[TroubleOrder] = One(
        EndMeta(
            name="trouble_order",
            cim_role="TroubleOrder",
            target="cim_python_sdk.model.iec61968.operations.trouble_order:TroubleOrder",
            many=False,
            lower=0,
            upper=1,
            inverse="location",
            aggregation="none",
        )
    )
    switching_order: One[SwitchingOrder] = One(
        EndMeta(
            name="switching_order",
            cim_role="SwitchingOrder",
            target="cim_python_sdk.model.iec61968.operations.switching_order:SwitchingOrder",
            many=False,
            lower=0,
            upper=1,
            inverse="location",
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
            inverse="location",
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
            inverse="changed_location",
            aggregation="none",
        )
    )
    outage_order: One[OutageOrder] = One(
        EndMeta(
            name="outage_order",
            cim_role="OutageOrder",
            target="cim_python_sdk.model.iec61968.operations.outage_order:OutageOrder",
            many=False,
            lower=0,
            upper=1,
            inverse="location",
            aggregation="none",
        )
    )
    fault: Many[Fault] = Many(
        EndMeta(
            name="fault",
            cim_role="Fault",
            target="cim_python_sdk.model.iec61970.base.faults.fault:Fault",
            many=True,
            lower=0,
            upper=None,
            inverse="location",
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
            inverse="location",
            aggregation="none",
        )
    )
    power_system_resources: Many[PowerSystemResource] = Many(
        EndMeta(
            name="power_system_resources",
            cim_role="PowerSystemResources",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=True,
            lower=0,
            upper=None,
            inverse="location",
            aggregation="none",
        )
    )
    crews: Many[OldCrew] = Many(
        EndMeta(
            name="crews",
            cim_role="Crews",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_crew:OldCrew",
            many=True,
            lower=0,
            upper=None,
            inverse="locations",
            aggregation="none",
        )
    )
    hazards: Many[AssetLocationHazard] = Many(
        EndMeta(
            name="hazards",
            cim_role="Hazards",
            target="cim_python_sdk.model.iec61968.assets.asset_location_hazard:AssetLocationHazard",
            many=True,
            lower=0,
            upper=None,
            inverse="locations",
            aggregation="none",
        )
    )
    land_properties: Many[LandProperty] = Many(
        EndMeta(
            name="land_properties",
            cim_role="LandProperties",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property:LandProperty",
            many=True,
            lower=0,
            upper=None,
            inverse="locations",
            aggregation="none",
        )
    )
    routes: Many[Route] = Many(
        EndMeta(
            name="routes",
            cim_role="Routes",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.route:Route",
            many=True,
            lower=0,
            upper=None,
            inverse="locations",
            aggregation="none",
        )
    )
    trouble_ticket: One[TroubleTicket] = One(
        EndMeta(
            name="trouble_ticket",
            cim_role="TroubleTicket",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=False,
            lower=0,
            upper=1,
            inverse="location",
            aggregation="none",
        )
    )
    coordinate_system: One[CoordinateSystem] = One(
        EndMeta(
            name="coordinate_system",
            cim_role="CoordinateSystem",
            target="cim_python_sdk.model.iec61968.common.coordinate_system:CoordinateSystem",
            many=False,
            lower=0,
            upper=1,
            inverse="locations",
            aggregation="none",
        )
    )
    position_points: Many[PositionPoint] = Many(
        EndMeta(
            name="position_points",
            cim_role="PositionPoints",
            target="cim_python_sdk.model.iec61968.common.position_point:PositionPoint",
            many=True,
            lower=0,
            upper=None,
            inverse="location",
            aggregation="none",
        )
    )
    measurements: Many[Measurement] = Many(
        EndMeta(
            name="measurements",
            cim_role="Measurements",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=True,
            lower=0,
            upper=None,
            inverse="locations",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Location",
        package="TC57CIM/IEC61968/Common",
        guid="{671B9EF5-A0CB-467e-ADAC-FBEA4156EEBB}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("main_address", "mainAddress", "StreetAddress", 0, 1, "compound"),
            AttrMeta("secondary_address", "secondaryAddress", "StreetAddress", 0, 1, "compound"),
            AttrMeta("phone1", "phone1", "TelephoneNumber", 0, 1, "compound"),
            AttrMeta("phone2", "phone2", "TelephoneNumber", 0, 1, "compound"),
            AttrMeta(
                "electronic_address", "electronicAddress", "ElectronicAddress", 0, 1, "compound"
            ),
            AttrMeta("geo_info_reference", "geoInfoReference", "str", 0, 1, "primitive"),
            AttrMeta("direction", "direction", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            environmental_location_kind.meta,
            assets.meta,
            environmental_monitoring_station.meta,
            trouble_order.meta,
            switching_order.meta,
            crew.meta,
            configuration_events.meta,
            outage_order.meta,
            fault.meta,
            incident.meta,
            power_system_resources.meta,
            crews.meta,
            hazards.meta,
            land_properties.meta,
            routes.meta,
            trouble_ticket.meta,
            coordinate_system.meta,
            position_points.meta,
            measurements.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        main_address: StreetAddress | None = None,
        secondary_address: StreetAddress | None = None,
        phone1: TelephoneNumber | None = None,
        phone2: TelephoneNumber | None = None,
        electronic_address: ElectronicAddress | None = None,
        geo_info_reference: str | None = None,
        direction: str | None = None,
        status: Status | None = None,
        environmental_location_kind: Iterable[EnvironmentalLocationType] | None = None,
        assets: Iterable[Asset] | None = None,
        environmental_monitoring_station: Iterable[EnvironmentalMonitoringStation] | None = None,
        trouble_order: TroubleOrder | None = None,
        switching_order: SwitchingOrder | None = None,
        crew: Iterable[Crew] | None = None,
        configuration_events: Iterable[ConfigurationEvent] | None = None,
        outage_order: OutageOrder | None = None,
        fault: Iterable[Fault] | None = None,
        incident: Incident | None = None,
        power_system_resources: Iterable[PowerSystemResource] | None = None,
        crews: Iterable[OldCrew] | None = None,
        hazards: Iterable[AssetLocationHazard] | None = None,
        land_properties: Iterable[LandProperty] | None = None,
        routes: Iterable[Route] | None = None,
        trouble_ticket: TroubleTicket | None = None,
        coordinate_system: CoordinateSystem | None = None,
        position_points: Iterable[PositionPoint] | None = None,
        measurements: Iterable[Measurement] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.main_address = main_address
        self.secondary_address = secondary_address
        self.phone1 = phone1
        self.phone2 = phone2
        self.electronic_address = electronic_address
        self.geo_info_reference = geo_info_reference
        self.direction = direction
        self.status = status
        if environmental_location_kind is not None:
            Location.environmental_location_kind.extend(self, environmental_location_kind)
        if assets is not None:
            Location.assets.extend(self, assets)
        if environmental_monitoring_station is not None:
            Location.environmental_monitoring_station.extend(self, environmental_monitoring_station)
        if trouble_order is not None:
            self.trouble_order = trouble_order
        if switching_order is not None:
            self.switching_order = switching_order
        if crew is not None:
            Location.crew.extend(self, crew)
        if configuration_events is not None:
            Location.configuration_events.extend(self, configuration_events)
        if outage_order is not None:
            self.outage_order = outage_order
        if fault is not None:
            Location.fault.extend(self, fault)
        if incident is not None:
            self.incident = incident
        if power_system_resources is not None:
            Location.power_system_resources.extend(self, power_system_resources)
        if crews is not None:
            Location.crews.extend(self, crews)
        if hazards is not None:
            Location.hazards.extend(self, hazards)
        if land_properties is not None:
            Location.land_properties.extend(self, land_properties)
        if routes is not None:
            Location.routes.extend(self, routes)
        if trouble_ticket is not None:
            self.trouble_ticket = trouble_ticket
        if coordinate_system is not None:
            self.coordinate_system = coordinate_system
        if position_points is not None:
            Location.position_points.extend(self, position_points)
        if measurements is not None:
            Location.measurements.extend(self, measurements)

    def add_environmental_location_kind(
        self, environmental_location_kind: EnvironmentalLocationType
    ) -> Self:
        return Location.environmental_location_kind.add(self, environmental_location_kind)

    def remove_environmental_location_kind(
        self, environmental_location_kind: EnvironmentalLocationType
    ) -> Self:
        return Location.environmental_location_kind.remove(self, environmental_location_kind)

    def clear_environmental_location_kind(self) -> Self:
        return Location.environmental_location_kind.clear(self)

    def num_environmental_location_kind(self) -> int:
        return Location.environmental_location_kind.count(self)

    def add_asset(self, asset: Asset) -> Self:
        return Location.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return Location.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return Location.assets.clear(self)

    def num_asset(self) -> int:
        return Location.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return Location.assets.get_by_mrid(self, mrid)

    def add_environmental_monitoring_station(
        self, environmental_monitoring_station: EnvironmentalMonitoringStation
    ) -> Self:
        return Location.environmental_monitoring_station.add(self, environmental_monitoring_station)

    def remove_environmental_monitoring_station(
        self, environmental_monitoring_station: EnvironmentalMonitoringStation
    ) -> Self:
        return Location.environmental_monitoring_station.remove(
            self, environmental_monitoring_station
        )

    def clear_environmental_monitoring_station(self) -> Self:
        return Location.environmental_monitoring_station.clear(self)

    def num_environmental_monitoring_station(self) -> int:
        return Location.environmental_monitoring_station.count(self)

    def get_environmental_monitoring_station_by_mrid(
        self, mrid: str
    ) -> EnvironmentalMonitoringStation | None:
        return Location.environmental_monitoring_station.get_by_mrid(self, mrid)

    def add_crew(self, crew: Crew) -> Self:
        return Location.crew.add(self, crew)

    def remove_crew(self, crew: Crew) -> Self:
        return Location.crew.remove(self, crew)

    def clear_crew(self) -> Self:
        return Location.crew.clear(self)

    def num_crew(self) -> int:
        return Location.crew.count(self)

    def get_crew_by_mrid(self, mrid: str) -> Crew | None:
        return Location.crew.get_by_mrid(self, mrid)

    def add_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return Location.configuration_events.add(self, configuration_event)

    def remove_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return Location.configuration_events.remove(self, configuration_event)

    def clear_configuration_events(self) -> Self:
        return Location.configuration_events.clear(self)

    def num_configuration_event(self) -> int:
        return Location.configuration_events.count(self)

    def get_configuration_event_by_mrid(self, mrid: str) -> ConfigurationEvent | None:
        return Location.configuration_events.get_by_mrid(self, mrid)

    def add_fault(self, fault: Fault) -> Self:
        return Location.fault.add(self, fault)

    def remove_fault(self, fault: Fault) -> Self:
        return Location.fault.remove(self, fault)

    def clear_fault(self) -> Self:
        return Location.fault.clear(self)

    def num_fault(self) -> int:
        return Location.fault.count(self)

    def get_fault_by_mrid(self, mrid: str) -> Fault | None:
        return Location.fault.get_by_mrid(self, mrid)

    def add_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return Location.power_system_resources.add(self, power_system_resource)

    def remove_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return Location.power_system_resources.remove(self, power_system_resource)

    def clear_power_system_resources(self) -> Self:
        return Location.power_system_resources.clear(self)

    def num_power_system_resource(self) -> int:
        return Location.power_system_resources.count(self)

    def get_power_system_resource_by_mrid(self, mrid: str) -> PowerSystemResource | None:
        return Location.power_system_resources.get_by_mrid(self, mrid)

    def add_crews(self, crews: OldCrew) -> Self:
        return Location.crews.add(self, crews)

    def remove_crews(self, crews: OldCrew) -> Self:
        return Location.crews.remove(self, crews)

    def clear_crews(self) -> Self:
        return Location.crews.clear(self)

    def num_crews(self) -> int:
        return Location.crews.count(self)

    def get_crews_by_mrid(self, mrid: str) -> OldCrew | None:
        return Location.crews.get_by_mrid(self, mrid)

    def add_hazard(self, hazard: AssetLocationHazard) -> Self:
        return Location.hazards.add(self, hazard)

    def remove_hazard(self, hazard: AssetLocationHazard) -> Self:
        return Location.hazards.remove(self, hazard)

    def clear_hazards(self) -> Self:
        return Location.hazards.clear(self)

    def num_hazard(self) -> int:
        return Location.hazards.count(self)

    def get_hazard_by_mrid(self, mrid: str) -> AssetLocationHazard | None:
        return Location.hazards.get_by_mrid(self, mrid)

    def add_land_property(self, land_property: LandProperty) -> Self:
        return Location.land_properties.add(self, land_property)

    def remove_land_property(self, land_property: LandProperty) -> Self:
        return Location.land_properties.remove(self, land_property)

    def clear_land_properties(self) -> Self:
        return Location.land_properties.clear(self)

    def num_land_property(self) -> int:
        return Location.land_properties.count(self)

    def get_land_property_by_mrid(self, mrid: str) -> LandProperty | None:
        return Location.land_properties.get_by_mrid(self, mrid)

    def add_route(self, route: Route) -> Self:
        return Location.routes.add(self, route)

    def remove_route(self, route: Route) -> Self:
        return Location.routes.remove(self, route)

    def clear_routes(self) -> Self:
        return Location.routes.clear(self)

    def num_route(self) -> int:
        return Location.routes.count(self)

    def get_route_by_mrid(self, mrid: str) -> Route | None:
        return Location.routes.get_by_mrid(self, mrid)

    def add_position_point(self, position_point: PositionPoint) -> Self:
        return Location.position_points.add(self, position_point)

    def remove_position_point(self, position_point: PositionPoint) -> Self:
        return Location.position_points.remove(self, position_point)

    def clear_position_points(self) -> Self:
        return Location.position_points.clear(self)

    def num_position_point(self) -> int:
        return Location.position_points.count(self)

    def add_measurement(self, measurement: Measurement) -> Self:
        return Location.measurements.add(self, measurement)

    def remove_measurement(self, measurement: Measurement) -> Self:
        return Location.measurements.remove(self, measurement)

    def clear_measurements(self) -> Self:
        return Location.measurements.clear(self)

    def num_measurement(self) -> int:
        return Location.measurements.count(self)

    def get_measurement_by_mrid(self, mrid: str) -> Measurement | None:
        return Location.measurements.get_by_mrid(self, mrid)
