"""CIM class PricingStructure (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.customers.revenue_kind import RevenueKind
    from cim_python_sdk.model.iec61968.customers.service_category import ServiceCategory
    from cim_python_sdk.model.iec61968.customers.tariff import Tariff
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61968.payment_metering.transaction import Transaction


class PricingStructure(Document):
    """Grouping of pricing components and prices used in the creation of customer charges and
    the eligibility criteria under which these terms may be offered to a customer. The
    reasons for grouping include state, customer classification, site characteristics,
    classification (i.e. fee price structure, deposit price structure, electric service
    price structure, etc.) and accounting requirements."""

    __slots__ = (
        "_customer_agreements",
        "_service_category",
        "_tariffs",
        "_transactions",
        "_usage_points",
        "code",
        "daily_ceiling_usage",
        "daily_estimated_usage",
        "daily_floor_usage",
        "revenue_kind",
        "tax_exemption",
    )

    code: str | None
    revenue_kind: RevenueKind | None
    tax_exemption: bool | None
    daily_estimated_usage: int | None
    daily_ceiling_usage: int | None
    daily_floor_usage: int | None

    transactions: Many[Transaction] = Many(
        EndMeta(
            name="transactions",
            cim_role="Transactions",
            target="cim_python_sdk.model.iec61968.payment_metering.transaction:Transaction",
            many=True,
            lower=0,
            upper=None,
            inverse="pricing_structure",
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
            inverse="pricing_structures",
            aggregation="none",
        )
    )
    service_category: One[ServiceCategory] = One(
        EndMeta(
            name="service_category",
            cim_role="ServiceCategory",
            target="cim_python_sdk.model.iec61968.customers.service_category:ServiceCategory",
            many=False,
            lower=1,
            upper=1,
            inverse="pricing_structures",
            aggregation="none",
        )
    )
    tariffs: Many[Tariff] = Many(
        EndMeta(
            name="tariffs",
            cim_role="Tariffs",
            target="cim_python_sdk.model.iec61968.customers.tariff:Tariff",
            many=True,
            lower=0,
            upper=None,
            inverse="pricing_structures",
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
            inverse="pricing_structures",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PricingStructure",
        package="TC57CIM/IEC61968/Customers",
        guid="{696BAC8C-6DA3-4fe3-BB2F-4D4572463FC2}",
        attributes=(
            AttrMeta("code", "code", "str", 0, 1, "primitive"),
            AttrMeta("revenue_kind", "revenueKind", "RevenueKind", 0, 1, "enumeration"),
            AttrMeta("tax_exemption", "taxExemption", "bool", 0, 1, "primitive"),
            AttrMeta("daily_estimated_usage", "dailyEstimatedUsage", "int", 0, 1, "primitive"),
            AttrMeta("daily_ceiling_usage", "dailyCeilingUsage", "int", 0, 1, "primitive"),
            AttrMeta("daily_floor_usage", "dailyFloorUsage", "int", 0, 1, "primitive"),
        ),
        ends=(
            transactions.meta,
            customer_agreements.meta,
            service_category.meta,
            tariffs.meta,
            usage_points.meta,
        ),
    )

    def __init__(
        self,
        *,
        code: str | None = None,
        revenue_kind: RevenueKind | None = None,
        tax_exemption: bool | None = None,
        daily_estimated_usage: int | None = None,
        daily_ceiling_usage: int | None = None,
        daily_floor_usage: int | None = None,
        transactions: Iterable[Transaction] | None = None,
        customer_agreements: Iterable[CustomerAgreement] | None = None,
        service_category: ServiceCategory | None = None,
        tariffs: Iterable[Tariff] | None = None,
        usage_points: Iterable[UsagePoint] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.code = code
        self.revenue_kind = revenue_kind
        self.tax_exemption = tax_exemption
        self.daily_estimated_usage = daily_estimated_usage
        self.daily_ceiling_usage = daily_ceiling_usage
        self.daily_floor_usage = daily_floor_usage
        if transactions is not None:
            PricingStructure.transactions.extend(self, transactions)
        if customer_agreements is not None:
            PricingStructure.customer_agreements.extend(self, customer_agreements)
        if service_category is not None:
            self.service_category = service_category
        if tariffs is not None:
            PricingStructure.tariffs.extend(self, tariffs)
        if usage_points is not None:
            PricingStructure.usage_points.extend(self, usage_points)

    def add_transaction(self, transaction: Transaction) -> Self:
        return PricingStructure.transactions.add(self, transaction)

    def remove_transaction(self, transaction: Transaction) -> Self:
        return PricingStructure.transactions.remove(self, transaction)

    def clear_transactions(self) -> Self:
        return PricingStructure.transactions.clear(self)

    def num_transaction(self) -> int:
        return PricingStructure.transactions.count(self)

    def get_transaction_by_mrid(self, mrid: str) -> Transaction | None:
        return PricingStructure.transactions.get_by_mrid(self, mrid)

    def add_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return PricingStructure.customer_agreements.add(self, customer_agreement)

    def remove_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return PricingStructure.customer_agreements.remove(self, customer_agreement)

    def clear_customer_agreements(self) -> Self:
        return PricingStructure.customer_agreements.clear(self)

    def num_customer_agreement(self) -> int:
        return PricingStructure.customer_agreements.count(self)

    def get_customer_agreement_by_mrid(self, mrid: str) -> CustomerAgreement | None:
        return PricingStructure.customer_agreements.get_by_mrid(self, mrid)

    def add_tariff(self, tariff: Tariff) -> Self:
        return PricingStructure.tariffs.add(self, tariff)

    def remove_tariff(self, tariff: Tariff) -> Self:
        return PricingStructure.tariffs.remove(self, tariff)

    def clear_tariffs(self) -> Self:
        return PricingStructure.tariffs.clear(self)

    def num_tariff(self) -> int:
        return PricingStructure.tariffs.count(self)

    def get_tariff_by_mrid(self, mrid: str) -> Tariff | None:
        return PricingStructure.tariffs.get_by_mrid(self, mrid)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return PricingStructure.usage_points.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return PricingStructure.usage_points.remove(self, usage_point)

    def clear_usage_points(self) -> Self:
        return PricingStructure.usage_points.clear(self)

    def num_usage_point(self) -> int:
        return PricingStructure.usage_points.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return PricingStructure.usage_points.get_by_mrid(self, mrid)
