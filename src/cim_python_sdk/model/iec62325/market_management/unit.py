"""CIM class Unit (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.ace_tariff_type import AceTariffType
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class Unit(CimObject):
    """The identification of the unit name for the time series quantities."""

    __slots__ = ("_ace_tariff_type", "_time_series", "name")

    name: str | None

    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="unit",
            aggregation="none",
        )
    )
    ace_tariff_type: Many[AceTariffType] = Many(
        EndMeta(
            name="ace_tariff_type",
            cim_role="AceTariffType",
            target="cim_python_sdk.model.iec62325.market_management.ace_tariff_type:AceTariffType",
            many=True,
            lower=0,
            upper=None,
            inverse="unit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Unit",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{B6A71106-5272-4bca-9E7D-136D2278B311}",
        attributes=(AttrMeta("name", "name", "str", 0, 1, "primitive"),),
        ends=(
            time_series.meta,
            ace_tariff_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        name: str | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        ace_tariff_type: Iterable[AceTariffType] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.name = name
        if time_series is not None:
            Unit.time_series.extend(self, time_series)
        if ace_tariff_type is not None:
            Unit.ace_tariff_type.extend(self, ace_tariff_type)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return Unit.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return Unit.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return Unit.time_series.clear(self)

    def num_time_series(self) -> int:
        return Unit.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return Unit.time_series.get_by_mrid(self, mrid)

    def add_ace_tariff_type(self, ace_tariff_type: AceTariffType) -> Self:
        return Unit.ace_tariff_type.add(self, ace_tariff_type)

    def remove_ace_tariff_type(self, ace_tariff_type: AceTariffType) -> Self:
        return Unit.ace_tariff_type.remove(self, ace_tariff_type)

    def clear_ace_tariff_type(self) -> Self:
        return Unit.ace_tariff_type.clear(self)

    def num_ace_tariff_type(self) -> int:
        return Unit.ace_tariff_type.count(self)
