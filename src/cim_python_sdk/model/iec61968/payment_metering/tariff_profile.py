"""CIM class TariffProfile (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.tariff import Tariff
    from cim_python_sdk.model.iec61968.payment_metering.consumption_tariff_interval import (
        ConsumptionTariffInterval,
    )
    from cim_python_sdk.model.iec61968.payment_metering.time_tariff_interval import (
        TimeTariffInterval,
    )


class TariffProfile(Document):
    """A schedule of charges; structure associated with Tariff that allows the definition of
    complex tarif structures such as step and time of use when used in conjunction with
    TimeTariffInterval and Charge. Inherited 'status.value' is defined in the context of the
    utility's business rules, for example: active, inactive, etc."""

    __slots__ = (
        "_consumption_tariff_intervals",
        "_tariffs",
        "_time_tariff_intervals",
        "tariff_cycle",
    )

    tariff_cycle: str | None

    time_tariff_intervals: Many[TimeTariffInterval] = Many(
        EndMeta(
            name="time_tariff_intervals",
            cim_role="TimeTariffIntervals",
            target="cim_python_sdk.model.iec61968.payment_metering.time_tariff_interval:TimeTariffInterval",
            many=True,
            lower=0,
            upper=None,
            inverse="tariff_profiles",
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
            inverse="tariff_profiles",
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
            inverse="tariff_profiles",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TariffProfile",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{96DD424D-40A2-4b2b-88EA-D66EE08B1313}",
        attributes=(AttrMeta("tariff_cycle", "tariffCycle", "str", 0, 1, "primitive"),),
        ends=(
            time_tariff_intervals.meta,
            consumption_tariff_intervals.meta,
            tariffs.meta,
        ),
    )

    def __init__(
        self,
        *,
        tariff_cycle: str | None = None,
        time_tariff_intervals: Iterable[TimeTariffInterval] | None = None,
        consumption_tariff_intervals: Iterable[ConsumptionTariffInterval] | None = None,
        tariffs: Iterable[Tariff] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tariff_cycle = tariff_cycle
        if time_tariff_intervals is not None:
            TariffProfile.time_tariff_intervals.extend(self, time_tariff_intervals)
        if consumption_tariff_intervals is not None:
            TariffProfile.consumption_tariff_intervals.extend(self, consumption_tariff_intervals)
        if tariffs is not None:
            TariffProfile.tariffs.extend(self, tariffs)

    def add_time_tariff_interval(self, time_tariff_interval: TimeTariffInterval) -> Self:
        return TariffProfile.time_tariff_intervals.add(self, time_tariff_interval)

    def remove_time_tariff_interval(self, time_tariff_interval: TimeTariffInterval) -> Self:
        return TariffProfile.time_tariff_intervals.remove(self, time_tariff_interval)

    def clear_time_tariff_intervals(self) -> Self:
        return TariffProfile.time_tariff_intervals.clear(self)

    def num_time_tariff_interval(self) -> int:
        return TariffProfile.time_tariff_intervals.count(self)

    def add_consumption_tariff_interval(
        self, consumption_tariff_interval: ConsumptionTariffInterval
    ) -> Self:
        return TariffProfile.consumption_tariff_intervals.add(self, consumption_tariff_interval)

    def remove_consumption_tariff_interval(
        self, consumption_tariff_interval: ConsumptionTariffInterval
    ) -> Self:
        return TariffProfile.consumption_tariff_intervals.remove(self, consumption_tariff_interval)

    def clear_consumption_tariff_intervals(self) -> Self:
        return TariffProfile.consumption_tariff_intervals.clear(self)

    def num_consumption_tariff_interval(self) -> int:
        return TariffProfile.consumption_tariff_intervals.count(self)

    def add_tariff(self, tariff: Tariff) -> Self:
        return TariffProfile.tariffs.add(self, tariff)

    def remove_tariff(self, tariff: Tariff) -> Self:
        return TariffProfile.tariffs.remove(self, tariff)

    def clear_tariffs(self) -> Self:
        return TariffProfile.tariffs.clear(self)

    def num_tariff(self) -> int:
        return TariffProfile.tariffs.count(self)

    def get_tariff_by_mrid(self, mrid: str) -> Tariff | None:
        return TariffProfile.tariffs.get_by_mrid(self, mrid)
