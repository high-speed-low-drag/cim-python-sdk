"""CIM class DemandResponseProgram (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.metering.end_device_group import EndDeviceGroup
    from cim_python_sdk.model.iec61968.metering.usage_point_group import UsagePointGroup
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class DemandResponseProgram(IdentifiedObject):
    """Demand response program."""

    __slots__ = (
        "_customer_agreements",
        "_end_device_groups",
        "_usage_point_groups",
        "type",
        "validity_interval",
    )

    type: str | None
    validity_interval: DateTimeInterval | None

    end_device_groups: Many[EndDeviceGroup] = Many(
        EndMeta(
            name="end_device_groups",
            cim_role="EndDeviceGroups",
            target="cim_python_sdk.model.iec61968.metering.end_device_group:EndDeviceGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="demand_response_programs",
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
            inverse="demand_response_programs",
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
            inverse="demand_response_programs",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DemandResponseProgram",
        package="TC57CIM/IEC61968/Metering",
        guid="{3AF161FE-E37F-43f2-9C8F-DB2CA19498A9}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("validity_interval", "validityInterval", "DateTimeInterval", 0, 1, "compound"),
        ),
        ends=(
            end_device_groups.meta,
            usage_point_groups.meta,
            customer_agreements.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        validity_interval: DateTimeInterval | None = None,
        end_device_groups: Iterable[EndDeviceGroup] | None = None,
        usage_point_groups: Iterable[UsagePointGroup] | None = None,
        customer_agreements: Iterable[CustomerAgreement] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.validity_interval = validity_interval
        if end_device_groups is not None:
            DemandResponseProgram.end_device_groups.extend(self, end_device_groups)
        if usage_point_groups is not None:
            DemandResponseProgram.usage_point_groups.extend(self, usage_point_groups)
        if customer_agreements is not None:
            DemandResponseProgram.customer_agreements.extend(self, customer_agreements)

    def add_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DemandResponseProgram.end_device_groups.add(self, end_device_group)

    def remove_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DemandResponseProgram.end_device_groups.remove(self, end_device_group)

    def clear_end_device_groups(self) -> Self:
        return DemandResponseProgram.end_device_groups.clear(self)

    def num_end_device_group(self) -> int:
        return DemandResponseProgram.end_device_groups.count(self)

    def get_end_device_group_by_mrid(self, mrid: str) -> EndDeviceGroup | None:
        return DemandResponseProgram.end_device_groups.get_by_mrid(self, mrid)

    def add_usage_point_group(self, usage_point_group: UsagePointGroup) -> Self:
        return DemandResponseProgram.usage_point_groups.add(self, usage_point_group)

    def remove_usage_point_group(self, usage_point_group: UsagePointGroup) -> Self:
        return DemandResponseProgram.usage_point_groups.remove(self, usage_point_group)

    def clear_usage_point_groups(self) -> Self:
        return DemandResponseProgram.usage_point_groups.clear(self)

    def num_usage_point_group(self) -> int:
        return DemandResponseProgram.usage_point_groups.count(self)

    def get_usage_point_group_by_mrid(self, mrid: str) -> UsagePointGroup | None:
        return DemandResponseProgram.usage_point_groups.get_by_mrid(self, mrid)

    def add_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return DemandResponseProgram.customer_agreements.add(self, customer_agreement)

    def remove_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return DemandResponseProgram.customer_agreements.remove(self, customer_agreement)

    def clear_customer_agreements(self) -> Self:
        return DemandResponseProgram.customer_agreements.clear(self)

    def num_customer_agreement(self) -> int:
        return DemandResponseProgram.customer_agreements.count(self)

    def get_customer_agreement_by_mrid(self, mrid: str) -> CustomerAgreement | None:
        return DemandResponseProgram.customer_agreements.get_by_mrid(self, mrid)
