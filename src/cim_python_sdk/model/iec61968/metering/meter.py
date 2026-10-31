"""CIM class Meter (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.metering.end_device import EndDevice

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.meter_multiplier import MeterMultiplier
    from cim_python_sdk.model.iec61968.metering.meter_reading import MeterReading
    from cim_python_sdk.model.iec61968.metering.meter_work_task import MeterWorkTask
    from cim_python_sdk.model.iec61968.payment_metering.transaction import Transaction


class Meter(EndDevice):
    """Physical asset that performs the metering role of the usage point. Used for measuring
    consumption and detection of events."""

    __slots__ = (
        "_meter_multipliers",
        "_meter_readings",
        "_meter_replacement_work_tasks",
        "_meter_service_work_task",
        "_vending_transactions",
        "connection_category",
        "form_number",
    )

    form_number: str | None
    connection_category: str | None

    meter_replacement_work_tasks: Many[MeterWorkTask] = Many(
        EndMeta(
            name="meter_replacement_work_tasks",
            cim_role="MeterReplacementWorkTasks",
            target="cim_python_sdk.model.iec61968.metering.meter_work_task:MeterWorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="old_meter",
            aggregation="none",
        )
    )
    meter_multipliers: Many[MeterMultiplier] = Many(
        EndMeta(
            name="meter_multipliers",
            cim_role="MeterMultipliers",
            target="cim_python_sdk.model.iec61968.metering.meter_multiplier:MeterMultiplier",
            many=True,
            lower=0,
            upper=None,
            inverse="meter",
            aggregation="none",
        )
    )
    vending_transactions: Many[Transaction] = Many(
        EndMeta(
            name="vending_transactions",
            cim_role="VendingTransactions",
            target="cim_python_sdk.model.iec61968.payment_metering.transaction:Transaction",
            many=True,
            lower=0,
            upper=None,
            inverse="meter",
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
            inverse="meter",
            aggregation="none",
        )
    )
    meter_service_work_task: Many[MeterWorkTask] = Many(
        EndMeta(
            name="meter_service_work_task",
            cim_role="MeterServiceWorkTask",
            target="cim_python_sdk.model.iec61968.metering.meter_work_task:MeterWorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="meter",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Meter",
        package="TC57CIM/IEC61968/Metering",
        guid="{205B6F34-8938-4372-BC87-FB51486FE4A6}",
        attributes=(
            AttrMeta("form_number", "formNumber", "str", 0, 1, "primitive"),
            AttrMeta("connection_category", "connectionCategory", "str", 0, 1, "primitive"),
        ),
        ends=(
            meter_replacement_work_tasks.meta,
            meter_multipliers.meta,
            vending_transactions.meta,
            meter_readings.meta,
            meter_service_work_task.meta,
        ),
    )

    def __init__(
        self,
        *,
        form_number: str | None = None,
        connection_category: str | None = None,
        meter_replacement_work_tasks: Iterable[MeterWorkTask] | None = None,
        meter_multipliers: Iterable[MeterMultiplier] | None = None,
        vending_transactions: Iterable[Transaction] | None = None,
        meter_readings: Iterable[MeterReading] | None = None,
        meter_service_work_task: Iterable[MeterWorkTask] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.form_number = form_number
        self.connection_category = connection_category
        if meter_replacement_work_tasks is not None:
            Meter.meter_replacement_work_tasks.extend(self, meter_replacement_work_tasks)
        if meter_multipliers is not None:
            Meter.meter_multipliers.extend(self, meter_multipliers)
        if vending_transactions is not None:
            Meter.vending_transactions.extend(self, vending_transactions)
        if meter_readings is not None:
            Meter.meter_readings.extend(self, meter_readings)
        if meter_service_work_task is not None:
            Meter.meter_service_work_task.extend(self, meter_service_work_task)

    def add_meter_replacement_work_task(self, meter_replacement_work_task: MeterWorkTask) -> Self:
        return Meter.meter_replacement_work_tasks.add(self, meter_replacement_work_task)

    def remove_meter_replacement_work_task(
        self, meter_replacement_work_task: MeterWorkTask
    ) -> Self:
        return Meter.meter_replacement_work_tasks.remove(self, meter_replacement_work_task)

    def clear_meter_replacement_work_tasks(self) -> Self:
        return Meter.meter_replacement_work_tasks.clear(self)

    def num_meter_replacement_work_task(self) -> int:
        return Meter.meter_replacement_work_tasks.count(self)

    def get_meter_replacement_work_task_by_mrid(self, mrid: str) -> MeterWorkTask | None:
        return Meter.meter_replacement_work_tasks.get_by_mrid(self, mrid)

    def add_meter_multiplier(self, meter_multiplier: MeterMultiplier) -> Self:
        return Meter.meter_multipliers.add(self, meter_multiplier)

    def remove_meter_multiplier(self, meter_multiplier: MeterMultiplier) -> Self:
        return Meter.meter_multipliers.remove(self, meter_multiplier)

    def clear_meter_multipliers(self) -> Self:
        return Meter.meter_multipliers.clear(self)

    def num_meter_multiplier(self) -> int:
        return Meter.meter_multipliers.count(self)

    def get_meter_multiplier_by_mrid(self, mrid: str) -> MeterMultiplier | None:
        return Meter.meter_multipliers.get_by_mrid(self, mrid)

    def add_vending_transaction(self, vending_transaction: Transaction) -> Self:
        return Meter.vending_transactions.add(self, vending_transaction)

    def remove_vending_transaction(self, vending_transaction: Transaction) -> Self:
        return Meter.vending_transactions.remove(self, vending_transaction)

    def clear_vending_transactions(self) -> Self:
        return Meter.vending_transactions.clear(self)

    def num_vending_transaction(self) -> int:
        return Meter.vending_transactions.count(self)

    def get_vending_transaction_by_mrid(self, mrid: str) -> Transaction | None:
        return Meter.vending_transactions.get_by_mrid(self, mrid)

    def add_meter_reading(self, meter_reading: MeterReading) -> Self:
        return Meter.meter_readings.add(self, meter_reading)

    def remove_meter_reading(self, meter_reading: MeterReading) -> Self:
        return Meter.meter_readings.remove(self, meter_reading)

    def clear_meter_readings(self) -> Self:
        return Meter.meter_readings.clear(self)

    def num_meter_reading(self) -> int:
        return Meter.meter_readings.count(self)

    def get_meter_reading_by_mrid(self, mrid: str) -> MeterReading | None:
        return Meter.meter_readings.get_by_mrid(self, mrid)

    def add_meter_service_work_task(self, meter_service_work_task: MeterWorkTask) -> Self:
        return Meter.meter_service_work_task.add(self, meter_service_work_task)

    def remove_meter_service_work_task(self, meter_service_work_task: MeterWorkTask) -> Self:
        return Meter.meter_service_work_task.remove(self, meter_service_work_task)

    def clear_meter_service_work_task(self) -> Self:
        return Meter.meter_service_work_task.clear(self)

    def num_meter_service_work_task(self) -> int:
        return Meter.meter_service_work_task.count(self)

    def get_meter_service_work_task_by_mrid(self, mrid: str) -> MeterWorkTask | None:
        return Meter.meter_service_work_task.get_by_mrid(self, mrid)
