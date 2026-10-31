"""CIM class ConsumptionTariffInterval (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.reading_type import ReadingType
    from cim_python_sdk.model.iec61968.payment_metering.charge import Charge
    from cim_python_sdk.model.iec61968.payment_metering.tariff_profile import TariffProfile
    from cim_python_sdk.model.iec61968.payment_metering.time_tariff_interval import (
        TimeTariffInterval,
    )


class ConsumptionTariffInterval(CimObject):
    """One of a sequence of intervals defined in terms of consumption quantity of a service
    such as electricity, water, gas, etc. It is typically used in association with
    TariffProfile to define the steps or blocks in a step tariff structure, where startValue
    simultaneously defines the entry value of this step and the closing value of the
    previous step. Where consumption is >= startValue it falls within this interval and
    where consumption is < startValue it falls within the previous interval."""

    __slots__ = (
        "_charges",
        "_reading_type",
        "_tariff_profiles",
        "_tou_tariff_intervals",
        "sequence_number",
        "start_value",
    )

    sequence_number: int | None
    start_value: float | None

    reading_type: One[ReadingType] = One(
        EndMeta(
            name="reading_type",
            cim_role="ReadingType",
            target="cim_python_sdk.model.iec61968.metering.reading_type:ReadingType",
            many=False,
            lower=0,
            upper=1,
            inverse="consumption_tariff_intervals",
            aggregation="none",
        )
    )
    charges: Many[Charge] = Many(
        EndMeta(
            name="charges",
            cim_role="Charges",
            target="cim_python_sdk.model.iec61968.payment_metering.charge:Charge",
            many=True,
            lower=0,
            upper=None,
            inverse="consumption_tariff_intervals",
            aggregation="none",
        )
    )
    tariff_profiles: Many[TariffProfile] = Many(
        EndMeta(
            name="tariff_profiles",
            cim_role="TariffProfiles",
            target="cim_python_sdk.model.iec61968.payment_metering.tariff_profile:TariffProfile",
            many=True,
            lower=0,
            upper=None,
            inverse="consumption_tariff_intervals",
            aggregation="none",
        )
    )
    tou_tariff_intervals: Many[TimeTariffInterval] = Many(
        EndMeta(
            name="tou_tariff_intervals",
            cim_role="TouTariffIntervals",
            target="cim_python_sdk.model.iec61968.payment_metering.time_tariff_interval:TimeTariffInterval",
            many=True,
            lower=0,
            upper=None,
            inverse="consumption_tariff_intervals",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConsumptionTariffInterval",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{DA1CBBFF-7002-47af-B95A-1EAAA72A6DFD}",
        attributes=(
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("start_value", "startValue", "float", 0, 1, "primitive"),
        ),
        ends=(
            reading_type.meta,
            charges.meta,
            tariff_profiles.meta,
            tou_tariff_intervals.meta,
        ),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        start_value: float | None = None,
        reading_type: ReadingType | None = None,
        charges: Iterable[Charge] | None = None,
        tariff_profiles: Iterable[TariffProfile] | None = None,
        tou_tariff_intervals: Iterable[TimeTariffInterval] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        self.start_value = start_value
        if reading_type is not None:
            self.reading_type = reading_type
        if charges is not None:
            ConsumptionTariffInterval.charges.extend(self, charges)
        if tariff_profiles is not None:
            ConsumptionTariffInterval.tariff_profiles.extend(self, tariff_profiles)
        if tou_tariff_intervals is not None:
            ConsumptionTariffInterval.tou_tariff_intervals.extend(self, tou_tariff_intervals)

    def add_charge(self, charge: Charge) -> Self:
        return ConsumptionTariffInterval.charges.add(self, charge)

    def remove_charge(self, charge: Charge) -> Self:
        return ConsumptionTariffInterval.charges.remove(self, charge)

    def clear_charges(self) -> Self:
        return ConsumptionTariffInterval.charges.clear(self)

    def num_charge(self) -> int:
        return ConsumptionTariffInterval.charges.count(self)

    def get_charge_by_mrid(self, mrid: str) -> Charge | None:
        return ConsumptionTariffInterval.charges.get_by_mrid(self, mrid)

    def add_tariff_profile(self, tariff_profile: TariffProfile) -> Self:
        return ConsumptionTariffInterval.tariff_profiles.add(self, tariff_profile)

    def remove_tariff_profile(self, tariff_profile: TariffProfile) -> Self:
        return ConsumptionTariffInterval.tariff_profiles.remove(self, tariff_profile)

    def clear_tariff_profiles(self) -> Self:
        return ConsumptionTariffInterval.tariff_profiles.clear(self)

    def num_tariff_profile(self) -> int:
        return ConsumptionTariffInterval.tariff_profiles.count(self)

    def get_tariff_profile_by_mrid(self, mrid: str) -> TariffProfile | None:
        return ConsumptionTariffInterval.tariff_profiles.get_by_mrid(self, mrid)

    def add_tou_tariff_interval(self, tou_tariff_interval: TimeTariffInterval) -> Self:
        return ConsumptionTariffInterval.tou_tariff_intervals.add(self, tou_tariff_interval)

    def remove_tou_tariff_interval(self, tou_tariff_interval: TimeTariffInterval) -> Self:
        return ConsumptionTariffInterval.tou_tariff_intervals.remove(self, tou_tariff_interval)

    def clear_tou_tariff_intervals(self) -> Self:
        return ConsumptionTariffInterval.tou_tariff_intervals.clear(self)

    def num_tou_tariff_interval(self) -> int:
        return ConsumptionTariffInterval.tou_tariff_intervals.count(self)
