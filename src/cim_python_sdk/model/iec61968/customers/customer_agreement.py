"""CIM class CustomerAgreement (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.agreement import Agreement

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.customers.customer_account import CustomerAccount
    from cim_python_sdk.model.iec61968.customers.pricing_structure import PricingStructure
    from cim_python_sdk.model.iec61968.customers.service_category import ServiceCategory
    from cim_python_sdk.model.iec61968.customers.service_location import ServiceLocation
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.standard_industry_code import (
        StandardIndustryCode,
    )
    from cim_python_sdk.model.iec61968.metering.demand_response_program import DemandResponseProgram
    from cim_python_sdk.model.iec61968.metering.meter_read_schedule import MeterReadSchedule
    from cim_python_sdk.model.iec61968.metering.meter_reading import MeterReading
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61968.payment_metering.auxiliary_agreement import (
        AuxiliaryAgreement,
    )
    from cim_python_sdk.model.iec61968.payment_metering.service_supplier import ServiceSupplier


class CustomerAgreement(Agreement):
    """Agreement between the customer and the service supplier to pay for service at a specific
    service location. It records certain billing information about the type of service
    provided at the service location and is used during charge creation to determine the
    type of service."""

    __slots__ = (
        "_auxiliary_agreements",
        "_customer",
        "_customer_account",
        "_demand_response_programs",
        "_meter_read_schedule",
        "_meter_readings",
        "_pricing_structures",
        "_service_category",
        "_service_locations",
        "_service_supplier",
        "_standard_industry_code",
        "_usage_points",
        "is_pre_pay",
        "load_mgmt",
        "shut_off_date_time",
    )

    load_mgmt: str | None
    is_pre_pay: bool | None
    shut_off_date_time: _dt.datetime | None

    usage_points: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_points",
            cim_role="UsagePoints",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_agreement",
            aggregation="none",
        )
    )
    customer: One[Customer] = One(
        EndMeta(
            name="customer",
            cim_role="Customer",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=False,
            lower=1,
            upper=1,
            inverse="customer_agreements",
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
            inverse="customer_agreements",
            aggregation="none",
        )
    )
    customer_account: One[CustomerAccount] = One(
        EndMeta(
            name="customer_account",
            cim_role="CustomerAccount",
            target="cim_python_sdk.model.iec61968.customers.customer_account:CustomerAccount",
            many=False,
            lower=1,
            upper=1,
            inverse="customer_agreements",
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
            inverse="customer_agreements",
            aggregation="none",
        )
    )
    service_supplier: One[ServiceSupplier] = One(
        EndMeta(
            name="service_supplier",
            cim_role="ServiceSupplier",
            target="cim_python_sdk.model.iec61968.payment_metering.service_supplier:ServiceSupplier",
            many=False,
            lower=1,
            upper=1,
            inverse="customer_agreements",
            aggregation="none",
        )
    )
    auxiliary_agreements: Many[AuxiliaryAgreement] = Many(
        EndMeta(
            name="auxiliary_agreements",
            cim_role="AuxiliaryAgreements",
            target="cim_python_sdk.model.iec61968.payment_metering.auxiliary_agreement:AuxiliaryAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_agreement",
            aggregation="none",
        )
    )
    standard_industry_code: One[StandardIndustryCode] = One(
        EndMeta(
            name="standard_industry_code",
            cim_role="StandardIndustryCode",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.standard_industry_code:StandardIndustryCode",
            many=False,
            lower=0,
            upper=1,
            inverse="customer_agreements",
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
            inverse="customer_agreement",
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
            inverse="customer_agreement",
            aggregation="none",
        )
    )
    service_locations: Many[ServiceLocation] = Many(
        EndMeta(
            name="service_locations",
            cim_role="ServiceLocations",
            target="cim_python_sdk.model.iec61968.customers.service_location:ServiceLocation",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_agreements",
            aggregation="none",
        )
    )
    demand_response_programs: Many[DemandResponseProgram] = Many(
        EndMeta(
            name="demand_response_programs",
            cim_role="DemandResponsePrograms",
            target="cim_python_sdk.model.iec61968.metering.demand_response_program:DemandResponseProgram",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_agreements",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CustomerAgreement",
        package="TC57CIM/IEC61968/Customers",
        guid="{5245DDE2-E142-46d1-B59C-512F29575A88}",
        attributes=(
            AttrMeta("load_mgmt", "loadMgmt", "str", 0, 1, "primitive"),
            AttrMeta("is_pre_pay", "isPrePay", "bool", 0, 1, "primitive"),
            AttrMeta("shut_off_date_time", "shutOffDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            usage_points.meta,
            customer.meta,
            service_category.meta,
            customer_account.meta,
            pricing_structures.meta,
            service_supplier.meta,
            auxiliary_agreements.meta,
            standard_industry_code.meta,
            meter_read_schedule.meta,
            meter_readings.meta,
            service_locations.meta,
            demand_response_programs.meta,
        ),
    )

    def __init__(
        self,
        *,
        load_mgmt: str | None = None,
        is_pre_pay: bool | None = None,
        shut_off_date_time: _dt.datetime | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        customer: Customer | None = None,
        service_category: ServiceCategory | None = None,
        customer_account: CustomerAccount | None = None,
        pricing_structures: Iterable[PricingStructure] | None = None,
        service_supplier: ServiceSupplier | None = None,
        auxiliary_agreements: Iterable[AuxiliaryAgreement] | None = None,
        standard_industry_code: StandardIndustryCode | None = None,
        meter_read_schedule: MeterReadSchedule | None = None,
        meter_readings: Iterable[MeterReading] | None = None,
        service_locations: Iterable[ServiceLocation] | None = None,
        demand_response_programs: Iterable[DemandResponseProgram] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.load_mgmt = load_mgmt
        self.is_pre_pay = is_pre_pay
        self.shut_off_date_time = shut_off_date_time
        if usage_points is not None:
            CustomerAgreement.usage_points.extend(self, usage_points)
        if customer is not None:
            self.customer = customer
        if service_category is not None:
            self.service_category = service_category
        if customer_account is not None:
            self.customer_account = customer_account
        if pricing_structures is not None:
            CustomerAgreement.pricing_structures.extend(self, pricing_structures)
        if service_supplier is not None:
            self.service_supplier = service_supplier
        if auxiliary_agreements is not None:
            CustomerAgreement.auxiliary_agreements.extend(self, auxiliary_agreements)
        if standard_industry_code is not None:
            self.standard_industry_code = standard_industry_code
        if meter_read_schedule is not None:
            self.meter_read_schedule = meter_read_schedule
        if meter_readings is not None:
            CustomerAgreement.meter_readings.extend(self, meter_readings)
        if service_locations is not None:
            CustomerAgreement.service_locations.extend(self, service_locations)
        if demand_response_programs is not None:
            CustomerAgreement.demand_response_programs.extend(self, demand_response_programs)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return CustomerAgreement.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return CustomerAgreement.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return CustomerAgreement.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return CustomerAgreement.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return CustomerAgreement.usage_points.get_by_mrid(self, mrid)

    def add_pricing_structure(self, pricing_structure: PricingStructure) -> Self:
        return CustomerAgreement.pricing_structures.add(self, pricing_structure)

    def remove_pricing_structure(self, pricing_structure: PricingStructure) -> Self:
        return CustomerAgreement.pricing_structures.remove(self, pricing_structure)

    def clear_pricing_structures(self) -> Self:
        return CustomerAgreement.pricing_structures.clear(self)

    def num_pricing_structure(self) -> int:
        return CustomerAgreement.pricing_structures.count(self)

    def get_pricing_structure_by_mrid(self, mrid: str) -> PricingStructure | None:
        return CustomerAgreement.pricing_structures.get_by_mrid(self, mrid)

    def add_auxiliary_agreement(self, auxiliary_agreement: AuxiliaryAgreement) -> Self:
        return CustomerAgreement.auxiliary_agreements.add(self, auxiliary_agreement)

    def remove_auxiliary_agreement(self, auxiliary_agreement: AuxiliaryAgreement) -> Self:
        return CustomerAgreement.auxiliary_agreements.remove(self, auxiliary_agreement)

    def clear_auxiliary_agreements(self) -> Self:
        return CustomerAgreement.auxiliary_agreements.clear(self)

    def num_auxiliary_agreement(self) -> int:
        return CustomerAgreement.auxiliary_agreements.count(self)

    def get_auxiliary_agreement_by_mrid(self, mrid: str) -> AuxiliaryAgreement | None:
        return CustomerAgreement.auxiliary_agreements.get_by_mrid(self, mrid)

    def add_meter_reading(self, meter_reading: MeterReading) -> Self:
        return CustomerAgreement.meter_readings.add(self, meter_reading)

    def remove_meter_reading(self, meter_reading: MeterReading) -> Self:
        return CustomerAgreement.meter_readings.remove(self, meter_reading)

    def clear_meter_readings(self) -> Self:
        return CustomerAgreement.meter_readings.clear(self)

    def num_meter_reading(self) -> int:
        return CustomerAgreement.meter_readings.count(self)

    def get_meter_reading_by_mrid(self, mrid: str) -> MeterReading | None:
        return CustomerAgreement.meter_readings.get_by_mrid(self, mrid)

    def add_service_location(self, service_location: ServiceLocation) -> Self:
        return CustomerAgreement.service_locations.add(self, service_location)

    def remove_service_location(self, service_location: ServiceLocation) -> Self:
        return CustomerAgreement.service_locations.remove(self, service_location)

    def clear_service_locations(self) -> Self:
        return CustomerAgreement.service_locations.clear(self)

    def num_service_location(self) -> int:
        return CustomerAgreement.service_locations.count(self)

    def get_service_location_by_mrid(self, mrid: str) -> ServiceLocation | None:
        return CustomerAgreement.service_locations.get_by_mrid(self, mrid)

    def add_demand_response_program(self, demand_response_program: DemandResponseProgram) -> Self:
        return CustomerAgreement.demand_response_programs.add(self, demand_response_program)

    def remove_demand_response_program(
        self, demand_response_program: DemandResponseProgram
    ) -> Self:
        return CustomerAgreement.demand_response_programs.remove(self, demand_response_program)

    def clear_demand_response_programs(self) -> Self:
        return CustomerAgreement.demand_response_programs.clear(self)

    def num_demand_response_program(self) -> int:
        return CustomerAgreement.demand_response_programs.count(self)

    def get_demand_response_program_by_mrid(self, mrid: str) -> DemandResponseProgram | None:
        return CustomerAgreement.demand_response_programs.get_by_mrid(self, mrid)
