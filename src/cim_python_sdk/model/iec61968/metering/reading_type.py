"""CIM class ReadingType (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.accumulation_kind import AccumulationKind
    from cim_python_sdk.model.iec61968.metering.aggregate_kind import AggregateKind
    from cim_python_sdk.model.iec61968.metering.channel import Channel
    from cim_python_sdk.model.iec61968.metering.commodity_kind import CommodityKind
    from cim_python_sdk.model.iec61968.metering.flow_direction_kind import FlowDirectionKind
    from cim_python_sdk.model.iec61968.metering.interval_block import IntervalBlock
    from cim_python_sdk.model.iec61968.metering.macro_period_kind import MacroPeriodKind
    from cim_python_sdk.model.iec61968.metering.measurement_kind import MeasurementKind
    from cim_python_sdk.model.iec61968.metering.measuring_period_kind import MeasuringPeriodKind
    from cim_python_sdk.model.iec61968.metering.meter_read_schedule import MeterReadSchedule
    from cim_python_sdk.model.iec61968.metering.metrology_requirement import MetrologyRequirement
    from cim_python_sdk.model.iec61968.metering.pending_calculation import PendingCalculation
    from cim_python_sdk.model.iec61968.metering.rational_number import RationalNumber
    from cim_python_sdk.model.iec61968.metering.reading import Reading
    from cim_python_sdk.model.iec61968.metering.reading_interharmonic import ReadingInterharmonic
    from cim_python_sdk.model.iec61968.payment_metering.consumption_tariff_interval import (
        ConsumptionTariffInterval,
    )
    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode
    from cim_python_sdk.model.iec61970.base.domain.currency import Currency
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class ReadingType(IdentifiedObject):
    """Detailed description for a type of a reading value. Values in attributes allow for the
    creation of recommended codes to be used for identifying reading value types as follows:
    <macroPeriod>.<aggregate>.<measuringPeriod>.<accumulation>.<flowDirection>.<commodity>.<measurementKind>.<interharmonic.numerator>.<interharmonic.denominator>.<argument.numerator>.<argument.denominator>.<tou>.<cpp>.<consumptionTier>.<phases>.<multiplier>.<unit>.<currency>."""

    __slots__ = (
        "_channel",
        "_consumption_tariff_intervals",
        "_interval_blocks",
        "_meter_read_schedule",
        "_metrology_requirements",
        "_pending_calculation",
        "_readings",
        "accumulation",
        "aggregate",
        "argument",
        "commodity",
        "consumption_tier",
        "cpp",
        "currency",
        "flow_direction",
        "interharmonic",
        "macro_period",
        "measurement_kind",
        "measuring_period",
        "multiplier",
        "phases",
        "tou",
        "unit",
    )

    macro_period: MacroPeriodKind | None
    aggregate: AggregateKind | None
    measuring_period: MeasuringPeriodKind | None
    accumulation: AccumulationKind | None
    flow_direction: FlowDirectionKind | None
    commodity: CommodityKind | None
    measurement_kind: MeasurementKind | None
    interharmonic: ReadingInterharmonic | None
    argument: RationalNumber | None
    tou: int | None
    cpp: int | None
    consumption_tier: int | None
    phases: PhaseCode | None
    multiplier: UnitMultiplier | None
    unit: UnitSymbol | None
    currency: Currency | None

    meter_read_schedule: One[MeterReadSchedule] = One(
        EndMeta(
            name="meter_read_schedule",
            cim_role="MeterReadSchedule",
            target="cim_python_sdk.model.iec61968.metering.meter_read_schedule:MeterReadSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="reading_type",
            aggregation="none",
        )
    )
    consumption_tariff_intervals: Many[ConsumptionTariffInterval] = Many(
        EndMeta(
            name="consumption_tariff_intervals",
            cim_role="ConsumptionTariffIntervals",
            target="cim_python_sdk.model.iec61968.payment_metering.consumption_tariff_interval:ConsumptionTariffInterval",
            many=True,
            lower=0,
            upper=None,
            inverse="reading_type",
            aggregation="none",
        )
    )
    pending_calculation: One[PendingCalculation] = One(
        EndMeta(
            name="pending_calculation",
            cim_role="PendingCalculation",
            target="cim_python_sdk.model.iec61968.metering.pending_calculation:PendingCalculation",
            many=False,
            lower=0,
            upper=1,
            inverse="reading_type",
            aggregation="none",
        )
    )
    interval_blocks: Many[IntervalBlock] = Many(
        EndMeta(
            name="interval_blocks",
            cim_role="IntervalBlocks",
            target="cim_python_sdk.model.iec61968.metering.interval_block:IntervalBlock",
            many=True,
            lower=0,
            upper=None,
            inverse="reading_type",
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
            inverse="reading_types",
            aggregation="none",
        )
    )
    channel: One[Channel] = One(
        EndMeta(
            name="channel",
            cim_role="Channel",
            target="cim_python_sdk.model.iec61968.metering.channel:Channel",
            many=False,
            lower=0,
            upper=1,
            inverse="reading_type",
            aggregation="none",
        )
    )
    readings: Many[Reading] = Many(
        EndMeta(
            name="readings",
            cim_role="Readings",
            target="cim_python_sdk.model.iec61968.metering.reading:Reading",
            many=True,
            lower=0,
            upper=None,
            inverse="reading_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReadingType",
        package="TC57CIM/IEC61968/Metering",
        guid="{256DE8A2-72B1-4be6-A8D1-1C3D16886B83}",
        attributes=(
            AttrMeta("macro_period", "macroPeriod", "MacroPeriodKind", 0, 1, "enumeration"),
            AttrMeta("aggregate", "aggregate", "AggregateKind", 0, 1, "enumeration"),
            AttrMeta(
                "measuring_period", "measuringPeriod", "MeasuringPeriodKind", 0, 1, "enumeration"
            ),
            AttrMeta("accumulation", "accumulation", "AccumulationKind", 0, 1, "enumeration"),
            AttrMeta("flow_direction", "flowDirection", "FlowDirectionKind", 0, 1, "enumeration"),
            AttrMeta("commodity", "commodity", "CommodityKind", 0, 1, "enumeration"),
            AttrMeta("measurement_kind", "measurementKind", "MeasurementKind", 0, 1, "enumeration"),
            AttrMeta("interharmonic", "interharmonic", "ReadingInterharmonic", 0, 1, "compound"),
            AttrMeta("argument", "argument", "RationalNumber", 0, 1, "compound"),
            AttrMeta("tou", "tou", "int", 0, 1, "primitive"),
            AttrMeta("cpp", "cpp", "int", 0, 1, "primitive"),
            AttrMeta("consumption_tier", "consumptionTier", "int", 0, 1, "primitive"),
            AttrMeta("phases", "phases", "PhaseCode", 0, 1, "enumeration"),
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("currency", "currency", "Currency", 0, 1, "enumeration"),
        ),
        ends=(
            meter_read_schedule.meta,
            consumption_tariff_intervals.meta,
            pending_calculation.meta,
            interval_blocks.meta,
            metrology_requirements.meta,
            channel.meta,
            readings.meta,
        ),
    )

    def __init__(
        self,
        *,
        macro_period: MacroPeriodKind | None = None,
        aggregate: AggregateKind | None = None,
        measuring_period: MeasuringPeriodKind | None = None,
        accumulation: AccumulationKind | None = None,
        flow_direction: FlowDirectionKind | None = None,
        commodity: CommodityKind | None = None,
        measurement_kind: MeasurementKind | None = None,
        interharmonic: ReadingInterharmonic | None = None,
        argument: RationalNumber | None = None,
        tou: int | None = None,
        cpp: int | None = None,
        consumption_tier: int | None = None,
        phases: PhaseCode | None = None,
        multiplier: UnitMultiplier | None = None,
        unit: UnitSymbol | None = None,
        currency: Currency | None = None,
        meter_read_schedule: MeterReadSchedule | None = None,
        consumption_tariff_intervals: Iterable[ConsumptionTariffInterval] | None = None,
        pending_calculation: PendingCalculation | None = None,
        interval_blocks: Iterable[IntervalBlock] | None = None,
        metrology_requirements: Iterable[MetrologyRequirement] | None = None,
        channel: Channel | None = None,
        readings: Iterable[Reading] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.macro_period = macro_period
        self.aggregate = aggregate
        self.measuring_period = measuring_period
        self.accumulation = accumulation
        self.flow_direction = flow_direction
        self.commodity = commodity
        self.measurement_kind = measurement_kind
        self.interharmonic = interharmonic
        self.argument = argument
        self.tou = tou
        self.cpp = cpp
        self.consumption_tier = consumption_tier
        self.phases = phases
        self.multiplier = multiplier
        self.unit = unit
        self.currency = currency
        if meter_read_schedule is not None:
            self.meter_read_schedule = meter_read_schedule
        if consumption_tariff_intervals is not None:
            ReadingType.consumption_tariff_intervals.extend(self, consumption_tariff_intervals)
        if pending_calculation is not None:
            self.pending_calculation = pending_calculation
        if interval_blocks is not None:
            ReadingType.interval_blocks.extend(self, interval_blocks)
        if metrology_requirements is not None:
            ReadingType.metrology_requirements.extend(self, metrology_requirements)
        if channel is not None:
            self.channel = channel
        if readings is not None:
            ReadingType.readings.extend(self, readings)

    def add_consumption_tariff_interval(
        self, consumption_tariff_interval: ConsumptionTariffInterval
    ) -> Self:
        return ReadingType.consumption_tariff_intervals.add(self, consumption_tariff_interval)

    def remove_consumption_tariff_interval(
        self, consumption_tariff_interval: ConsumptionTariffInterval
    ) -> Self:
        return ReadingType.consumption_tariff_intervals.remove(self, consumption_tariff_interval)

    def clear_consumption_tariff_intervals(self) -> Self:
        return ReadingType.consumption_tariff_intervals.clear(self)

    def num_consumption_tariff_interval(self) -> int:
        return ReadingType.consumption_tariff_intervals.count(self)

    def add_interval_block(self, interval_block: IntervalBlock) -> Self:
        return ReadingType.interval_blocks.add(self, interval_block)

    def remove_interval_block(self, interval_block: IntervalBlock) -> Self:
        return ReadingType.interval_blocks.remove(self, interval_block)

    def clear_interval_blocks(self) -> Self:
        return ReadingType.interval_blocks.clear(self)

    def num_interval_block(self) -> int:
        return ReadingType.interval_blocks.count(self)

    def add_metrology_requirement(self, metrology_requirement: MetrologyRequirement) -> Self:
        return ReadingType.metrology_requirements.add(self, metrology_requirement)

    def remove_metrology_requirement(self, metrology_requirement: MetrologyRequirement) -> Self:
        return ReadingType.metrology_requirements.remove(self, metrology_requirement)

    def clear_metrology_requirements(self) -> Self:
        return ReadingType.metrology_requirements.clear(self)

    def num_metrology_requirement(self) -> int:
        return ReadingType.metrology_requirements.count(self)

    def get_metrology_requirement_by_mrid(self, mrid: str) -> MetrologyRequirement | None:
        return ReadingType.metrology_requirements.get_by_mrid(self, mrid)

    def add_reading(self, reading: Reading) -> Self:
        return ReadingType.readings.add(self, reading)

    def remove_reading(self, reading: Reading) -> Self:
        return ReadingType.readings.remove(self, reading)

    def clear_readings(self) -> Self:
        return ReadingType.readings.clear(self)

    def num_reading(self) -> int:
        return ReadingType.readings.count(self)

    def get_reading_by_mrid(self, mrid: str) -> Reading | None:
        return ReadingType.readings.get_by_mrid(self, mrid)
