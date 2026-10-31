"""CIM class ServiceLocation (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.work.work_location import WorkLocation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.customers.service_request import ServiceRequest
    from cim_python_sdk.model.iec61968.customers.trouble_ticket import TroubleTicket
    from cim_python_sdk.model.iec61968.metering.end_device import EndDevice
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint


class ServiceLocation(WorkLocation):
    """A real estate location, commonly referred to as premises."""

    __slots__ = (
        "_asset_service_location",
        "_customer_agreements",
        "_end_devices",
        "_service_request",
        "_trouble_ticket_service_location",
        "_usage_points",
        "access_method",
        "needs_inspection",
        "site_access_problem",
    )

    access_method: str | None
    site_access_problem: str | None
    needs_inspection: bool | None

    asset_service_location: Many[Asset] = Many(
        EndMeta(
            name="asset_service_location",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="service_location",
            aggregation="none",
        )
    )
    trouble_ticket_service_location: Many[TroubleTicket] = Many(
        EndMeta(
            name="trouble_ticket_service_location",
            cim_role="TroubleTicket",
            target="cim_python_sdk.model.iec61968.customers.trouble_ticket:TroubleTicket",
            many=True,
            lower=0,
            upper=None,
            inverse="service_location",
            aggregation="none",
        )
    )
    service_request: Many[ServiceRequest] = Many(
        EndMeta(
            name="service_request",
            cim_role="ServiceRequest",
            target="cim_python_sdk.model.iec61968.customers.service_request:ServiceRequest",
            many=True,
            lower=0,
            upper=None,
            inverse="service_location",
            aggregation="none",
        )
    )
    usage_points: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_points",
            cim_role="UsagePoints",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="service_location",
            aggregation="none",
        )
    )
    customer_agreements: Many[CustomerAgreement] = Many(
        EndMeta(
            name="customer_agreements",
            cim_role="CustomerAgreements",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="service_locations",
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
            inverse="service_location_end_devices",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ServiceLocation",
        package="TC57CIM/IEC61968/Customers",
        guid="{90D00036-1728-473a-9966-26BADB297110}",
        attributes=(
            AttrMeta("access_method", "accessMethod", "str", 0, 1, "primitive"),
            AttrMeta("site_access_problem", "siteAccessProblem", "str", 0, 1, "primitive"),
            AttrMeta("needs_inspection", "needsInspection", "bool", 0, 1, "primitive"),
        ),
        ends=(
            asset_service_location.meta,
            trouble_ticket_service_location.meta,
            service_request.meta,
            usage_points.meta,
            customer_agreements.meta,
            end_devices.meta,
        ),
    )

    def __init__(
        self,
        *,
        access_method: str | None = None,
        site_access_problem: str | None = None,
        needs_inspection: bool | None = None,
        asset_service_location: Iterable[Asset] | None = None,
        trouble_ticket_service_location: Iterable[TroubleTicket] | None = None,
        service_request: Iterable[ServiceRequest] | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        customer_agreements: Iterable[CustomerAgreement] | None = None,
        end_devices: Iterable[EndDevice] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.access_method = access_method
        self.site_access_problem = site_access_problem
        self.needs_inspection = needs_inspection
        if asset_service_location is not None:
            ServiceLocation.asset_service_location.extend(self, asset_service_location)
        if trouble_ticket_service_location is not None:
            ServiceLocation.trouble_ticket_service_location.extend(
                self, trouble_ticket_service_location
            )
        if service_request is not None:
            ServiceLocation.service_request.extend(self, service_request)
        if usage_points is not None:
            ServiceLocation.usage_points.extend(self, usage_points)
        if customer_agreements is not None:
            ServiceLocation.customer_agreements.extend(self, customer_agreements)
        if end_devices is not None:
            ServiceLocation.end_devices.extend(self, end_devices)

    def add_asset_service_location(self, asset_service_location: Asset) -> Self:
        return ServiceLocation.asset_service_location.add(self, asset_service_location)

    def remove_asset_service_location(self, asset_service_location: Asset) -> Self:
        return ServiceLocation.asset_service_location.remove(self, asset_service_location)

    def clear_asset_service_location(self) -> Self:
        return ServiceLocation.asset_service_location.clear(self)

    def num_asset_service_location(self) -> int:
        return ServiceLocation.asset_service_location.count(self)

    def get_asset_service_location_by_mrid(self, mrid: str) -> Asset | None:
        return ServiceLocation.asset_service_location.get_by_mrid(self, mrid)

    def add_trouble_ticket_service_location(
        self, trouble_ticket_service_location: TroubleTicket
    ) -> Self:
        return ServiceLocation.trouble_ticket_service_location.add(
            self, trouble_ticket_service_location
        )

    def remove_trouble_ticket_service_location(
        self, trouble_ticket_service_location: TroubleTicket
    ) -> Self:
        return ServiceLocation.trouble_ticket_service_location.remove(
            self, trouble_ticket_service_location
        )

    def clear_trouble_ticket_service_location(self) -> Self:
        return ServiceLocation.trouble_ticket_service_location.clear(self)

    def num_trouble_ticket_service_location(self) -> int:
        return ServiceLocation.trouble_ticket_service_location.count(self)

    def get_trouble_ticket_service_location_by_mrid(self, mrid: str) -> TroubleTicket | None:
        return ServiceLocation.trouble_ticket_service_location.get_by_mrid(self, mrid)

    def add_service_request(self, service_request: ServiceRequest) -> Self:
        return ServiceLocation.service_request.add(self, service_request)

    def remove_service_request(self, service_request: ServiceRequest) -> Self:
        return ServiceLocation.service_request.remove(self, service_request)

    def clear_service_request(self) -> Self:
        return ServiceLocation.service_request.clear(self)

    def num_service_request(self) -> int:
        return ServiceLocation.service_request.count(self)

    def get_service_request_by_mrid(self, mrid: str) -> ServiceRequest | None:
        return ServiceLocation.service_request.get_by_mrid(self, mrid)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return ServiceLocation.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return ServiceLocation.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return ServiceLocation.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return ServiceLocation.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return ServiceLocation.usage_points.get_by_mrid(self, mrid)

    def add_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return ServiceLocation.customer_agreements.add(self, customer_agreement)

    def remove_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return ServiceLocation.customer_agreements.remove(self, customer_agreement)

    def clear_customer_agreements(self) -> Self:
        return ServiceLocation.customer_agreements.clear(self)

    def num_customer_agreement(self) -> int:
        return ServiceLocation.customer_agreements.count(self)

    def get_customer_agreement_by_mrid(self, mrid: str) -> CustomerAgreement | None:
        return ServiceLocation.customer_agreements.get_by_mrid(self, mrid)

    def add_end_device(self, end_device: EndDevice) -> Self:
        return ServiceLocation.end_devices.add(self, end_device)

    def remove_end_device(self, end_device: EndDevice) -> Self:
        return ServiceLocation.end_devices.remove(self, end_device)

    def clear_end_devices(self) -> Self:
        return ServiceLocation.end_devices.clear(self)

    def num_end_device(self) -> int:
        return ServiceLocation.end_devices.count(self)

    def get_end_device_by_mrid(self, mrid: str) -> EndDevice | None:
        return ServiceLocation.end_devices.get_by_mrid(self, mrid)
