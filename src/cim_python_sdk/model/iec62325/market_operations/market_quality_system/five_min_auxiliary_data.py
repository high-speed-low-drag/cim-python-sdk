"""CIM class FiveMinAuxiliaryData (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_values import (
        AuxiliaryValues,
    )


class FiveMinAuxiliaryData(CimObject):
    """Models 5-Minutes Auxiliary Data."""

    __slots__ = ("_auxillary_values", "interval_start_time", "update_time_stamp", "update_user")

    interval_start_time: _dt.datetime | None
    update_user: str | None
    update_time_stamp: _dt.datetime | None

    auxillary_values: Many[AuxiliaryValues] = Many(
        EndMeta(
            name="auxillary_values",
            cim_role="AuxillaryValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_values:AuxiliaryValues",
            many=True,
            lower=1,
            upper=None,
            inverse="five_min_auxillary_data",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FiveMinAuxiliaryData",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{394D0052-710F-40b4-88D5-2CAAB902C5E6}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
        ),
        ends=(auxillary_values.meta,),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        update_user: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        auxillary_values: Iterable[AuxiliaryValues] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        self.update_user = update_user
        self.update_time_stamp = update_time_stamp
        if auxillary_values is not None:
            FiveMinAuxiliaryData.auxillary_values.extend(self, auxillary_values)

    def add_auxillary_value(self, auxillary_value: AuxiliaryValues) -> Self:
        return FiveMinAuxiliaryData.auxillary_values.add(self, auxillary_value)

    def remove_auxillary_value(self, auxillary_value: AuxiliaryValues) -> Self:
        return FiveMinAuxiliaryData.auxillary_values.remove(self, auxillary_value)

    def clear_auxillary_values(self) -> Self:
        return FiveMinAuxiliaryData.auxillary_values.clear(self)

    def num_auxillary_value(self) -> int:
        return FiveMinAuxiliaryData.auxillary_values.count(self)
