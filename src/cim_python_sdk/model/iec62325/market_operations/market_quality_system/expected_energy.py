"""CIM class ExpectedEnergy (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.expected_energy_values import (
        ExpectedEnergyValues,
    )


class ExpectedEnergy(CimObject):
    """Model Expected Energy from Market Clearing, interval based."""

    __slots__ = (
        "_expected_energy_values",
        "interval_start_time",
        "update_time_stamp",
        "update_user",
    )

    interval_start_time: _dt.datetime | None
    update_user: str | None
    update_time_stamp: _dt.datetime | None

    expected_energy_values: Many[ExpectedEnergyValues] = Many(
        EndMeta(
            name="expected_energy_values",
            cim_role="ExpectedEnergyValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.expected_energy_values:ExpectedEnergyValues",
            many=True,
            lower=1,
            upper=None,
            inverse="expected_energy",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExpectedEnergy",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{7B23FCCD-6749-4a1a-BC0C-0876AA127229}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
        ),
        ends=(expected_energy_values.meta,),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        update_user: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        expected_energy_values: Iterable[ExpectedEnergyValues] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        self.update_user = update_user
        self.update_time_stamp = update_time_stamp
        if expected_energy_values is not None:
            ExpectedEnergy.expected_energy_values.extend(self, expected_energy_values)

    def add_expected_energy_value(self, expected_energy_value: ExpectedEnergyValues) -> Self:
        return ExpectedEnergy.expected_energy_values.add(self, expected_energy_value)

    def remove_expected_energy_value(self, expected_energy_value: ExpectedEnergyValues) -> Self:
        return ExpectedEnergy.expected_energy_values.remove(self, expected_energy_value)

    def clear_expected_energy_values(self) -> Self:
        return ExpectedEnergy.expected_energy_values.clear(self)

    def num_expected_energy_value(self) -> int:
        return ExpectedEnergy.expected_energy_values.count(self)
