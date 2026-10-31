"""CIM class MeterReadSchedule (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.time_schedule import TimeSchedule
    from cim_python_sdk.model.iec61968.customers.customer_account import CustomerAccount
    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.metering.end_device import EndDevice
    from cim_python_sdk.model.iec61968.metering.end_device_group import EndDeviceGroup
    from cim_python_sdk.model.iec61968.metering.reading_type import ReadingType
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61968.metering.usage_point_group import UsagePointGroup


class MeterReadSchedule(Document):
    """CIM class MeterReadSchedule."""

    __slots__ = (
        "_customer_account",
        "_customer_agreement",
        "_end_device",
        "_end_device_group",
        "_reading_type",
        "_time_schedule",
        "_usage_point",
        "_usage_point_group",
    )

    usage_point: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_point",
            cim_role="UsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_read_schedule",
            aggregation="none",
        )
    )
    end_device_group: Many[EndDeviceGroup] = Many(
        EndMeta(
            name="end_device_group",
            cim_role="EndDeviceGroup",
            target="cim_python_sdk.model.iec61968.metering.end_device_group:EndDeviceGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_read_schedule",
            aggregation="none",
        )
    )
    reading_type: Many[ReadingType] = Many(
        EndMeta(
            name="reading_type",
            cim_role="ReadingType",
            target="cim_python_sdk.model.iec61968.metering.reading_type:ReadingType",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_read_schedule",
            aggregation="none",
        )
    )
    usage_point_group: Many[UsagePointGroup] = Many(
        EndMeta(
            name="usage_point_group",
            cim_role="UsagePointGroup",
            target="cim_python_sdk.model.iec61968.metering.usage_point_group:UsagePointGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_read_schedule",
            aggregation="none",
        )
    )
    time_schedule: Many[TimeSchedule] = Many(
        EndMeta(
            name="time_schedule",
            cim_role="TimeSchedule",
            target="cim_python_sdk.model.iec61968.common.time_schedule:TimeSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_read_schedule",
            aggregation="none",
        )
    )
    customer_agreement: Many[CustomerAgreement] = Many(
        EndMeta(
            name="customer_agreement",
            cim_role="CustomerAgreement",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_read_schedule",
            aggregation="none",
        )
    )
    end_device: Many[EndDevice] = Many(
        EndMeta(
            name="end_device",
            cim_role="EndDevice",
            target="cim_python_sdk.model.iec61968.metering.end_device:EndDevice",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_read_schedule",
            aggregation="none",
        )
    )
    customer_account: Many[CustomerAccount] = Many(
        EndMeta(
            name="customer_account",
            cim_role="CustomerAccount",
            target="cim_python_sdk.model.iec61968.customers.customer_account:CustomerAccount",
            many=True,
            lower=0,
            upper=None,
            inverse="meter_read_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeterReadSchedule",
        package="TC57CIM/IEC61968/Metering",
        guid="{C19E9BE4-42B1-42a9-BCED-95A9592F796B}",
        ends=(
            usage_point.meta,
            end_device_group.meta,
            reading_type.meta,
            usage_point_group.meta,
            time_schedule.meta,
            customer_agreement.meta,
            end_device.meta,
            customer_account.meta,
        ),
    )

    def __init__(
        self,
        *,
        usage_point: Iterable[UsagePoint] | None = None,
        end_device_group: Iterable[EndDeviceGroup] | None = None,
        reading_type: Iterable[ReadingType] | None = None,
        usage_point_group: Iterable[UsagePointGroup] | None = None,
        time_schedule: Iterable[TimeSchedule] | None = None,
        customer_agreement: Iterable[CustomerAgreement] | None = None,
        end_device: Iterable[EndDevice] | None = None,
        customer_account: Iterable[CustomerAccount] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if usage_point is not None:
            MeterReadSchedule.usage_point.extend(self, usage_point)
        if end_device_group is not None:
            MeterReadSchedule.end_device_group.extend(self, end_device_group)
        if reading_type is not None:
            MeterReadSchedule.reading_type.extend(self, reading_type)
        if usage_point_group is not None:
            MeterReadSchedule.usage_point_group.extend(self, usage_point_group)
        if time_schedule is not None:
            MeterReadSchedule.time_schedule.extend(self, time_schedule)
        if customer_agreement is not None:
            MeterReadSchedule.customer_agreement.extend(self, customer_agreement)
        if end_device is not None:
            MeterReadSchedule.end_device.extend(self, end_device)
        if customer_account is not None:
            MeterReadSchedule.customer_account.extend(self, customer_account)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return MeterReadSchedule.usage_point.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return MeterReadSchedule.usage_point.remove(self, usage_point)

    def clear_usage_point(self) -> Self:
        return MeterReadSchedule.usage_point.clear(self)

    def num_usage_point(self) -> int:
        return MeterReadSchedule.usage_point.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return MeterReadSchedule.usage_point.get_by_mrid(self, mrid)

    def add_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return MeterReadSchedule.end_device_group.add(self, end_device_group)

    def remove_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return MeterReadSchedule.end_device_group.remove(self, end_device_group)

    def clear_end_device_group(self) -> Self:
        return MeterReadSchedule.end_device_group.clear(self)

    def num_end_device_group(self) -> int:
        return MeterReadSchedule.end_device_group.count(self)

    def get_end_device_group_by_mrid(self, mrid: str) -> EndDeviceGroup | None:
        return MeterReadSchedule.end_device_group.get_by_mrid(self, mrid)

    def add_reading_type(self, reading_type: ReadingType) -> Self:
        return MeterReadSchedule.reading_type.add(self, reading_type)

    def remove_reading_type(self, reading_type: ReadingType) -> Self:
        return MeterReadSchedule.reading_type.remove(self, reading_type)

    def clear_reading_type(self) -> Self:
        return MeterReadSchedule.reading_type.clear(self)

    def num_reading_type(self) -> int:
        return MeterReadSchedule.reading_type.count(self)

    def get_reading_type_by_mrid(self, mrid: str) -> ReadingType | None:
        return MeterReadSchedule.reading_type.get_by_mrid(self, mrid)

    def add_usage_point_group(self, usage_point_group: UsagePointGroup) -> Self:
        return MeterReadSchedule.usage_point_group.add(self, usage_point_group)

    def remove_usage_point_group(self, usage_point_group: UsagePointGroup) -> Self:
        return MeterReadSchedule.usage_point_group.remove(self, usage_point_group)

    def clear_usage_point_group(self) -> Self:
        return MeterReadSchedule.usage_point_group.clear(self)

    def num_usage_point_group(self) -> int:
        return MeterReadSchedule.usage_point_group.count(self)

    def get_usage_point_group_by_mrid(self, mrid: str) -> UsagePointGroup | None:
        return MeterReadSchedule.usage_point_group.get_by_mrid(self, mrid)

    def add_time_schedule(self, time_schedule: TimeSchedule) -> Self:
        return MeterReadSchedule.time_schedule.add(self, time_schedule)

    def remove_time_schedule(self, time_schedule: TimeSchedule) -> Self:
        return MeterReadSchedule.time_schedule.remove(self, time_schedule)

    def clear_time_schedule(self) -> Self:
        return MeterReadSchedule.time_schedule.clear(self)

    def num_time_schedule(self) -> int:
        return MeterReadSchedule.time_schedule.count(self)

    def get_time_schedule_by_mrid(self, mrid: str) -> TimeSchedule | None:
        return MeterReadSchedule.time_schedule.get_by_mrid(self, mrid)

    def add_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return MeterReadSchedule.customer_agreement.add(self, customer_agreement)

    def remove_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return MeterReadSchedule.customer_agreement.remove(self, customer_agreement)

    def clear_customer_agreement(self) -> Self:
        return MeterReadSchedule.customer_agreement.clear(self)

    def num_customer_agreement(self) -> int:
        return MeterReadSchedule.customer_agreement.count(self)

    def get_customer_agreement_by_mrid(self, mrid: str) -> CustomerAgreement | None:
        return MeterReadSchedule.customer_agreement.get_by_mrid(self, mrid)

    def add_end_device(self, end_device: EndDevice) -> Self:
        return MeterReadSchedule.end_device.add(self, end_device)

    def remove_end_device(self, end_device: EndDevice) -> Self:
        return MeterReadSchedule.end_device.remove(self, end_device)

    def clear_end_device(self) -> Self:
        return MeterReadSchedule.end_device.clear(self)

    def num_end_device(self) -> int:
        return MeterReadSchedule.end_device.count(self)

    def get_end_device_by_mrid(self, mrid: str) -> EndDevice | None:
        return MeterReadSchedule.end_device.get_by_mrid(self, mrid)

    def add_customer_account(self, customer_account: CustomerAccount) -> Self:
        return MeterReadSchedule.customer_account.add(self, customer_account)

    def remove_customer_account(self, customer_account: CustomerAccount) -> Self:
        return MeterReadSchedule.customer_account.remove(self, customer_account)

    def clear_customer_account(self) -> Self:
        return MeterReadSchedule.customer_account.clear(self)

    def num_customer_account(self) -> int:
        return MeterReadSchedule.customer_account.count(self)

    def get_customer_account_by_mrid(self, mrid: str) -> CustomerAccount | None:
        return MeterReadSchedule.customer_account.get_by_mrid(self, mrid)
