"""CIM class TimeSeries (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.environmental_monitoring_station import (
        EnvironmentalMonitoringStation,
    )
    from cim_python_sdk.model.iec62325.market_common.market_participant import MarketParticipant
    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_management.attribute_instance_component import (
        AttributeInstanceComponent,
    )
    from cim_python_sdk.model.iec62325.market_management.auction import Auction
    from cim_python_sdk.model.iec62325.market_management.constraint_duration import (
        ConstraintDuration,
    )
    from cim_python_sdk.model.iec62325.market_management.date_and_or_time import DateAndOrTime
    from cim_python_sdk.model.iec62325.market_management.domain import Domain
    from cim_python_sdk.model.iec62325.market_management.flow_direction import FlowDirection
    from cim_python_sdk.model.iec62325.market_management.market_document import MarketDocument
    from cim_python_sdk.model.iec62325.market_management.market_evaluation_point import (
        MarketEvaluationPoint,
    )
    from cim_python_sdk.model.iec62325.market_management.market_object_status import (
        MarketObjectStatus,
    )
    from cim_python_sdk.model.iec62325.market_management.mkt_psr_type import MktPSRType
    from cim_python_sdk.model.iec62325.market_management.period import Period
    from cim_python_sdk.model.iec62325.market_management.point import Point
    from cim_python_sdk.model.iec62325.market_management.price import Price
    from cim_python_sdk.model.iec62325.market_management.quantity import Quantity
    from cim_python_sdk.model.iec62325.market_management.reason import Reason
    from cim_python_sdk.model.iec62325.market_management.unit import Unit


class TimeSeries(IdentifiedObject):
    """A set of regular time-ordered measurements or values of quantitative nature of an
    individual or collective phenomenon taken at successive, in most cases equidistant,
    periods / points of time."""

    __slots__ = (
        "_attribute_instance_component",
        "_auction",
        "_constraint_duration",
        "_date_and_or_time",
        "_domain",
        "_environmental_monitoring_station",
        "_flow_direction",
        "_market_document",
        "_market_evaluation_point",
        "_market_object_status",
        "_market_participant",
        "_mkt_psr_type",
        "_period",
        "_point",
        "_price",
        "_quantity",
        "_reason",
        "_registered_resource",
        "_unit",
        "business_type",
        "cancelled_ts",
        "curve_type",
        "object_aggregation",
        "product",
        "version",
    )

    business_type: str | None
    cancelled_ts: str | None
    curve_type: str | None
    object_aggregation: str | None
    product: str | None
    version: str | None

    constraint_duration: Many[ConstraintDuration] = Many(
        EndMeta(
            name="constraint_duration",
            cim_role="ConstraintDuration",
            target="cim_python_sdk.model.iec62325.market_management.constraint_duration:ConstraintDuration",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    flow_direction: Many[FlowDirection] = Many(
        EndMeta(
            name="flow_direction",
            cim_role="FlowDirection",
            target="cim_python_sdk.model.iec62325.market_management.flow_direction:FlowDirection",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    attribute_instance_component: Many[AttributeInstanceComponent] = Many(
        EndMeta(
            name="attribute_instance_component",
            cim_role="AttributeInstanceComponent",
            target="cim_python_sdk.model.iec62325.market_management.attribute_instance_component:AttributeInstanceComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    market_participant: Many[MarketParticipant] = Many(
        EndMeta(
            name="market_participant",
            cim_role="MarketParticipant",
            target="cim_python_sdk.model.iec62325.market_common.market_participant:MarketParticipant",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    unit: Many[Unit] = Many(
        EndMeta(
            name="unit",
            cim_role="Unit",
            target="cim_python_sdk.model.iec62325.market_management.unit:Unit",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    period: Many[Period] = Many(
        EndMeta(
            name="period",
            cim_role="Period",
            target="cim_python_sdk.model.iec62325.market_management.period:Period",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    domain: Many[Domain] = Many(
        EndMeta(
            name="domain",
            cim_role="Domain",
            target="cim_python_sdk.model.iec62325.market_management.domain:Domain",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    date_and_or_time: Many[DateAndOrTime] = Many(
        EndMeta(
            name="date_and_or_time",
            cim_role="DateAndOrTime",
            target="cim_python_sdk.model.iec62325.market_management.date_and_or_time:DateAndOrTime",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    auction: Many[Auction] = Many(
        EndMeta(
            name="auction",
            cim_role="Auction",
            target="cim_python_sdk.model.iec62325.market_management.auction:Auction",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
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
            inverse="time_series",
            aggregation="none",
        )
    )
    price: Many[Price] = Many(
        EndMeta(
            name="price",
            cim_role="Price",
            target="cim_python_sdk.model.iec62325.market_management.price:Price",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    market_document: Many[MarketDocument] = Many(
        EndMeta(
            name="market_document",
            cim_role="MarketDocument",
            target="cim_python_sdk.model.iec62325.market_management.market_document:MarketDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    quantity: Many[Quantity] = Many(
        EndMeta(
            name="quantity",
            cim_role="Quantity",
            target="cim_python_sdk.model.iec62325.market_management.quantity:Quantity",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    mkt_psr_type: Many[MktPSRType] = Many(
        EndMeta(
            name="mkt_psr_type",
            cim_role="MktPSRType",
            target="cim_python_sdk.model.iec62325.market_management.mkt_psr_type:MktPSRType",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    market_evaluation_point: Many[MarketEvaluationPoint] = Many(
        EndMeta(
            name="market_evaluation_point",
            cim_role="MarketEvaluationPoint",
            target="cim_python_sdk.model.iec62325.market_management.market_evaluation_point:MarketEvaluationPoint",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    market_object_status: Many[MarketObjectStatus] = Many(
        EndMeta(
            name="market_object_status",
            cim_role="MarketObjectStatus",
            target="cim_python_sdk.model.iec62325.market_management.market_object_status:MarketObjectStatus",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    point: Many[Point] = Many(
        EndMeta(
            name="point",
            cim_role="Point",
            target="cim_python_sdk.model.iec62325.market_management.point:Point",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )
    reason: Many[Reason] = Many(
        EndMeta(
            name="reason",
            cim_role="Reason",
            target="cim_python_sdk.model.iec62325.market_management.reason:Reason",
            many=True,
            lower=0,
            upper=None,
            inverse="time_series",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TimeSeries",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{4E4FCB53-20DF-4ce4-947E-E3D41406911E}",
        attributes=(
            AttrMeta("business_type", "businessType", "str", 0, 1, "primitive"),
            AttrMeta("cancelled_ts", "cancelledTS", "str", 0, 1, "primitive"),
            AttrMeta("curve_type", "curveType", "str", 0, 1, "primitive"),
            AttrMeta("object_aggregation", "objectAggregation", "str", 0, 1, "primitive"),
            AttrMeta("product", "product", "str", 0, 1, "primitive"),
            AttrMeta("version", "version", "str", 0, 1, "primitive"),
        ),
        ends=(
            constraint_duration.meta,
            flow_direction.meta,
            attribute_instance_component.meta,
            market_participant.meta,
            unit.meta,
            period.meta,
            domain.meta,
            date_and_or_time.meta,
            auction.meta,
            environmental_monitoring_station.meta,
            price.meta,
            market_document.meta,
            quantity.meta,
            mkt_psr_type.meta,
            market_evaluation_point.meta,
            registered_resource.meta,
            market_object_status.meta,
            point.meta,
            reason.meta,
        ),
    )

    def __init__(
        self,
        *,
        business_type: str | None = None,
        cancelled_ts: str | None = None,
        curve_type: str | None = None,
        object_aggregation: str | None = None,
        product: str | None = None,
        version: str | None = None,
        constraint_duration: Iterable[ConstraintDuration] | None = None,
        flow_direction: Iterable[FlowDirection] | None = None,
        attribute_instance_component: Iterable[AttributeInstanceComponent] | None = None,
        market_participant: Iterable[MarketParticipant] | None = None,
        unit: Iterable[Unit] | None = None,
        period: Iterable[Period] | None = None,
        domain: Iterable[Domain] | None = None,
        date_and_or_time: Iterable[DateAndOrTime] | None = None,
        auction: Iterable[Auction] | None = None,
        environmental_monitoring_station: Iterable[EnvironmentalMonitoringStation] | None = None,
        price: Iterable[Price] | None = None,
        market_document: Iterable[MarketDocument] | None = None,
        quantity: Iterable[Quantity] | None = None,
        mkt_psr_type: Iterable[MktPSRType] | None = None,
        market_evaluation_point: Iterable[MarketEvaluationPoint] | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        market_object_status: Iterable[MarketObjectStatus] | None = None,
        point: Iterable[Point] | None = None,
        reason: Iterable[Reason] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.business_type = business_type
        self.cancelled_ts = cancelled_ts
        self.curve_type = curve_type
        self.object_aggregation = object_aggregation
        self.product = product
        self.version = version
        if constraint_duration is not None:
            TimeSeries.constraint_duration.extend(self, constraint_duration)
        if flow_direction is not None:
            TimeSeries.flow_direction.extend(self, flow_direction)
        if attribute_instance_component is not None:
            TimeSeries.attribute_instance_component.extend(self, attribute_instance_component)
        if market_participant is not None:
            TimeSeries.market_participant.extend(self, market_participant)
        if unit is not None:
            TimeSeries.unit.extend(self, unit)
        if period is not None:
            TimeSeries.period.extend(self, period)
        if domain is not None:
            TimeSeries.domain.extend(self, domain)
        if date_and_or_time is not None:
            TimeSeries.date_and_or_time.extend(self, date_and_or_time)
        if auction is not None:
            TimeSeries.auction.extend(self, auction)
        if environmental_monitoring_station is not None:
            TimeSeries.environmental_monitoring_station.extend(
                self, environmental_monitoring_station
            )
        if price is not None:
            TimeSeries.price.extend(self, price)
        if market_document is not None:
            TimeSeries.market_document.extend(self, market_document)
        if quantity is not None:
            TimeSeries.quantity.extend(self, quantity)
        if mkt_psr_type is not None:
            TimeSeries.mkt_psr_type.extend(self, mkt_psr_type)
        if market_evaluation_point is not None:
            TimeSeries.market_evaluation_point.extend(self, market_evaluation_point)
        if registered_resource is not None:
            TimeSeries.registered_resource.extend(self, registered_resource)
        if market_object_status is not None:
            TimeSeries.market_object_status.extend(self, market_object_status)
        if point is not None:
            TimeSeries.point.extend(self, point)
        if reason is not None:
            TimeSeries.reason.extend(self, reason)

    def add_constraint_duration(self, constraint_duration: ConstraintDuration) -> Self:
        return TimeSeries.constraint_duration.add(self, constraint_duration)

    def remove_constraint_duration(self, constraint_duration: ConstraintDuration) -> Self:
        return TimeSeries.constraint_duration.remove(self, constraint_duration)

    def clear_constraint_duration(self) -> Self:
        return TimeSeries.constraint_duration.clear(self)

    def num_constraint_duration(self) -> int:
        return TimeSeries.constraint_duration.count(self)

    def add_flow_direction(self, flow_direction: FlowDirection) -> Self:
        return TimeSeries.flow_direction.add(self, flow_direction)

    def remove_flow_direction(self, flow_direction: FlowDirection) -> Self:
        return TimeSeries.flow_direction.remove(self, flow_direction)

    def clear_flow_direction(self) -> Self:
        return TimeSeries.flow_direction.clear(self)

    def num_flow_direction(self) -> int:
        return TimeSeries.flow_direction.count(self)

    def add_attribute_instance_component(
        self, attribute_instance_component: AttributeInstanceComponent
    ) -> Self:
        return TimeSeries.attribute_instance_component.add(self, attribute_instance_component)

    def remove_attribute_instance_component(
        self, attribute_instance_component: AttributeInstanceComponent
    ) -> Self:
        return TimeSeries.attribute_instance_component.remove(self, attribute_instance_component)

    def clear_attribute_instance_component(self) -> Self:
        return TimeSeries.attribute_instance_component.clear(self)

    def num_attribute_instance_component(self) -> int:
        return TimeSeries.attribute_instance_component.count(self)

    def add_market_participant(self, market_participant: MarketParticipant) -> Self:
        return TimeSeries.market_participant.add(self, market_participant)

    def remove_market_participant(self, market_participant: MarketParticipant) -> Self:
        return TimeSeries.market_participant.remove(self, market_participant)

    def clear_market_participant(self) -> Self:
        return TimeSeries.market_participant.clear(self)

    def num_market_participant(self) -> int:
        return TimeSeries.market_participant.count(self)

    def get_market_participant_by_mrid(self, mrid: str) -> MarketParticipant | None:
        return TimeSeries.market_participant.get_by_mrid(self, mrid)

    def add_unit(self, unit: Unit) -> Self:
        return TimeSeries.unit.add(self, unit)

    def remove_unit(self, unit: Unit) -> Self:
        return TimeSeries.unit.remove(self, unit)

    def clear_unit(self) -> Self:
        return TimeSeries.unit.clear(self)

    def num_unit(self) -> int:
        return TimeSeries.unit.count(self)

    def add_period(self, period: Period) -> Self:
        return TimeSeries.period.add(self, period)

    def remove_period(self, period: Period) -> Self:
        return TimeSeries.period.remove(self, period)

    def clear_period(self) -> Self:
        return TimeSeries.period.clear(self)

    def num_period(self) -> int:
        return TimeSeries.period.count(self)

    def add_domain(self, domain: Domain) -> Self:
        return TimeSeries.domain.add(self, domain)

    def remove_domain(self, domain: Domain) -> Self:
        return TimeSeries.domain.remove(self, domain)

    def clear_domain(self) -> Self:
        return TimeSeries.domain.clear(self)

    def num_domain(self) -> int:
        return TimeSeries.domain.count(self)

    def get_domain_by_mrid(self, mrid: str) -> Domain | None:
        return TimeSeries.domain.get_by_mrid(self, mrid)

    def add_date_and_or_time(self, date_and_or_time: DateAndOrTime) -> Self:
        return TimeSeries.date_and_or_time.add(self, date_and_or_time)

    def remove_date_and_or_time(self, date_and_or_time: DateAndOrTime) -> Self:
        return TimeSeries.date_and_or_time.remove(self, date_and_or_time)

    def clear_date_and_or_time(self) -> Self:
        return TimeSeries.date_and_or_time.clear(self)

    def num_date_and_or_time(self) -> int:
        return TimeSeries.date_and_or_time.count(self)

    def add_auction(self, auction: Auction) -> Self:
        return TimeSeries.auction.add(self, auction)

    def remove_auction(self, auction: Auction) -> Self:
        return TimeSeries.auction.remove(self, auction)

    def clear_auction(self) -> Self:
        return TimeSeries.auction.clear(self)

    def num_auction(self) -> int:
        return TimeSeries.auction.count(self)

    def get_auction_by_mrid(self, mrid: str) -> Auction | None:
        return TimeSeries.auction.get_by_mrid(self, mrid)

    def add_environmental_monitoring_station(
        self, environmental_monitoring_station: EnvironmentalMonitoringStation
    ) -> Self:
        return TimeSeries.environmental_monitoring_station.add(
            self, environmental_monitoring_station
        )

    def remove_environmental_monitoring_station(
        self, environmental_monitoring_station: EnvironmentalMonitoringStation
    ) -> Self:
        return TimeSeries.environmental_monitoring_station.remove(
            self, environmental_monitoring_station
        )

    def clear_environmental_monitoring_station(self) -> Self:
        return TimeSeries.environmental_monitoring_station.clear(self)

    def num_environmental_monitoring_station(self) -> int:
        return TimeSeries.environmental_monitoring_station.count(self)

    def get_environmental_monitoring_station_by_mrid(
        self, mrid: str
    ) -> EnvironmentalMonitoringStation | None:
        return TimeSeries.environmental_monitoring_station.get_by_mrid(self, mrid)

    def add_price(self, price: Price) -> Self:
        return TimeSeries.price.add(self, price)

    def remove_price(self, price: Price) -> Self:
        return TimeSeries.price.remove(self, price)

    def clear_price(self) -> Self:
        return TimeSeries.price.clear(self)

    def num_price(self) -> int:
        return TimeSeries.price.count(self)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return TimeSeries.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return TimeSeries.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return TimeSeries.market_document.clear(self)

    def num_market_document(self) -> int:
        return TimeSeries.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return TimeSeries.market_document.get_by_mrid(self, mrid)

    def add_quantity(self, quantity: Quantity) -> Self:
        return TimeSeries.quantity.add(self, quantity)

    def remove_quantity(self, quantity: Quantity) -> Self:
        return TimeSeries.quantity.remove(self, quantity)

    def clear_quantity(self) -> Self:
        return TimeSeries.quantity.clear(self)

    def num_quantity(self) -> int:
        return TimeSeries.quantity.count(self)

    def add_mkt_psr_type(self, mkt_psr_type: MktPSRType) -> Self:
        return TimeSeries.mkt_psr_type.add(self, mkt_psr_type)

    def remove_mkt_psr_type(self, mkt_psr_type: MktPSRType) -> Self:
        return TimeSeries.mkt_psr_type.remove(self, mkt_psr_type)

    def clear_mkt_psr_type(self) -> Self:
        return TimeSeries.mkt_psr_type.clear(self)

    def num_mkt_psr_type(self) -> int:
        return TimeSeries.mkt_psr_type.count(self)

    def get_mkt_psr_type_by_mrid(self, mrid: str) -> MktPSRType | None:
        return TimeSeries.mkt_psr_type.get_by_mrid(self, mrid)

    def add_market_evaluation_point(self, market_evaluation_point: MarketEvaluationPoint) -> Self:
        return TimeSeries.market_evaluation_point.add(self, market_evaluation_point)

    def remove_market_evaluation_point(
        self, market_evaluation_point: MarketEvaluationPoint
    ) -> Self:
        return TimeSeries.market_evaluation_point.remove(self, market_evaluation_point)

    def clear_market_evaluation_point(self) -> Self:
        return TimeSeries.market_evaluation_point.clear(self)

    def num_market_evaluation_point(self) -> int:
        return TimeSeries.market_evaluation_point.count(self)

    def get_market_evaluation_point_by_mrid(self, mrid: str) -> MarketEvaluationPoint | None:
        return TimeSeries.market_evaluation_point.get_by_mrid(self, mrid)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return TimeSeries.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return TimeSeries.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return TimeSeries.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return TimeSeries.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return TimeSeries.registered_resource.get_by_mrid(self, mrid)

    def add_market_object_status(self, market_object_status: MarketObjectStatus) -> Self:
        return TimeSeries.market_object_status.add(self, market_object_status)

    def remove_market_object_status(self, market_object_status: MarketObjectStatus) -> Self:
        return TimeSeries.market_object_status.remove(self, market_object_status)

    def clear_market_object_status(self) -> Self:
        return TimeSeries.market_object_status.clear(self)

    def num_market_object_status(self) -> int:
        return TimeSeries.market_object_status.count(self)

    def add_point(self, point: Point) -> Self:
        return TimeSeries.point.add(self, point)

    def remove_point(self, point: Point) -> Self:
        return TimeSeries.point.remove(self, point)

    def clear_point(self) -> Self:
        return TimeSeries.point.clear(self)

    def num_point(self) -> int:
        return TimeSeries.point.count(self)

    def add_reason(self, reason: Reason) -> Self:
        return TimeSeries.reason.add(self, reason)

    def remove_reason(self, reason: Reason) -> Self:
        return TimeSeries.reason.remove(self, reason)

    def clear_reason(self) -> Self:
        return TimeSeries.reason.clear(self)

    def num_reason(self) -> int:
        return TimeSeries.reason.count(self)
