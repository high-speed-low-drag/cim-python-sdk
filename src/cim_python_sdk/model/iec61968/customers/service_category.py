"""CIM class ServiceCategory (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.configuration_event import ConfigurationEvent
    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.customers.pricing_structure import PricingStructure
    from cim_python_sdk.model.iec61968.customers.service_kind import ServiceKind
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint


class ServiceCategory(IdentifiedObject):
    """Category of service provided to the customer."""

    __slots__ = (
        "_configuration_events",
        "_customer_agreements",
        "_pricing_structures",
        "_usage_points",
        "kind",
    )

    kind: ServiceKind | None

    customer_agreements: Many[CustomerAgreement] = Many(
        EndMeta(
            name="customer_agreements",
            cim_role="CustomerAgreements",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="service_category",
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
            inverse="changed_service_category",
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
            inverse="service_category",
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
            inverse="service_category",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ServiceCategory",
        package="TC57CIM/IEC61968/Customers",
        guid="{3B841B0B-C66B-47e6-86F3-2AD7396BFDC0}",
        attributes=(AttrMeta("kind", "kind", "ServiceKind", 0, 1, "enumeration"),),
        ends=(
            customer_agreements.meta,
            configuration_events.meta,
            pricing_structures.meta,
            usage_points.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: ServiceKind | None = None,
        customer_agreements: Iterable[CustomerAgreement] | None = None,
        configuration_events: Iterable[ConfigurationEvent] | None = None,
        pricing_structures: Iterable[PricingStructure] | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if customer_agreements is not None:
            ServiceCategory.customer_agreements.extend(self, customer_agreements)
        if configuration_events is not None:
            ServiceCategory.configuration_events.extend(self, configuration_events)
        if pricing_structures is not None:
            ServiceCategory.pricing_structures.extend(self, pricing_structures)
        if usage_points is not None:
            ServiceCategory.usage_points.extend(self, usage_points)

    def add_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return ServiceCategory.customer_agreements.add(self, customer_agreement)

    def remove_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return ServiceCategory.customer_agreements.remove(self, customer_agreement)

    def clear_customer_agreements(self) -> Self:
        return ServiceCategory.customer_agreements.clear(self)

    def num_customer_agreement(self) -> int:
        return ServiceCategory.customer_agreements.count(self)

    def get_customer_agreement_by_mrid(self, mrid: str) -> CustomerAgreement | None:
        return ServiceCategory.customer_agreements.get_by_mrid(self, mrid)

    def add_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return ServiceCategory.configuration_events.add(self, configuration_event)

    def remove_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return ServiceCategory.configuration_events.remove(self, configuration_event)

    def clear_configuration_events(self) -> Self:
        return ServiceCategory.configuration_events.clear(self)

    def num_configuration_event(self) -> int:
        return ServiceCategory.configuration_events.count(self)

    def get_configuration_event_by_mrid(self, mrid: str) -> ConfigurationEvent | None:
        return ServiceCategory.configuration_events.get_by_mrid(self, mrid)

    def add_pricing_structure(self, pricing_structure: PricingStructure) -> Self:
        return ServiceCategory.pricing_structures.add(self, pricing_structure)

    def remove_pricing_structure(self, pricing_structure: PricingStructure) -> Self:
        return ServiceCategory.pricing_structures.remove(self, pricing_structure)

    def clear_pricing_structures(self) -> Self:
        return ServiceCategory.pricing_structures.clear(self)

    def num_pricing_structure(self) -> int:
        return ServiceCategory.pricing_structures.count(self)

    def get_pricing_structure_by_mrid(self, mrid: str) -> PricingStructure | None:
        return ServiceCategory.pricing_structures.get_by_mrid(self, mrid)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return ServiceCategory.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return ServiceCategory.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return ServiceCategory.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return ServiceCategory.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return ServiceCategory.usage_points.get_by_mrid(self, mrid)
