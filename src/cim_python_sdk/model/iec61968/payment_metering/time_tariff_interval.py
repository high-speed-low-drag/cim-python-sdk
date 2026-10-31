"""CIM class TimeTariffInterval (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.charge import Charge
    from cim_python_sdk.model.iec61968.payment_metering.consumption_tariff_interval import (
        ConsumptionTariffInterval,
    )
    from cim_python_sdk.model.iec61968.payment_metering.tariff_profile import TariffProfile


class TimeTariffInterval(CimObject):
    """One of a sequence of time intervals defined in terms of real time. It is typically used
    in association with TariffProfile to define the intervals in a time of use tariff
    structure, where startDateTime simultaneously determines the starting point of this
    interval and the ending point of the previous interval."""

    __slots__ = (
        "_charges",
        "_consumption_tariff_intervals",
        "_tariff_profiles",
        "sequence_number",
        "start_time",
    )

    sequence_number: int | None
    start_time: _dt.time | None

    charges: Many[Charge] = Many(
        EndMeta(
            name="charges",
            cim_role="Charges",
            target="cim_python_sdk.model.iec61968.payment_metering.charge:Charge",
            many=True,
            lower=0,
            upper=None,
            inverse="time_tariff_intervals",
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
            inverse="time_tariff_intervals",
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
            inverse="tou_tariff_intervals",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TimeTariffInterval",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{A61EEF7B-B1DE-4db9-9825-F1BA4F9C0478}",
        attributes=(
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("start_time", "startTime", "time", 0, 1, "primitive"),
        ),
        ends=(
            charges.meta,
            tariff_profiles.meta,
            consumption_tariff_intervals.meta,
        ),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        start_time: _dt.time | None = None,
        charges: Iterable[Charge] | None = None,
        tariff_profiles: Iterable[TariffProfile] | None = None,
        consumption_tariff_intervals: Iterable[ConsumptionTariffInterval] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        self.start_time = start_time
        if charges is not None:
            TimeTariffInterval.charges.extend(self, charges)
        if tariff_profiles is not None:
            TimeTariffInterval.tariff_profiles.extend(self, tariff_profiles)
        if consumption_tariff_intervals is not None:
            TimeTariffInterval.consumption_tariff_intervals.extend(
                self, consumption_tariff_intervals
            )

    def add_charge(self, charge: Charge) -> Self:
        return TimeTariffInterval.charges.add(self, charge)

    def remove_charge(self, charge: Charge) -> Self:
        return TimeTariffInterval.charges.remove(self, charge)

    def clear_charges(self) -> Self:
        return TimeTariffInterval.charges.clear(self)

    def num_charge(self) -> int:
        return TimeTariffInterval.charges.count(self)

    def get_charge_by_mrid(self, mrid: str) -> Charge | None:
        return TimeTariffInterval.charges.get_by_mrid(self, mrid)

    def add_tariff_profile(self, tariff_profile: TariffProfile) -> Self:
        return TimeTariffInterval.tariff_profiles.add(self, tariff_profile)

    def remove_tariff_profile(self, tariff_profile: TariffProfile) -> Self:
        return TimeTariffInterval.tariff_profiles.remove(self, tariff_profile)

    def clear_tariff_profiles(self) -> Self:
        return TimeTariffInterval.tariff_profiles.clear(self)

    def num_tariff_profile(self) -> int:
        return TimeTariffInterval.tariff_profiles.count(self)

    def get_tariff_profile_by_mrid(self, mrid: str) -> TariffProfile | None:
        return TimeTariffInterval.tariff_profiles.get_by_mrid(self, mrid)

    def add_consumption_tariff_interval(
        self, consumption_tariff_interval: ConsumptionTariffInterval
    ) -> Self:
        return TimeTariffInterval.consumption_tariff_intervals.add(
            self, consumption_tariff_interval
        )

    def remove_consumption_tariff_interval(
        self, consumption_tariff_interval: ConsumptionTariffInterval
    ) -> Self:
        return TimeTariffInterval.consumption_tariff_intervals.remove(
            self, consumption_tariff_interval
        )

    def clear_consumption_tariff_intervals(self) -> Self:
        return TimeTariffInterval.consumption_tariff_intervals.clear(self)

    def num_consumption_tariff_interval(self) -> int:
        return TimeTariffInterval.consumption_tariff_intervals.count(self)
